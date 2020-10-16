from django.db import models

class person(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    profession=models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    city=models.CharField(max_length=30)
    state=models.CharField(max_length=30)
    pincode=models.IntegerField()
    phoneno=models.IntegerField()
    emailid=models.EmailField()
    profile=models.TextField(max_length=100)

    def __str__(self):
        return self.firstname

class education(models.Model):
    institute=models.CharField(max_length=40)
    startingyear=models.IntegerField()
    endingyear=models.IntegerField()
    grade=models.CharField(max_length=4)
    course=models.CharField(max_length=20)

    def __str__(self):
        return self.institute

class experience(models.Model):
    company=models.CharField(max_length=40)
    startingyear=models.IntegerField()
    endingyear=models.IntegerField()
    post=models.CharField(max_length=20)
    details=models.TextField(max_length=200)

    def __str__(self):
        return self.company

class projects(models.Model):
    topic=models.CharField(max_length=40)
    startingyear=models.IntegerField()
    endingyear=models.IntegerField()
    details=models.TextField(max_length=200)

    def __str__(self):
        return self.topic

class whole(models.Model):
    person=models.ForeignKey(person, on_delete=models.CASCADE)
    education=models.ForeignKey(education, on_delete=models.CASCADE)
    experience=models.ForeignKey(experience, on_delete=models.CASCADE)




# Create your models here.

class FilesUpload(models.Model):
    file = models.FileField()


    def __str__(self):
        return self.file


