from django.db import models

# Create your models here.

from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # Enables WYSIWYG editor

    created_at = models.DateTimeField(auto_now_add=True)

