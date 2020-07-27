from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'alarm', views.Alarms, basename='alarms')
router.register(r'color', views.Colors, basename='colors')
# router.register(r'running', views.Running, basename='running')

urlpatterns = router.urls