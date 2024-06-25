from django.db import models


class VwOdbcPtPatientinfo(models.Model):
    # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')
    # Field name made lowercase.
    patient_uid = models.IntegerField(
        db_column='Patient_UID', primary_key=True)
    # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=35,
                                db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=35,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=35,
                                  db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    chartnumber = models.CharField(db_column='ChartNumber', max_length=12,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=15,
                             db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    aptste = models.CharField(db_column='AptSte', max_length=30,
                              db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30,
                               db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10,
                               db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30,
                            db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3,
                             db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    areacode = models.CharField(db_column='AreaCode', max_length=3,
                                db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    officephone = models.CharField(db_column='OfficePhone', max_length=25,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    officeextension = models.CharField(db_column='OfficeExtension', max_length=6,
                                       db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=25,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    other = models.CharField(db_column='Other', max_length=25,
                             db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    phonetype = models.CharField(db_column='PhoneType', max_length=1,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50,
                             db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    maritalstatus = models.SmallIntegerField(
        db_column='MaritalStatus', blank=True, null=True)
    # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)
    # Field name made lowercase.
    deceased = models.DateTimeField(
        db_column='Deceased', blank=True, null=True)
    # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1,
                              db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    ssn = models.CharField(db_column='SSN', max_length=12,
                           db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    relationship = models.SmallIntegerField(
        db_column='Relationship', blank=True, null=True)
    # Field name made lowercase.
    hipaarelationship = models.CharField(
        db_column='HIPAARelationship', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(
        db_column='ResponsiblePartyFID', blank=True, null=True)
    # Field name made lowercase.
    profilefid = models.IntegerField(
        db_column='ProfileFID', blank=True, null=True)
    # Field name made lowercase.
    financialclassfid = models.IntegerField(
        db_column='FinancialClassFID', blank=True, null=True)
    # Field name made lowercase.
    employer = models.CharField(db_column='Employer', max_length=100,
                                db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    employerfid = models.IntegerField(
        db_column='EmployerFID', blank=True, null=True)
    # Field name made lowercase.
    insuranceorder = models.CharField(db_column='InsuranceOrder', max_length=45,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    ar_patportionfid = models.IntegerField(
        db_column='AR_PatPortionFID', blank=True, null=True)
    # Field name made lowercase.
    ar_insportionfid = models.IntegerField(
        db_column='AR_InsPortionFID', blank=True, null=True)
    # Field name made lowercase.
    createdat = models.DateTimeField(
        db_column='CreatedAt', blank=True, null=True)
    # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)
    # Field name made lowercase.
    recalcbuckets = models.BooleanField(
        db_column='RecalcBuckets', blank=True, null=True)
    # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=107,
                                db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    changedat = models.DateTimeField(
        db_column='ChangedAt', blank=True, null=True)
    # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    bucketsupdatedat = models.DateTimeField(
        db_column='BucketsUpdatedAt', blank=True, null=True)
    # Field name made lowercase.
    birthmonth = models.IntegerField(
        db_column='BirthMonth', blank=True, null=True)
    # Field name made lowercase.
    isdeceased = models.IntegerField(
        db_column='IsDeceased', blank=True, null=True)
    # Field name made lowercase.
    ethnicityfid = models.IntegerField(
        db_column='EthnicityFID', blank=True, null=True)
    # Field name made lowercase.
    languagefid = models.IntegerField(
        db_column='LanguageFID', blank=True, null=True)
    # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50,
                                db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    communicationnote = models.CharField(db_column='CommunicationNote', max_length=255,
                                         db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_PatientInfo'
        app_label = 'AMD_Test'


class VwOdbcBillBilling(models.Model):
    # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')
    # Field name made lowercase.
    billing_uid = models.IntegerField(
        db_column='Billing_UID', primary_key=True)
    # Field name made lowercase.
    billingrunfid = models.IntegerField(
        db_column='BillingRunFID', blank=True, null=True)
    # Field name made lowercase.
    collectionletterfid = models.IntegerField(
        db_column='CollectionLetterFID', blank=True, null=True)
    # Field name made lowercase.
    iswrittenoff = models.BooleanField(
        db_column='IsWrittenOff', blank=True, null=True)
    # Field name made lowercase.
    holdfid = models.IntegerField(db_column='HoldFID', blank=True, null=True)
    # Field name made lowercase.
    movefid = models.IntegerField(db_column='MoveFID', blank=True, null=True)
    # Field name made lowercase.
    billingdate = models.DateTimeField(
        db_column='BillingDate', blank=True, null=True)
    # Field name made lowercase.
    statementgroupfid = models.IntegerField(
        db_column='StatementGroupFID', blank=True, null=True)
    # Field name made lowercase.
    profilefid = models.IntegerField(
        db_column='ProfileFID', blank=True, null=True)
    # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(
        db_column='ResponsiblePartyFID', blank=True, null=True)
    # Field name made lowercase.
    patientfid = models.IntegerField(
        db_column='PatientFID', blank=True, null=True)
    # Field name made lowercase.
    orderfield = models.CharField(db_column='OrderField', max_length=107,
                                  db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    sumfee = models.DecimalField(
        db_column='SumFee', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    insuranceportion = models.DecimalField(
        db_column='InsurancePortion', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    patientportion = models.DecimalField(
        db_column='PatientPortion', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    insurancebalance = models.DecimalField(
        db_column='InsuranceBalance', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    patientbalance = models.DecimalField(
        db_column='PatientBalance', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    ins_current = models.DecimalField(
        db_column='Ins_Current', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    pt_current = models.DecimalField(
        db_column='Pt_Current', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    ins_30_days = models.DecimalField(
        db_column='Ins_30_Days', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    pt_30_days = models.DecimalField(
        db_column='Pt_30_Days', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    ins_60_days = models.DecimalField(
        db_column='Ins_60_Days', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    pt_60_days = models.DecimalField(
        db_column='Pt_60_Days', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    ins_90_days = models.DecimalField(
        db_column='Ins_90_Days', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    pt_90_days = models.DecimalField(
        db_column='Pt_90_Days', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    ins_120_days = models.DecimalField(
        db_column='Ins_120_Days', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    pt_120_days = models.DecimalField(
        db_column='Pt_120_Days', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    insunapplied = models.DecimalField(
        db_column='InsUnapplied', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    ptunapplied = models.DecimalField(
        db_column='PtUnapplied', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    paymentdue = models.DecimalField(
        db_column='PaymentDue', max_digits=19, decimal_places=4, blank=True, null=True)
    # Field name made lowercase.
    agencyeligibledate = models.DateTimeField(
        db_column='AgencyEligibleDate', blank=True, null=True)
    # Field name made lowercase.
    statementcount = models.SmallIntegerField(
        db_column='StatementCount', blank=True, null=True)
    collectionlettercount = models.SmallIntegerField(
        db_column='CollectionLetterCount', blank=True, null=True)  # Field name made lowercase.
    collectionagencycount = models.SmallIntegerField(
        db_column='CollectionAgencyCount', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    createdat = models.DateTimeField(
        db_column='CreatedAt', blank=True, null=True)
    # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    changedat = models.DateTimeField(
        db_column='ChangedAt', blank=True, null=True)
    # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    dunningmessage = models.CharField(db_column='DunningMessage', max_length=120,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    billingmessage = models.CharField(db_column='BillingMessage', max_length=8000,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    oldestchargeagingdate = models.DateTimeField(
        db_column='OldestChargeAgingDate', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_Billing'
        app_label = 'AMD_Test'


class VwOdbcApptsAppointments(models.Model):
    # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')
    # Field name made lowercase.
    appointment_uid = models.IntegerField(
        db_column='Appointment_UID', primary_key=True)
    # Field name made lowercase.
    patientfid = models.IntegerField(
        db_column='PatientFID', blank=True, null=True)
    # Field name made lowercase.
    columnheadingfid = models.IntegerField(
        db_column='ColumnHeadingFID', blank=True, null=True)
    # Field name made lowercase.
    startdatetime = models.DateTimeField(
        db_column='StartDateTime', blank=True, null=True)
    # Field name made lowercase.
    duration = models.SmallIntegerField(
        db_column='Duration', blank=True, null=True)
    # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=10,
                             db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    profilefid = models.IntegerField(
        db_column='ProfileFID', blank=True, null=True)
    # Field name made lowercase.
    waitlist = models.BooleanField(db_column='WaitList', blank=True, null=True)
    # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=6000,
                                db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    apptstatus = models.SmallIntegerField(
        db_column='ApptStatus', blank=True, null=True)
    # Field name made lowercase.
    arrivetime = models.DateTimeField(
        db_column='ArriveTime', blank=True, null=True)
    # Field name made lowercase.
    othertime = models.DateTimeField(
        db_column='OtherTime', blank=True, null=True)
    # Field name made lowercase.
    seentime = models.DateTimeField(
        db_column='SeenTime', blank=True, null=True)
    # Field name made lowercase.
    visitposted = models.BooleanField(
        db_column='VisitPosted', blank=True, null=True)
    # Field name made lowercase.
    confirmuser = models.CharField(db_column='ConfirmUser', max_length=12,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    confirmdate = models.DateTimeField(
        db_column='ConfirmDate', blank=True, null=True)
    # Field name made lowercase.
    confirmmethodfid = models.IntegerField(
        db_column='ConfirmMethodFID', blank=True, null=True)
    # Field name made lowercase.
    changedat = models.DateTimeField(
        db_column='ChangedAt', blank=True, null=True)
    # Field name made lowercase.
    createdat = models.DateTimeField(
        db_column='CreatedAt', blank=True, null=True)
    # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    referralplanfid = models.IntegerField(
        db_column='ReferralPlanFID', blank=True, null=True)
    # Field name made lowercase.
    updatereferral = models.BooleanField(
        db_column='UpdateReferral', blank=True, null=True)
    extrainsuranceinformationfid = models.IntegerField(
        db_column='ExtraInsuranceInformationFID', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    episodefid = models.IntegerField(
        db_column='EpisodeFID', blank=True, null=True)
    # Field name made lowercase.
    facilityfid = models.IntegerField(
        db_column='FacilityFID', blank=True, null=True)
    # Field name made lowercase.
    visitnote = models.CharField(db_column='VisitNote', max_length=80,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    includeonhcfa = models.BooleanField(
        db_column='IncludeOnHCFA', blank=True, null=True)
    insurancebillingsequence = models.CharField(db_column='InsuranceBillingSequence', max_length=45,
                                                db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    acceptassignment = models.BooleanField(
        db_column='AcceptAssignment', blank=True, null=True)
    # Field name made lowercase.
    forcepaperclaim = models.BooleanField(
        db_column='ForcePaperClaim', blank=True, null=True)
    # Field name made lowercase.
    paymentfid = models.IntegerField(
        db_column='PaymentFID', blank=True, null=True)
    # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=12,
                                  db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    approvedat = models.DateTimeField(
        db_column='ApprovedAt', blank=True, null=True)
    # Field name made lowercase.
    claimeditstatusfid = models.IntegerField(
        db_column='ClaimEditStatusFID', blank=True, null=True)
    # Field name made lowercase.
    referenceid = models.CharField(db_column='ReferenceID', max_length=50,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    documentationcomplete = models.BooleanField(
        db_column='DocumentationComplete', blank=True, null=True)
    # Field name made lowercase.
    appttypes = models.CharField(db_column='ApptTypes', max_length=50,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    apptinstructions = models.CharField(db_column='ApptInstructions', max_length=50,
                                        db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    recurringappointmentfid = models.IntegerField(
        db_column='RecurringAppointmentFID', blank=True, null=True)
    # Field name made lowercase.
    billingnote = models.CharField(db_column='BillingNote', max_length=255,
                                   db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    visitactionhistoryfid = models.IntegerField(
        db_column='VisitActionHistoryFID', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_Appointments'
        app_label = 'AMD_Test'


class VwOdbcActvInstvisit(models.Model):
    # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')
    # Field name made lowercase.
    instvisit_uid = models.IntegerField(
        db_column='InstVisit_UID', primary_key=True)
    admittingdiagnosiscodefid = models.IntegerField(
        db_column='AdmittingDiagnosisCodeFID', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    attendingprvprofilefid = models.IntegerField(
        db_column='AttendingPrvProfileFID', blank=True, null=True)
    # Field name made lowercase.
    operatingprvprofilefid = models.IntegerField(
        db_column='OperatingPrvProfileFID', blank=True, null=True)
    # Field name made lowercase.
    otherproviderprofilefid = models.IntegerField(
        db_column='OtherProviderProfileFID', blank=True, null=True)
    principaldiagnosiscodefid = models.IntegerField(
        db_column='PrincipalDiagnosisCodeFID', blank=True, null=True)  # Field name made lowercase.
    principalprocedurecodefid = models.IntegerField(
        db_column='PrincipalProcedureCodeFID', blank=True, null=True)  # Field name made lowercase.
    relatedgroupdiagnosiscodefid = models.IntegerField(
        db_column='RelatedGroupDiagnosisCodeFID', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)
    # Field name made lowercase.
    admissiondate = models.DateTimeField(
        db_column='AdmissionDate', blank=True, null=True)
    admissionsourcecode = models.CharField(db_column='AdmissionSourceCode', max_length=1,
                                           db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    admissiontime = models.CharField(db_column='AdmissionTime', max_length=2,
                                     db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    admissiontypecode = models.CharField(
        db_column='AdmissionTypeCode', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    admittingdiagnosistypecode = models.CharField(db_column='AdmittingDiagnosisTypeCode', max_length=2,
                                                  db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    authorizationexceptcode = models.CharField(db_column='AuthorizationExceptCode', max_length=1,
                                               db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billclassificationcode = models.CharField(db_column='BillClassificationCode', max_length=1,
                                              db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    billingnotetext = models.CharField(db_column='BillingNoteText', max_length=80,
                                       db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    coinsureddaysqty = models.SmallIntegerField(
        db_column='CoInsuredDaysQty', blank=True, null=True)
    # Field name made lowercase.
    covereddaysqty = models.SmallIntegerField(
        db_column='CoveredDaysQty', blank=True, null=True)
    # Field name made lowercase.
    delayreasoncode = models.CharField(db_column='DelayReasonCode', max_length=2,
                                       db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    demonstrationprojectid = models.CharField(db_column='DemonstrationProjectID', max_length=30,
                                              db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    deviceexemptid = models.CharField(db_column='DeviceExemptID', max_length=30,
                                      db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    dischargetime = models.CharField(db_column='DischargeTime', max_length=2,
                                     db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    explanationofbenefitscode = models.CharField(db_column='ExplanationOfBenefitsCode', max_length=1,
                                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    facilitytypecode = models.CharField(db_column='FacilityTypeCode', max_length=1,
                                        db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    noncovereddaysqty = models.SmallIntegerField(
        db_column='NonCoveredDaysQty', blank=True, null=True)
    # Field name made lowercase.
    notetext = models.CharField(db_column='NoteText', max_length=80,
                                db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    notetypecode = models.CharField(db_column='NoteTypeCode', max_length=3,
                                    db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    originalreferenceid = models.CharField(db_column='OriginalReferenceID', max_length=30,
                                           db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    patientstatuscode = models.CharField(
        db_column='PatientStatusCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    principalproceduredate = models.DateTimeField(
        db_column='PrincipalProcedureDate', blank=True, null=True)
    principalproceduretypecode = models.CharField(db_column='PrincipalProcedureTypeCode', max_length=2,
                                                  db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    referralid = models.CharField(db_column='ReferralID', max_length=30,
                                  db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    # Field name made lowercase.
    reservedaysqty = models.SmallIntegerField(
        db_column='ReserveDaysQty', blank=True, null=True)
    # Field name made lowercase.
    stmtfromdate = models.DateTimeField(
        db_column='StmtFromDate', blank=True, null=True)
    # Field name made lowercase.
    stmtthrudate = models.DateTimeField(
        db_column='StmtThruDate', blank=True, null=True)
    submissionreasoncode = models.CharField(db_column='SubmissionReasonCode', max_length=1,
                                            db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    # Field name made lowercase.
    changedat = models.DateTimeField(
        db_column='ChangedAt', blank=True, null=True)
    # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12,
                                 db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_InstVisit'
        app_label = 'AMD_Test'
