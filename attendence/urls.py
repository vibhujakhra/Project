from posixpath import basename
from rest_framework.routers import DefaultRouter
from . import views
from django.views.generic import TemplateView
from django.urls import path
# from django.conf.urls import url


router=DefaultRouter()

urlpatterns = [
    path(r'upload-sheet',
        TemplateView.as_view(template_name="upload_sheet.html")),
    path(r'wp/', views.SheetUploadView.as_view(), name="wp"),
    path(r'pie-chart', views.pie_chart, name='pie-chart'),
]
router.register('submit', views.StoreData, basename='submit')

urlpatterns += router.urls
