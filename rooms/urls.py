from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("", views.RoomViewSet)

app_name = "rooms"

urlpatterns = router.urls
