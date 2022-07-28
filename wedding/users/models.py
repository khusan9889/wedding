# from email.policy import default
# from logging import PlaceHolder
# from tkinter import Widget
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


countries = (
    ("Ташкент" , "Ташкент"),
    ("Самарканд", "Самарканд"),
    ("Бухара", "Бухара "),
    ("Нукус", "Нукус"),
    ("Хива", "Хива"),
    ("Андижан", "Андижан"),
    ("Джизак", "Джизак"),
    ("Кашкадарья", "Кашкадарья"),
    ("Навои","Навои"),
    ("Наманган","Наманган"),
    ("Сурхандарья","Сурхандарья"),
    ("Фергана","Фергана"),
    ("Хорезм","Хорезм")
)

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    patronymic = models.CharField(max_length=50)
    phone_number = PhoneNumberField()
    country = models.CharField(max_length=20,choices=countries, default='1')


    class Meta:
        verbose_name_plural = "User"

    def __str__(self):
        return self.first_name

        