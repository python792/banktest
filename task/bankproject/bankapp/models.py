from django.db import models
from django.urls import reverse
# Create your models here.

class branch(models.Model):
    name = models.CharField(max_length=300,unique=True)
    slug = models.SlugField(max_length=300, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'branch'
        verbose_name_plural = 'branches'

        def __str__(self):
            return self.name

class place(models.Model):
        pname = models.CharField(max_length=250, unique=True)
        slug = models.SlugField(max_length=300, unique=True)
        branch = models.ForeignKey(branch, on_delete=models.CASCADE)

        class Meta:
            ordering = ('pname',)
            verbose_name = 'place'
            verbose_name_plural = 'places'

        def __str__(self):
            return self.pname

class userdetail(models.Model):
    firstname = models.CharField(max_length=250)
    lastname = models.CharField(max_length=250)
    age = models.IntegerField()
    gender = models.CharField(max_length=250)
    email = models.TextField(unique=False)
    address = models.CharField(max_length=250)
    bankbranch = models.CharField(max_length=250)
    Type = models.CharField(max_length=250)


    class Meta:
        db_table = 'userdetail'


    def __str__(self):
        return '{}'.format(self.name)