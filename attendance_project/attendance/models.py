from django.db import models

# Create your models here.

#TODO make max_length values exposable as Docker ENV VAR?

class Student(models.Model):
    last_name = models.CharField('last name', max_length=50, null=False)
    uuid = models.JSONField('uuid' ,null=False)

    # not sure if I'm going to use these values...
    first_name = models.CharField('first name', max_length=50, blank=True)
    school_id = models.CharField('school id', max_length=10, blank=True)
    course = models.CharField(max_length=50,blank=True)
    section = models.CharField(max_length=5, blank=True)

    def __str__(self):
        return f"{self.last_name} in {self.course} section {self.section}"

class Attendance(models.Model):
    last_name = models.ForeignKey(to=Student, on_delete=models.CASCADE)
    date_time = models.DateTimeField('date & time')
    excused = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.last_name.first_name or self.last_name.last_name} attended class on {self.date_time} with uuid of {self.last_name.uuid['uuid'][0]}"