from django.shortcuts import render
from django.http import HttpResponse
from . import models
import pandas as pd
import random

data = pd.read_excel("C:/Users/Anurag Shukla/Desktop/Microsoft Gondi/ProjectBackendNew/projectBackEnd/main/res/wordsData.xlsx")
DATA_LEN =len(data)
# Create your views here.
def getTen(request):
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
    return HttpResponse("Success")