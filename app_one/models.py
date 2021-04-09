from django.db import models

class Dojo(models.Model):
    name = models.CharField(max_length = 60)
    city = models.CharField(max_length = 60)
    state = models.CharField(max_length = 60)
    desc = models.TextField()
    #ninjas.all()




class Ninja(models.Model):
    dojo = models.ForeignKey(Dojo, related_name="ninjas", on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 60)
    last_name = models.CharField(max_length = 60)
