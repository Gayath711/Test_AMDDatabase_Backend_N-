
from django.contrib import admin
from django.urls import path

from AMD_Test import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/getPatientInfo/', views.getPatientInfo),
    path('api/dataFromMSSQL/', views.dataFromMSSQL),
    path('api/load_data_from_mssql', views.load_data_from_mssql)

]
