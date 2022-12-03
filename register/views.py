from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status, permissions
from django.core.cache import cache
from .models import *
from .serializers import *

HOC_PHAN_DANG_KY = "HOC_PHAN_DANG_KY"
HOC_PHAN_DANG_KY_TRONG_KY = "HOC_PHAN_DANG_KY_TRONG_KY"

# Create your views here.

class LoadData(viewsets.ViewSet):
    # Load all data to redis for each student
    def load_all_data_register(self, request, *args, **kwargs):
        students = SinhVien.objects.only('id', 'mssv')
        serializer = SinhVienIdSerializer(students, many=True)
        count = 0
        for id in students:
            # print(id.mssv)
            hocphan = HocPhan.objects.raw("""select hp.* from hoc_phan as hp 
                    inner join ctdt_hoc_phan as ctdthp on hp.id = ctdthp.hoc_phan_id
                    inner join ctdt on ctdthp.ctdt_id = ctdt.ctdt_id 
                    inner join lop_sinh_hoat as lsh on ctdt.ctdt_id=lsh.ctdt_id
                    inner join sinh_vien as sv on lsh.id = sv.id_lop 
                    where sv.id = %s and (NOT EXISTS (select 0 from sinh_vien_hoc_phan as 
                    svhp1 where svhp1.hoc_phan_id = hp.id and svhp1.sinh_vien_id = sv.id) 
                    OR EXISTS(select 0 from sinh_vien_hoc_phan as svhp2 where svhp2.hoc_phan_id = hp.id and 
                    svhp2.sinh_vien_id = sv.id and svhp2.diem_trung_binh < 4))
                    and (NOT EXISTS (select 0 from tien_quyet as tq1 inner join sinh_vien_hoc_phan as svhp2 
                    where svhp2.sinh_vien_id = sv.id and 
                    svhp2.hoc_phan_id=tq1.hoc_phan_id and svhp2.diem_trung_binh < 4 and tq1.ctdt_hoc_phan_id = ctdthp.id))
                    and not exists (select 1 from hoc_truoc as ht3  where ctdthp.id = ht3.ctdt_hoc_phan_id 
                    and ht3.hoc_phan_id not in (select svhp5.hoc_phan_id from sinh_vien_hoc_phan as svhp5 
                    where svhp5.sinh_vien_id = %s))""", 
                    (id.id, id.id))
            hocphan_serializer = HocPhanSerializer(hocphan, many=True)
            cache.set(HOC_PHAN_DANG_KY + "_" + str(id.mssv), hocphan_serializer.data, timeout=3*24*60*60)
        hocphandks = HocPhanDangKy.objects.all()
        hocphanser = HocPhanDangKySerializer(hocphandks, many=True)
        cache.set(HOC_PHAN_DANG_KY_TRONG_KY, hocphanser.data, timeout=3*24*60*60)
        # print(hocphan_serializer.data)
        # for h in hocphan:
        #     print(h.ten_hoc_phan)
        # print("count ", count)
        # count += 1
        # print(count)
        return Response({"successs": True})
    
class GetData(viewsets.ViewSet):
    def get_hoc_phan_sv_dk(self, request, *args, **kwargs):
        mssv = request.GET.get('mssv')
        data = cache.get(HOC_PHAN_DANG_KY + "_" + mssv)
        list_mahocphan = []
        for i in data:
            list_mahocphan.append(i['ma_hoc_phan'])
        hoc_phan_trong_ky = cache.get(HOC_PHAN_DANG_KY_TRONG_KY)
        response = []
        for hocphan in hoc_phan_trong_ky:
            for mhp in list_mahocphan:
                if mhp in hocphan['ma_hoc_phan']:
                    response.append(hocphan)
                    break
        if data == None or mssv == None:
            return Response({"success": False})
        return Response({"success" : True,
                         "data": response})
    def test(self, request, *args, **kwargs):
        data = cache.clear()
        print(data)
        return Response({"success": True})
    def dktinchi(self, request, *args, **kwargs):
        mssv = request.GET.get('mssv')
        mahp = request.GET.get('ma_hoc_phan')
        hoc_phan_trong_ky = cache.get(HOC_PHAN_DANG_KY_TRONG_KY)
        for hoc_phan in hoc_phan_trong_ky:
            if hoc_phan['ma_hoc_phan'] == mahp:
                hoc_phan_dk = cache.get(mahp)
                if hoc_phan_dk == None:
                    data = [mssv]
                    cache.set(mahp, data, timeout=3*24*60*60)
                else:
                    hoc_phan_dk.append(mssv)
                    cache.set(mahp, hoc_phan_dk, timeout=3*24*60*60)
                sinh_viendk = cache.get(mssv)
                if sinh_viendk == None:
                    data = [hoc_phan]
                    cache.set(mssv, data, timeout=3*24*60*60)
                else:
                    sinh_viendk.append(hoc_phan)
                    cache.set(mssv, sinh_viendk, timeout=3*24*60*60)
        return Response({"success":True,
                         "data": cache.get(mahp)})
    def get_hoc_phan(self, request, *args, **kwargs):
        mahp = request.GET.get('ma_hoc_phan')
        sinh_vien_dang_ky = cache.get(mahp)
        return Response({"success": True, 
                         'data': sinh_vien_dang_ky})
    def get_hoc_phan_sinh_vien(self, request, *args, **kwargs):
        mssv = request.GET.get('mssv')
        return Response({"success": True,
                         "data": cache.get(mssv)})
        