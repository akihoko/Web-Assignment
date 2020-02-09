from django.conf import settings
from django.db import models

# Create your models here.

class items(models.Model):
    hotel_img=models.FileField()
    hotel_name=models.CharField(max_length=50)

    def __str__(self):
        return self.hotel_name

class Hotels(models.Model):
    hotel=models.ForeignKey(items,on_delete=models.CASCADE)
    description=models.TextField()
    logo=models.FileField(blank=True)
    img1=models.FileField(blank=True)
    img2 = models.FileField(blank=True)
    img3 = models.FileField(blank=True)
    img4 = models.FileField(blank=True)

class Room(models.Model):
    hotel=models.ForeignKey(items,on_delete=models.CASCADE)
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    Room_type=models.CharField(max_length=70)
    Numberofguests=models.IntegerField()
    Numberofrooms=models.IntegerField()
    Price=models.IntegerField()
    Duration=models.IntegerField()
    BookedDate=models.DateField()
    BookedFor=models.DateField()


