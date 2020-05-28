from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import json
from bs4 import BeautifulSoup
import requests

def index(request):
  array = ['2891.TW']

  show = []
  for i in array:
    url = 'https://tw.stock.yahoo.com/q/q?s=' + i[:4]  # 要請求的網址
    list_req = requests.get(url)
    soup = BeautifulSoup(list_req.content, "html.parser")
    tables = soup.findAll('table')
    tab = tables[1]
    # columns = [th.text.replace('\n', '') for th in tab.find('tr').find_all('th')]
    trs = tab.find_all('tr')[1:]
    rows = list()
    for tr in trs:
      rows.append([td.text.replace('\n', '').replace('\xa0', '') for td in tr.find_all('td')])
  item = rows[1][0][:-6]
  time = rows[1][1]
  price = rows[1][2]
  message = item+"於"+time+"成交價為"+price
  return JsonResponse({"message":message})

