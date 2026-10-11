from django.urls import path
from . import views

urlpatterns=[
    path('api/create_stock/' , views.create_stock_api , name="create_stock_api"),
    path('api/list_stock/' , views.list_stock_api , name="list_stock_api"),
    path('api/detail_stock/<int:id>/' , views.detail_stock_api , name="detail_stock_api"),
    path('api/update_stock/<int:id>/' , views.update_stock_api , name="update_stock_api"),
    path('api/delete_stock/<int:id>/' , views.delete_stock_api , name="delete_stock_api"),

    path('api/summary_stock/' , views.summary_stock_api , name="summary_stock_api"),
]