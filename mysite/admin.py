from django.contrib import admin

class MyAdminSite(admin.AdminSite):
    site_header = ('Moja strona ankietowa ReaktorPWN')
    site_title = ('Strona Administracyjna')