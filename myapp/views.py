from django.shortcuts import render
from .models import *
from .serializers import*
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from bs4 import BeautifulSoup
import json
import requests


# from selenium.webdriver.common.by import By

# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# # Create your views here.


# def update():
#     driver = webdriver.Chrome(ChromeDriverManager().install())
#     driver.get('https://coinmarketcap.com/')
#     driver.maximize_window()
    
#     driver.implicitly_wait(5)
#     roster_tbody = driver.find_element(By.XPATH, "//*[@id='__next']/div/div[1]/div[2]/div/div[1]/div[5]/table/tbody")
#     tr = roster_tbody.find_elements(By.TAG_NAME, "tr")
#     print("number of table rows: " + str(len(tr)))
#     l=[]
#     for i in tr:
#         l.append(i.text)
#     a=[]
#     for i in range(len(tr)):
#         a.append(l[i].split('\n'))
#     count = 0
#     for row in a:
#         if(count >= 10):
            
#             print(row)
#             # cryp = CryptoCoin(name=a, price=b)
#             # cryp.save()
#             continue
#         q = row[4]
#         x,y,z = q.split()
#         cryp = CryptoCoin(name=row[1]+" "+row[2], price=row[3], onehour=x, oneday=y, sevenday=z, marketcap=row[5], volume=row[6], supply=row[7]) 
#         cryp.save()
#         count+=1
#         #print(row)
      

#     # table = driver.find_element(By.TAG_NAME, 'tr')
#     # print(table)


def updateDB():
    

    session = requests.Session()
    html = session.get('https://coinmarketcap.com/').text
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find('table')
    table_rows = table.find_all_next('tr')
    count = 0

    for tr in table_rows:
        if(count==0):
            count+=1
            continue
        if(count >= 10):
            cryp = CryptoCoin(name=row[2], price=row[3])
            cryp.save()
            continue
        td = tr.find_all('td')
        row = [i.text for i in td]
        #print(len(row))
        cryp = CryptoCoin(name=row[2], price=row[3], onehour=row[4], oneday=row[5], sevenday=row[6], marketcap=row[7], volume=row[8], supply=row[9]) 
        cryp.save()
        count+=1
        #print(row)

class CryptoCoinApiView(APIView):
    def get(self,request):
        CryptoCoin.objects.all().delete()
        updateDB()
        crypto=CryptoCoin.objects.all()
        serializer=CryptoCoinSerializer(crypto,many=True)
        return Response(serializer.data)

