from django.urls import path, re_path
from . import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('department/', views.departmentApi),
    path('department/<int:id>', views.departmentApi),

    path('hero/', views.heroApi),
    path('hero/<int:id>', views.heroApi),

    path('SaveFile', views.saveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)