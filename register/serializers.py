from rest_framework import serializers
from .models import *

class SinhVienSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinhVien
        fields = '__all__'
class HocPhanIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = HocPhan
        fields = ('id', )
class HocPhanSerializer(serializers.ModelSerializer):
    class Meta:
        model = HocPhan
        fields = "__all__"
class SinhVienIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = SinhVien
        fields = ('id', 'mssv')
class HocPhanDangKySerializer(serializers.ModelSerializer):
    class Meta:
        model = HocPhanDangKy
        fields = '__all__'