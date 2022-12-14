# Generated by Django 4.1 on 2022-12-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ctdt',
            fields=[
                ('ctdt_id', models.AutoField(primary_key=True, serialize=False)),
                ('ten_ct', models.CharField(blank=True, max_length=1000, null=True)),
                ('ma_ct', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('so_tin_chi', models.FloatField(blank=True, null=True)),
                ('so_ky', models.IntegerField(blank=True, null=True)),
                ('tu', models.DateField(blank=True, null=True)),
                ('den', models.DateField(blank=True, null=True)),
            ],
            options={
                'db_table': 'ctdt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='CtdtHocPhan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'ctdt_hoc_phan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HocPhan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_hoc_phan', models.CharField(blank=True, max_length=255, null=True)),
                ('ma_hoc_phan', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('so_tin_chi', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'hoc_phan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HocTruoc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'hoc_truoc',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LopSinhHoat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten_lop', models.CharField(blank=True, max_length=255, null=True)),
                ('khoa', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'lop_sinh_hoat',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SinhVien',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mssv', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('ten_sv', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'sinh_vien',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SinhVienHocPhan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diem_trung_binh', models.FloatField(blank=True, null=True)),
            ],
            options={
                'db_table': 'sinh_vien_hoc_phan',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SongHanh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'song_hanh',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TienQuyet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'tien_quyet',
                'managed': False,
            },
        ),
    ]
