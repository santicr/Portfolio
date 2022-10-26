from django.db import models

# Create your models here.
class Project(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField()
    img = models.ImageField(upload_to = 'projects')
    url = models.URLField(max_length = 200)

    def __str__(self):
        return f'Project: {self.name}'
