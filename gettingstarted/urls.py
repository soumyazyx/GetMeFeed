from django.urls import path, include
from django.contrib import admin
from core.views import TestView

admin.autodiscover()

urlpatterns = [
    path("", TestView.as_view(), name="test"),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
