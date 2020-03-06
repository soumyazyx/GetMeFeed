from django.urls import path, include
from django.contrib import admin
from core.views import TestView, NASAView

admin.autodiscover()

urlpatterns = [
    path("", TestView.as_view(), name="test"),
    path("test/", TestView.as_view(), name="test2"),
    path("NASA/", NASAView.as_view(), name="NASA"),
    path("admin/", admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]
