
import os
from django.conf import settings
from django.db import models

# Create your models here.

class Users(models.Model):

    id         = models.AutoField(primary_key=True)
    email      = models.EmailField(max_length=200)
    fname      = models.CharField(max_length=100)
    lname      = models.CharField(max_length=100)
    username   = models.CharField(max_length=100)
    pattern    = models.CharField(max_length=100)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return str('{0} : {1}'.format(
            self.id,
            self.username))

class UsersLogin(models.Model):

    id         = models.AutoField(primary_key=True)
    username   = models.CharField(max_length=100)
    pattern    = models.CharField(max_length=100)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return str('{0} : {1}'.format(
            self.id,
            self.username))

