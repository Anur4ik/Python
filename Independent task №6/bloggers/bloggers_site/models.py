from django.db import models
from django.utils import timezone

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=Blogger.Status.PUBLISHED)
class NewsPublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status=News.Status.PUBLISHED)
class Blogger(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    category = models.CharField(max_length=50)
    bio = models.TextField()
    socials = models.JSONField(default=dict, help_text="Посилання на соц. мережі, напр.: {'youtube': 'url'}")
    objects = models.Manager()
    published = PublishedManager()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.name


class Content(models.Model):
    class ContentType(models.TextChoices):
        ARTICLE = 'AR', 'Стаття'
        POST = 'PT', 'Пост'
    blogger = models.ForeignKey(
        Blogger,
        on_delete=models.CASCADE,
        related_name='content_pieces'
    )
    type = models.CharField(
        max_length=2,
        choices=ContentType.choices,
        default=ContentType.ARTICLE
    )
    title = models.CharField(max_length=250)
    description = models.TextField(max_length=500, help_text="Напишіть тут повний текст статті або посту")
    published_date = models.DateTimeField(default=timezone.now, help_text="Дата публікації контенту")
    class Meta:
        ordering = ['-published_date']
        indexes = [
            models.Index(fields=['-published_date']),
        ]

    def __str__(self):
        return f"{self.get_type_display()} від {self.blogger.name}: {self.title}"


class News(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        PUBLISHED = 'PB', 'Published'

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    content = models.TextField()

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    published = NewsPublishedManager()

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    )

    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish']),
        ]

    def __str__(self):
        return self.title