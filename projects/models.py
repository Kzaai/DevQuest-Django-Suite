from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200) #tytul
    description = models.TextField() #opis 
    technology = models.CharField(max_length=100) #technologia
    created_at = models.DateTimeField(auto_now_add=True) #data utworzenia



    def __str__(self):
        return self.title
    
