from django.db import models
import uuid
# Create your models here.

class User(models.Model):
    IMEI = models.CharField(max_length=200)
    offset = models.IntegerField(default=0)

    def __str__(self):
        return self.IMEI

class Question(models.Model):
    word = models.CharField(max_length=200)
    id = models.IntegerField(editable=False)
    id.primary_key = True

    def __str__(self):
        return self.word

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)

    def __str__(self):
        return str(self.user) + " | " + str(self.question) + " | " + str(self.answer)