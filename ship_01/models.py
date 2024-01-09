from django.db import models

# Create your models here.
class ShipList(models.Model):
    code = models.IntegerField(db_column='CODE', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', max_length=200)  # Field name made lowercase.
    owner = models.ForeignKey('UserList', models.DO_NOTHING, db_column='OWNER', blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(db_column='TYPE', max_length=30, blank=True, null=True)  # Field name made lowercase.
    length = models.IntegerField(db_column='LENGTH', blank=True, null=True)  # Field name made lowercase.
    height = models.IntegerField(db_column='HEIGHT', blank=True, null=True)  # Field name made lowercase.
    width = models.IntegerField(db_column='WIDTH', blank=True, null=True)  # Field name made lowercase.
    waterline = models.IntegerField(db_column='WATERLINE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ship_list'


class UserList(models.Model):
    id = models.CharField(db_column='ID', primary_key=True, max_length=100)  # Field name made lowercase.
    pw = models.CharField(db_column='PW', max_length=15, blank=True, null=True)  # Field name made lowercase.
    dept = models.CharField(db_column='DEPT', max_length=20, blank=True, null=True)  # Field name made lowercase.
    tel = models.CharField(db_column='TEL', max_length=20, blank=True, null=True)  # Field name made lowercase.
    e_mail = models.CharField(db_column='E_MAIL', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_list'

