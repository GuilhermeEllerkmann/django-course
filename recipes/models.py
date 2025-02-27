from django.contrib.auth.models import User
from django.db import models
from typing import Optional
from django.core.validators import MaxLengthValidator


class Category(models.Model):
    name: models.CharField = models.CharField(max_length=65)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    title: models.CharField = models.CharField(
        max_length=65,
        validators=[MaxLengthValidator(65)]
    )
    description: models.CharField = models.CharField(max_length=165)
    slug: models.SlugField = models.SlugField()
    preparation_time: models.IntegerField = models.IntegerField()
    preparation_time_unit: models.CharField = models.CharField(max_length=65)
    servings: models.IntegerField = models.IntegerField()
    servings_unit: models.CharField = models.CharField(max_length=65)
    preparation_steps: models.TextField = models.TextField()
    preparation_steps_is_html: models.BooleanField = models.BooleanField(
        default=False
        )
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)
    updated_at: models.DateTimeField = models.DateTimeField(auto_now=True)
    is_published: models.BooleanField = models.BooleanField(default=False)
    cover: models.ImageField = models.ImageField(
        upload_to='recipes/covers/%Y/%m/%d/'
        )
    category: Optional[models.ForeignKey] = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default=None
    )
    author: Optional[models.ForeignKey] = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True
    )

    def __str__(self) -> str:
        return self.title
