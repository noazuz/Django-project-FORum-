from django.db import models
from django.urls import reverse

class Category(models.Model):
    title = models.CharField(max_length=256)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("category_list", kwargs={"pk": self.pk})
    

class Post(models.Model):
    title = models.CharField(max_length=256)
    content = models.TextField(default='soon...')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    watched = models.IntegerField(default=0)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={"pk": self.pk})