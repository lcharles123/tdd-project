from django.db import models

# class -> Tables
# atributos -> columns
# instancias -> linhas
class Item(models.Model):
    text = models.TextField(default='')
