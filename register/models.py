# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

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
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
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


class Ctdt(models.Model):
    ctdt_id = models.AutoField(primary_key=True)
    ten_ct = models.CharField(max_length=1000, blank=True, null=True)
    ma_ct = models.CharField(unique=True, max_length=50, blank=True, null=True)
    so_tin_chi = models.FloatField(blank=True, null=True)
    so_ky = models.IntegerField(blank=True, null=True)
    tu = models.DateField(blank=True, null=True)
    den = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctdt'


class CtdtHocPhan(models.Model):
    id = models.AutoField(primary_key=True)
    ctdt = models.ForeignKey(Ctdt, models.DO_NOTHING, blank=True, null=True)
    hoc_phan = models.ForeignKey('HocPhan', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ctdt_hoc_phan'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HocPhan(models.Model):
    id = models.AutoField(primary_key=True)
    ten_hoc_phan = models.CharField(max_length=255, blank=True, null=True)
    ma_hoc_phan = models.CharField(unique=True, max_length=255, blank=True, null=True)
    so_tin_chi = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hoc_phan'


class HocPhanDangKy(models.Model):
    id = models.AutoField(primary_key=True)
    ten_hoc_phan = models.CharField(max_length=100, blank=True, null=True)
    ma_hoc_phan = models.CharField(unique=True, max_length=50)
    so_tin_chi = models.FloatField(blank=True, null=True)
    giao_vien = models.CharField(max_length=100, blank=True, null=True)
    lich_hoc = models.CharField(max_length=100, blank=True, null=True)
    so_tuan = models.CharField(max_length=50, blank=True, null=True)
    tong_so_luong = models.IntegerField(blank=True, null=True)
    da_dang_ky = models.IntegerField(blank=True, null=True)
    clc = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hoc_phan_dang_ky'


class HocTruoc(models.Model):
    id = models.AutoField(primary_key=True)
    ctdt_hoc_phan = models.ForeignKey(CtdtHocPhan, models.DO_NOTHING, blank=True, null=True)
    hoc_phan = models.ForeignKey(HocPhan, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hoc_truoc'


class LopSinhHoat(models.Model):
    id = models.AutoField(primary_key=True)
    ten_lop = models.CharField(max_length=255, blank=True, null=True)
    khoa = models.CharField(max_length=255, blank=True, null=True)
    ctdt = models.ForeignKey(Ctdt, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lop_sinh_hoat'


class SinhVien(models.Model):
    id = models.AutoField(primary_key=True)
    mssv = models.CharField(unique=True, max_length=50, blank=True, null=True)
    ten_sv = models.CharField(max_length=100, blank=True, null=True)
    id_lop = models.ForeignKey(LopSinhHoat, models.DO_NOTHING, db_column='id_lop', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sinh_vien'


class SinhVienHocPhan(models.Model):
    id = models.AutoField(primary_key=True)
    sinh_vien = models.ForeignKey(SinhVien, models.DO_NOTHING, blank=True, null=True)
    hoc_phan = models.ForeignKey(HocPhan, models.DO_NOTHING, blank=True, null=True)
    diem_trung_binh = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sinh_vien_hoc_phan'


class SongHanh(models.Model):
    id = models.AutoField(primary_key=True)
    ctdt_hoc_phan = models.ForeignKey(CtdtHocPhan, models.DO_NOTHING, blank=True, null=True)
    hoc_phan = models.ForeignKey(HocPhan, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'song_hanh'


class TienQuyet(models.Model):
    id = models.AutoField(primary_key=True)
    ctdt_hoc_phan = models.ForeignKey(CtdtHocPhan, models.DO_NOTHING, blank=True, null=True)
    hoc_phan = models.ForeignKey(HocPhan, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tien_quyet'
