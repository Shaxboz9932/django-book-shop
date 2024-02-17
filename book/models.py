from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    price = models.FloatField(max_length=10)
    description = models.TextField()
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    pulished = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title
