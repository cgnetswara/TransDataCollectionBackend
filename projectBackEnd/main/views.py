from django.shortcuts import render
from django.http import HttpResponse
from . import models
import pandas as pd
import random, json

data = pd.read_excel("C:/Users/Anurag Shukla/Desktop/Microsoft Gondi/ProjectBackendNew/projectBackEnd/main/res/wordsData.xlsx")
DATA_LEN =len(data)
# Create your views here.
def getTen(request):
    dicti = {}
    QRows = []
    random.seed(9000)
    while len(QRows) != 10:
        id = random.randint(0, DATA_LEN-1)
        if id not in QRows:
            QRows.append(id)
    toShow = []
    for i in QRows:
        preExist = models.Question.objects.filter(id=i)
        if len(preExist) == 0:
            newEntry = models.Question()
            newEntry.word = data['Hindi'].iloc[i]
            newEntry.id = i
            newEntry.save()
        dicti[i] = data['Hindi'].iloc[i]

    return HttpResponse(str(dicti))

def submitAnswer(request, IMEI, qId, answerGiven):
    user = models.User()
    user.IMEI = IMEI
    user.save()
    question = models.Question.objects.get(id=qId)
    answerObject = models.Answer()
    answerObject.question = question
    answerObject.answer = answerGiven
    answerObject.user = user
    answerObject.save()
    return HttpResponse("Success")


