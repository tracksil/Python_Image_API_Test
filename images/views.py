import os.path
from django.shortcuts import render, redirect
from django.http import JsonResponse
from colorthief import ColorThief
import requests
from .forms import UploadForm
from .models import Images
from .serializers import ImagesSerializer


def images_list(request):

    images = Images.objects.all()
    serializer = ImagesSerializer(images, many=True)
    return JsonResponse(serializer.data, safe=False)


def upload(request):
    if request.POST:
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')
    return render(request, 'images/upload.html', {'form': UploadForm})


def update_image(request, photo_id):
    image = Images.objects.get(pk=photo_id)
    form = UploadForm(request.POST or None, instance=image)
    if form.is_valid():
        file_path = f"media/{image.image}"

        if os.path.isfile(file_path) and 'image' in request.FILES:
            os.remove(file_path)

            new_image = request.FILES['image']
            image.image = new_image

            image.url = f'/media/images/{new_image.name}'

            im = ColorThief(new_image)
            color = im.get_color(quality=1)
            image.dominant_color = '#%02x%02x%02x' % color

        form.save()
        return redirect('home')
    return render(request, 'images/update.html', {'form': form})


def delete_image(request, photo_id):
    image = Images.objects.get(pk=photo_id)
    file_path = f"media/{image.image}"
    if os.path.isfile(file_path):
        os.remove(file_path)
    image.delete()
    return redirect('home')


def import_images(request):

    response = requests.get('https://jsonplaceholder.typicode.com/photos')
    for r in response.json():
        image = Images(title=r['title'], album_id=r['albumId'], url=r['url'])
        image.save()

    return redirect('home')
