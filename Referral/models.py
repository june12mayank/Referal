from django.db import models

# Create your models here.

class Person(models.Model):
    def __str__(self):
        return self.name

    name= models.CharField(max_length=50)
    company= models.CharField(max_length=30)
    experienceDescription= models.TextField()
    email= models.EmailField(max_length=70)

class Job(models.Model):    
    def __str__(self):
        return self.heading

    company= models.CharField(max_length=30)
    heading= models.CharField(max_length=70)
    description= models.TextField()
    post_date= models.DateTimeField('Date_Posted')
    person= models.ForeignKey(Person, on_delete=models.CASCADE)






