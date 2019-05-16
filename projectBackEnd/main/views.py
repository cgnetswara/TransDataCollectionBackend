from django.shortcuts import render
from django.http import HttpResponse
from . import models
import pandas as pd
import random, json

data = pd.read_excel("C:/Users/Anurag Shukla/Desktop/Microsoft Gondi/ProjectBackendNew/projectBackEnd/main/res/wordsData.xlsx")
DATA_LEN =len(data)
# Create your views here.

def home(request):
    return  HttpResponse("The server started successfully. Make sure the android application is in the same network.")

def getTen(request, IMEI):
    dicti = {}
    QRows = []
    user = models.User()
    # random.seed(9000)
    # while len(QRows) != 10:
    #     id = random.randint(0, DATA_LEN-1)
    #     if id not in QRows:
    #         QRows.append(id)
    # toShow = []
    # for i in QRows:
    #     preExist = models.Question.objects.filter(id=i)
    #     if len(preExist) == 0:
    #         newEntry = models.Question()
    #         newEntry.word = data['Hindi'].iloc[i]
    #         newEntry.id = i
    #         newEntry.save()
    #     dicti[i] = data['Hindi'].iloc[i]
    try:
        user = models.User.objects.get(IMEI = IMEI)
    except:
        user.IMEI = IMEI
        user.save()

    offset = user.offset
    for i in range(offset, offset+10):
        dicti[i] = data['Hindi'].iloc[i]
        newEntry = models.Question()
        newEntry.word = data['Hindi'].iloc[i]
        newEntry.id = i
        newEntry.save()
    user.save()
    jsonDict = {'words': dicti, 'offset': offset}
    return HttpResponse((json.dumps(jsonDict)))

def submitAnswer(request, IMEI, qId, answerGiven):
    # if(len(models.User.filter(IMEI=IMEI)) == 0):
    #     user = models.User()
    #     user.IMEI = IMEI
    #     user.save()

    user = models.User.objects.get(IMEI=IMEI)
    question = models.Question.objects.get(id=qId)
    question.save()
    userAnswer = models.UserAnswer()
    try:
        answer = models.Answer.objects.get(question=question, answer=answerGiven)
        answer.count += 1
        answer.save()
    except:
        answer = models.Answer()
        answer.question = question
        answer.answer = answerGiven
        answer.save()

    userAnswer.user = user
    userAnswer.answer = answer
    userAnswer.save()

    # answerObject = models.Answer()
    # answerObject.question = question
    # answerObject.answer = answerGiven
    # answerObject.user = user
    # answerObject.save()
    user.offset = qId+1
    user.save()
    return HttpResponse("Success")


