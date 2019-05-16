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
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)
    count = models.IntegerField(default=1)

    def __str__(self):
        return str(self.question) + " | " + str(self.answer)

class UserAnswer(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
