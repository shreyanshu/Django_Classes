from django.db import models


# Create your models here.
class Room(models.Model):
    room_no = models.IntegerField()
    floor_no = models.IntegerField()

    def __str__(self):
        return "F"+str(self.floor_no)+"R"+str(self.room_no)



class Student(models.Model):
    name = models.CharField(max_length=255)
    roll = models.IntegerField()
    sec = models.CharField(max_length=12)
    room = models.ForeignKey(Room, on_delete=models.PROTECT, null=True)
    photo = models.ImageField(upload_to='student_pics', default='test.png')


class Department(models.Model):
    name = models.CharField(max_length=255, null=False)
    code = models.IntegerField()


class DepartmentHead(models.Model):
    name = models.CharField(max_length=255)
    department = models.OneToOneField(Department, on_delete=models.CASCADE)


class Subject(models.Model):
    name = models.CharField(max_length=240)
    code = models.CharField(max_length=4)
    student = models.ManyToManyField(Student, related_name='student')
