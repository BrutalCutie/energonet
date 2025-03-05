from django.urls import include, path
from rest_framework import routers

from net import views
from net.apps import NetConfig

app_name = NetConfig.name

router = routers.DefaultRouter()
router.register(r"nets", views.NetMemberViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
