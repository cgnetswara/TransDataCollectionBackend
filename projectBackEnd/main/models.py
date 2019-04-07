from django.db import models
import uuid
# Create your models here.
class User(models.Model):
    IMEI = models.CharField(max_length=200)

class Question(models.Model):
    word = models.CharField(max_length=200)
    id = models.IntegerField(editable=False)
    id.primary_key = True

    def __str__(self):
        return self.word

class UserQA(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    QId = models.ForeignKey(Question, on_delete=models.CASCADE)
    AId = models.IntegerField()

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=200)