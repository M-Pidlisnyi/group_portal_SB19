from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Subject(models.Model):
    subject_list = [('Bio', 'Biology'), ('Alg', "Algebra"), ('Geom', "Geometry"), ('Ch', 'Chemistry'), ('PE', "Physical Education")]
    name = models.CharField(max_length=50, choices=subject_list)
    def __str__(self):
        return self.name
class Mark(models.Model):
    grade_list = [('12', '12'),('11', '11'), ('10', '10'), ('9', '9'), ('8', '8'), ('7', '7'), ('6', '6'), ('5', '5'), ('4', '4'), ('3', '3'), ('2', '2'), ('1', '1')]
    grade = models.CharField(max_length=2, choices=grade_list)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user} - {self.subject} - {self.grade} - {self.date}"
class Role(models.Model):
    name = 'main'
    permissions = models.ManyToManyField('auth.Permission')
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)