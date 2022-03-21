from django.db import models

class Player(models.Model):
    full_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username


class Code(models.Model):
    name = models.CharField(max_length=20, unique=True)
    name_human_readable = models.CharField(max_length=50)
    achievers_left = models.IntegerField(default=5)
    message = models.TextField(max_length=280)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    code = models.ForeignKey(Code, on_delete=models.CASCADE)
    points = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)

    #TODO: add a function that returns wheter the transaction was before the end of the event