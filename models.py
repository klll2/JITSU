# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    user_id = models.CharField(primary_key=True, max_length=20)
    user_tag_1 = models.CharField(unique=True, max_length=20, blank=True, null=True)
    user_tag_2 = models.CharField(unique=True, max_length=20, blank=True, null=True)
    user_tag_3 = models.CharField(unique=True, max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class Userword(models.Model):
    word = models.ForeignKey('Word', models.DO_NOTHING)
    user = models.ForeignKey(User, models.DO_NOTHING)
    userword_fav = models.IntegerField()
    userword_mem = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userword'


class Word(models.Model):
    word_id = models.IntegerField(primary_key=True)
    word_jap = models.CharField(max_length=20)
    word_kor = models.CharField(max_length=20)
    word_def = models.CharField(max_length=100)
    word_tag = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'word'
