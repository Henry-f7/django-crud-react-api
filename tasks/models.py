from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    deletetime = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def delete(self, using=None, keep_parents=False):
        self.deletetime = timezone.now()
        self.save()
        return self
