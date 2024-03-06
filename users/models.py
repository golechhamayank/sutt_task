from django.db import models

# Create your models here.

class Trip(models.Model):
    #creator = SocialAccount.objects.all()[0].user.email
    creator_email = models.EmailField(max_length = 100, default = "")
    dest = models.CharField(unique = True, max_length = 150)
    date_start = models.DateField()
    date_end = models.DateField()
    est_exp = models.IntegerField(default = 0, null = False)
    
    def __str__(self):
        return self.dest

class Event(models.Model):
    creator_email = models.EmailField(max_length = 100, default = "")
    trip = models.ForeignKey(Trip,on_delete = models.CASCADE)
    name = models.CharField(max_length = 250)
    start = models.DateTimeField(blank = True, null = True)
    desc = models.CharField(max_length = 500, blank = True, null = True)
    exp = models.IntegerField(default = 0, null = False)

    def __str__(self):
        return self.name
  
    

class Wingie(models.Model):
    creator_email = models.EmailField(max_length = 100, default = "")
    trip = models.ForeignKey(Trip,on_delete = models.CASCADE)
    bits_id = models.CharField(max_length = 13)
    email_id = models.EmailField(max_length = 100,default = "")
    
    def __str__(self):
        return self.bits_id