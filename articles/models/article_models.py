from django.db import models

# Create your models here.
class Article(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    medicament = models.CharField(max_length=50,blank=False,unique=True)
    imgLinkAddress = models.URLField(blank=True,null=True)
    description = models.TextField()
    quantite = models.IntegerField()

    class Meta:
        ordering = ['-created']
    def __str__(self):
        return self.medicament

    