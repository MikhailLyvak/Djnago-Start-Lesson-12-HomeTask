from django.db import models

class AnimeType(models.Model):
    name = models.CharField(max_length= 63)

    def __str__(self) -> str:
        return f"{self.name}"
    
class Anime(models.Model):
    name = models.CharField(max_length = 255)
    description = models.TextField(blank=True, null=True)
    type = models.ForeignKey(AnimeType, on_delete=models.CASCADE, blank=True, null=True)
    episodes = models.PositiveIntegerField(blank=True, null=True)
    my_episode = models.PositiveIntegerField(blank=False, null=False)
    my_rating = models.PositiveBigIntegerField(blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.name} Rating: {self.my_rating} {self.type} | {self.my_episode}/{self.episodes}"

    