from django.db import models



class StreamPlatform(models.Model):
    name=models.CharField(max_length=50)
    about=models.CharField(max_length=200)
    website=models.URLField( max_length=200)
    
    def __str__(self):
        return self.name


class Watchlist(models.Model):
    title=models.CharField( max_length=50)
    description=models.CharField( max_length=150)
    active=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.name
    