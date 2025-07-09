from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index, name="index"),
    path("bonus/", bonus, name="bonus"),
    path("cleaning/", cleaning, name="cleaning"),
    path("instructions/", instructions, name="instructions"),
    path("kitchen/", kitchen, name="kitchen"),
    path("productCleaning/<int:pk>/", productCleaning, name="productCleaning"),
    path("productCooking/<int:pk>/", productCooking, name="productCooking"),
    path("recipes/", recipes, name="recipes"),
    path("support/", support, name="support"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
