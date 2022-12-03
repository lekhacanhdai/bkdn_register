from django.urls import path
from .views import *

urlpatterns = [
    path('load', LoadData.as_view({'get': 'load_all_data_register'})),
    path('hoc-phan', GetData.as_view({'get': 'get_hoc_phan_sv_dk'})),
    path('test', GetData.as_view({'get': 'test'})),
    path('dang-ky', GetData.as_view({'get': 'dktinchi'})),
    path('hoc-phan-dang-ky', GetData.as_view({'get': 'get_hoc_phan'})),
    path('sinh-vien-dang-ky', GetData.as_view({'get': 'get_hoc_phan_sinh_vien'})),
]
