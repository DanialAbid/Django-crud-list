
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('create',views.create,name='create'),
    path('create/category',views.create_cate,name='createcate'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:pk>/', views.delete, name='delete'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
