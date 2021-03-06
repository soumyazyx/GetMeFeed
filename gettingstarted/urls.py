from django.urls import path, include
from django.contrib import admin
from core.views import TestView, NASAView, dummy, SPACEDOTCOMView

admin.autodiscover()

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("dummy/", dummy, name="dummy"),
    path("", TestView.as_view(), name="test"),
    path("NASA/", NASAView.as_view(), name="NASA"),
    path("SPACEDOTCOM/", SPACEDOTCOMView.as_view(), name="SPACEDOTCOM")
]
