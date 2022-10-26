import os.path
from django.db import models
from django.db.models.signals import post_save
from colorthief import ColorThief


def user_directory_path(instance, filename):
    return f'images/{filename}'


class Images(models.Model):
    photo_id = models.AutoField(primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    album_id = models.IntegerField()
    image = models.ImageField(upload_to=user_directory_path, blank=True, null=True, height_field='height', width_field='width')
    dominant_color = models.CharField(max_length=7, blank=True, null=True, editable=False)
    width = models.IntegerField(blank=True, null=True, editable=False)
    height = models.IntegerField(blank=True, null=True, editable=False)
    url = models.URLField(blank=True, null=True, editable=False)


def dominant_color_post_save(sender, instance, created, *args, **kwargs):

    if created:
        if not instance.url:
            instance.url = f'/media/{instance.image}'
            instance.save()
        if os.path.isfile(f'media/{instance.image}'):
            file_path = f'media/images/{os.path.basename(instance.image.name)}'
            im = ColorThief(file_path)
            color = im.get_color(quality=1)
            instance.dominant_color = '#%02x%02x%02x' % color
            instance.save()


post_save.connect(dominant_color_post_save, sender=Images)
