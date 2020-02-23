from django.urls import path, include
from django.contrib import admin
from core.views import test_view

admin.autodiscover()

urlpatterns = [
    path("", test_view, name="test_view"),
    path("admin/", admin.site.urls),
]
