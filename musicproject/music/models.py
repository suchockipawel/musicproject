from django.db import models

# Create your models here.



class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    release_date = models.DateField()
    genre = models.CharField(max_length=50, blank=True)
    cover_image = models.ImageField(upload_to='album_covers/', blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.title} by {self.artist}"


class Song(models.Model):
    album = models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.title} ({self.duration})"