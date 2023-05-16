from django.db import models

# Create your models here.

class Blog(models.Model):
    """
    Blog model for app
    """
    title = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    catgory = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    content = models.TextField()
    status = models.BooleanField
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class Caregory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
