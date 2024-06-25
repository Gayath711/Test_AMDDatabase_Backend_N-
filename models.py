# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class OdbcRunhistory(models.Model):
    runhistoryid = models.IntegerField(db_column='RunHistoryID', blank=True, null=True)  # Field name made lowercase.
    rundate = models.DateTimeField(db_column='RunDate', blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='TableName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    begintime = models.DateTimeField(db_column='BeginTime', blank=True, null=True)  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='EndTime', blank=True, null=True)  # Field name made lowercase.
    runtime = models.CharField(db_column='RunTime', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rows = models.IntegerField(db_column='Rows', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ODBC_RunHistory'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    first_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    last_name = models.CharField(max_length=150, db_collation='SQL_Latin1_General_CP1_CI_AS')
    email = models.CharField(max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS')
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    object_repr = models.CharField(max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS')
    action_flag = models.SmallIntegerField()
    change_message = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')
    model = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    name = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS')
    session_data = models.TextField(db_collation='SQL_Latin1_General_CP1_CI_AS')
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DocreaderMymodel(models.Model):
    id = models.BigAutoField(primary_key=True)
    file = models.CharField(max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS')

    class Meta:
        managed = False
        db_table = 'docreader_mymodel'


class VwOdbcActvBatchinformation(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    batchinformation_uid = models.IntegerField(db_column='BatchInformation_UID')  # Field name made lowercase.
    batchnumber = models.IntegerField(db_column='BatchNumber', blank=True, null=True)  # Field name made lowercase.
    postingdate = models.DateTimeField(db_column='PostingDate', blank=True, null=True)  # Field name made lowercase.
    servicedate = models.DateTimeField(db_column='ServiceDate', blank=True, null=True)  # Field name made lowercase.
    dateclosed = models.DateTimeField(db_column='DateClosed', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    batchowner = models.CharField(db_column='BatchOwner', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    receivedate = models.DateTimeField(db_column='ReceiveDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_BatchInformation'


class VwOdbcActvCarrierbillinghistory(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    carrierbillinghistory_uid = models.IntegerField(db_column='CarrierBillingHistory_UID')  # Field name made lowercase.
    seqnumberlastbilled = models.IntegerField(db_column='SeqNumberLastBilled', blank=True, null=True)  # Field name made lowercase.
    carrierbilleddate = models.DateTimeField(db_column='CarrierBilledDate', blank=True, null=True)  # Field name made lowercase.
    chargedetailfid = models.IntegerField(db_column='ChargeDetailFID', blank=True, null=True)  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    proxyvisitfid = models.IntegerField(db_column='ProxyVisitFID', blank=True, null=True)  # Field name made lowercase.
    claimidsuffix = models.CharField(db_column='ClaimIDSuffix', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    claimid = models.CharField(db_column='ClaimID', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    paperedi = models.CharField(db_column='PaperEDI', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    carriercode = models.CharField(db_column='CarrierCode', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    previoussequencenumber = models.IntegerField(db_column='PreviousSequenceNumber', blank=True, null=True)  # Field name made lowercase.
    billedamount = models.DecimalField(db_column='BilledAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    isdemand = models.BooleanField(db_column='IsDemand', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_CarrierBillingHistory'


class VwOdbcActvChargedetail(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    chargedetail_uid = models.IntegerField(db_column='ChargeDetail_UID')  # Field name made lowercase.
    postingdate = models.DateTimeField(db_column='PostingDate', blank=True, null=True)  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(db_column='ResponsiblePartyFID', blank=True, null=True)  # Field name made lowercase.
    begindateofservice = models.DateTimeField(db_column='BeginDateOfService', blank=True, null=True)  # Field name made lowercase.
    enddateofservice = models.DateTimeField(db_column='EndDateOfService', blank=True, null=True)  # Field name made lowercase.
    chargecodefid = models.IntegerField(db_column='ChargeCodeFID', blank=True, null=True)  # Field name made lowercase.
    placeofservicefid = models.IntegerField(db_column='PlaceOfServiceFID', blank=True, null=True)  # Field name made lowercase.
    typeofservicefid = models.IntegerField(db_column='TypeOfServiceFID', blank=True, null=True)  # Field name made lowercase.
    agingdate = models.DateTimeField(db_column='AgingDate', blank=True, null=True)  # Field name made lowercase.
    billinsurance = models.BooleanField(db_column='BillInsurance', blank=True, null=True)  # Field name made lowercase.
    insurancebilled = models.BooleanField(db_column='InsuranceBilled', blank=True, null=True)  # Field name made lowercase.
    fee = models.DecimalField(db_column='Fee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    units = models.DecimalField(db_column='Units', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    dayclosed = models.BooleanField(db_column='DayClosed', blank=True, null=True)  # Field name made lowercase.
    posted = models.BooleanField(db_column='Posted', blank=True, null=True)  # Field name made lowercase.
    void = models.BooleanField(db_column='Void', blank=True, null=True)  # Field name made lowercase.
    voidedfid = models.IntegerField(db_column='VoidedFID', blank=True, null=True)  # Field name made lowercase.
    lastbilledcarriersequencenumber = models.IntegerField(db_column='LastBilledCarrierSequenceNumber', blank=True, null=True)  # Field name made lowercase.
    paidoff = models.BooleanField(db_column='PaidOff', blank=True, null=True)  # Field name made lowercase.
    patientportion = models.DecimalField(db_column='PatientPortion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    insuranceportion = models.DecimalField(db_column='InsurancePortion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    financialclassfid = models.IntegerField(db_column='FinancialClassFID', blank=True, null=True)  # Field name made lowercase.
    batchinformationfid = models.IntegerField(db_column='BatchInformationFID', blank=True, null=True)  # Field name made lowercase.
    allowedamount = models.DecimalField(db_column='AllowedAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    paymentplan = models.BooleanField(db_column='PaymentPlan', blank=True, null=True)  # Field name made lowercase.
    insurancebalance = models.DecimalField(db_column='InsuranceBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    patientbalance = models.DecimalField(db_column='PatientBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    carrierbillinghistoryfid = models.IntegerField(db_column='CarrierBillingHistoryFID', blank=True, null=True)  # Field name made lowercase.
    asstproviderfid = models.IntegerField(db_column='AsstProviderFID', blank=True, null=True)  # Field name made lowercase.
    residentfid = models.IntegerField(db_column='ResidentFID', blank=True, null=True)  # Field name made lowercase.
    protected = models.BooleanField(db_column='Protected', blank=True, null=True)  # Field name made lowercase.
    notefid = models.IntegerField(db_column='NoteFID', blank=True, null=True)  # Field name made lowercase.
    netfee = models.BooleanField(db_column='NetFee', blank=True, null=True)  # Field name made lowercase.
    lineitemnote = models.CharField(db_column='LineItemNote', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    includeonstatement = models.BooleanField(db_column='IncludeOnStatement', blank=True, null=True)  # Field name made lowercase.
    duration = models.IntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    cobcodefid = models.IntegerField(db_column='COBCodeFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diagnosiscodes = models.CharField(db_column='DiagnosisCodes', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    modifiers = models.CharField(db_column='Modifiers', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    assessmentdate = models.DateTimeField(db_column='AssessmentDate', blank=True, null=True)  # Field name made lowercase.
    attendingprvprofilefid = models.IntegerField(db_column='AttendingPrvProfileFID', blank=True, null=True)  # Field name made lowercase.
    noncoveredcharges = models.DecimalField(db_column='NonCoveredCharges', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    operatingprvprofilefid = models.IntegerField(db_column='OperatingPrvProfileFID', blank=True, null=True)  # Field name made lowercase.
    otherproviderprofilefid = models.IntegerField(db_column='OtherProviderProfileFID', blank=True, null=True)  # Field name made lowercase.
    facilitytaxamount = models.DecimalField(db_column='FacilityTaxAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    servicetaxamount = models.DecimalField(db_column='ServiceTaxAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unitstypecode = models.CharField(db_column='UnitsTypeCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    doswassystemgenerated = models.BooleanField(db_column='DOSWasSystemGenerated', blank=True, null=True)  # Field name made lowercase.
    totaldue = models.DecimalField(db_column='TotalDue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalportion = models.DecimalField(db_column='TotalPortion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    billstatusfid = models.IntegerField(db_column='BillStatusFID', blank=True, null=True)  # Field name made lowercase.
    firsttimeunbilled = models.DateTimeField(db_column='FirstTimeUnbilled', blank=True, null=True)  # Field name made lowercase.
    periodfid = models.IntegerField(db_column='PeriodFID', blank=True, null=True)  # Field name made lowercase.
    expectedamount = models.DecimalField(db_column='ExpectedAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_ChargeDetail'


class VwOdbcActvClaimedits(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    claimedit_uid = models.IntegerField(db_column='ClaimEdit_UID')  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    claimeditfid = models.IntegerField(db_column='ClaimEditFID', blank=True, null=True)  # Field name made lowercase.
    rulecode = models.CharField(db_column='RuleCode', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    procedurecode = models.CharField(db_column='ProcedureCode', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    errormessage = models.CharField(db_column='ErrorMessage', max_length=4096, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shorterrormessage = models.CharField(db_column='ShortErrorMessage', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    claimeditstatusfid = models.IntegerField(db_column='ClaimEditStatusFID', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_ClaimEdits'


class VwOdbcActvClaimrun(models.Model):
    claimrun_uid = models.IntegerField(db_column='ClaimRun_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    submitterfid = models.IntegerField(db_column='SubmitterFID', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    submittedat = models.DateTimeField(db_column='SubmittedAt', blank=True, null=True)  # Field name made lowercase.
    receivedat = models.DateTimeField(db_column='ReceivedAt', blank=True, null=True)  # Field name made lowercase.
    paidat = models.DateTimeField(db_column='PaidAt', blank=True, null=True)  # Field name made lowercase.
    claimtemplatefid = models.IntegerField(db_column='ClaimTemplateFID', blank=True, null=True)  # Field name made lowercase.
    datafileurl = models.CharField(db_column='DataFileURL', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    htmlfileurl = models.CharField(db_column='HTMLFileURL', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    trackingnumber = models.CharField(db_column='TrackingNumber', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    testmode = models.BooleanField(db_column='TestMode', blank=True, null=True)  # Field name made lowercase.
    claimcount = models.IntegerField(db_column='ClaimCount', blank=True, null=True)  # Field name made lowercase.
    isdemand = models.BooleanField(db_column='IsDemand', blank=True, null=True)  # Field name made lowercase.
    istrial = models.BooleanField(db_column='IsTrial', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_ClaimRun'


class VwOdbcActvClaimsubmission(models.Model):
    claimsubmission_uid = models.IntegerField(db_column='ClaimSubmission_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    claimrunfid = models.IntegerField(db_column='ClaimRunFID', blank=True, null=True)  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    proxyvisitfid = models.IntegerField(db_column='ProxyVisitFID', blank=True, null=True)  # Field name made lowercase.
    claimid = models.CharField(db_column='ClaimId', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    totalamount = models.DecimalField(db_column='TotalAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    thirdpartystatusfid = models.SmallIntegerField(db_column='ThirdPartyStatusFID', blank=True, null=True)  # Field name made lowercase.
    thirdpartypayorid = models.CharField(db_column='ThirdPartyPayorID', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    thirdpartyclaimid = models.CharField(db_column='ThirdPartyClaimID', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    hideexclusion = models.BooleanField(db_column='HideExclusion', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_ClaimSubmission'


class VwOdbcActvCustomclaimfieldvaluecharge(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    customclaimfieldvaluecharge_uid = models.IntegerField(db_column='CustomClaimFieldValueCharge_UID')  # Field name made lowercase.
    chargedetailfid = models.IntegerField(db_column='ChargeDetailFID', blank=True, null=True)  # Field name made lowercase.
    claimfieldfid = models.IntegerField(db_column='ClaimFieldFID', blank=True, null=True)  # Field name made lowercase.
    textvalue = models.CharField(db_column='TextValue', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fidvalue = models.IntegerField(db_column='FIDValue', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_CustomClaimFieldValueCharge'


class VwOdbcActvCustomclaimfieldvaluevisit(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    customclaimfieldvaluevisit_uid = models.IntegerField(db_column='CustomClaimFieldValueVisit_UID')  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    claimfieldfid = models.IntegerField(db_column='ClaimFieldFID', blank=True, null=True)  # Field name made lowercase.
    textvalue = models.CharField(db_column='TextValue', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fidvalue = models.IntegerField(db_column='FIDValue', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_CustomClaimFieldValueVisit'


class VwOdbcActvEpisodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    episode_uid = models.IntegerField(db_column='Episode_UID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(db_column='ResponsiblePartyFID', blank=True, null=True)  # Field name made lowercase.
    insurancebillingsequence = models.CharField(db_column='InsuranceBillingSequence', max_length=45, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    financialclassfid = models.IntegerField(db_column='FinancialClassFID', blank=True, null=True)  # Field name made lowercase.
    referralplanfid = models.IntegerField(db_column='ReferralPlanFID', blank=True, null=True)  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    extrainsuranceinformationfid = models.IntegerField(db_column='ExtraInsuranceInformationFID', blank=True, null=True)  # Field name made lowercase.
    groupbymonth = models.BooleanField(db_column='GroupByMonth', blank=True, null=True)  # Field name made lowercase.
    plancreatedate = models.DateTimeField(db_column='PlanCreateDate', blank=True, null=True)  # Field name made lowercase.
    ptoffsetdays = models.SmallIntegerField(db_column='PTOffsetDays', blank=True, null=True)  # Field name made lowercase.
    stoffsetdays = models.SmallIntegerField(db_column='STOffsetDays', blank=True, null=True)  # Field name made lowercase.
    otoffsetdays = models.SmallIntegerField(db_column='OTOffsetDays', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_Episodes'


class VwOdbcActvEvaluation(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    evaluation_uid = models.IntegerField(db_column='Evaluation_UID')  # Field name made lowercase.
    episodefid = models.IntegerField(db_column='EpisodeFID', blank=True, null=True)  # Field name made lowercase.
    evaluationdate = models.DateTimeField(db_column='EvaluationDate', blank=True, null=True)  # Field name made lowercase.
    evaluationtypefid = models.IntegerField(db_column='EvaluationTypeFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_Evaluation'


class VwOdbcActvExtrainsuranceinformation(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    extrainsuranceinfo_uid = models.IntegerField(db_column='ExtraInsuranceInfo_UID')  # Field name made lowercase.
    hospitalentrydate = models.DateTimeField(db_column='HospitalEntryDate', blank=True, null=True)  # Field name made lowercase.
    hospitalreleasedate = models.DateTimeField(db_column='HospitalReleaseDate', blank=True, null=True)  # Field name made lowercase.
    totaldisabilitystartdate = models.DateTimeField(db_column='TotalDisabilityStartDate', blank=True, null=True)  # Field name made lowercase.
    totaldisabilityenddate = models.DateTimeField(db_column='TotalDisabilityEndDate', blank=True, null=True)  # Field name made lowercase.
    datesimilarsymptom = models.DateTimeField(db_column='DateSimilarSymptom', blank=True, null=True)  # Field name made lowercase.
    dateofinjury = models.DateTimeField(db_column='DateofInjury', blank=True, null=True)  # Field name made lowercase.
    resultofaccident = models.BooleanField(db_column='ResultofAccident', blank=True, null=True)  # Field name made lowercase.
    emergencytreatment = models.BooleanField(db_column='EmergencyTreatment', blank=True, null=True)  # Field name made lowercase.
    workinjury = models.BooleanField(db_column='WorkInjury', blank=True, null=True)  # Field name made lowercase.
    outsidelab = models.BooleanField(db_column='OutsideLab', blank=True, null=True)  # Field name made lowercase.
    payprovider = models.BooleanField(db_column='PayProvider', blank=True, null=True)  # Field name made lowercase.
    releasesignature = models.BooleanField(db_column='ReleaseSignature', blank=True, null=True)  # Field name made lowercase.
    epsdt = models.BooleanField(db_column='EPSDT', blank=True, null=True)  # Field name made lowercase.
    familyplanning = models.CharField(db_column='FamilyPlanning', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    supplierprovidernumber = models.CharField(db_column='SupplierProviderNumber', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    outsidelabcharges = models.DecimalField(db_column='OutsideLabCharges', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    accidentstate = models.CharField(db_column='AccidentState', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    text1 = models.CharField(db_column='Text1', max_length=75, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    autoaccident = models.BooleanField(db_column='AutoAccident', blank=True, null=True)  # Field name made lowercase.
    datelastseen = models.DateTimeField(db_column='DateLastSeen', blank=True, null=True)  # Field name made lowercase.
    medicaidresubcode = models.CharField(db_column='MedicaidResubCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    originalrefnum = models.CharField(db_column='OriginalRefNum', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    supervisingprofilefid = models.IntegerField(db_column='SupervisingProfileFID', blank=True, null=True)  # Field name made lowercase.
    orderingrefproviderfid = models.IntegerField(db_column='OrderingRefProviderFID', blank=True, null=True)  # Field name made lowercase.
    accidentcrimevictim = models.BooleanField(db_column='AccidentCrimeVictim', blank=True, null=True)  # Field name made lowercase.
    accidentwithmedcoverage = models.BooleanField(db_column='AccidentWithMedCoverage', blank=True, null=True)  # Field name made lowercase.
    accidentwithoutmedcoverage = models.BooleanField(db_column='AccidentWithoutMedCoverage', blank=True, null=True)  # Field name made lowercase.
    accidentwithnofaultcoverage = models.BooleanField(db_column='AccidentWithNoFaultCoverage', blank=True, null=True)  # Field name made lowercase.
    conditionpregnant = models.BooleanField(db_column='ConditionPregnant', blank=True, null=True)  # Field name made lowercase.
    lasttherapydate = models.DateTimeField(db_column='LastTherapyDate', blank=True, null=True)  # Field name made lowercase.
    symptomdate = models.DateTimeField(db_column='SymptomDate', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_ExtraInsuranceInformation'


class VwOdbcActvHipaasituationalfieldvalues(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    situationalfieldvalue_uid = models.IntegerField(db_column='SituationalFieldValue_UID')  # Field name made lowercase.
    extrainsuranceinfofid = models.IntegerField(db_column='ExtraInsuranceInfoFID', blank=True, null=True)  # Field name made lowercase.
    situationalfieldfid = models.IntegerField(db_column='SituationalFieldFID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_HipaaSituationalFieldValues'


class VwOdbcActvInsthealthinfo(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    insthealthinfo_uid = models.IntegerField(db_column='InstHealthInfo_UID')  # Field name made lowercase.
    chargecodefid = models.IntegerField(db_column='ChargeCodeFID', blank=True, null=True)  # Field name made lowercase.
    diagnosiscodefid = models.IntegerField(db_column='DiagnosisCodeFID', blank=True, null=True)  # Field name made lowercase.
    healthinfocodefid = models.IntegerField(db_column='HealthInfoCodeFID', blank=True, null=True)  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    fromdate = models.DateTimeField(db_column='FromDate', blank=True, null=True)  # Field name made lowercase.
    thrudate = models.DateTimeField(db_column='ThruDate', blank=True, null=True)  # Field name made lowercase.
    typecode = models.CharField(db_column='TypeCode', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_InstHealthInfo'


class VwOdbcActvInstpaperwork(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    instpaperwork_uid = models.IntegerField(db_column='InstPaperwork_UID')  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    availibilitycode = models.CharField(db_column='AvailibilityCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    controlnumber = models.CharField(db_column='ControlNumber', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    reporttypecode = models.CharField(db_column='ReportTypeCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_InstPaperwork'


class VwOdbcActvInstvisit(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    instvisit_uid = models.IntegerField(db_column='InstVisit_UID')  # Field name made lowercase.
    admittingdiagnosiscodefid = models.IntegerField(db_column='AdmittingDiagnosisCodeFID', blank=True, null=True)  # Field name made lowercase.
    attendingprvprofilefid = models.IntegerField(db_column='AttendingPrvProfileFID', blank=True, null=True)  # Field name made lowercase.
    operatingprvprofilefid = models.IntegerField(db_column='OperatingPrvProfileFID', blank=True, null=True)  # Field name made lowercase.
    otherproviderprofilefid = models.IntegerField(db_column='OtherProviderProfileFID', blank=True, null=True)  # Field name made lowercase.
    principaldiagnosiscodefid = models.IntegerField(db_column='PrincipalDiagnosisCodeFID', blank=True, null=True)  # Field name made lowercase.
    principalprocedurecodefid = models.IntegerField(db_column='PrincipalProcedureCodeFID', blank=True, null=True)  # Field name made lowercase.
    relatedgroupdiagnosiscodefid = models.IntegerField(db_column='RelatedGroupDiagnosisCodeFID', blank=True, null=True)  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    admissiondate = models.DateTimeField(db_column='AdmissionDate', blank=True, null=True)  # Field name made lowercase.
    admissionsourcecode = models.CharField(db_column='AdmissionSourceCode', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    admissiontime = models.CharField(db_column='AdmissionTime', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    admissiontypecode = models.CharField(db_column='AdmissionTypeCode', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    admittingdiagnosistypecode = models.CharField(db_column='AdmittingDiagnosisTypeCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    authorizationexceptcode = models.CharField(db_column='AuthorizationExceptCode', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billclassificationcode = models.CharField(db_column='BillClassificationCode', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billingnotetext = models.CharField(db_column='BillingNoteText', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    coinsureddaysqty = models.SmallIntegerField(db_column='CoInsuredDaysQty', blank=True, null=True)  # Field name made lowercase.
    covereddaysqty = models.SmallIntegerField(db_column='CoveredDaysQty', blank=True, null=True)  # Field name made lowercase.
    delayreasoncode = models.CharField(db_column='DelayReasonCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    demonstrationprojectid = models.CharField(db_column='DemonstrationProjectID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    deviceexemptid = models.CharField(db_column='DeviceExemptID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dischargetime = models.CharField(db_column='DischargeTime', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    explanationofbenefitscode = models.CharField(db_column='ExplanationOfBenefitsCode', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    facilitytypecode = models.CharField(db_column='FacilityTypeCode', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    noncovereddaysqty = models.SmallIntegerField(db_column='NonCoveredDaysQty', blank=True, null=True)  # Field name made lowercase.
    notetext = models.CharField(db_column='NoteText', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    notetypecode = models.CharField(db_column='NoteTypeCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    originalreferenceid = models.CharField(db_column='OriginalReferenceID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    patientstatuscode = models.CharField(db_column='PatientStatusCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    principalproceduredate = models.DateTimeField(db_column='PrincipalProcedureDate', blank=True, null=True)  # Field name made lowercase.
    principalproceduretypecode = models.CharField(db_column='PrincipalProcedureTypeCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    referralid = models.CharField(db_column='ReferralID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reservedaysqty = models.SmallIntegerField(db_column='ReserveDaysQty', blank=True, null=True)  # Field name made lowercase.
    stmtfromdate = models.DateTimeField(db_column='StmtFromDate', blank=True, null=True)  # Field name made lowercase.
    stmtthrudate = models.DateTimeField(db_column='StmtThruDate', blank=True, null=True)  # Field name made lowercase.
    submissionreasoncode = models.CharField(db_column='SubmissionReasonCode', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_InstVisit'


class VwOdbcActvPaymentdetailreason(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    paymentdetailreason_uid = models.IntegerField(db_column='PaymentDetailReason_UID')  # Field name made lowercase.
    paymentdetailfid = models.IntegerField(db_column='PaymentDetailFID', blank=True, null=True)  # Field name made lowercase.
    paymentreasonfid = models.IntegerField(db_column='PaymentReasonFID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    units = models.DecimalField(db_column='Units', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_PaymentDetailReason'


class VwOdbcActvPaymentdetails(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    paymentdetail_uid = models.IntegerField(db_column='PaymentDetail_UID')  # Field name made lowercase.
    paymentfid = models.IntegerField(db_column='PaymentFID', blank=True, null=True)  # Field name made lowercase.
    paymentamount = models.DecimalField(db_column='PaymentAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    paymentstatus = models.CharField(db_column='PaymentStatus', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chargedetailfid = models.IntegerField(db_column='ChargeDetailFID', blank=True, null=True)  # Field name made lowercase.
    posted = models.BooleanField(db_column='Posted', blank=True, null=True)  # Field name made lowercase.
    void = models.BooleanField(db_column='Void', blank=True, null=True)  # Field name made lowercase.
    unapplied = models.BooleanField(db_column='Unapplied', blank=True, null=True)  # Field name made lowercase.
    transferred = models.BooleanField(db_column='Transferred', blank=True, null=True)  # Field name made lowercase.
    reasoncode = models.CharField(db_column='ReasonCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    voidedfid = models.IntegerField(db_column='VoidedFID', blank=True, null=True)  # Field name made lowercase.
    transferredfid = models.IntegerField(db_column='TransferredFID', blank=True, null=True)  # Field name made lowercase.
    protected = models.BooleanField(db_column='Protected', blank=True, null=True)  # Field name made lowercase.
    lastactionhistoryfid = models.IntegerField(db_column='LastActionHistoryFID', blank=True, null=True)  # Field name made lowercase.
    reversalfid = models.IntegerField(db_column='ReversalFID', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_PaymentDetails'


class VwOdbcActvPaymentplan(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    paymentplan_uid = models.IntegerField(db_column='PaymentPlan_UID')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate', blank=True, null=True)  # Field name made lowercase.
    payment = models.DecimalField(db_column='Payment', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    interestpercent = models.DecimalField(db_column='InterestPercent', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    annualmonthly = models.BooleanField(db_column='AnnualMonthly', blank=True, null=True)  # Field name made lowercase.
    duration = models.DecimalField(db_column='Duration', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(db_column='ResponsiblePartyFID', blank=True, null=True)  # Field name made lowercase.
    totalpaymentplanamount = models.DecimalField(db_column='TotalPaymentPlanAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalcharges = models.DecimalField(db_column='TotalCharges', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_PaymentPlan'


class VwOdbcActvPayments(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    payment_uid = models.IntegerField(db_column='Payment_UID')  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    paymentsource = models.SmallIntegerField(db_column='PaymentSource', blank=True, null=True)  # Field name made lowercase.
    paymentamount = models.DecimalField(db_column='PaymentAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    paymentmethodfid = models.IntegerField(db_column='PaymentMethodFID', blank=True, null=True)  # Field name made lowercase.
    checknumber = models.CharField(db_column='CheckNumber', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    payingcarrierfid = models.IntegerField(db_column='PayingCarrierFID', blank=True, null=True)  # Field name made lowercase.
    notefid = models.IntegerField(db_column='NoteFID', blank=True, null=True)  # Field name made lowercase.
    includeonstatement = models.BooleanField(db_column='IncludeonStatement', blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
    depositdate = models.DateTimeField(db_column='DepositDate', blank=True, null=True)  # Field name made lowercase.
    batchinformationfid = models.IntegerField(db_column='BatchInformationFID', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    paymentcodefid = models.IntegerField(db_column='PaymentCodeFID', blank=True, null=True)  # Field name made lowercase.
    dayclosed = models.BooleanField(db_column='DayClosed', blank=True, null=True)  # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(db_column='ResponsiblePartyFID', blank=True, null=True)  # Field name made lowercase.
    takebackamount = models.DecimalField(db_column='TakebackAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    takebacknote = models.CharField(db_column='TakebackNote', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    appliedat = models.DateTimeField(db_column='AppliedAt', blank=True, null=True)  # Field name made lowercase.
    appliedby = models.CharField(db_column='AppliedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    periodfid = models.IntegerField(db_column='PeriodFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_Payments'


class VwOdbcActvProviderinvoice(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    providerinvoice_uid = models.IntegerField(db_column='ProviderInvoice_UID')  # Field name made lowercase.
    invoicenumber = models.IntegerField(db_column='InvoiceNumber', blank=True, null=True)  # Field name made lowercase.
    checknumber = models.CharField(db_column='CheckNumber', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    checkpostedat = models.DateTimeField(db_column='CheckPostedAt', blank=True, null=True)  # Field name made lowercase.
    checkpostedby = models.CharField(db_column='CheckPostedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    providerfid = models.IntegerField(db_column='ProviderFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_ProviderInvoice'


class VwOdbcActvProviderinvoicedetail(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    providerinvoicedetail_uid = models.IntegerField(db_column='ProviderInvoiceDetail_UID')  # Field name made lowercase.
    providerinvoicefid = models.IntegerField(db_column='ProviderInvoiceFID', blank=True, null=True)  # Field name made lowercase.
    chargedetailfid = models.IntegerField(db_column='ChargeDetailFID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_ProviderInvoiceDetail'


class VwOdbcActvWriteoffdetails(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    writeoffdetail_uid = models.IntegerField(db_column='WriteOffDetail_UID')  # Field name made lowercase.
    writeofffid = models.IntegerField(db_column='WriteOffFID', blank=True, null=True)  # Field name made lowercase.
    writeoffamount = models.DecimalField(db_column='WriteOffAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    chargedetailfid = models.IntegerField(db_column='ChargeDetailFID', blank=True, null=True)  # Field name made lowercase.
    posted = models.BooleanField(db_column='Posted', blank=True, null=True)  # Field name made lowercase.
    void = models.BooleanField(db_column='Void', blank=True, null=True)  # Field name made lowercase.
    unapplied = models.BooleanField(db_column='Unapplied', blank=True, null=True)  # Field name made lowercase.
    transferred = models.BooleanField(db_column='Transferred', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    voidedfid = models.IntegerField(db_column='VoidedFID', blank=True, null=True)  # Field name made lowercase.
    transferredfid = models.IntegerField(db_column='TransferredFID', blank=True, null=True)  # Field name made lowercase.
    protected = models.BooleanField(db_column='Protected', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_WriteOffDetails'


class VwOdbcActvWriteoffs(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    writeoffs_uid = models.IntegerField(db_column='WriteOffs_UID')  # Field name made lowercase.
    writeoffcodefid = models.IntegerField(db_column='WriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    void = models.BooleanField(db_column='Void', blank=True, null=True)  # Field name made lowercase.
    batchinformationfid = models.IntegerField(db_column='BatchInformationFID', blank=True, null=True)  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
    writeoffsource = models.SmallIntegerField(db_column='WriteoffSource', blank=True, null=True)  # Field name made lowercase.
    dayclosed = models.BooleanField(db_column='DayClosed', blank=True, null=True)  # Field name made lowercase.
    notefid = models.IntegerField(db_column='NoteFID', blank=True, null=True)  # Field name made lowercase.
    includeonstatement = models.BooleanField(db_column='IncludeonStatement', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    periodfid = models.IntegerField(db_column='PeriodFID', blank=True, null=True)  # Field name made lowercase.
    effectivedate = models.DateTimeField(db_column='EffectiveDate', blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_WriteOffs'


class VwOdbcActvLnkChargedetailDiagnosiscodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    chargedetaildiagnosiscode_uid = models.IntegerField(db_column='ChargeDetailDiagnosisCode_UID')  # Field name made lowercase.
    chargedetailfid = models.IntegerField(db_column='ChargeDetailFID', blank=True, null=True)  # Field name made lowercase.
    diagnosiscodefid = models.IntegerField(db_column='DiagnosisCodeFID', blank=True, null=True)  # Field name made lowercase.
    codesequence = models.IntegerField(db_column='CodeSequence', blank=True, null=True)  # Field name made lowercase.
    codeset = models.SmallIntegerField(db_column='CodeSet', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_lnk_ChargeDetail_DiagnosisCodes'


class VwOdbcActvLnkChargedetailModifiercodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    chargedetailmodifiercode_uid = models.IntegerField(db_column='ChargeDetailModifierCode_UID')  # Field name made lowercase.
    chargedetailfid = models.IntegerField(db_column='ChargeDetailFID', blank=True, null=True)  # Field name made lowercase.
    modifiercodefid = models.IntegerField(db_column='ModifierCodeFID', blank=True, null=True)  # Field name made lowercase.
    codesequence = models.IntegerField(db_column='CodeSequence', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_lnk_ChargeDetail_ModifierCodes'


class VwOdbcActvLnkPaymentRemarkcodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    paymentremarkcode_uid = models.IntegerField(db_column='PaymentRemarkCode_UID')  # Field name made lowercase.
    paymentfid = models.IntegerField(db_column='PaymentFID', blank=True, null=True)  # Field name made lowercase.
    remarkcodefid = models.IntegerField(db_column='RemarkCodeFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_actv_lnk_Payment_RemarkCodes'


class VwOdbcApptsAppointmenthistory(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    appointmenthistory_uid = models.IntegerField(db_column='AppointmentHistory_UID')  # Field name made lowercase.
    appointmentfid = models.IntegerField(db_column='AppointmentFID', blank=True, null=True)  # Field name made lowercase.
    columnheadingfid = models.IntegerField(db_column='ColumnHeadingFID', blank=True, null=True)  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime', blank=True, null=True)  # Field name made lowercase.
    action = models.SmallIntegerField(db_column='Action', blank=True, null=True)  # Field name made lowercase.
    cancelnoshowreasonfid = models.IntegerField(db_column='CancelNoShowReasonFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_AppointmentHistory'


class VwOdbcApptsAppointments(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    appointment_uid = models.IntegerField(db_column='Appointment_UID')  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    columnheadingfid = models.IntegerField(db_column='ColumnHeadingFID', blank=True, null=True)  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime', blank=True, null=True)  # Field name made lowercase.
    duration = models.SmallIntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    waitlist = models.BooleanField(db_column='WaitList', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apptstatus = models.SmallIntegerField(db_column='ApptStatus', blank=True, null=True)  # Field name made lowercase.
    arrivetime = models.DateTimeField(db_column='ArriveTime', blank=True, null=True)  # Field name made lowercase.
    othertime = models.DateTimeField(db_column='OtherTime', blank=True, null=True)  # Field name made lowercase.
    seentime = models.DateTimeField(db_column='SeenTime', blank=True, null=True)  # Field name made lowercase.
    visitposted = models.BooleanField(db_column='VisitPosted', blank=True, null=True)  # Field name made lowercase.
    confirmuser = models.CharField(db_column='ConfirmUser', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    confirmdate = models.DateTimeField(db_column='ConfirmDate', blank=True, null=True)  # Field name made lowercase.
    confirmmethodfid = models.IntegerField(db_column='ConfirmMethodFID', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    referralplanfid = models.IntegerField(db_column='ReferralPlanFID', blank=True, null=True)  # Field name made lowercase.
    updatereferral = models.BooleanField(db_column='UpdateReferral', blank=True, null=True)  # Field name made lowercase.
    extrainsuranceinformationfid = models.IntegerField(db_column='ExtraInsuranceInformationFID', blank=True, null=True)  # Field name made lowercase.
    episodefid = models.IntegerField(db_column='EpisodeFID', blank=True, null=True)  # Field name made lowercase.
    facilityfid = models.IntegerField(db_column='FacilityFID', blank=True, null=True)  # Field name made lowercase.
    visitnote = models.CharField(db_column='VisitNote', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    includeonhcfa = models.BooleanField(db_column='IncludeOnHCFA', blank=True, null=True)  # Field name made lowercase.
    insurancebillingsequence = models.CharField(db_column='InsuranceBillingSequence', max_length=45, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    acceptassignment = models.BooleanField(db_column='AcceptAssignment', blank=True, null=True)  # Field name made lowercase.
    forcepaperclaim = models.BooleanField(db_column='ForcePaperClaim', blank=True, null=True)  # Field name made lowercase.
    paymentfid = models.IntegerField(db_column='PaymentFID', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    approvedat = models.DateTimeField(db_column='ApprovedAt', blank=True, null=True)  # Field name made lowercase.
    claimeditstatusfid = models.IntegerField(db_column='ClaimEditStatusFID', blank=True, null=True)  # Field name made lowercase.
    referenceid = models.CharField(db_column='ReferenceID', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    documentationcomplete = models.BooleanField(db_column='DocumentationComplete', blank=True, null=True)  # Field name made lowercase.
    appttypes = models.CharField(db_column='ApptTypes', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    apptinstructions = models.CharField(db_column='ApptInstructions', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    recurringappointmentfid = models.IntegerField(db_column='RecurringAppointmentFID', blank=True, null=True)  # Field name made lowercase.
    billingnote = models.CharField(db_column='BillingNote', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    visitactionhistoryfid = models.IntegerField(db_column='VisitActionHistoryFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_Appointments'


class VwOdbcApptsBlockholdexceptions(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    blockholdexception_uid = models.IntegerField(db_column='BlockHoldException_UID')  # Field name made lowercase.
    blockholdrulefid = models.IntegerField(db_column='BlockHoldRuleFID', blank=True, null=True)  # Field name made lowercase.
    exceptiondate = models.DateTimeField(db_column='ExceptionDate', blank=True, null=True)  # Field name made lowercase.
    columnheadingfid = models.IntegerField(db_column='ColumnHeadingFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_BlockHoldExceptions'


class VwOdbcApptsBlockholdrules(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    blockholdrule_uid = models.IntegerField(db_column='BlockHoldRule_UID')  # Field name made lowercase.
    reasonfid = models.IntegerField(db_column='ReasonFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    columnheadingfid = models.IntegerField(db_column='ColumnHeadingFID', blank=True, null=True)  # Field name made lowercase.
    startdatetime = models.DateTimeField(db_column='StartDateTime', blank=True, null=True)  # Field name made lowercase.
    enddatetime = models.DateTimeField(db_column='EndDateTime', blank=True, null=True)  # Field name made lowercase.
    ruletype = models.SmallIntegerField(db_column='RuleType', blank=True, null=True)  # Field name made lowercase.
    daysofweek = models.SmallIntegerField(db_column='DaysOfWeek', blank=True, null=True)  # Field name made lowercase.
    interval = models.SmallIntegerField(db_column='Interval', blank=True, null=True)  # Field name made lowercase.
    holdcolor = models.CharField(db_column='HoldColor', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ruletext = models.CharField(db_column='RuleText', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    providers = models.CharField(db_column='Providers', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    columnheadings = models.CharField(db_column='ColumnHeadings', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_BlockHoldRules'


class VwOdbcApptsInsuranceorder(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    appointmentfid = models.IntegerField(db_column='AppointmentFID', blank=True, null=True)  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    patientinsurancecoveragefid = models.IntegerField(db_column='PatientInsuranceCoverageFID', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.SmallIntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_InsuranceOrder'


class VwOdbcApptsWaitlist(models.Model):
    waitlist_uid = models.IntegerField(db_column='WaitList_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    appointmentfid = models.IntegerField(db_column='AppointmentFID', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    removecomments = models.CharField(db_column='RemoveComments', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_WaitList'


class VwOdbcApptsLnkAppointmentsApptinstructions(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    appointmentapptinstruction_uid = models.IntegerField(db_column='AppointmentApptInstruction_UID')  # Field name made lowercase.
    appointmentfid = models.IntegerField(db_column='AppointmentFID', blank=True, null=True)  # Field name made lowercase.
    apptinstructionfid = models.IntegerField(db_column='ApptInstructionFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_lnk_Appointments_ApptInstructions'


class VwOdbcApptsLnkAppointmentsAppttypes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    appointmentappttype_uid = models.IntegerField(db_column='AppointmentApptType_UID')  # Field name made lowercase.
    appointmentfid = models.IntegerField(db_column='AppointmentFID', blank=True, null=True)  # Field name made lowercase.
    appttypefid = models.IntegerField(db_column='ApptTypeFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_lnk_Appointments_ApptTypes'


class VwOdbcApptsLnkAppttypesettingsApptinstructions(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    appttypesettingsapptinstruction_uid = models.IntegerField(db_column='ApptTypeSettingsApptInstruction_UID')  # Field name made lowercase.
    appttypesettingsfid = models.IntegerField(db_column='ApptTypeSettingsFID', blank=True, null=True)  # Field name made lowercase.
    apptinstructionfid = models.IntegerField(db_column='ApptInstructionFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_lnk_ApptTypeSettings_ApptInstructions'


class VwOdbcApptsLnkBlockholdrulesColumnheadings(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    blockholdrulefid = models.IntegerField(db_column='BlockHoldRuleFID', blank=True, null=True)  # Field name made lowercase.
    columnheadingfid = models.IntegerField(db_column='ColumnHeadingFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_lnk_BlockHoldRules_ColumnHeadings'


class VwOdbcApptsLnkBlockholdrulesProviders(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    blockholdrulefid = models.IntegerField(db_column='BlockHoldRuleFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_lnk_BlockHoldRules_Providers'


class VwOdbcApptsLnkPagesColumnheadings(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    pagescolumnheadings_uid = models.IntegerField(db_column='PagesColumnHeadings_UID')  # Field name made lowercase.
    pagefid = models.IntegerField(db_column='PageFID', blank=True, null=True)  # Field name made lowercase.
    columnheadingfid = models.IntegerField(db_column='ColumnHeadingFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_lnk_Pages_ColumnHeadings'


class VwOdbcApptsLnkWaitlistColumnheadings(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    waitlistfid = models.IntegerField(db_column='WaitListFID', blank=True, null=True)  # Field name made lowercase.
    columnheadingfid = models.IntegerField(db_column='ColumnHeadingFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_lnk_WaitList_ColumnHeadings'


class VwOdbcApptsLnkWaitlistProviders(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    waitlistfid = models.IntegerField(db_column='WaitListFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_lnk_WaitList_Providers'


class VwOdbcApptsMfApptinstructions(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    apptinstruction_uid = models.IntegerField(db_column='ApptInstruction_UID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instruction = models.CharField(db_column='Instruction', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_mf_ApptInstructions'


class VwOdbcApptsMfAppttypesettingdocuments(models.Model):
    appttypesettingdocument_uid = models.IntegerField(db_column='ApptTypeSettingDocument_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    appttypesettingsfid = models.IntegerField(db_column='ApptTypeSettingsFID', blank=True, null=True)  # Field name made lowercase.
    documenttemplatefid = models.IntegerField(db_column='DocumentTemplateFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_mf_ApptTypeSettingDocuments'


class VwOdbcApptsMfAppttypesettings(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    appttypesettings_uid = models.IntegerField(db_column='ApptTypeSettings_UID')  # Field name made lowercase.
    appttypefid = models.IntegerField(db_column='ApptTypeFID', blank=True, null=True)  # Field name made lowercase.
    duration = models.SmallIntegerField(db_column='Duration', blank=True, null=True)  # Field name made lowercase.
    color = models.CharField(db_column='Color', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hide = models.BooleanField(db_column='Hide', blank=True, null=True)  # Field name made lowercase.
    chargesliptemplatefid = models.IntegerField(db_column='ChargeSlipTemplateFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    documents = models.CharField(db_column='Documents', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instructions = models.CharField(db_column='Instructions', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    waitlistpriorityfid = models.IntegerField(db_column='WaitListPriorityFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_mf_ApptTypeSettings'


class VwOdbcApptsMfAppttypes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    appttype_uid = models.IntegerField(db_column='ApptType_UID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)  # Field name made lowercase.
    isbillable = models.BooleanField(db_column='IsBillable', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_mf_ApptTypes'


class VwOdbcApptsMfColumnheadings(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    columnheading_uid = models.IntegerField(db_column='ColumnHeading_UID')  # Field name made lowercase.
    columnheading = models.CharField(db_column='ColumnHeading', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    usepatientprovider = models.BooleanField(db_column='UsePatientProvider', blank=True, null=True)  # Field name made lowercase.
    daystarttime = models.CharField(db_column='DayStartTime', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dayendtime = models.CharField(db_column='DayEndTime', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    timeincrement = models.SmallIntegerField(db_column='TimeIncrement', blank=True, null=True)  # Field name made lowercase.
    workweek = models.CharField(db_column='WorkWeek', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    autoholddays = models.IntegerField(db_column='AutoHoldDays', blank=True, null=True)  # Field name made lowercase.
    useautoholddefault = models.BooleanField(db_column='UseAutoHoldDefault', blank=True, null=True)  # Field name made lowercase.
    facilityfid = models.IntegerField(db_column='FacilityFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_mf_ColumnHeadings'


class VwOdbcApptsMfConfirmmethods(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    confirmmethod_uid = models.IntegerField(db_column='ConfirmMethod_UID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    confirmmethod = models.CharField(db_column='ConfirmMethod', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_mf_ConfirmMethods'


class VwOdbcApptsMfPages(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    page_uid = models.IntegerField(db_column='Page_UID')  # Field name made lowercase.
    pagename = models.CharField(db_column='PageName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pagegroup = models.SmallIntegerField(db_column='PageGroup', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.SmallIntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.
    userfid = models.IntegerField(db_column='UserFID', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_mf_Pages'


class VwOdbcApptsMfProviderschedulesetup(models.Model):
    providerschedulesetup_uid = models.IntegerField(db_column='ProviderScheduleSetup_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    daystarttime = models.CharField(db_column='DayStartTime', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dayendtime = models.CharField(db_column='DayEndTime', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    timeincrement = models.SmallIntegerField(db_column='TimeIncrement', blank=True, null=True)  # Field name made lowercase.
    workweek = models.CharField(db_column='WorkWeek', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_mf_ProviderScheduleSetup'


class VwOdbcApptsMfReasons(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    reason_uid = models.IntegerField(db_column='Reason_UID')  # Field name made lowercase.
    type = models.SmallIntegerField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_appts_mf_Reasons'


class VwOdbcBillBilling(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    billing_uid = models.IntegerField(db_column='Billing_UID')  # Field name made lowercase.
    billingrunfid = models.IntegerField(db_column='BillingRunFID', blank=True, null=True)  # Field name made lowercase.
    collectionletterfid = models.IntegerField(db_column='CollectionLetterFID', blank=True, null=True)  # Field name made lowercase.
    iswrittenoff = models.BooleanField(db_column='IsWrittenOff', blank=True, null=True)  # Field name made lowercase.
    holdfid = models.IntegerField(db_column='HoldFID', blank=True, null=True)  # Field name made lowercase.
    movefid = models.IntegerField(db_column='MoveFID', blank=True, null=True)  # Field name made lowercase.
    billingdate = models.DateTimeField(db_column='BillingDate', blank=True, null=True)  # Field name made lowercase.
    statementgroupfid = models.IntegerField(db_column='StatementGroupFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(db_column='ResponsiblePartyFID', blank=True, null=True)  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    orderfield = models.CharField(db_column='OrderField', max_length=107, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sumfee = models.DecimalField(db_column='SumFee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    insuranceportion = models.DecimalField(db_column='InsurancePortion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    patientportion = models.DecimalField(db_column='PatientPortion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    insurancebalance = models.DecimalField(db_column='InsuranceBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    patientbalance = models.DecimalField(db_column='PatientBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ins_current = models.DecimalField(db_column='Ins_Current', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pt_current = models.DecimalField(db_column='Pt_Current', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ins_30_days = models.DecimalField(db_column='Ins_30_Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pt_30_days = models.DecimalField(db_column='Pt_30_Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ins_60_days = models.DecimalField(db_column='Ins_60_Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pt_60_days = models.DecimalField(db_column='Pt_60_Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ins_90_days = models.DecimalField(db_column='Ins_90_Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pt_90_days = models.DecimalField(db_column='Pt_90_Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ins_120_days = models.DecimalField(db_column='Ins_120_Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pt_120_days = models.DecimalField(db_column='Pt_120_Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    insunapplied = models.DecimalField(db_column='InsUnapplied', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ptunapplied = models.DecimalField(db_column='PtUnapplied', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    paymentdue = models.DecimalField(db_column='PaymentDue', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    agencyeligibledate = models.DateTimeField(db_column='AgencyEligibleDate', blank=True, null=True)  # Field name made lowercase.
    statementcount = models.SmallIntegerField(db_column='StatementCount', blank=True, null=True)  # Field name made lowercase.
    collectionlettercount = models.SmallIntegerField(db_column='CollectionLetterCount', blank=True, null=True)  # Field name made lowercase.
    collectionagencycount = models.SmallIntegerField(db_column='CollectionAgencyCount', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dunningmessage = models.CharField(db_column='DunningMessage', max_length=120, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billingmessage = models.CharField(db_column='BillingMessage', max_length=8000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    oldestchargeagingdate = models.DateTimeField(db_column='OldestChargeAgingDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_Billing'


class VwOdbcBillBillingdetail(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    billingdetail_uid = models.IntegerField(db_column='BillingDetail_UID')  # Field name made lowercase.
    billingfid = models.IntegerField(db_column='BillingFID', blank=True, null=True)  # Field name made lowercase.
    chargedetailfid = models.IntegerField(db_column='ChargeDetailFID', blank=True, null=True)  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    writeoffcodefid = models.IntegerField(db_column='WriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    writeofffid = models.IntegerField(db_column='WriteOffFID', blank=True, null=True)  # Field name made lowercase.
    episodefid = models.IntegerField(db_column='EpisodeFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(db_column='ResponsiblePartyFID', blank=True, null=True)  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    chargecodefid = models.IntegerField(db_column='ChargeCodeFID', blank=True, null=True)  # Field name made lowercase.
    fee = models.DecimalField(db_column='Fee', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    receipts = models.DecimalField(db_column='Receipts', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    patientreceipts = models.DecimalField(db_column='PatientReceipts', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    adjustments = models.DecimalField(db_column='Adjustments', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    patientportion = models.DecimalField(db_column='PatientPortion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    patientbalance = models.DecimalField(db_column='PatientBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    insuranceportion = models.DecimalField(db_column='InsurancePortion', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    insurancebalance = models.DecimalField(db_column='InsuranceBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dos = models.DateTimeField(db_column='DOS', blank=True, null=True)  # Field name made lowercase.
    isstatementcharge = models.BooleanField(db_column='IsStatementCharge', blank=True, null=True)  # Field name made lowercase.
    isbalanceforward = models.BooleanField(db_column='IsBalanceForward', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    detaildescription = models.CharField(db_column='DetailDescription', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    paymentplanmessage = models.CharField(db_column='PaymentPlanMessage', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lineitemnote = models.CharField(db_column='LineItemNote', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_BillingDetail'


class VwOdbcBillBillingformat(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    billingformat_uid = models.IntegerField(db_column='BillingFormat_UID')  # Field name made lowercase.
    billingformatname = models.CharField(db_column='BillingFormatName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    iselectronic = models.BooleanField(db_column='IsElectronic', blank=True, null=True)  # Field name made lowercase.
    byrespparty = models.BooleanField(db_column='ByRespParty', blank=True, null=True)  # Field name made lowercase.
    bypatient = models.BooleanField(db_column='ByPatient', blank=True, null=True)  # Field name made lowercase.
    iscollections = models.BooleanField(db_column='IsCollections', blank=True, null=True)  # Field name made lowercase.
    isagency = models.BooleanField(db_column='IsAgency', blank=True, null=True)  # Field name made lowercase.
    reportingservicesid = models.CharField(db_column='ReportingServicesID', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_BillingFormat'


class VwOdbcBillBillinglineitem(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    billinglineitem_uid = models.IntegerField(db_column='BillingLineItem_UID')  # Field name made lowercase.
    billingdetailfid = models.IntegerField(db_column='BillingDetailFID', blank=True, null=True)  # Field name made lowercase.
    paymentfid = models.IntegerField(db_column='PaymentFID', blank=True, null=True)  # Field name made lowercase.
    writeofffid = models.IntegerField(db_column='WriteOffFID', blank=True, null=True)  # Field name made lowercase.
    lineitemtype = models.CharField(db_column='LineItemType', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    entrydate = models.DateTimeField(db_column='EntryDate', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    linetypefid = models.SmallIntegerField(db_column='LineTypeFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_BillingLineItem'


class VwOdbcBillBillingrun(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    billingrun_uid = models.IntegerField(db_column='BillingRun_UID')  # Field name made lowercase.
    requestfid = models.IntegerField(db_column='RequestFID', blank=True, null=True)  # Field name made lowercase.
    billingstatusfid = models.SmallIntegerField(db_column='BillingStatusFID', blank=True, null=True)  # Field name made lowercase.
    billingformatfid = models.IntegerField(db_column='BillingFormatFID', blank=True, null=True)  # Field name made lowercase.
    isdemand = models.BooleanField(db_column='IsDemand', blank=True, null=True)  # Field name made lowercase.
    ispaymentplan = models.BooleanField(db_column='IsPaymentPlan', blank=True, null=True)  # Field name made lowercase.
    byresponsibleparty = models.BooleanField(db_column='ByResponsibleParty', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_BillingRun'


class VwOdbcBillBillingstatus(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    billingstatus_uid = models.SmallIntegerField(db_column='BillingStatus_UID', blank=True, null=True)  # Field name made lowercase.
    billingstatusdescription = models.CharField(db_column='BillingStatusDescription', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_BillingStatus'


class VwOdbcBillHold(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    hold_uid = models.IntegerField(db_column='Hold_UID')  # Field name made lowercase.
    holdtypefid = models.SmallIntegerField(db_column='HoldTypeFID', blank=True, null=True)  # Field name made lowercase.
    holduntildate = models.DateTimeField(db_column='HoldUntilDate', blank=True, null=True)  # Field name made lowercase.
    holdreasonfid = models.IntegerField(db_column='HoldReasonFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_Hold'


class VwOdbcBillHoldtype(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    holdtype_uid = models.SmallIntegerField(db_column='HoldType_UID', blank=True, null=True)  # Field name made lowercase.
    holdtypedescription = models.CharField(db_column='HoldTypeDescription', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_HoldType'


class VwOdbcBillLinetype(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    linetype_uid = models.SmallIntegerField(db_column='LineType_UID', blank=True, null=True)  # Field name made lowercase.
    linetypedescription = models.CharField(db_column='LineTypeDescription', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_LineType'


class VwOdbcBillMove(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    move_uid = models.IntegerField(db_column='Move_UID')  # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(db_column='ResponsiblePartyFID', blank=True, null=True)  # Field name made lowercase.
    frombillingformatfid = models.IntegerField(db_column='FromBillingFormatFID', blank=True, null=True)  # Field name made lowercase.
    tobillingformatfid = models.IntegerField(db_column='ToBillingFormatFID', blank=True, null=True)  # Field name made lowercase.
    expiredate = models.DateTimeField(db_column='ExpireDate', blank=True, null=True)  # Field name made lowercase.
    holdreasonfid = models.IntegerField(db_column='HoldReasonFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_Move'


class VwOdbcBillPaymentplandetail(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    paymentplandetail_uid = models.IntegerField(db_column='PaymentPlanDetail_UID')  # Field name made lowercase.
    billingfid = models.IntegerField(db_column='BillingFID', blank=True, null=True)  # Field name made lowercase.
    chargedetailfid = models.IntegerField(db_column='ChargeDetailFID', blank=True, null=True)  # Field name made lowercase.
    patientbalance = models.DecimalField(db_column='PatientBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_PaymentPlanDetail'


class VwOdbcBillRequestqueue(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    request_uid = models.IntegerField(db_column='Request_UID')  # Field name made lowercase.
    billingstatusfid = models.SmallIntegerField(db_column='BillingStatusFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_bill_RequestQueue'


class VwOdbcColAccount(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    account_uid = models.IntegerField(db_column='Account_UID')  # Field name made lowercase.
    worklistlicensekey = models.IntegerField(db_column='WorklistLicenseKey')  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorkListFID', blank=True, null=True)  # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(db_column='ResponsiblePartyFID', blank=True, null=True)  # Field name made lowercase.
    insurancebalance = models.DecimalField(db_column='InsuranceBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    patientbalance = models.DecimalField(db_column='PatientBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pastduepatientbalance = models.DecimalField(db_column='PastDuePatientBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pastdueinsurancebalance = models.DecimalField(db_column='PastDueInsuranceBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dayspastdue = models.IntegerField(db_column='DaysPastDue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_Account'


class VwOdbcColAccountforce(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    accountforce_uid = models.IntegerField(db_column='AccountForce_UID')  # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(db_column='ResponsiblePartyFID', blank=True, null=True)  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorklistFID', blank=True, null=True)  # Field name made lowercase.
    worklistlicensekey = models.IntegerField(db_column='WorklistLicenseKey')  # Field name made lowercase.
    forceuntildate = models.DateField(db_column='ForceUntilDate', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_AccountForce'


class VwOdbcColAction(models.Model):
    action_uid = models.IntegerField(db_column='Action_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    action = models.CharField(db_column='Action', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nextactionfid = models.IntegerField(db_column='NextActionFID', blank=True, null=True)  # Field name made lowercase.
    followupdays = models.SmallIntegerField(db_column='FollowUpDays', blank=True, null=True)  # Field name made lowercase.
    defaultsentletter = models.BooleanField(db_column='DefaultSentLetter', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_Action'


class VwOdbcColActionhistory(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    actionhistory_uid = models.IntegerField(db_column='ActionHistory_UID')  # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(db_column='ResponsiblePartyFID', blank=True, null=True)  # Field name made lowercase.
    actionfid = models.IntegerField(db_column='ActionFID', blank=True, null=True)  # Field name made lowercase.
    nextactionfid = models.IntegerField(db_column='NextActionFID', blank=True, null=True)  # Field name made lowercase.
    actiondate = models.DateTimeField(db_column='ActionDate', blank=True, null=True)  # Field name made lowercase.
    nextactiondate = models.DateTimeField(db_column='NextActionDate', blank=True, null=True)  # Field name made lowercase.
    collectorfid = models.IntegerField(db_column='CollectorFID', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    promisedpayment = models.DecimalField(db_column='PromisedPayment', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    promiseddate = models.DateTimeField(db_column='PromisedDate', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_ActionHistory'


class VwOdbcColDenialactionhistory(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    actionhistory_uid = models.IntegerField(db_column='ActionHistory_UID')  # Field name made lowercase.
    paymentdetailfid = models.IntegerField(db_column='PaymentDetailFID', blank=True, null=True)  # Field name made lowercase.
    actionfid = models.IntegerField(db_column='ActionFID', blank=True, null=True)  # Field name made lowercase.
    nextactionfid = models.IntegerField(db_column='NextActionFID', blank=True, null=True)  # Field name made lowercase.
    actiondate = models.DateTimeField(db_column='ActionDate', blank=True, null=True)  # Field name made lowercase.
    nextactiondate = models.DateTimeField(db_column='NextActionDate', blank=True, null=True)  # Field name made lowercase.
    username = models.CharField(db_column='Username', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_DenialActionHistory'


class VwOdbcColVisit(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    colvisit_uid = models.IntegerField(db_column='ColVisit_UID')  # Field name made lowercase.
    worklistlicensekey = models.IntegerField(db_column='WorklistLicenseKey')  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorkListFID', blank=True, null=True)  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    insurancebalance = models.DecimalField(db_column='InsuranceBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    patientbalance = models.DecimalField(db_column='PatientBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pastduepatientbalance = models.DecimalField(db_column='PastDuePatientBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    pastdueinsurancebalance = models.DecimalField(db_column='PastDueInsuranceBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    dayspastdue = models.IntegerField(db_column='DaysPastDue', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_Visit'


class VwOdbcColVisitactionhistory(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    visitactionhistory_uid = models.IntegerField(db_column='VisitActionHistory_UID')  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    actionfid = models.IntegerField(db_column='ActionFID', blank=True, null=True)  # Field name made lowercase.
    nextactionfid = models.IntegerField(db_column='NextActionFID', blank=True, null=True)  # Field name made lowercase.
    actiondate = models.DateTimeField(db_column='ActionDate', blank=True, null=True)  # Field name made lowercase.
    nextactiondate = models.DateTimeField(db_column='NextActionDate', blank=True, null=True)  # Field name made lowercase.
    collectorfid = models.IntegerField(db_column='CollectorFID', blank=True, null=True)  # Field name made lowercase.
    balance = models.DecimalField(db_column='Balance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    promisedpayment = models.DecimalField(db_column='PromisedPayment', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    promiseddate = models.DateTimeField(db_column='PromisedDate', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_VisitActionHistory'


class VwOdbcColVisitforce(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    visitforce_uid = models.IntegerField(db_column='VisitForce_UID')  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorklistFID', blank=True, null=True)  # Field name made lowercase.
    worklistlicensekey = models.IntegerField(db_column='WorklistLicenseKey')  # Field name made lowercase.
    forceuntildate = models.DateField(db_column='ForceUntilDate', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_VisitForce'


class VwOdbcColWorklist(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    worklist_uid = models.IntegerField(db_column='WorkList_UID')  # Field name made lowercase.
    collectorfid = models.IntegerField(db_column='CollectorFID', blank=True, null=True)  # Field name made lowercase.
    priorityorder = models.IntegerField(db_column='PriorityOrder', blank=True, null=True)  # Field name made lowercase.
    worklistname = models.CharField(db_column='WorkListName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    familyinsuranceboth = models.SmallIntegerField(db_column='FamilyInsuranceBoth', blank=True, null=True)  # Field name made lowercase.
    dayspastdue = models.IntegerField(db_column='DaysPastDue', blank=True, null=True)  # Field name made lowercase.
    rplastnamefrom = models.CharField(db_column='RPLastNameFrom', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rplastnameto = models.CharField(db_column='RPLastNameTo', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    carriers = models.CharField(db_column='Carriers', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    accounttypes = models.CharField(db_column='AccountTypes', max_length=261, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    actions = models.CharField(db_column='Actions', max_length=261, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carriercategories = models.CharField(db_column='CarrierCategories', max_length=261, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    financialclasses = models.CharField(db_column='FinancialClasses', max_length=261, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    profiles = models.CharField(db_column='Profiles', max_length=261, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    groups = models.CharField(db_column='Groups', max_length=261, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    paymentreasons = models.CharField(db_column='PaymentReasons', max_length=261, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_WorkList'


class VwOdbcColWorklistCarrier(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    worklistcarrier_uid = models.IntegerField(db_column='WorklistCarrier_UID', blank=True, null=True)  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorkListFID', blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    carriercode = models.CharField(db_column='CarrierCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_WorkList_Carrier'


class VwOdbcColWorklistAccounttype(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    worklistaccounttype_uid = models.IntegerField(db_column='WorklistAccountType_UID', blank=True, null=True)  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorklistFID', blank=True, null=True)  # Field name made lowercase.
    accounttypefid = models.IntegerField(db_column='AccountTypeFID', blank=True, null=True)  # Field name made lowercase.
    accounttypecode = models.CharField(db_column='AccountTypeCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_Worklist_AccountType'


class VwOdbcColWorklistAction(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    worklistaction_uid = models.IntegerField(db_column='WorklistAction_UID', blank=True, null=True)  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorklistFID', blank=True, null=True)  # Field name made lowercase.
    actionfid = models.IntegerField(db_column='ActionFID', blank=True, null=True)  # Field name made lowercase.
    actioncode = models.CharField(db_column='ActionCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_Worklist_Action'


class VwOdbcColWorklistCarriercategory(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    worklistcarriercategory_uid = models.IntegerField(db_column='WorklistCarrierCategory_UID', blank=True, null=True)  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorklistFID', blank=True, null=True)  # Field name made lowercase.
    carriercategoryfid = models.IntegerField(db_column='CarrierCategoryFID', blank=True, null=True)  # Field name made lowercase.
    carriercategorycode = models.CharField(db_column='CarrierCategoryCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_Worklist_CarrierCategory'


class VwOdbcColWorklistFinancialclass(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    worklistfinancialclass_uid = models.IntegerField(db_column='WorklistFinancialClass_UID', blank=True, null=True)  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorklistFID', blank=True, null=True)  # Field name made lowercase.
    financialclassfid = models.IntegerField(db_column='FinancialClassFID', blank=True, null=True)  # Field name made lowercase.
    financialclasscode = models.CharField(db_column='FinancialClassCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_Worklist_FinancialClass'


class VwOdbcColWorklistGroup(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    worklistgroup_uid = models.IntegerField(db_column='WorklistGroup_UID', blank=True, null=True)  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorklistFID', blank=True, null=True)  # Field name made lowercase.
    groupfid = models.IntegerField(db_column='GroupFID', blank=True, null=True)  # Field name made lowercase.
    groupcode = models.CharField(db_column='GroupCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_Worklist_Group'


class VwOdbcColWorklistPaymentreason(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    worklistpaymentreason_uid = models.IntegerField(db_column='WorklistPaymentReason_UID')  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorklistFID', blank=True, null=True)  # Field name made lowercase.
    paymentreasonfid = models.IntegerField(db_column='PaymentReasonFID', blank=True, null=True)  # Field name made lowercase.
    paymentreasoncode = models.CharField(db_column='PaymentReasonCode', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_Worklist_PaymentReason'


class VwOdbcColWorklistProfile(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    worklistprofile_uid = models.IntegerField(db_column='WorklistProfile_UID', blank=True, null=True)  # Field name made lowercase.
    worklistfid = models.IntegerField(db_column='WorklistFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    profilecode = models.CharField(db_column='ProfileCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_col_Worklist_Profile'


class VwOdbcCtClaimrun(models.Model):
    claimrun_uid = models.IntegerField(db_column='ClaimRun_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    claimrunfid = models.IntegerField(db_column='ClaimRunFID', blank=True, null=True)  # Field name made lowercase.
    eventfid = models.IntegerField(db_column='EventFID', blank=True, null=True)  # Field name made lowercase.
    eventdate = models.DateTimeField(db_column='EventDate', blank=True, null=True)  # Field name made lowercase.
    isproblem = models.BooleanField(db_column='IsProblem', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ct_ClaimRun'


class VwOdbcCtClaimsubmission(models.Model):
    claimsubmission_uid = models.IntegerField(db_column='ClaimSubmission_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    claimsubmissionfid = models.IntegerField(db_column='ClaimSubmissionFID', blank=True, null=True)  # Field name made lowercase.
    eventfid = models.IntegerField(db_column='EventFID', blank=True, null=True)  # Field name made lowercase.
    eventdate = models.DateTimeField(db_column='EventDate', blank=True, null=True)  # Field name made lowercase.
    isproblem = models.BooleanField(db_column='IsProblem', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=1000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ct_ClaimSubmission'


class VwOdbcCtClaimsubmissionfilematch(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    claimsubmissionfid = models.IntegerField(db_column='ClaimSubmissionFID', blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='FilePath', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filedate = models.DateTimeField(db_column='FileDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ct_ClaimSubmissionFileMatch'


class VwOdbcCtClaimthirdpartystatus(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    thirdpartystatus_uid = models.SmallIntegerField(db_column='ThirdPartyStatus_UID', blank=True, null=True)  # Field name made lowercase.
    statusdescription = models.CharField(db_column='StatusDescription', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ct_ClaimThirdPartyStatus'


class VwOdbcCtEvent(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    event_uid = models.IntegerField(db_column='Event_UID')  # Field name made lowercase.
    eventdescription = models.CharField(db_column='EventDescription', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    displayinapplication = models.BooleanField(db_column='DisplayInApplication', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ct_Event'


class VwOdbcEdiEraClaimstatuscodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    claimcode = models.CharField(db_column='ClaimCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    claimdescription = models.CharField(db_column='ClaimDescription', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_edi_Era_ClaimStatusCodes'


class VwOdbcEdiEraPaymentcodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    paymentcode = models.CharField(db_column='PaymentCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    paymentdescription = models.CharField(db_column='PaymentDescription', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_edi_Era_PaymentCodes'


class VwOdbcEdiEraReport(models.Model):
    report_uid = models.IntegerField(db_column='Report_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    datereceived = models.DateTimeField(db_column='DateReceived', blank=True, null=True)  # Field name made lowercase.
    reportxml = models.TextField(db_column='ReportXML', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    paymentnumber = models.CharField(db_column='PaymentNumber', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    paymentcode = models.CharField(db_column='PaymentCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_edi_Era_Report'


class VwOdbcEdiEraReportclaim(models.Model):
    eraclaim_uid = models.IntegerField(db_column='ERAClaim_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    reportfid = models.IntegerField(db_column='ReportFID', blank=True, null=True)  # Field name made lowercase.
    carrierid = models.CharField(db_column='CarrierID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carriername = models.CharField(db_column='CarrierName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carrierclaimid = models.CharField(db_column='CarrierClaimID', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    patientid = models.CharField(db_column='PatientID', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    claimstatus = models.CharField(db_column='ClaimStatus', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    claimid = models.CharField(db_column='ClaimID', max_length=38, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    visitid = models.IntegerField(db_column='VisitID', blank=True, null=True)  # Field name made lowercase.
    postfailed = models.BooleanField(db_column='PostFailed', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    claimpaymentamount = models.DecimalField(db_column='ClaimPaymentAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    patientfullname = models.CharField(db_column='PatientFullName', max_length=765, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_edi_Era_ReportClaim'


class VwOdbcEdiEraReportclaimadjudication(models.Model):
    eraadjudication_uid = models.IntegerField(db_column='ERAAdjudication_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    reportfid = models.IntegerField(db_column='ReportFID', blank=True, null=True)  # Field name made lowercase.
    eraclaimfid = models.IntegerField(db_column='ERAClaimFID', blank=True, null=True)  # Field name made lowercase.
    remarkcode = models.CharField(db_column='RemarkCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inpatient = models.BooleanField(db_column='InPatient', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_edi_Era_ReportClaimAdjudication'


class VwOdbcEdiEraReportdetail(models.Model):
    erareportdetail_uid = models.IntegerField(db_column='ERAReportDetail_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    reportfid = models.IntegerField(db_column='ReportFID', blank=True, null=True)  # Field name made lowercase.
    eraclaimfid = models.IntegerField(db_column='ERAClaimFID', blank=True, null=True)  # Field name made lowercase.
    chargecode = models.CharField(db_column='ChargeCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    amountcode = models.CharField(db_column='AmountCode', max_length=7, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    amountpaid = models.DecimalField(db_column='AmountPaid', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountadjusted = models.DecimalField(db_column='AmountAdjusted', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountclaim = models.DecimalField(db_column='AmountClaim', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountpatient = models.DecimalField(db_column='AmountPatient', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amountallowed = models.DecimalField(db_column='AmountAllowed', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    amounttakeback = models.DecimalField(db_column='AmountTakeback', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    servicedate = models.CharField(db_column='ServiceDate', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chargedetailid = models.IntegerField(db_column='ChargeDetailID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_edi_Era_ReportDetail'


class VwOdbcEdiEraReportdetailadjudication(models.Model):
    eradetailadjudication_uid = models.IntegerField(db_column='ERADetailAdjudication_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    reportfid = models.IntegerField(db_column='ReportFID', blank=True, null=True)  # Field name made lowercase.
    eraclaimfid = models.IntegerField(db_column='ERAClaimFID', blank=True, null=True)  # Field name made lowercase.
    erareportdetailfid = models.IntegerField(db_column='ERAReportDetailFID', blank=True, null=True)  # Field name made lowercase.
    qualifier = models.CharField(db_column='Qualifier', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    remarkcode = models.CharField(db_column='RemarkCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_edi_Era_ReportDetailAdjudication'


class VwOdbcEdiEraReportdetailreason(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    reportdetailreason_uid = models.IntegerField(db_column='ReportDetailReason_UID')  # Field name made lowercase.
    erareportdetailfid = models.IntegerField(db_column='ERAReportDetailFID', blank=True, null=True)  # Field name made lowercase.
    paymentreasonfid = models.IntegerField(db_column='PaymentReasonFID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    units = models.DecimalField(db_column='Units', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_edi_Era_ReportDetailReason'


class VwOdbcEdiFormats(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    format_uid = models.IntegerField(db_column='Format_UID')  # Field name made lowercase.
    formatcode = models.CharField(db_column='FormatCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    classname = models.CharField(db_column='ClassName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_edi_Formats'


class VwOdbcEdiSubmitters(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    submitter_uid = models.IntegerField(db_column='Submitter_UID')  # Field name made lowercase.
    submittercode = models.CharField(db_column='SubmitterCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    submittername = models.CharField(db_column='SubmitterName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    submitterid = models.CharField(db_column='SubmitterID', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billingid = models.CharField(db_column='BillingID', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ein = models.CharField(db_column='EIN', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tpn = models.CharField(db_column='TPN', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    test = models.BooleanField(db_column='Test', blank=True, null=True)  # Field name made lowercase.
    billingname = models.CharField(db_column='BillingName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billingaptste = models.CharField(db_column='BillingAptSte', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billingaddress = models.CharField(db_column='BillingAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billingcity = models.CharField(db_column='BillingCity', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billingstate = models.CharField(db_column='BillingState', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billingzip = models.CharField(db_column='BillingZip', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billingcontact = models.CharField(db_column='BillingContact', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billingphone = models.CharField(db_column='BillingPhone', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billasgroup = models.BooleanField(db_column='BillAsGroup', blank=True, null=True)  # Field name made lowercase.
    billingseq = models.SmallIntegerField(db_column='BillingSeq', blank=True, null=True)  # Field name made lowercase.
    formatfid = models.IntegerField(db_column='FormatFID', blank=True, null=True)  # Field name made lowercase.
    partnerfid = models.IntegerField(db_column='PartnerFID', blank=True, null=True)  # Field name made lowercase.
    field1 = models.CharField(db_column='Field1', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    field3 = models.CharField(db_column='Field3', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    paytoname = models.BooleanField(db_column='PayToName', blank=True, null=True)  # Field name made lowercase.
    paytoadd = models.BooleanField(db_column='PayToAdd', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_edi_Submitters'


class VwOdbcEhrMessage(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    message_uid = models.IntegerField(db_column='Message_UID')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reminder_datetime = models.DateTimeField(db_column='Reminder_Datetime', blank=True, null=True)  # Field name made lowercase.
    message = models.CharField(db_column='Message', max_length=4000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    finished_datetime = models.DateTimeField(db_column='Finished_Datetime', blank=True, null=True)  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    reminduser = models.CharField(db_column='RemindUser', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.SmallIntegerField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    seendate = models.DateTimeField(db_column='SeenDate', blank=True, null=True)  # Field name made lowercase.
    accountfid = models.IntegerField(db_column='AccountFID', blank=True, null=True)  # Field name made lowercase.
    messagedistfid = models.IntegerField(db_column='MessageDistFID', blank=True, null=True)  # Field name made lowercase.
    messagetype = models.CharField(db_column='MessageType', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    priority = models.CharField(db_column='Priority', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    linkedtypeid = models.IntegerField(db_column='LinkedTypeID', blank=True, null=True)  # Field name made lowercase.
    linkeditemid = models.IntegerField(db_column='LinkedItemID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ehr_Message'


class VwOdbcEhrMessagedist(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    messagedist_uid = models.IntegerField(db_column='MessageDist_UID')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    group_name = models.CharField(db_column='Group_Name', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    group_desc = models.CharField(db_column='Group_Desc', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ehr_MessageDist'


class VwOdbcEntLicensekeys(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    licensename = models.CharField(db_column='LicenseName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ent_LicenseKeys'


class VwOdbcEntPrivilege(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    privilegename = models.CharField(db_column='PrivilegeName', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    categoryfid = models.IntegerField(db_column='CategoryFID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    privcreate = models.BooleanField(db_column='PrivCreate', blank=True, null=True)  # Field name made lowercase.
    privread = models.BooleanField(db_column='PrivRead', blank=True, null=True)  # Field name made lowercase.
    privupdate = models.BooleanField(db_column='PrivUpdate', blank=True, null=True)  # Field name made lowercase.
    privdelete = models.BooleanField(db_column='PrivDelete', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ent_Privilege'


class VwOdbcEntPrivilegecategory(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    category_uid = models.IntegerField(db_column='Category_UID')  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ent_PrivilegeCategory'


class VwOdbcEntRole(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    role_uid = models.IntegerField(db_column='Role_UID')  # Field name made lowercase.
    rolename = models.CharField(db_column='RoleName', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    toolbarcode = models.CharField(db_column='ToolbarCode', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ent_Role'


class VwOdbcEntUser(models.Model):
    user_uid = models.IntegerField(db_column='User_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    rolefid = models.IntegerField(db_column='RoleFID', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    login = models.CharField(db_column='Login', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    passwordchangedat = models.DateTimeField(db_column='PasswordChangedAt', blank=True, null=True)  # Field name made lowercase.
    mustchangepassword = models.BooleanField(db_column='MustChangePassword', blank=True, null=True)  # Field name made lowercase.
    admin = models.BooleanField(db_column='Admin', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='ExpirationDate', blank=True, null=True)  # Field name made lowercase.
    emrproviders = models.CharField(db_column='EMRProviders', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emrcolumns = models.CharField(db_column='EMRColumns', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    promptforproblems = models.BooleanField(db_column='PromptForProblems', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ent_User'


class VwOdbcEntUserstatuses(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    statusdescription = models.CharField(db_column='StatusDescription', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ent_UserStatuses'


class VwOdbcEntLnkCbouserslicensekeys(models.Model):
    userfid = models.IntegerField(db_column='UserFID', blank=True, null=True)  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ent_lnk_CboUsersLicenseKeys'


class VwOdbcEntLnkRolesprivilege(models.Model):
    rolesprivilege_uid = models.IntegerField(db_column='RolesPrivilege_UID')  # Field name made lowercase.
    rolefid = models.IntegerField(db_column='RoleFID', blank=True, null=True)  # Field name made lowercase.
    privilegename = models.CharField(db_column='PrivilegeName', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    privcreate = models.BooleanField(db_column='PrivCreate', blank=True, null=True)  # Field name made lowercase.
    privread = models.BooleanField(db_column='PrivRead', blank=True, null=True)  # Field name made lowercase.
    privupdate = models.BooleanField(db_column='PrivUpdate', blank=True, null=True)  # Field name made lowercase.
    privdelete = models.BooleanField(db_column='PrivDelete', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ent_lnk_RolesPrivilege'


class VwOdbcEntLnkUserEmrprovider(models.Model):
    useremrprovider_uid = models.IntegerField(db_column='UserEMRProvider_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    userfid = models.IntegerField(db_column='UserFID', blank=True, null=True)  # Field name made lowercase.
    providerfid = models.IntegerField(db_column='ProviderFID', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_ent_lnk_User_EMRProvider'


class VwOdbcFcmFile(models.Model):
    file_uid = models.IntegerField(db_column='File_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filelocation = models.CharField(db_column='FileLocation', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filetype = models.CharField(db_column='FileType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fileext = models.CharField(db_column='FileExt', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filesize = models.IntegerField(db_column='FileSize', blank=True, null=True)  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    visitfid = models.IntegerField(db_column='VisitFID', blank=True, null=True)  # Field name made lowercase.
    facilityfid = models.IntegerField(db_column='FacilityFID', blank=True, null=True)  # Field name made lowercase.
    referringproviderfid = models.IntegerField(db_column='ReferringProviderFID', blank=True, null=True)  # Field name made lowercase.
    dos = models.DateTimeField(db_column='DOS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    printedat = models.DateTimeField(db_column='PrintedAt', blank=True, null=True)  # Field name made lowercase.
    printedby = models.CharField(db_column='PrintedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reviewedat = models.DateTimeField(db_column='ReviewedAt', blank=True, null=True)  # Field name made lowercase.
    reviewedby = models.CharField(db_column='ReviewedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    approvedat = models.DateTimeField(db_column='ApprovedAt', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lockedat = models.DateTimeField(db_column='LockedAt', blank=True, null=True)  # Field name made lowercase.
    lockedby = models.CharField(db_column='LockedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    revision = models.IntegerField(db_column='Revision', blank=True, null=True)  # Field name made lowercase.
    zipmode = models.SmallIntegerField(db_column='ZipMode', blank=True, null=True)  # Field name made lowercase.
    encoded = models.BooleanField(db_column='Encoded', blank=True, null=True)  # Field name made lowercase.
    serverfile = models.BooleanField(db_column='ServerFile', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    catcodelist = models.CharField(db_column='CatCodeList', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_fcm_File'


class VwOdbcFcmFiledochistory(models.Model):
    filedochistory_uid = models.IntegerField(db_column='FileDocHistory_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    filefid = models.IntegerField(db_column='FileFID', blank=True, null=True)  # Field name made lowercase.
    revision = models.IntegerField(db_column='Revision', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filelocation = models.CharField(db_column='FileLocation', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filesize = models.IntegerField(db_column='FileSize', blank=True, null=True)  # Field name made lowercase.
    comments = models.CharField(db_column='Comments', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    printedat = models.DateTimeField(db_column='PrintedAt', blank=True, null=True)  # Field name made lowercase.
    printedby = models.CharField(db_column='PrintedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reviewedat = models.DateTimeField(db_column='ReviewedAt', blank=True, null=True)  # Field name made lowercase.
    reviewedby = models.CharField(db_column='ReviewedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    approvedat = models.DateTimeField(db_column='ApprovedAt', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lockedat = models.DateTimeField(db_column='LockedAt', blank=True, null=True)  # Field name made lowercase.
    lockedby = models.CharField(db_column='LockedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countchars = models.IntegerField(db_column='CountChars', blank=True, null=True)  # Field name made lowercase.
    countcharswspaces = models.IntegerField(db_column='CountCharsWSpaces', blank=True, null=True)  # Field name made lowercase.
    countwords = models.IntegerField(db_column='CountWords', blank=True, null=True)  # Field name made lowercase.
    countlines = models.IntegerField(db_column='CountLines', blank=True, null=True)  # Field name made lowercase.
    countparas = models.IntegerField(db_column='CountParas', blank=True, null=True)  # Field name made lowercase.
    countpages = models.IntegerField(db_column='CountPages', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_fcm_FileDocHistory'


class VwOdbcFcmFiledocinfo(models.Model):
    filedocinfo_uid = models.IntegerField(db_column='FileDocInfo_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    filefid = models.IntegerField(db_column='FileFID', blank=True, null=True)  # Field name made lowercase.
    resourcefid = models.IntegerField(db_column='ResourceFID', blank=True, null=True)  # Field name made lowercase.
    countchars = models.IntegerField(db_column='CountChars', blank=True, null=True)  # Field name made lowercase.
    countcharswspaces = models.IntegerField(db_column='CountCharsWSpaces', blank=True, null=True)  # Field name made lowercase.
    countwords = models.IntegerField(db_column='CountWords', blank=True, null=True)  # Field name made lowercase.
    countlines = models.IntegerField(db_column='CountLines', blank=True, null=True)  # Field name made lowercase.
    countparas = models.IntegerField(db_column='CountParas', blank=True, null=True)  # Field name made lowercase.
    countpages = models.IntegerField(db_column='CountPages', blank=True, null=True)  # Field name made lowercase.
    templatedescription = models.CharField(db_column='TemplateDescription', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_fcm_FileDocInfo'


class VwOdbcFcmFiledocinfolog(models.Model):
    filedocinfolog_uid = models.IntegerField(db_column='FileDocInfoLog_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    filedocinfofid = models.IntegerField(db_column='FileDocInfoFID', blank=True, null=True)  # Field name made lowercase.
    action = models.SmallIntegerField(db_column='Action', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_fcm_FileDocInfoLog'


class VwOdbcFcmFilelog(models.Model):
    filelog_uid = models.IntegerField(db_column='FileLog_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    filefid = models.IntegerField(db_column='FileFID', blank=True, null=True)  # Field name made lowercase.
    action = models.SmallIntegerField(db_column='Action', blank=True, null=True)  # Field name made lowercase.
    notes = models.CharField(db_column='Notes', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_fcm_FileLog'


class VwOdbcFcmLnkFilefilecategory(models.Model):
    filefilecategory_uid = models.IntegerField(db_column='FileFileCategory_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    filefid = models.IntegerField(db_column='FileFID', blank=True, null=True)  # Field name made lowercase.
    filecategoryfid = models.IntegerField(db_column='FileCategoryFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_fcm_lnk_FileFileCategory'


class VwOdbcFcmLnkFileresource(models.Model):
    fileresource_uid = models.IntegerField(db_column='FileResource_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    resourcefid = models.IntegerField(db_column='ResourceFID', blank=True, null=True)  # Field name made lowercase.
    filefid = models.IntegerField(db_column='FileFID', blank=True, null=True)  # Field name made lowercase.
    downloadstatus = models.IntegerField(db_column='DownloadStatus', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_fcm_lnk_FileResource'


class VwOdbcHcPeriod(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    period_uid = models.IntegerField(db_column='Period_UID')  # Field name made lowercase.
    periodmonthfid = models.IntegerField(db_column='PeriodMonthFID', blank=True, null=True)  # Field name made lowercase.
    periodmonth = models.CharField(db_column='PeriodMonth', max_length=9, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    periodyear = models.IntegerField(db_column='PeriodYear', blank=True, null=True)  # Field name made lowercase.
    periodstatusfid = models.IntegerField(db_column='PeriodStatusFID', blank=True, null=True)  # Field name made lowercase.
    periodstatus = models.CharField(db_column='PeriodStatus', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    periodstepfid = models.IntegerField(db_column='PeriodStepFID', blank=True, null=True)  # Field name made lowercase.
    periodstep = models.CharField(db_column='PeriodStep', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateTimeField(db_column='EffectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    calendarstartdate = models.DateTimeField(db_column='CalendarStartDate', blank=True, null=True)  # Field name made lowercase.
    calendarenddate = models.DateTimeField(db_column='CalendarEndDate', blank=True, null=True)  # Field name made lowercase.
    effectivestartdate = models.DateTimeField(db_column='EffectiveStartDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_hc_Period'


class VwOdbcMainAccountsreceivable(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    accountreceivable_uid = models.IntegerField(db_column='AccountReceivable_UID')  # Field name made lowercase.
    lastyeareoy = models.DecimalField(db_column='LastYearEOY', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ar_current = models.DecimalField(db_column='AR_Current', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ar_30_days = models.DecimalField(db_column='AR_30_Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ar_60_days = models.DecimalField(db_column='AR_60_Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ar_90_days = models.DecimalField(db_column='AR_90_Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ar_morethan120days = models.DecimalField(db_column='AR_MoreThan120Days', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    unappliedmoney = models.DecimalField(db_column='UnappliedMoney', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalbalance = models.DecimalField(db_column='TotalBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_main_AccountsReceivable'


class VwOdbcMainFinancialsummaries(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    financialsummary_uid = models.IntegerField(db_column='FinancialSummary_UID')  # Field name made lowercase.
    mtd_charges = models.DecimalField(db_column='MTD_Charges', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mtd_payments = models.DecimalField(db_column='MTD_Payments', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mtd_writeoffs = models.DecimalField(db_column='MTD_WriteOffs', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    mtd_units = models.DecimalField(db_column='MTD_Units', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    ytd_charges = models.DecimalField(db_column='YTD_Charges', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ytd_payments = models.DecimalField(db_column='YTD_Payments', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ytd_writeoffs = models.DecimalField(db_column='YTD_WriteOffs', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    ytd_units = models.DecimalField(db_column='YTD_Units', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    totalbalance = models.DecimalField(db_column='TotalBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    totalunppliedmoney = models.DecimalField(db_column='TotalUnppliedMoney', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_main_FinancialSummaries'


class VwOdbcMainNotes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    note_uid = models.IntegerField(db_column='Note_UID')  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_main_Notes'


class VwOdbcMainSystemdefault(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    systemdefault_uid = models.IntegerField(db_column='SystemDefault_UID')  # Field name made lowercase.
    categoryfid = models.IntegerField(db_column='CategoryFID', blank=True, null=True)  # Field name made lowercase.
    sequencenumber = models.SmallIntegerField(db_column='SequenceNumber', blank=True, null=True)  # Field name made lowercase.
    defaultname = models.CharField(db_column='DefaultName', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elementtype = models.CharField(db_column='ElementType', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datatype = models.CharField(db_column='Datatype', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    extrainfo = models.CharField(db_column='ExtraInfo', max_length=3000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    systemdefault = models.BooleanField(db_column='SystemDefault', blank=True, null=True)  # Field name made lowercase.
    readonly = models.BooleanField(db_column='ReadOnly', blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    defaultvaluedescription = models.CharField(db_column='DefaultValueDescription', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cboonly = models.BooleanField(db_column='CBOOnly', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_main_SystemDefault'


class VwOdbcMainSystemdefaultcategory(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    category_uid = models.IntegerField(db_column='Category_UID')  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    parentcategoryfid = models.IntegerField(db_column='ParentCategoryFID', blank=True, null=True)  # Field name made lowercase.
    sequencenumber = models.SmallIntegerField(db_column='SequenceNumber', blank=True, null=True)  # Field name made lowercase.
    featureaccessrequired = models.CharField(db_column='FeatureAccessRequired', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_main_SystemDefaultCategory'


class VwOdbcMainSystemdefaultlicensekey(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    systemdefaultfid = models.IntegerField(db_column='SystemDefaultFID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    valuedescription = models.CharField(db_column='ValueDescription', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_main_SystemDefaultLicenseKey'


class VwOdbcMainUserfiles(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    userfile_uid = models.IntegerField(db_column='UserFile_UID')  # Field name made lowercase.
    userfield1 = models.CharField(db_column='UserField1', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfield2 = models.CharField(db_column='UserField2', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfield3 = models.CharField(db_column='UserField3', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfield4 = models.CharField(db_column='UserField4', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfield5 = models.CharField(db_column='UserField5', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfield6 = models.CharField(db_column='UserField6', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfield7 = models.CharField(db_column='UserField7', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfield8 = models.CharField(db_column='UserField8', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_main_UserFiles'


class VwOdbcMfAccounttypes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    accounttype_uid = models.IntegerField(db_column='AccountType_UID')  # Field name made lowercase.
    accounttypecode = models.CharField(db_column='AccountTypeCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    smallbalancewriteoffs = models.BooleanField(db_column='SmallBalanceWriteOffs', blank=True, null=True)  # Field name made lowercase.
    amtslessthan = models.DecimalField(db_column='AmtsLessThan', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    writeoffcodefid = models.IntegerField(db_column='WriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    minimumstatementbalance = models.DecimalField(db_column='MinimumStatementBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    calculatefinancecharge = models.BooleanField(db_column='CalculateFinanceCharge', blank=True, null=True)  # Field name made lowercase.
    sendstatement = models.BooleanField(db_column='SendStatement', blank=True, null=True)  # Field name made lowercase.
    stmtformatname = models.CharField(db_column='STMTFormatName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stmtformatformfid = models.IntegerField(db_column='STMTFormatFormFID', blank=True, null=True)  # Field name made lowercase.
    billingcycle = models.DecimalField(db_column='BillingCycle', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    finchgpercentage = models.DecimalField(db_column='FinChgPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    finchgminimumbalance = models.DecimalField(db_column='FinChgMinimumBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    finchgminimumcharge = models.DecimalField(db_column='FinChgMinimumCharge', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    finchgstarttime = models.CharField(db_column='FinChgStartTime', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    calculatestatementcharges = models.BooleanField(db_column='CalculateStatementCharges', blank=True, null=True)  # Field name made lowercase.
    statementchargeamount = models.DecimalField(db_column='StatementChargeAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    chargecodefid = models.IntegerField(db_column='ChargeCodeFID', blank=True, null=True)  # Field name made lowercase.
    stmttypebfoi = models.BooleanField(db_column='StmtTypeBFOI', blank=True, null=True)  # Field name made lowercase.
    dunningmessagefid = models.IntegerField(db_column='DunningMessageFID', blank=True, null=True)  # Field name made lowercase.
    dunningmessage30fid = models.IntegerField(db_column='DunningMessage30FID', blank=True, null=True)  # Field name made lowercase.
    dunningmessage60fid = models.IntegerField(db_column='DunningMessage60FID', blank=True, null=True)  # Field name made lowercase.
    dunningmessage90fid = models.IntegerField(db_column='DunningMessage90FID', blank=True, null=True)  # Field name made lowercase.
    dunningmessage120fid = models.IntegerField(db_column='DunningMessage120FID', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    onestatementrequired = models.BooleanField(db_column='OneStatementRequired', blank=True, null=True)  # Field name made lowercase.
    statementsbeforecollections = models.SmallIntegerField(db_column='StatementsBeforeCollections', blank=True, null=True)  # Field name made lowercase.
    collectionrulefid = models.IntegerField(db_column='CollectionRuleFID', blank=True, null=True)  # Field name made lowercase.
    collectionformatfid = models.IntegerField(db_column='CollectionFormatFID', blank=True, null=True)  # Field name made lowercase.
    statementformatfid = models.IntegerField(db_column='StatementFormatFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_AccountTypes'


class VwOdbcMfCobcodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    cobcode_uid = models.IntegerField(db_column='COBCode_UID')  # Field name made lowercase.
    cobcode = models.CharField(db_column='COBCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_COBCodes'


class VwOdbcMfCptimportdefaults(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    cptimportdefault_uid = models.IntegerField(db_column='CPTImportDefault_UID')  # Field name made lowercase.
    defaultname = models.CharField(db_column='DefaultName', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lowcode = models.CharField(db_column='LowCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    highcode = models.CharField(db_column='HighCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    posvalue = models.CharField(db_column='POSValue', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tosvalue = models.CharField(db_column='TOSValue', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chargecodecategoryfid = models.IntegerField(db_column='ChargeCodeCategoryFID', blank=True, null=True)  # Field name made lowercase.
    tax = models.BooleanField(db_column='Tax', blank=True, null=True)  # Field name made lowercase.
    ancillary = models.BooleanField(db_column='Ancillary', blank=True, null=True)  # Field name made lowercase.
    electronic = models.BooleanField(db_column='Electronic', blank=True, null=True)  # Field name made lowercase.
    reqclia = models.BooleanField(db_column='ReqCLIA', blank=True, null=True)  # Field name made lowercase.
    billinsurance = models.BooleanField(db_column='BillInsurance', blank=True, null=True)  # Field name made lowercase.
    billpatient = models.BooleanField(db_column='BillPatient', blank=True, null=True)  # Field name made lowercase.
    assesscopay = models.BooleanField(db_column='AssessCopay', blank=True, null=True)  # Field name made lowercase.
    overwrite = models.BooleanField(db_column='Overwrite', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_CPTImportDefaults'


class VwOdbcMfCarriercategories(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    carriercategory_uid = models.IntegerField(db_column='CarrierCategory_UID')  # Field name made lowercase.
    carriercategorycode = models.CharField(db_column='CarrierCategoryCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carriercategorydescription = models.CharField(db_column='CarrierCategoryDescription', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_CarrierCategories'


class VwOdbcMfCarriers(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    carrier_uid = models.IntegerField(db_column='Carrier_UID')  # Field name made lowercase.
    carriercode = models.CharField(db_column='CarrierCode', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carriername = models.CharField(db_column='CarrierName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    aptste = models.CharField(db_column='AptSte', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(db_column='AreaCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    paperformfid = models.IntegerField(db_column='PaperFormFID', blank=True, null=True)  # Field name made lowercase.
    standardcopaydollaramt = models.DecimalField(db_column='StandardCopayDollarAmt', max_digits=10, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    standardcopaypercent = models.DecimalField(db_column='StandardCoPayPercent', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    notefid = models.IntegerField(db_column='NoteFID', blank=True, null=True)  # Field name made lowercase.
    dme = models.BooleanField(db_column='DME', blank=True, null=True)  # Field name made lowercase.
    edicpidnumber = models.CharField(db_column='EDICPIDNumber', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elecformfid = models.IntegerField(db_column='ElecFormFID', blank=True, null=True)  # Field name made lowercase.
    medigapnumber = models.CharField(db_column='MedigapNumber', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    typeofinsurance = models.CharField(db_column='TypeofInsurance', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sourceofpayment = models.CharField(db_column='SourceofPayment', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    statecoveragecode = models.CharField(db_column='StateCoverageCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    elecclaimsbillprimaryonly = models.BooleanField(db_column='ElecClaimsBillPrimaryOnly', blank=True, null=True)  # Field name made lowercase.
    payorid = models.CharField(db_column='PayorID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    payorsubid = models.CharField(db_column='PayorSubID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    eligibilityphonenumber = models.CharField(db_column='EligibilityPhoneNumber', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    eligibilityphoneextension = models.CharField(db_column='EligibilityPhoneExtension', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    preauthphonenumber = models.CharField(db_column='PreAuthPhoneNumber', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    preauthphoneextension = models.CharField(db_column='PreAuthPhoneExtension', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    faxnumber = models.CharField(db_column='FaxNumber', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    providerrelationsphonenumber = models.CharField(db_column='ProviderRelationsPhoneNumber', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    providerrelationsphoneextension = models.CharField(db_column='ProviderRelationsPhoneExtension', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emailaddress = models.CharField(db_column='EmailAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    carriercategoryfid = models.IntegerField(db_column='CarrierCategoryFID', blank=True, null=True)  # Field name made lowercase.
    financialsummaryfid = models.IntegerField(db_column='FinancialSummaryFID', blank=True, null=True)  # Field name made lowercase.
    accountreceivablefid = models.IntegerField(db_column='AccountReceivableFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    checkbox = models.CharField(db_column='Checkbox', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    requirereferral = models.BooleanField(db_column='RequireReferral', blank=True, null=True)  # Field name made lowercase.
    mtdclaims = models.IntegerField(db_column='MTDClaims', blank=True, null=True)  # Field name made lowercase.
    ytdclaims = models.IntegerField(db_column='YTDClaims', blank=True, null=True)  # Field name made lowercase.
    billzerodollarclaims = models.BooleanField(db_column='BillZeroDollarClaims', blank=True, null=True)  # Field name made lowercase.
    posaliaschangedat = models.DateTimeField(db_column='POSAliasChangedAt', blank=True, null=True)  # Field name made lowercase.
    tosaliaschangedat = models.DateTimeField(db_column='TOSAliasChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    approvedat = models.DateTimeField(db_column='ApprovedAt', blank=True, null=True)  # Field name made lowercase.
    approvedby = models.CharField(db_column='ApprovedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    provideridrequired = models.BooleanField(db_column='ProviderIDRequired', blank=True, null=True)  # Field name made lowercase.
    ediagreementrequired = models.BooleanField(db_column='EDIAgreementRequired', blank=True, null=True)  # Field name made lowercase.
    ediagreementapproved = models.BooleanField(db_column='EDIAgreementApproved', blank=True, null=True)  # Field name made lowercase.
    wasimported = models.BooleanField(db_column='WasImported', blank=True, null=True)  # Field name made lowercase.
    importcode = models.CharField(db_column='ImportCode', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usemastercarrierlist = models.BooleanField(db_column='UseMasterCarrierList', blank=True, null=True)  # Field name made lowercase.
    mergedtocarrierfid = models.IntegerField(db_column='MergedToCarrierFID', blank=True, null=True)  # Field name made lowercase.
    secondarypaperformfid = models.IntegerField(db_column='SecondaryPaperFormFID', blank=True, null=True)  # Field name made lowercase.
    grpprovidprefix = models.CharField(db_column='GrpProvIDPrefix', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    grpidsuffix = models.CharField(db_column='GrpIDSuffix', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    providsuffix = models.CharField(db_column='ProvIDSuffix', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    includesupervisingprovider = models.SmallIntegerField(db_column='IncludeSupervisingProvider', blank=True, null=True)  # Field name made lowercase.
    includeorderingprovider = models.SmallIntegerField(db_column='IncludeOrderingProvider', blank=True, null=True)  # Field name made lowercase.
    useprovidernpifid = models.IntegerField(db_column='UseProviderNPIFID', blank=True, null=True)  # Field name made lowercase.
    suppressrenderinginfo = models.BooleanField(db_column='SuppressRenderingInfo', blank=True, null=True)  # Field name made lowercase.
    instcontactname = models.CharField(db_column='InstContactName', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instaddress1 = models.CharField(db_column='InstAddress1', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instaddress2 = models.CharField(db_column='InstAddress2', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instzipcode = models.CharField(db_column='InstZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instcity = models.CharField(db_column='InstCity', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    inststate = models.CharField(db_column='InstState', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instareacode = models.CharField(db_column='InstAreaCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    insteligibilityphonenumber = models.CharField(db_column='InstEligibilityPhoneNumber', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    insteligibilityphoneextension = models.CharField(db_column='InstEligibilityPhoneExtension', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instpreauthphonenumber = models.CharField(db_column='InstPreAuthPhoneNumber', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instpreauthphoneextension = models.CharField(db_column='InstPreAuthPhoneExtension', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instproviderrelationsphonenumber = models.CharField(db_column='InstProviderRelationsPhoneNumber', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instproviderrelationsphoneextension = models.CharField(db_column='InstProviderRelationsPhoneExtension', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instfaxnumber = models.CharField(db_column='InstFaxNumber', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instemailaddress = models.CharField(db_column='InstEmailAddress', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instprovideridrequired = models.BooleanField(db_column='InstProviderIDRequired', blank=True, null=True)  # Field name made lowercase.
    instediagreementrequired = models.BooleanField(db_column='InstEDIAgreementRequired', blank=True, null=True)  # Field name made lowercase.
    instediagreementapproved = models.BooleanField(db_column='InstEDIAgreementApproved', blank=True, null=True)  # Field name made lowercase.
    instgrpprovidprefix = models.CharField(db_column='InstGrpProvIDPrefix', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instpaperformfid = models.IntegerField(db_column='InstPaperFormFID', blank=True, null=True)  # Field name made lowercase.
    instelecformfid = models.IntegerField(db_column='InstElecFormFID', blank=True, null=True)  # Field name made lowercase.
    instedicpidnumber = models.CharField(db_column='InstEDICPIDNumber', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instpayorid = models.CharField(db_column='InstPayorID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instpayorsubid = models.CharField(db_column='InstPayorSubID', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instbillzerodollarclaims = models.BooleanField(db_column='InstBillZeroDollarClaims', blank=True, null=True)  # Field name made lowercase.
    primaryclaimtypefid = models.IntegerField(db_column='PrimaryClaimTypeFID', blank=True, null=True)  # Field name made lowercase.
    secondaryclaimtypefid = models.IntegerField(db_column='SecondaryClaimTypeFID', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    noteschangedat = models.DateTimeField(db_column='NotesChangedAt', blank=True, null=True)  # Field name made lowercase.
    instnotes = models.TextField(db_column='InstNotes', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    instnoteschangedat = models.DateTimeField(db_column='InstNotesChangedAt', blank=True, null=True)  # Field name made lowercase.
    webaddress = models.CharField(db_column='WebAddress', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instwebaddress = models.CharField(db_column='InstWebAddress', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    othercontact = models.CharField(db_column='OtherContact', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instothercontact = models.CharField(db_column='InstOtherContact', max_length=200, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    instuseprovidernpifid = models.IntegerField(db_column='InstUseProviderNPIFID', blank=True, null=True)  # Field name made lowercase.
    renderingqualfid = models.IntegerField(db_column='RenderingQualFID', blank=True, null=True)  # Field name made lowercase.
    renderingsourcefid = models.IntegerField(db_column='RenderingSourceFID', blank=True, null=True)  # Field name made lowercase.
    billingqualfid = models.IntegerField(db_column='BillingQualFID', blank=True, null=True)  # Field name made lowercase.
    billingsourcefid = models.IntegerField(db_column='BillingSourceFID', blank=True, null=True)  # Field name made lowercase.
    referringqualfid = models.IntegerField(db_column='ReferringQualFID', blank=True, null=True)  # Field name made lowercase.
    referringsourcefid = models.IntegerField(db_column='ReferringSourceFID', blank=True, null=True)  # Field name made lowercase.
    billasfid = models.IntegerField(db_column='BillAsFID', blank=True, null=True)  # Field name made lowercase.
    enablemonthlybilling = models.BooleanField(db_column='EnableMonthlyBilling', blank=True, null=True)  # Field name made lowercase.
    icd9enddate = models.DateTimeField(db_column='Icd9EndDate', blank=True, null=True)  # Field name made lowercase.
    icd10startdate = models.DateTimeField(db_column='Icd10StartDate', blank=True, null=True)  # Field name made lowercase.
    followprimarycodeset = models.BooleanField(db_column='FollowPrimaryCodeSet', blank=True, null=True)  # Field name made lowercase.
    financialclassfid = models.IntegerField(db_column='FinancialClassFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_Carriers'


class VwOdbcMfChargesliptemplates(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    chargesliptemplate_uid = models.IntegerField(db_column='ChargeSlipTemplate_UID')  # Field name made lowercase.
    chargesliptemplatecode = models.CharField(db_column='ChargeSlipTemplateCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chargesliptemplatedescription = models.CharField(db_column='ChargeSlipTemplateDescription', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    codeset = models.IntegerField(db_column='CodeSet', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ChargeSlipTemplates'


class VwOdbcMfChargesliptemplatesRows(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    chargesliptemplatefid = models.IntegerField(db_column='ChargeSlipTemplateFID', blank=True, null=True)  # Field name made lowercase.
    itemcode1 = models.CharField(db_column='ItemCode1', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemdescription1 = models.CharField(db_column='ItemDescription1', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemcode2 = models.CharField(db_column='ItemCode2', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemdescription2 = models.CharField(db_column='ItemDescription2', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemcode3 = models.CharField(db_column='ItemCode3', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemdescription3 = models.CharField(db_column='ItemDescription3', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemcode4 = models.CharField(db_column='ItemCode4', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemdescription4 = models.CharField(db_column='ItemDescription4', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    itemtype = models.CharField(db_column='ItemType', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rownum = models.IntegerField(db_column='RowNum', blank=True, null=True)  # Field name made lowercase.
    headeronly = models.BooleanField(db_column='HeaderOnly', blank=True, null=True)  # Field name made lowercase.
    numberofcolumns = models.SmallIntegerField(db_column='NumberOfColumns', blank=True, null=True)  # Field name made lowercase.
    templatediagrowcount = models.SmallIntegerField(db_column='TemplateDiagRowCount', blank=True, null=True)  # Field name made lowercase.
    templateprocrowcount = models.SmallIntegerField(db_column='TemplateProcRowCount', blank=True, null=True)  # Field name made lowercase.
    displayrowtype = models.SmallIntegerField(db_column='DisplayRowType', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ChargeSlipTemplates_Rows'


class VwOdbcMfChargesliptemplatesSDiagnosis(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    chargeslipdiag_uid = models.IntegerField(db_column='ChargeslipDiag_UID')  # Field name made lowercase.
    diagnosiscodefid = models.IntegerField(db_column='DiagnosisCodeFID', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    chargesliptemplatefid = models.IntegerField(db_column='ChargeSlipTemplateFID', blank=True, null=True)  # Field name made lowercase.
    diagcode = models.CharField(db_column='DiagCode', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    hasleaf = models.BooleanField(db_column='HasLeaf', blank=True, null=True)  # Field name made lowercase.
    diagnosisdescription = models.CharField(db_column='DiagnosisDescription', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diagnosissequence = models.SmallIntegerField(db_column='DiagnosisSequence', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    collapsed = models.BooleanField(db_column='Collapsed', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ChargeslipTemplates_s_Diagnosis'


class VwOdbcMfChargesliptemplatesSProcedures(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    chargesliptemplateprocedures_uid = models.IntegerField(db_column='ChargeslipTemplateProcedures_UID')  # Field name made lowercase.
    chargecodefid = models.IntegerField(db_column='ChargeCodeFID', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    chargesliptemplatefid = models.IntegerField(db_column='ChargeSlipTemplateFID', blank=True, null=True)  # Field name made lowercase.
    proceduredescription = models.CharField(db_column='ProcedureDescription', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    proceduresequence = models.SmallIntegerField(db_column='ProcedureSequence', blank=True, null=True)  # Field name made lowercase.
    collapsed = models.BooleanField(db_column='Collapsed', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ChargeslipTemplates_s_Procedures'


class VwOdbcMfClaimeditexceptions(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    claimeditexception_uid = models.IntegerField(db_column='ClaimEditException_UID')  # Field name made lowercase.
    claimeditfid = models.IntegerField(db_column='ClaimEditFID', blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    ignoreedit = models.BooleanField(db_column='IgnoreEdit', blank=True, null=True)  # Field name made lowercase.
    shorterrormessage = models.CharField(db_column='ShortErrorMessage', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ClaimEditExceptions'


class VwOdbcMfClaimeditstatuses(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    claimeditstatus_uid = models.IntegerField(db_column='ClaimEditStatus_UID')  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.SmallIntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ClaimEditStatuses'


class VwOdbcMfClaimedits(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    claimedit_uid = models.IntegerField(db_column='ClaimEdit_UID')  # Field name made lowercase.
    editnumber = models.BigIntegerField(db_column='EditNumber', blank=True, null=True)  # Field name made lowercase.
    errormessage = models.CharField(db_column='ErrorMessage', max_length=4096, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    shorterrormessage = models.CharField(db_column='ShortErrorMessage', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    claimeditchecksum = models.IntegerField(db_column='ClaimEditChecksum', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ClaimEdits'


class VwOdbcMfCollectionrule(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    collectionrule_uid = models.IntegerField(db_column='CollectionRule_UID')  # Field name made lowercase.
    rulename = models.CharField(db_column='RuleName', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_CollectionRule'


class VwOdbcMfCollectionrulestep(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    collectionrulestep_uid = models.IntegerField(db_column='CollectionRuleStep_UID')  # Field name made lowercase.
    collectionrulefid = models.IntegerField(db_column='CollectionRuleFID', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.SmallIntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.
    collectiontemplatefid = models.IntegerField(db_column='CollectionTemplateFID', blank=True, null=True)  # Field name made lowercase.
    iscollectionagency = models.BooleanField(db_column='IsCollectionAgency', blank=True, null=True)  # Field name made lowercase.
    daysnopayment = models.SmallIntegerField(db_column='DaysNoPayment', blank=True, null=True)  # Field name made lowercase.
    writeoffbalance = models.DecimalField(db_column='WriteOffBalance', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    writeoffcodefid = models.IntegerField(db_column='WriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    display = models.IntegerField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    writeoffentireaccount = models.BooleanField(db_column='WriteoffEntireAccount', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_CollectionRuleStep'


class VwOdbcMfCustomclaimfield(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    claimfield_uid = models.IntegerField(db_column='ClaimField_UID')  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fielddescription = models.CharField(db_column='FieldDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    datatypefid = models.IntegerField(db_column='DataTypeFID', blank=True, null=True)  # Field name made lowercase.
    subtypefid = models.IntegerField(db_column='SubTypeFID', blank=True, null=True)  # Field name made lowercase.
    userfileselectlistfid = models.IntegerField(db_column='UserFileSelectListFID', blank=True, null=True)  # Field name made lowercase.
    isrequired = models.BooleanField(db_column='IsRequired', blank=True, null=True)  # Field name made lowercase.
    includeintooltip = models.BooleanField(db_column='IncludeInTooltip', blank=True, null=True)  # Field name made lowercase.
    includeinepisode = models.BooleanField(db_column='IncludeInEpisode', blank=True, null=True)  # Field name made lowercase.
    displaylevelfid = models.IntegerField(db_column='DisplayLevelFID', blank=True, null=True)  # Field name made lowercase.
    defaulttextvalue = models.CharField(db_column='DefaultTextValue', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    defaultfidvalue = models.IntegerField(db_column='DefaultFIDValue', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)  # Field name made lowercase.
    ishipaa = models.BooleanField(db_column='IsHipaa', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_CustomClaimField'


class VwOdbcMfDrgcodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    drgcode_uid = models.IntegerField(db_column='DRGCode_UID')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_DRGCodes'


class VwOdbcMfDiagnosiscodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    diagnosiscode_uid = models.IntegerField(db_column='DiagnosisCode_UID')  # Field name made lowercase.
    diagnosiscode = models.CharField(db_column='DiagnosisCode', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    insurancedescription = models.CharField(db_column='InsuranceDescription', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    statementdescription = models.CharField(db_column='StatementDescription', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diagnosisxref1 = models.CharField(db_column='DiagnosisXRef1', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diagnosisxref2 = models.CharField(db_column='DiagnosisXRef2', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diagnosisxref3 = models.CharField(db_column='DiagnosisXref3', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    codeset = models.SmallIntegerField(db_column='CodeSet', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_DiagnosisCodes'


class VwOdbcMfDocumenttemplateexceptions(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    documenttemplateexception_uid = models.IntegerField(db_column='DocumentTemplateException_UID')  # Field name made lowercase.
    documenttemplatefid = models.IntegerField(db_column='DocumentTemplateFID', blank=True, null=True)  # Field name made lowercase.
    printername = models.CharField(db_column='PrinterName', max_length=256, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    adjustleftmargin = models.DecimalField(db_column='AdjustLeftMargin', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    adjusttopmargin = models.DecimalField(db_column='AdjustTopMargin', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_DocumentTemplateExceptions'


class VwOdbcMfDocumenttemplates(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    documenttemplate_uid = models.IntegerField(db_column='DocumentTemplate_UID')  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    templatetype = models.CharField(db_column='TemplateType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filename = models.CharField(db_column='FileName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filelocation = models.CharField(db_column='FileLocation', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    defaultdocumentname = models.CharField(db_column='DefaultDocumentName', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    defaultdocumentdescription = models.CharField(db_column='DefaultDocumentDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    documentcontents = models.TextField(db_column='DocumentContents', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    documentcontentschangedat = models.DateTimeField(db_column='DocumentContentsChangedAt', blank=True, null=True)  # Field name made lowercase.
    adjustleftmargin = models.DecimalField(db_column='AdjustLeftMargin', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    adjusttopmargin = models.DecimalField(db_column='AdjustTopMargin', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    countcharacters = models.IntegerField(db_column='CountCharacters', blank=True, null=True)  # Field name made lowercase.
    countcharswspaces = models.IntegerField(db_column='CountCharsWSpaces', blank=True, null=True)  # Field name made lowercase.
    countwords = models.IntegerField(db_column='CountWords', blank=True, null=True)  # Field name made lowercase.
    countlines = models.IntegerField(db_column='CountLines', blank=True, null=True)  # Field name made lowercase.
    countparas = models.IntegerField(db_column='CountParas', blank=True, null=True)  # Field name made lowercase.
    countpages = models.IntegerField(db_column='CountPages', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_DocumentTemplates'


class VwOdbcMfDunningmessages(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    dunningmessage_uid = models.IntegerField(db_column='DunningMessage_UID')  # Field name made lowercase.
    dunningmessagecode = models.CharField(db_column='DunningMessageCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    messagedescription = models.CharField(db_column='MessageDescription', max_length=120, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_DunningMessages'


class VwOdbcMfEmployers(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    employer_uid = models.IntegerField(db_column='Employer_UID')  # Field name made lowercase.
    employercode = models.CharField(db_column='EmployerCode', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    employername = models.CharField(db_column='EmployerName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptste = models.CharField(db_column='AptSte', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(db_column='AreaCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    officephone = models.CharField(db_column='OfficePhone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    officeextension = models.CharField(db_column='OfficeExtension', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user1 = models.CharField(db_column='User1', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user2 = models.CharField(db_column='User2', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user3 = models.CharField(db_column='User3', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    user4 = models.CharField(db_column='User4', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    workerscompcarrierfid = models.IntegerField(db_column='WorkersCompCarrierFID', blank=True, null=True)  # Field name made lowercase.
    workerscomppolicynumber = models.CharField(db_column='WorkersCompPolicyNumber', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    workerscompsubscriberfid = models.IntegerField(db_column='WorkersCompSubscriberFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    noteschangedat = models.DateTimeField(db_column='NotesChangedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_Employers'


class VwOdbcMfFacilities(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    facility_uid = models.IntegerField(db_column='Facility_UID')  # Field name made lowercase.
    facilitycode = models.CharField(db_column='FacilityCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    facilityname = models.CharField(db_column='FacilityName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    facilityalias = models.CharField(db_column='FacilityAlias', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptste = models.CharField(db_column='AptSte', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(db_column='AreaCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    contactname = models.CharField(db_column='ContactName', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    facilitytype = models.SmallIntegerField(db_column='FacilityType', blank=True, null=True)  # Field name made lowercase.
    financialsummaryfid = models.IntegerField(db_column='FinancialSummaryFID', blank=True, null=True)  # Field name made lowercase.
    includeonclaims = models.BooleanField(db_column='IncludeOnClaims', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    licensenumber = models.CharField(db_column='LicenseNumber', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfacilityid = models.CharField(db_column='UserFacilityID', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    facilitynpi = models.CharField(db_column='FacilityNPI', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    xrefidschangedat = models.DateTimeField(db_column='XRefIDsChangedAt', blank=True, null=True)  # Field name made lowercase.
    facilitytypefid = models.IntegerField(db_column='FacilityTypeFID', blank=True, null=True)  # Field name made lowercase.
    billclassfid = models.IntegerField(db_column='BillClassFID', blank=True, null=True)  # Field name made lowercase.
    googleplaceid = models.CharField(db_column='GooglePlaceID', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_Facilities'


class VwOdbcMfFacilitiesSXrefids(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    facilityxrefid_uid = models.IntegerField(db_column='FacilityXRefID_UID')  # Field name made lowercase.
    facilityfid = models.IntegerField(db_column='FacilityFID', blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    carrierfacilityxrefidnumber = models.CharField(db_column='CarrierFacilityXrefIDNumber', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_Facilities_s_XRefIDs'


class VwOdbcMfFeeschedulechargecode(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    feescheduleversionfid = models.IntegerField(db_column='FeeScheduleVersionFID', blank=True, null=True)  # Field name made lowercase.
    chargecodefid = models.IntegerField(db_column='ChargeCodeFID', blank=True, null=True)  # Field name made lowercase.
    amount = models.DecimalField(db_column='Amount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_FeeScheduleChargeCode'


class VwOdbcMfFeescheduleversions(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    feescheduleversion_uid = models.IntegerField(db_column='FeeScheduleVersion_UID')  # Field name made lowercase.
    feeschedulefid = models.IntegerField(db_column='FeeScheduleFID', blank=True, null=True)  # Field name made lowercase.
    begindate = models.DateTimeField(db_column='BeginDate', blank=True, null=True)  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_FeeScheduleVersions'


class VwOdbcMfFeeschedules(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    feeschedule_uid = models.IntegerField(db_column='FeeSchedule_UID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    amounttype = models.CharField(db_column='AmountType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_FeeSchedules'


class VwOdbcMfFilecategory(models.Model):
    filecategory_uid = models.IntegerField(db_column='FileCategory_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    categorycode = models.CharField(db_column='CategoryCode', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    filegroupfid = models.IntegerField(db_column='FileGroupFID', blank=True, null=True)  # Field name made lowercase.
    approveby = models.SmallIntegerField(db_column='ApproveBy', blank=True, null=True)  # Field name made lowercase.
    level = models.SmallIntegerField(db_column='Level', blank=True, null=True)  # Field name made lowercase.
    filetype = models.SmallIntegerField(db_column='FileType', blank=True, null=True)  # Field name made lowercase.
    systemfiletype = models.BooleanField(db_column='SystemFileType', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    systemcategory = models.BooleanField(db_column='SystemCategory', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    defaultcategory = models.BooleanField(db_column='DefaultCategory', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_FileCategory'


class VwOdbcMfFilegroup(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    filegroup_uid = models.IntegerField(db_column='FileGroup_UID')  # Field name made lowercase.
    groupcode = models.CharField(db_column='GroupCode', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_FileGroup'


class VwOdbcMfFinancialclasses(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    financialclass_uid = models.IntegerField(db_column='FinancialClass_UID')  # Field name made lowercase.
    financialclasscode = models.CharField(db_column='FinancialClassCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    riskpercentage = models.DecimalField(db_column='RiskPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    riskwriteoffcodefid = models.IntegerField(db_column='RiskWriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    autowriteoff = models.BooleanField(db_column='AutoWriteOff', blank=True, null=True)  # Field name made lowercase.
    writeoffcodefid = models.IntegerField(db_column='WriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    allowablewriteoffcodefid = models.IntegerField(db_column='AllowableWriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    acceptassignment = models.BooleanField(db_column='AcceptAssignment', blank=True, null=True)  # Field name made lowercase.
    responsibility = models.BooleanField(db_column='Responsibility', blank=True, null=True)  # Field name made lowercase.
    billinsurance = models.BooleanField(db_column='BillInsurance', blank=True, null=True)  # Field name made lowercase.
    billlab = models.BooleanField(db_column='BillLab', blank=True, null=True)  # Field name made lowercase.
    defaultaccounttypefid = models.IntegerField(db_column='DefaultAccountTypeFID', blank=True, null=True)  # Field name made lowercase.
    accountreceivablefid = models.IntegerField(db_column='AccountReceivableFID', blank=True, null=True)  # Field name made lowercase.
    financialsummaryfid = models.IntegerField(db_column='FinancialSummaryFID', blank=True, null=True)  # Field name made lowercase.
    allowablefeeschedulefid = models.IntegerField(db_column='AllowableFeeScheduleFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    chargeallowable = models.BooleanField(db_column='ChargeAllowable', blank=True, null=True)  # Field name made lowercase.
    capwriteoff = models.SmallIntegerField(db_column='CapWriteOff', blank=True, null=True)  # Field name made lowercase.
    capwriteoffcodefid = models.IntegerField(db_column='CapWriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    allowsalestax = models.BooleanField(db_column='AllowSalesTax', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_FinancialClasses'


class VwOdbcMfFollowupinstructions(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    followupinstruction_uid = models.IntegerField(db_column='FollowUpInstruction_UID')  # Field name made lowercase.
    followupinstructioncode = models.CharField(db_column='FollowUpInstructionCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_FollowUpInstructions'


class VwOdbcMfFormsletters(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    form_uid = models.IntegerField(db_column='Form_UID')  # Field name made lowercase.
    formname = models.CharField(db_column='FormName', max_length=250, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    formtype = models.CharField(db_column='FormType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    actualletter = models.TextField(db_column='ActualLetter', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    actualletterchangedat = models.DateTimeField(db_column='ActualLetterChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_FormsLetters'


class VwOdbcMfHealthinformationcode(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    healthinformationcode_uid = models.IntegerField(db_column='HealthInformationCode_UID')  # Field name made lowercase.
    hicode = models.CharField(db_column='HICode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_HealthInformationCode'


class VwOdbcMfHipaasituationalfields(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    situationalfield_uid = models.IntegerField(db_column='SituationalField_UID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    loop = models.CharField(db_column='Loop', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    segmentposition = models.IntegerField(db_column='SegmentPosition', blank=True, null=True)  # Field name made lowercase.
    referencedesignator = models.SmallIntegerField(db_column='ReferenceDesignator', blank=True, null=True)  # Field name made lowercase.
    length = models.SmallIntegerField(db_column='Length', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_HipaaSituationalFields'


class VwOdbcMfHoldreason(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    holdreason_uid = models.IntegerField(db_column='HoldReason_UID')  # Field name made lowercase.
    holdreasoncode = models.CharField(db_column='HoldReasonCode', max_length=8, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_HoldReason'


class VwOdbcMfLanguages(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    languageid = models.IntegerField(db_column='LanguageID', blank=True, null=True)  # Field name made lowercase.
    languagecode = models.CharField(db_column='LanguageCode', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    languagecodelong = models.CharField(db_column='LanguageCodeLong', max_length=4, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    languagedescription = models.CharField(db_column='LanguageDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_Languages'


class VwOdbcMfNotetypes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    notetype_uid = models.IntegerField(db_column='NoteType_UID')  # Field name made lowercase.
    notetypecode = models.CharField(db_column='NoteTypeCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_NoteTypes'


class VwOdbcMfOfficekeygroup(models.Model):
    officekeygroup_uid = models.IntegerField(db_column='OfficeKeyGroup_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    officekeygroupname = models.CharField(db_column='OfficeKeyGroupName', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    isuserdefined = models.BooleanField(db_column='IsUserDefined', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    managedkeys = models.CharField(db_column='ManagedKeys', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_OfficeKeyGroup'


class VwOdbcMfPggroups(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    group_uid = models.IntegerField(db_column='Group_UID')  # Field name made lowercase.
    groupcode = models.CharField(db_column='GroupCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptste = models.CharField(db_column='AptSte', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(db_column='AreaCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    license = models.CharField(db_column='License', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    federalid = models.CharField(db_column='FederalID', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clianumber = models.CharField(db_column='CLIANumber', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    npinumber = models.CharField(db_column='NPINumber', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfilefid = models.IntegerField(db_column='UserFileFID', blank=True, null=True)  # Field name made lowercase.
    feeschedulefid = models.IntegerField(db_column='FeeScheduleFID', blank=True, null=True)  # Field name made lowercase.
    financialsummaryfid = models.IntegerField(db_column='FinancialSummaryFID', blank=True, null=True)  # Field name made lowercase.
    accountreceivablefid = models.IntegerField(db_column='AccountReceivableFID', blank=True, null=True)  # Field name made lowercase.
    practicefid = models.IntegerField(db_column='PracticeFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    xrefidschangedat = models.DateTimeField(db_column='XRefIDsChangedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    taxonomy = models.CharField(db_column='Taxonomy', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_PGGroups'


class VwOdbcMfPggroupsSXrefids(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    groupxrefid_uid = models.IntegerField(db_column='GroupXRefID_UID')  # Field name made lowercase.
    groupfid = models.IntegerField(db_column='GroupFID', blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    carriergroupxrefidnumber = models.CharField(db_column='CarrierGroupXRefIDNumber', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    enrolleddate = models.DateTimeField(db_column='EnrolledDate', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_PGGroups_s_XRefIDs'


class VwOdbcMfPgpractice(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    practice_uid = models.IntegerField(db_column='Practice_UID')  # Field name made lowercase.
    practicecode = models.CharField(db_column='PracticeCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    practicename = models.CharField(db_column='PracticeName', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptste = models.CharField(db_column='AptSte', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(db_column='AreaCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    officephone = models.CharField(db_column='OfficePhone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    other = models.CharField(db_column='Other', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phonetype = models.CharField(db_column='PhoneType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    license = models.CharField(db_column='License', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    federaltaxid = models.CharField(db_column='FederalTaxID', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clianumber = models.CharField(db_column='CLIANumber', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfilefid = models.IntegerField(db_column='UserFileFID', blank=True, null=True)  # Field name made lowercase.
    financialsummaryfid = models.IntegerField(db_column='FinancialSummaryFID', blank=True, null=True)  # Field name made lowercase.
    accountreceivablefid = models.IntegerField(db_column='AccountReceivableFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    companywebsite = models.CharField(db_column='CompanyWebSite', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    googleplaceid = models.CharField(db_column='GooglePlaceID', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_PGPractice'


class VwOdbcMfPgprofiles(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    profile_uid = models.IntegerField(db_column='Profile_UID')  # Field name made lowercase.
    profilecode = models.CharField(db_column='ProfileCode', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptste = models.CharField(db_column='AptSte', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(db_column='AreaCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    officephone = models.CharField(db_column='OfficePhone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    officeextension = models.CharField(db_column='OfficeExtension', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    facilityfid = models.IntegerField(db_column='FacilityFID', blank=True, null=True)  # Field name made lowercase.
    license = models.CharField(db_column='License', max_length=18, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    federalid = models.CharField(db_column='FederalID', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    clianumber = models.CharField(db_column='CLIANumber', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfilefid = models.IntegerField(db_column='UserFileFID', blank=True, null=True)  # Field name made lowercase.
    feeschedulefid = models.IntegerField(db_column='FeeScheduleFID', blank=True, null=True)  # Field name made lowercase.
    financialsummaryfid = models.IntegerField(db_column='FinancialSummaryFID', blank=True, null=True)  # Field name made lowercase.
    accountreceivablefid = models.IntegerField(db_column='AccountReceivableFID', blank=True, null=True)  # Field name made lowercase.
    providerfid = models.IntegerField(db_column='ProviderFID', blank=True, null=True)  # Field name made lowercase.
    groupfid = models.IntegerField(db_column='GroupFID', blank=True, null=True)  # Field name made lowercase.
    practicefid = models.IntegerField(db_column='PracticeFID', blank=True, null=True)  # Field name made lowercase.
    referringproviderfid = models.IntegerField(db_column='ReferringProviderFID', blank=True, null=True)  # Field name made lowercase.
    statementgroupfid = models.IntegerField(db_column='StatementGroupFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    billasfid = models.IntegerField(db_column='BillAsFID', blank=True, null=True)  # Field name made lowercase.
    taxonomy = models.CharField(db_column='Taxonomy', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    npinumber = models.CharField(db_column='NPINumber', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    xrefidschangedat = models.DateTimeField(db_column='XRefIDsChangedAt', blank=True, null=True)  # Field name made lowercase.
    isdefault = models.BooleanField(db_column='IsDefault', blank=True, null=True)  # Field name made lowercase.
    hideinchargeentry = models.BooleanField(db_column='HideInChargeEntry', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    codesetpreference = models.IntegerField(db_column='CodeSetPreference', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_PGProfiles'


class VwOdbcMfPgprofilesSXrefids(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    providerxrefid_uid = models.IntegerField(db_column='ProviderXRefID_UID')  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    carrierproviderxrefidnumber = models.CharField(db_column='CarrierProviderXrefIDNumber', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    enrolleddate = models.DateTimeField(db_column='EnrolledDate', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_PGProfiles_s_XRefIDs'


class VwOdbcMfPgproviders(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    provider_uid = models.IntegerField(db_column='Provider_UID')  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    cell = models.CharField(db_column='Cell', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    pager = models.CharField(db_column='Pager', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    financialsummaryfid = models.IntegerField(db_column='FinancialSummaryFID', blank=True, null=True)  # Field name made lowercase.
    accountreceivablefid = models.IntegerField(db_column='AccountReceivableFID', blank=True, null=True)  # Field name made lowercase.
    practicefid = models.IntegerField(db_column='PracticeFID', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='Type', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    status = models.CharField(db_column='Status', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isinstitutional = models.BooleanField(db_column='IsInstitutional', blank=True, null=True)  # Field name made lowercase.
    payschedulefid = models.IntegerField(db_column='PayScheduleFID', blank=True, null=True)  # Field name made lowercase.
    inactiveat = models.DateTimeField(db_column='InactiveAt', blank=True, null=True)  # Field name made lowercase.
    inactiveby = models.CharField(db_column='InactiveBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    upinnumber = models.CharField(db_column='UPINNumber', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    deanumber = models.CharField(db_column='DEANumber', max_length=17, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emraccess = models.CharField(db_column='EMRAccess', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    emractiveat = models.DateTimeField(db_column='EMRActiveAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=107, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_PGProviders'


class VwOdbcMfPaymentdenialcategory(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    paymentdenialcategory_uid = models.IntegerField(db_column='PaymentDenialCategory_UID')  # Field name made lowercase.
    paymentdenialcategorycode = models.CharField(db_column='PaymentDenialCategoryCode', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    paymentdenialcategorydescription = models.CharField(db_column='PaymentDenialCategoryDescription', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    kpienabled = models.BooleanField(db_column='KpiEnabled', blank=True, null=True)  # Field name made lowercase.
    systemdenialcategory = models.BooleanField(db_column='SystemDenialCategory', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_PaymentDenialCategory'


class VwOdbcMfPaymentnote(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    paymentnote_uid = models.IntegerField(db_column='PaymentNote_UID')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_PaymentNote'


class VwOdbcMfPaymentreasons(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    paymentreason_uid = models.IntegerField(db_column='PaymentReason_UID')  # Field name made lowercase.
    code = models.CharField(db_column='Code', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    includezerodollar = models.BooleanField(db_column='IncludeZeroDollar', blank=True, null=True)  # Field name made lowercase.
    excludefromdenials = models.BooleanField(db_column='ExcludeFromDenials', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    paymentdenialcategoryfid = models.IntegerField(db_column='PaymentDenialCategoryFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_PaymentReasons'


class VwOdbcMfPlaceofservice(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    pos_uid = models.IntegerField(db_column='POS_UID')  # Field name made lowercase.
    posdescription = models.CharField(db_column='POSDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    posvalue = models.CharField(db_column='POSValue', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_PlaceOfService'


class VwOdbcMfPlaceofserviceAlias(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    alias_uid = models.IntegerField(db_column='Alias_UID')  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    posaliasvalue = models.CharField(db_column='POSAliasValue', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    placeofservicefid = models.IntegerField(db_column='PlaceOfServiceFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_PlaceOfService_Alias'


class VwOdbcMfProcchargecodecategories(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    chargecodecategory_uid = models.IntegerField(db_column='ChargeCodeCategory_UID')  # Field name made lowercase.
    chargecategorycode = models.CharField(db_column='ChargeCategoryCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ProcChargeCodeCategories'


class VwOdbcMfProcchargecodetype(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    procchargecodetype_uid = models.IntegerField(db_column='ProcChargeCodeType_UID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ProcChargeCodeType'


class VwOdbcMfProcchargecodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    chargecode_uid = models.IntegerField(db_column='ChargeCode_UID')  # Field name made lowercase.
    chargecode = models.CharField(db_column='ChargeCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    insurancedescription = models.CharField(db_column='InsuranceDescription', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    statementdescription = models.CharField(db_column='StatementDescription', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    units = models.DecimalField(db_column='Units', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    placeofservicefid = models.IntegerField(db_column='PlaceOfServiceFID', blank=True, null=True)  # Field name made lowercase.
    typeofservicefid = models.IntegerField(db_column='TypeOfServiceFID', blank=True, null=True)  # Field name made lowercase.
    chargecodecategoryfid = models.IntegerField(db_column='ChargeCodeCategoryFID', blank=True, null=True)  # Field name made lowercase.
    followupinstructionfid = models.IntegerField(db_column='FollowUpInstructionFID', blank=True, null=True)  # Field name made lowercase.
    tax = models.BooleanField(db_column='Tax', blank=True, null=True)  # Field name made lowercase.
    billelectronically = models.BooleanField(db_column='BillElectronically', blank=True, null=True)  # Field name made lowercase.
    requireclianumber = models.BooleanField(db_column='RequireCLIANumber', blank=True, null=True)  # Field name made lowercase.
    financialsummaryfid = models.IntegerField(db_column='FinancialSummaryFID', blank=True, null=True)  # Field name made lowercase.
    xrefbox1 = models.CharField(db_column='XRefBox1', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    xrefbox2 = models.CharField(db_column='XRefBox2', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    xrefbox3 = models.CharField(db_column='XRefBox3', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    xrefbox4 = models.CharField(db_column='XRefBox4', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    xrefbox5 = models.CharField(db_column='XRefBox5', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    xrefbox6 = models.CharField(db_column='XRefBox6', max_length=11, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    accountreceivablefid = models.IntegerField(db_column='AccountReceivableFID', blank=True, null=True)  # Field name made lowercase.
    dollarcopay = models.BooleanField(db_column='DollarCopay', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    billinsurance = models.BooleanField(db_column='BillInsurance', blank=True, null=True)  # Field name made lowercase.
    billpatient = models.BooleanField(db_column='BillPatient', blank=True, null=True)  # Field name made lowercase.
    revenuecodefid = models.IntegerField(db_column='RevenueCodeFID', blank=True, null=True)  # Field name made lowercase.
    customrvu = models.DecimalField(db_column='CustomRVU', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    costcodechargecodefid = models.IntegerField(db_column='CostCodeChargeCodeFID', blank=True, null=True)  # Field name made lowercase.
    procchargecodetypefid = models.IntegerField(db_column='ProcChargeCodeTypeFID', blank=True, null=True)  # Field name made lowercase.
    left5xrefbox1 = models.CharField(db_column='Left5XRefBox1', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ndc = models.CharField(db_column='NDC', max_length=13, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ndcdescription = models.CharField(db_column='NDCDescription', max_length=80, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ndcquantity = models.DecimalField(db_column='NDCQuantity', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    userfileformfid = models.IntegerField(db_column='UserFileFormFID', blank=True, null=True)  # Field name made lowercase.
    facilityfid = models.IntegerField(db_column='FacilityFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ProcChargeCodes'


class VwOdbcMfProcmodifiercodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    modifiercode_uid = models.IntegerField(db_column='ModifierCode_UID')  # Field name made lowercase.
    modifiercode = models.CharField(db_column='ModifierCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ProcModifierCodes'


class VwOdbcMfProcpaymentcodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    paymentcode_uid = models.IntegerField(db_column='PaymentCode_UID')  # Field name made lowercase.
    paymentcode = models.CharField(db_column='PaymentCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ProcPaymentCodes'


class VwOdbcMfProcwriteoffcodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    writeoffcode_uid = models.IntegerField(db_column='WriteOffCode_UID')  # Field name made lowercase.
    writeoffcode = models.CharField(db_column='WriteOffCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ProcWriteOffCodes'


class VwOdbcMfProviderfinancialclassexception(models.Model):
    providerfinancialclassexception_uid = models.IntegerField(db_column='ProviderFinancialClassException_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    financialclassfid = models.IntegerField(db_column='FinancialClassFID', blank=True, null=True)  # Field name made lowercase.
    financialclasscode = models.CharField(db_column='FinancialClassCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    riskpercentage = models.DecimalField(db_column='RiskPercentage', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    riskwriteoffcodefid = models.IntegerField(db_column='RiskWriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    autowriteoff = models.BooleanField(db_column='AutoWriteOff', blank=True, null=True)  # Field name made lowercase.
    writeoffcodefid = models.IntegerField(db_column='WriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    allowablewriteoffcodefid = models.IntegerField(db_column='AllowableWriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    acceptassignment = models.BooleanField(db_column='AcceptAssignment', blank=True, null=True)  # Field name made lowercase.
    responsibility = models.BooleanField(db_column='Responsibility', blank=True, null=True)  # Field name made lowercase.
    billinsurance = models.BooleanField(db_column='BillInsurance', blank=True, null=True)  # Field name made lowercase.
    billlab = models.BooleanField(db_column='BillLab', blank=True, null=True)  # Field name made lowercase.
    defaultaccounttypefid = models.IntegerField(db_column='DefaultAccountTypeFID', blank=True, null=True)  # Field name made lowercase.
    accountreceivablefid = models.IntegerField(db_column='AccountReceivableFID', blank=True, null=True)  # Field name made lowercase.
    financialsummaryfid = models.IntegerField(db_column='FinancialSummaryFID', blank=True, null=True)  # Field name made lowercase.
    allowablefeeschedulefid = models.IntegerField(db_column='AllowableFeeScheduleFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    capwriteoff = models.BooleanField(db_column='CapWriteOff', blank=True, null=True)  # Field name made lowercase.
    capwriteoffcodefid = models.IntegerField(db_column='CapWriteOffCodeFID', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ProviderFinancialClassException'


class VwOdbcMfProviderfinancialclasses(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    financialclassfid = models.IntegerField(db_column='FinancialClassFID', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ProviderFinancialClasses'


class VwOdbcMfRecalldefaults(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    recalldefault_uid = models.IntegerField(db_column='RecallDefault_UID')  # Field name made lowercase.
    appttypefid = models.IntegerField(db_column='ApptTypeFID', blank=True, null=True)  # Field name made lowercase.
    chargesliptemplatefid = models.IntegerField(db_column='ChargeSlipTemplateFID', blank=True, null=True)  # Field name made lowercase.
    nextappttypefid = models.IntegerField(db_column='NextApptTypeFID', blank=True, null=True)  # Field name made lowercase.
    numberof = models.CharField(db_column='NumberOf', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    daysweeksmonthsyears = models.CharField(db_column='DaysWeeksMonthsYears', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_RecallDefaults'


class VwOdbcMfReferralplansources(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    referralplansources_uid = models.IntegerField(db_column='ReferralPlanSources_UID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ReferralPlanSources'


class VwOdbcMfReferralplanstatuscodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    referralplanstatus_uid = models.IntegerField(db_column='ReferralPlanStatus_UID')  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ReferralPlanStatusCodes'


class VwOdbcMfReferringproviders(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    referringprovider_uid = models.IntegerField(db_column='ReferringProvider_UID')  # Field name made lowercase.
    referringprovidercode = models.CharField(db_column='ReferringProviderCode', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptste = models.CharField(db_column='AptSte', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(db_column='AreaCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    practicename = models.CharField(db_column='PracticeName', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    licensenumber = models.CharField(db_column='LicenseNumber', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    speciality = models.CharField(db_column='Speciality', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    taxonomy = models.CharField(db_column='Taxonomy', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    npinumber = models.CharField(db_column='NPINumber', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    includeonhcfa = models.BooleanField(db_column='IncludeonHCFA', blank=True, null=True)  # Field name made lowercase.
    officephone = models.CharField(db_column='OfficePhone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fax = models.CharField(db_column='Fax', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    other = models.CharField(db_column='Other', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phonetype = models.CharField(db_column='PhoneType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    userfilefid = models.IntegerField(db_column='UserFileFID', blank=True, null=True)  # Field name made lowercase.
    accountreceivablefid = models.IntegerField(db_column='AccountReceivableFID', blank=True, null=True)  # Field name made lowercase.
    financialsummaryfid = models.IntegerField(db_column='FinancialSummaryFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    xrefidschangedat = models.DateTimeField(db_column='XRefIDsChangedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=107, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ReferringProviders'


class VwOdbcMfReferringprovidersSXrefids(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    providerxrefid_uid = models.IntegerField(db_column='ProviderXRefID_UID')  # Field name made lowercase.
    referringproviderfid = models.IntegerField(db_column='ReferringProviderFID', blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    carrierproviderxrefidnumber = models.CharField(db_column='CarrierProviderXrefIDNumber', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ReferringProviders_s_XRefIDs'


class VwOdbcMfRemarkcodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    remarkcode_uid = models.IntegerField(db_column='RemarkCode_UID')  # Field name made lowercase.
    remarkcode = models.CharField(db_column='RemarkCode', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    importedfromera = models.BooleanField(db_column='ImportedFromERA', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_RemarkCodes'


class VwOdbcMfRevenuecode(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    revenuecode_uid = models.IntegerField(db_column='RevenueCode_UID')  # Field name made lowercase.
    revenuecode = models.CharField(db_column='RevenueCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    rolluponclaim = models.BooleanField(db_column='RollUpOnClaim', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_RevenueCode'


class VwOdbcMfStatementgroups(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    statementgroup_uid = models.IntegerField(db_column='StatementGroup_UID')  # Field name made lowercase.
    statementgroupcode = models.CharField(db_column='StatementGroupCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    usepracticesettings = models.BooleanField(db_column='UsePracticeSettings', blank=True, null=True)  # Field name made lowercase.
    statementgroupname = models.CharField(db_column='StatementGroupName', max_length=40, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptste = models.CharField(db_column='AptSte', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    officephone = models.CharField(db_column='OfficePhone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    officeextension = models.CharField(db_column='OfficeExtension', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    federaltaxid = models.CharField(db_column='FederalTaxID', max_length=14, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_StatementGroups'


class VwOdbcMfTypeofservice(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    tos_uid = models.IntegerField(db_column='TOS_UID')  # Field name made lowercase.
    tosdescription = models.CharField(db_column='TosDescription', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tosvalue = models.CharField(db_column='TosValue', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_TypeOfService'


class VwOdbcMfTypeofserviceAlias(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    alias_uid = models.IntegerField(db_column='Alias_UID')  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    typeofservicefid = models.IntegerField(db_column='TypeOfServiceFID', blank=True, null=True)  # Field name made lowercase.
    tosaliasvalue = models.CharField(db_column='TOSAliasValue', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_TypeOfService_Alias'


class VwOdbcMfUserfileselectlist(models.Model):
    userfileselectlist_uid = models.IntegerField(db_column='UserFileSelectList_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    optionlist = models.CharField(db_column='OptionList', max_length=4000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    iscmn = models.BooleanField(db_column='IsCMN', blank=True, null=True)  # Field name made lowercase.
    ishipaa = models.BooleanField(db_column='IsHipaa', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_UserFileSelectList'


class VwOdbcMfUserfileselectlistoption(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    userfileselectlistfid = models.IntegerField(db_column='UserFileSelectListFID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_UserFileSelectListOption'


class VwOdbcMfUserfiletemplatefields(models.Model):
    userfiletemplatefield_uid = models.IntegerField(db_column='UserFileTemplateField_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    userfiletemplatefid = models.IntegerField(db_column='UserFileTemplateFID', blank=True, null=True)  # Field name made lowercase.
    fieldname = models.CharField(db_column='FieldName', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    alias = models.CharField(db_column='Alias', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.
    datatype = models.CharField(db_column='DataType', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    subtype = models.CharField(db_column='Subtype', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    isrequired = models.BooleanField(db_column='IsRequired', blank=True, null=True)  # Field name made lowercase.
    defaultvalue = models.CharField(db_column='DefaultValue', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    normalrangelow = models.DecimalField(db_column='NormalRangeLow', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    normalrangehigh = models.DecimalField(db_column='NormalRangeHigh', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    includeinlist = models.BooleanField(db_column='IncludeInList', blank=True, null=True)  # Field name made lowercase.
    includeinmailmerge = models.BooleanField(db_column='IncludeInMailMerge', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_UserFileTemplateFields'


class VwOdbcMfUserfiletemplates(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    userfiletemplate_uid = models.IntegerField(db_column='UserFileTemplate_UID')  # Field name made lowercase.
    templatecode = models.CharField(db_column='TemplateCode', max_length=5, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    templatename = models.CharField(db_column='TemplateName', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.
    issingleuse = models.BooleanField(db_column='IsSingleUse', blank=True, null=True)  # Field name made lowercase.
    includeinmailmerge = models.BooleanField(db_column='IncludeInMailMerge', blank=True, null=True)  # Field name made lowercase.
    includeonfacesheet = models.BooleanField(db_column='IncludeOnFaceSheet', blank=True, null=True)  # Field name made lowercase.
    alwaysshowonfacesheet = models.BooleanField(db_column='AlwaysShowOnFaceSheet', blank=True, null=True)  # Field name made lowercase.
    includeindemographics = models.BooleanField(db_column='IncludeInDemographics', blank=True, null=True)  # Field name made lowercase.
    alwaysshowindemographics = models.BooleanField(db_column='AlwaysShowInDemographics', blank=True, null=True)  # Field name made lowercase.
    restrictupdates = models.BooleanField(db_column='RestrictUpdates', blank=True, null=True)  # Field name made lowercase.
    systemtype = models.SmallIntegerField(db_column='SystemType', blank=True, null=True)  # Field name made lowercase.
    sortbyfield1fid = models.IntegerField(db_column='SortByField1FID', blank=True, null=True)  # Field name made lowercase.
    sortbydesc1 = models.BooleanField(db_column='SortByDesc1', blank=True, null=True)  # Field name made lowercase.
    sortbyfield2fid = models.IntegerField(db_column='SortByField2FID', blank=True, null=True)  # Field name made lowercase.
    sortbydesc2 = models.BooleanField(db_column='SortByDesc2', blank=True, null=True)  # Field name made lowercase.
    fieldlist = models.CharField(db_column='FieldList', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_UserFileTemplates'


class VwOdbcMfUserfilevalidation(models.Model):
    userfilevalidation_uid = models.IntegerField(db_column='UserFileValidation_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    regex = models.CharField(db_column='RegEx', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    errormsg = models.CharField(db_column='ErrorMsg', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_UserFileValidation'


class VwOdbcMfZipcodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    zipcode_uid = models.IntegerField(db_column='ZipCode_UID')  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(db_column='AreaCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_ZipCodes'


class VwOdbcMfLnkOfficekeygroupLicensekey(models.Model):
    officekeygroupfid = models.IntegerField(db_column='OfficeKeyGroupFID', blank=True, null=True)  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_mf_lnk_OfficeKeyGroup_LicenseKey'


class VwOdbcMiscHipaarelationship(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    relationshipcode = models.CharField(db_column='RelationshipCode', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=64, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_misc_HipaaRelationship'


class VwOdbcMiscSelectlist(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    selectlist_uid = models.IntegerField(db_column='SelectList_UID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    useuid = models.BooleanField(db_column='UseUID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_misc_SelectList'


class VwOdbcMiscSelectlistoption(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey', blank=True, null=True)  # Field name made lowercase.
    selectlistoption_uid = models.IntegerField(db_column='SelectListOption_UID')  # Field name made lowercase.
    selectlistfid = models.IntegerField(db_column='SelectListFID', blank=True, null=True)  # Field name made lowercase.
    value = models.CharField(db_column='Value', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.IntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_misc_SelectListOption'


class VwOdbcPortAccount(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    account_uid = models.IntegerField(db_column='Account_UID')  # Field name made lowercase.
    accountname = models.CharField(db_column='AccountName', max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    loginemail = models.CharField(db_column='LoginEmail', max_length=254, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastloggedinat = models.DateTimeField(db_column='LastLoggedInAt', blank=True, null=True)  # Field name made lowercase.
    accountdisabled = models.BooleanField(db_column='AccountDisabled', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sendnotifications = models.BooleanField(db_column='SendNotifications', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_port_Account'


class VwOdbcPtFormbatch(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    formbatch_uid = models.IntegerField(db_column='FormBatch_UID')  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_FormBatch'


class VwOdbcPtFormsletter(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    formletter_uid = models.IntegerField(db_column='FormLetter_UID')  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    printed = models.CharField(db_column='Printed', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    templatefid = models.IntegerField(db_column='TemplateFID', blank=True, null=True)  # Field name made lowercase.
    actualletter = models.TextField(db_column='ActualLetter', db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_FormsLetter'


class VwOdbcPtInsurancecoverages(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    patientinsurancecoverage_uid = models.IntegerField(db_column='PatientInsuranceCoverage_UID')  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    active = models.BooleanField(db_column='Active', blank=True, null=True)  # Field name made lowercase.
    sequencenumber = models.SmallIntegerField(db_column='SequenceNumber', blank=True, null=True)  # Field name made lowercase.
    effectivestartdate = models.DateTimeField(db_column='EffectiveStartDate', blank=True, null=True)  # Field name made lowercase.
    effectiveenddate = models.DateTimeField(db_column='EffectiveEndDate', blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    coverage = models.SmallIntegerField(db_column='Coverage', blank=True, null=True)  # Field name made lowercase.
    subscriberidnumber = models.CharField(db_column='SubscriberIDNumber', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    responsiblepartysubscriberfid = models.IntegerField(db_column='ResponsiblePartySubscriberFID', blank=True, null=True)  # Field name made lowercase.
    relationshippatienttosubscriber = models.SmallIntegerField(db_column='RelationshipPatienttoSubscriber', blank=True, null=True)  # Field name made lowercase.
    groupname = models.CharField(db_column='GroupName', max_length=20, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    groupnumber = models.CharField(db_column='GroupNumber', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    copaydollaramount = models.DecimalField(db_column='CopayDollarAmount', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    copaypercentageamount = models.DecimalField(db_column='CopayPercentageAmount', max_digits=18, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    annualdeductible = models.DecimalField(db_column='AnnualDeductible', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    deductibleamountmet = models.DecimalField(db_column='DeductibleAmountMet', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    yearendmonth = models.CharField(db_column='YearEndMonth', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lifetimebenefit = models.DecimalField(db_column='LifeTimeBenefit', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    studentstatus = models.SmallIntegerField(db_column='StudentStatus', blank=True, null=True)  # Field name made lowercase.
    notefid = models.IntegerField(db_column='NoteFID', blank=True, null=True)  # Field name made lowercase.
    benefitinfochangedat = models.DateTimeField(db_column='BenefitInfoChangedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    payerid = models.CharField(db_column='PayerID', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_InsuranceCoverages'


class VwOdbcPtInsuranceorder(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    patientinsurancecoveragefid = models.IntegerField(db_column='PatientInsuranceCoverageFID', blank=True, null=True)  # Field name made lowercase.
    ordinal = models.SmallIntegerField(db_column='Ordinal', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_InsuranceOrder'


class VwOdbcPtMemos(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    memo_uid = models.IntegerField(db_column='Memo_UID')  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    memotype = models.CharField(db_column='MemoType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    memotext = models.CharField(db_column='MemoText', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    expiredate = models.DateTimeField(db_column='ExpireDate', blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_Memos'


class VwOdbcPtNote(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    note_uid = models.IntegerField(db_column='Note_UID')  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    notetypefid = models.IntegerField(db_column='NoteTypeFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(db_column='Note', max_length=6000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_Note'


class VwOdbcPtPatientinfo(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    patient_uid = models.IntegerField(db_column='Patient_UID')  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    chartnumber = models.CharField(db_column='ChartNumber', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    aptste = models.CharField(db_column='AptSte', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(db_column='AreaCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    officephone = models.CharField(db_column='OfficePhone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    officeextension = models.CharField(db_column='OfficeExtension', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    other = models.CharField(db_column='Other', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phonetype = models.CharField(db_column='PhoneType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    maritalstatus = models.SmallIntegerField(db_column='MaritalStatus', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    deceased = models.DateTimeField(db_column='Deceased', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ssn = models.CharField(db_column='SSN', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    relationship = models.SmallIntegerField(db_column='Relationship', blank=True, null=True)  # Field name made lowercase.
    hipaarelationship = models.CharField(db_column='HIPAARelationship', max_length=2, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    responsiblepartyfid = models.IntegerField(db_column='ResponsiblePartyFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    financialclassfid = models.IntegerField(db_column='FinancialClassFID', blank=True, null=True)  # Field name made lowercase.
    employer = models.CharField(db_column='Employer', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    employerfid = models.IntegerField(db_column='EmployerFID', blank=True, null=True)  # Field name made lowercase.
    insuranceorder = models.CharField(db_column='InsuranceOrder', max_length=45, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ar_patportionfid = models.IntegerField(db_column='AR_PatPortionFID', blank=True, null=True)  # Field name made lowercase.
    ar_insportionfid = models.IntegerField(db_column='AR_InsPortionFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    recalcbuckets = models.BooleanField(db_column='RecalcBuckets', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=107, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bucketsupdatedat = models.DateTimeField(db_column='BucketsUpdatedAt', blank=True, null=True)  # Field name made lowercase.
    birthmonth = models.IntegerField(db_column='BirthMonth', blank=True, null=True)  # Field name made lowercase.
    isdeceased = models.IntegerField(db_column='IsDeceased', blank=True, null=True)  # Field name made lowercase.
    ethnicityfid = models.IntegerField(db_column='EthnicityFID', blank=True, null=True)  # Field name made lowercase.
    languagefid = models.IntegerField(db_column='LanguageFID', blank=True, null=True)  # Field name made lowercase.
    language = models.CharField(db_column='Language', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    communicationnote = models.CharField(db_column='CommunicationNote', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_PatientInfo'


class VwOdbcPtRecallvisits(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    recallvisit_uid = models.IntegerField(db_column='RecallVisit_UID')  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    daterecallrequested = models.DateTimeField(db_column='DateRecallRequested', blank=True, null=True)  # Field name made lowercase.
    recallduedate = models.DateTimeField(db_column='RecallDueDate', blank=True, null=True)  # Field name made lowercase.
    recallappttypefid = models.IntegerField(db_column='RecallApptTypeFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    appointmentfid = models.IntegerField(db_column='AppointmentFID', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_RecallVisits'


class VwOdbcPtReferralplans(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    referralplan_uid = models.IntegerField(db_column='ReferralPlan_UID')  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    referraltype = models.CharField(db_column='ReferralType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    defaultinchargeentry = models.BooleanField(db_column='DefaultinChargeEntry', blank=True, null=True)  # Field name made lowercase.
    byreferringproviderfid = models.IntegerField(db_column='ByReferringProviderFID', blank=True, null=True)  # Field name made lowercase.
    toreferringproviderfid = models.IntegerField(db_column='ToReferringProviderFID', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    preauthcode = models.CharField(db_column='PreAuthCode', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    expirationdate = models.DateTimeField(db_column='ExpirationDate', blank=True, null=True)  # Field name made lowercase.
    maxcharge = models.DecimalField(db_column='MaxCharge', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    usedcharge = models.DecimalField(db_column='UsedCharge', max_digits=19, decimal_places=4, blank=True, null=True)  # Field name made lowercase.
    maxauthvisits = models.IntegerField(db_column='MaxAuthVisits', blank=True, null=True)  # Field name made lowercase.
    authvisitsused = models.IntegerField(db_column='AuthVisitsUsed', blank=True, null=True)  # Field name made lowercase.
    chargecodefid = models.IntegerField(db_column='ChargeCodeFID', blank=True, null=True)  # Field name made lowercase.
    statuscodefid = models.IntegerField(db_column='StatusCodeFID', blank=True, null=True)  # Field name made lowercase.
    referralplansourcefid = models.IntegerField(db_column='ReferralPlanSourceFID', blank=True, null=True)  # Field name made lowercase.
    facilityfid = models.IntegerField(db_column='FacilityFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    preauthorizationrequired = models.IntegerField(db_column='PreAuthorizationRequired', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    sequenceno = models.IntegerField(db_column='SequenceNo', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    diagnosiscodes = models.CharField(db_column='DiagnosisCodes', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    creationdate = models.DateTimeField(db_column='CreationDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_ReferralPlans'


class VwOdbcPtResponsibleparties(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    responsibleparty_uid = models.IntegerField(db_column='ResponsibleParty_UID')  # Field name made lowercase.
    aptste = models.CharField(db_column='AptSte', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(db_column='Address', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    zipcode = models.CharField(db_column='ZipCode', max_length=10, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    city = models.CharField(db_column='City', max_length=30, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    areacode = models.CharField(db_column='AreaCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    countrycode = models.CharField(db_column='CountryCode', max_length=3, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    employer = models.CharField(db_column='Employer', max_length=100, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    middlename = models.CharField(db_column='MiddleName', max_length=35, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    accounttypefid = models.IntegerField(db_column='AccountTypeFID', blank=True, null=True)  # Field name made lowercase.
    officephone = models.CharField(db_column='OfficePhone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    officeextension = models.CharField(db_column='OfficeExtension', max_length=6, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    homephone = models.CharField(db_column='HomePhone', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    other = models.CharField(db_column='Other', max_length=25, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    phonetype = models.CharField(db_column='PhoneType', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateTimeField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=1, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    ssn = models.CharField(db_column='SSN', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(db_column='Title', max_length=15, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    employmentstatus = models.SmallIntegerField(db_column='EmploymentStatus', blank=True, null=True)  # Field name made lowercase.
    ar_rpportionfid = models.IntegerField(db_column='AR_RPPortionFID', blank=True, null=True)  # Field name made lowercase.
    ar_insportionfid = models.IntegerField(db_column='AR_InsPortionFID', blank=True, null=True)  # Field name made lowercase.
    stmtformatname = models.CharField(db_column='STMTFormatName', max_length=50, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    stmtformsfid = models.IntegerField(db_column='STMTFormsFID', blank=True, null=True)  # Field name made lowercase.
    openitembfwd = models.BooleanField(db_column='OpenItemBFWD', blank=True, null=True)  # Field name made lowercase.
    sendstmt = models.BooleanField(db_column='SendSTMT', blank=True, null=True)  # Field name made lowercase.
    stmtrestartdate = models.DateTimeField(db_column='STMTRestartDate', blank=True, null=True)  # Field name made lowercase.
    stmtbillingcycle = models.SmallIntegerField(db_column='STMTBillingCycle', blank=True, null=True)  # Field name made lowercase.
    financecharge = models.BooleanField(db_column='FinanceCharge', blank=True, null=True)  # Field name made lowercase.
    communicatebyemail = models.BooleanField(db_column='CommunicateByEmail', blank=True, null=True)  # Field name made lowercase.
    lastactionhistoryfid = models.IntegerField(db_column='LastActionHistoryFID', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    bucketsupdatedat = models.DateTimeField(db_column='BucketsUpdatedAt', blank=True, null=True)  # Field name made lowercase.
    fullname = models.CharField(db_column='FullName', max_length=107, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    holdreasonfid = models.IntegerField(db_column='HoldReasonFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_ResponsibleParties'


class VwOdbcPtUserfileinstances(models.Model):
    userfileinstance_uid = models.IntegerField(db_column='UserFileInstance_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    userfiletemplatefid = models.IntegerField(db_column='UserFileTemplateFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_UserFileInstances'


class VwOdbcPtUserfilevalues(models.Model):
    userfilevalue_uid = models.IntegerField(db_column='UserFileValue_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    userfileinstancefid = models.IntegerField(db_column='UserFileInstanceFID', blank=True, null=True)  # Field name made lowercase.
    userfiletemplatefieldfid = models.IntegerField(db_column='UserFileTemplateFieldFID', blank=True, null=True)  # Field name made lowercase.
    fidvalue = models.IntegerField(db_column='FIDValue', blank=True, null=True)  # Field name made lowercase.
    textvalue = models.CharField(db_column='TextValue', max_length=2000, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_UserFileValues'


class VwOdbcPtLnkPatientinfoRace(models.Model):
    patientinfo_race_uid = models.IntegerField(db_column='PatientInfo_Race_UID')  # Field name made lowercase.
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    patientfid = models.IntegerField(db_column='PatientFID', blank=True, null=True)  # Field name made lowercase.
    racefid = models.IntegerField(db_column='RaceFID', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    createdby = models.CharField(db_column='CreatedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    createdat = models.DateTimeField(db_column='CreatedAt', blank=True, null=True)  # Field name made lowercase.
    changedby = models.CharField(db_column='ChangedBy', max_length=12, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    changedat = models.DateTimeField(db_column='ChangedAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_lnk_PatientInfo_Race'


class VwOdbcPtLnkReferralplanDiagnosiscodes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    referralplandiagnosiscode_uid = models.IntegerField(db_column='ReferralPlanDiagnosisCode_UID')  # Field name made lowercase.
    referralplanfid = models.IntegerField(db_column='ReferralPlanFID', blank=True, null=True)  # Field name made lowercase.
    diagnosiscodefid = models.IntegerField(db_column='DiagnosisCodeFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_lnk_ReferralPlan_DiagnosisCodes'


class VwOdbcPtLnkReferralplanNotes(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    referralplannote_uid = models.IntegerField(db_column='ReferralPlanNote_UID')  # Field name made lowercase.
    referralplanfid = models.IntegerField(db_column='ReferralPlanFID', blank=True, null=True)  # Field name made lowercase.
    notefid = models.IntegerField(db_column='NoteFID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_pt_lnk_ReferralPlan_Notes'


class VwOdbcRptUnbilledclaims(models.Model):
    licensekey = models.IntegerField(db_column='LicenseKey')  # Field name made lowercase.
    chargedetailfid = models.IntegerField(db_column='ChargeDetailFID', blank=True, null=True)  # Field name made lowercase.
    carrierfid = models.IntegerField(db_column='CarrierFID', blank=True, null=True)  # Field name made lowercase.
    profilefid = models.IntegerField(db_column='ProfileFID', blank=True, null=True)  # Field name made lowercase.
    submitterfid = models.IntegerField(db_column='SubmitterFID', blank=True, null=True)  # Field name made lowercase.
    paperformfid = models.IntegerField(db_column='PaperFormFID', blank=True, null=True)  # Field name made lowercase.
    primaryother = models.SmallIntegerField(db_column='PrimaryOther', blank=True, null=True)  # Field name made lowercase.
    reason = models.CharField(db_column='Reason', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    display = models.BooleanField(db_column='Display', blank=True, null=True)  # Field name made lowercase.
    enablemonthlybilling = models.BooleanField(db_column='EnableMonthlyBilling', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vw_ODBC_rpt_UnbilledClaims'
