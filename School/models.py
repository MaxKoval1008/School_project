from django.db import models


class School(models.Model):
    school_number = models.IntegerField()
    address = models.TextField(max_length=1000)
    school_characteristic = models.CharField(max_length=1000, null=True, blank=True)

    def __int__(self):
        return self.school_number


class Group(models.Model):
    group_number = models.IntegerField(unique=True)
    course = models.IntegerField()
    motto = models.CharField(max_length=100, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __int__(self):
        return self.group_number


class Student(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    eng = models.IntegerField()
    math = models.IntegerField()
    bio = models.IntegerField()
    phis = models.IntegerField()
    chem = models.IntegerField()
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return self.lastname
