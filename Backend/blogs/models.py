from django.db import models
from django.conf import settings
from django.utils.text import slugify


def blog_image_upload_location(instance, filename):
    file_path = f'blogs/images/{instance.author.username}/{filename}'
    return file_path


def blog_video_upload_location(instance, filename):
    file_path = f'blogs/videos/{instance.author.username}/{filename}'
    return file_path


class Blog(models.Model):
    title = models.CharField(max_length=120, unique=True)
    content = models.TextField()
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(null=True, blank=True, unique=True)
    image = models.ImageField(
        upload_to=blog_image_upload_location, null=True, blank=True)
    video = models.FileField(
        upload_to=blog_video_upload_location, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.author.username}-{self.title}')
        super(Blog, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-date_created', '-date_updated']
