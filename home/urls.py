from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
app_name = "home"
urlpatterns = [
    path("",HomeView.as_view(),name='home'),
    path("<slug:slug>", ProductDetailView.as_view(),name="product_detail")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)