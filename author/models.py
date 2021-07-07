
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
        return str('Username : {0} : Email : {1} : Pattren : {2}'.format(
            self.username,
            self.email,
            self.pattern))

class UsersLogin(models.Model):

    id         = models.AutoField(primary_key=True)
    username   = models.CharField(max_length=100)
    pattern    = models.CharField(max_length=100)

    def __unicode__(self):
        return self.id

    class Meta:
        ordering = ('id',)
        verbose_name = 'UserLogin'
        verbose_name_plural = 'UsersLogin'

    def __str__(self):
        return str('Username : {0} : Pattren : {1}'.format(
            self.username,
            self.pattern))

