
from .utils import generate_random_id 
from django.utils.text import slugify
from django.db import models
from django.contrib.auth import get_user_model
from .managers import ActiveLinkManager
  
        



# Create your models here.

class Link(models.Model):
    target_url = models.URLField(max_length = 200)
    description = models.CharField(max_length = 200)
    identifier = models.SlugField(blank = True, unique = True)
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField(default=True)
    objects = models.Manager()
    public = ActiveLinkManager()
    
    def __str__(self):
        return self.target_url
    
    def save(self, *args, **kwargs):
        self.identifier = slugify(generate_random_id())
        super(Link, self).save(*args, **kwargs)
    
    
    