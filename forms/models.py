from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
    subject_list = [('Bio', 'Biology'), ('Alg', "Algebra"), ('Geom', "Geometry"), ('Ch', 'Chemistry'), ('PE', "Physical Education")]
    name = models.CharField(max_length=50, choices=subject_list)
class Mark(models.Model):
    grade_list = [('12', '12'),('11', '11'), ('10', '10'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')]
    grade = models.CharField(max_length=2, choices=grade_list)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()