from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from images import views

urlpatterns = [
    path('', views.images_list, name='home'),
    path('image/upload', views.upload, name='upload'),
    path('image/update/<photo_id>', views.update_image, name='update'),
    path('image/delete/<photo_id>', views.delete_image, name='delete-image'),
    path('images/import', views.import_images, name='import'),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
