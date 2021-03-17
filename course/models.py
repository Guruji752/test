from django.db import models
from datetime import datetime
from embed_video.fields import EmbedVideoField
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from .fields import OrderField
from django import forms
from tinymce import models as tinymce_models


# Create your models here.
class Course(models.Model):
    owner = models.ForeignKey(User, related_name='courses_created', on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=100, default="Course_name")
    tag_line = models.CharField(max_length=500, blank=True)
    title_tag = models.CharField(max_length=500, blank=True)
    course_duration = models.CharField(max_length=20, blank=True)
    selling_price_dolor = models.IntegerField(blank=True)
    orignal_price_dolor = models.IntegerField(blank=True)
    price = models.IntegerField(blank=True)
    orignal_price_rupees = models.IntegerField(blank=True)
    selling_price_dirham = models.IntegerField(blank=True)
    orignal_price_dirham = models.IntegerField(blank=True)
    brif_summery = tinymce_models.HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    course_content = tinymce_models.HTMLField()
    course_objective = tinymce_models.HTMLField()
    course_aims = tinymce_models.HTMLField()
    course_outcomes = tinymce_models.HTMLField()
    teaching = tinymce_models.HTMLField()
    sample_certificate = models.ImageField(upload_to='certificate/')
    posting_date = models.DateTimeField(default=datetime.now, blank=True)
    description_video = EmbedVideoField(blank=True)
    image = models.ImageField(upload_to='course/')
    is_published = models.BooleanField(default=True)
    is_popluar = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    banner = models.ImageField(upload_to='banner/')

    def __str__(self):
        return self.name


class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])
    video_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.order}. {self.title}'

    class Meta:
        ordering = ['order']


class Content(models.Model):
    module = models.ForeignKey(Module, related_name='contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE,
                                     limit_choices_to={'model__in': ('text', 'video', 'image', 'file')})
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()


class File(ItemBase):
    file = models.FileField(upload_to='files')


class Image(ItemBase):
    file = models.FileField(upload_to='images')


class Video(ItemBase):
    url = models.URLField()


class PaymentPage(models.Model):
    name = models.CharField(max_length=300)
    course_title = models.CharField(max_length=500)
    username = models.CharField(max_length=500)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    refference_image = models.ImageField()
    refference = models.CharField(max_length=200)

