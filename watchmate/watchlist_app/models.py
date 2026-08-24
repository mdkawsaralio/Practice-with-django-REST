from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


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
    platform=models.ForeignKey(StreamPlatform, on_delete=models.CASCADE,related_name="watchlist_data",null=True)
    
    
    def __str__(self):
        return self.title
    
    
class Reviews(models.Model):
    rating=models.PositiveIntegerField(validators=[MinValueValidator(1),MaxValueValidator(5)])
    decription=models.CharField(max_length=200,null=True)
    created=models.DateField(auto_now_add=True)
    update=models.DateField(auto_now=True)
    active=models.BooleanField(default=True)
    watchlist=models.ForeignKey(Watchlist, on_delete=models.CASCADE,related_name="reviews")
    
    
    
    def __str__(self):
        return f"{str(self.rating) } - {self.watchlist.title}"
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    