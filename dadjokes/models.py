from django.db import models

# Create your models here.

class Joke(models.Model):
    text = models.TextField()
    contributor_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.text[:50]}... by {self.contributor_name}"

    class Meta:
        ordering = ['-created_at']


class Picture(models.Model):
    image_url = models.URLField(max_length=500)
    contributor_name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Picture by {self.contributor_name}"

    class Meta:
        ordering = ['-created_at']
