from django.shortcuts import render
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
import pymssql
from django.conf import settings
from .models import VwOdbcPtPatientinfo, VwOdbcApptsAppointments, VwOdbcActvInstvisit


def getPatientInfo(request):
    server = settings.DATABASES['default']['HOST']
    database = "RootMea"
    username = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']

    bill_number = request.GET.get('billNumber')
    print(settings.DATABASES['default']['NAME'])

    conn = pymssql.connect(server=server, user=username,
                           password=password, database=database)
    cursor = conn.cursor()

    cursor.execute(
        'SELECT b.FullName,b.Address,b.City,b.State, b.CountryCode, b.HomePhone, b.DOB, b.Email, b.Gender, b.CommunicationNote FROM vw_ODBC_bill_Billing a join vw_ODBC_pt_PatientInfo b on a.patientFID = b.patient_UID where Billing_UID = ' + bill_number)

    rows = cursor.fetchall()

    data = []
    for row in rows:
        data.append({
            'Name': row[0],
            'Address': row[1],
            'City': row[2],
            'State': row[3],
            'Country': row[4],
            'PhoneNumber': row[5],
            'DOB': row[6],
            'Email': row[7],
            'Gender': row[8],
            'Notes': row[9]
            # Add more fields as needed
        })
    print(data)
    cursor.close()
    conn.close()
    return HttpResponse(data)


def load_data_from_mssql(request):

    patient_obj = VwOdbcPtPatientinfo.objects.all()
    for patient in patient_obj:
        appointment_obj = VwOdbcApptsAppointments.objects.all()
        print(appointment_obj)
        for appointment in appointment_obj:
            instvisit_obj = VwOdbcActvInstvisit.objects.all()
        for invist in instvisit_obj:
            data = []
            data.append({
                'Name': patient.firstname,
                'Address': patient.address,
                'City': patient.city,
                'State': patient.state,
                'Country': patient.countrycode,
                'PhoneNumber': patient.homephone,
                'DOB': patient.dob,
                'Email': patient.email,
                'Gender': patient.gender,
                'Notes': patient.communicationnote,
                'NoteType': invist.notetypecode
            })
    return JsonResponse(data, safe=False)


def dataFromMSSQL(request):
    name = request.GET.get('name')
    dob = request.GET.get('dob')
    phone = request.GET.get('phone')
    patient_obj = VwOdbcPtPatientinfo.objects.filter(
        Q(firstname=name) & Q(dob=dob) & Q(homephone=phone))
    for patient in patient_obj:
        appointment_obj = VwOdbcApptsAppointments.objects.filter(
            patientfid=patient.patient_uid)
        print(appointment_obj)
        for appointment in appointment_obj:
            instvisit_obj = VwOdbcActvInstvisit.objects.filter(
                visitfid=appointment.appointment_uid)
        for invist in instvisit_obj:
            data = []
            data.append({
                'Name': patient.firstname,
                'Address': patient.address,
                'City': patient.city,
                'State': patient.state,
                'Country': patient.countrycode,
                'PhoneNumber': patient.homephone,
                'DOB': patient.dob,
                'Email': patient.email,
                'Gender': patient.gender,
                'Notes': patient.communicationnote,
                'NoteType': invist.notetypecode,
                'AdmissionTypecode': invist.admissiontypecode,
                'AdmittingDiagnosisTypeCode': invist.admittingdiagnosistypecode,
                'PatientStatusCode': invist.patientstatuscode,
                'AdmissionDate': invist.admissiondate
            })

    return JsonResponse(data, safe=False)
