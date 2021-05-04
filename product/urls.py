from django.urls import path
from .views import ProductView
from .views import ProductMarkView

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'', ProductView)


urlpatterns = [
    path('marks', ProductMarkView.as_view({'get': 'list', 'post': 'create'})),
]
urlpatterns += router.urls
