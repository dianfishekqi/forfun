#!/bin/python3

from pyquery import PyQuery 
import urllib3

http = urllib3.PoolManager()
req = http.request('GET','http://rezultatet.kqz-ks.org/Results.aspx?RaceID=1&UnitID=1&IsPS=0&Turnout=0&LangID=2')
the_page = req.data
pq = PyQuery(the_page)
tag = pq('#tableresults tr')
print("----------------------")
for party in tag.items():
   #print(party.find('img').attr('src'))
    if party.find('img').attr('src') == "img/Parties/35.jpg":
        print("LVV")
        print(party.find('.txt-dark-red.strong.rtxt').text()+" VOTUES")
        print(party.find('.txt-red.strong.rtxt').text())
        print("----------------------")
    if party.find('img').attr('src') == "img/Parties/12.jpg":
        print("PAN")
        print(party.find('.txt-dark-red.strong.rtxt').text()+" VOTUES")
        print(party.find('.txt-red.strong.rtxt').text())
        print("----------------------")
    if party.find('img').attr('src') == "img/Parties/16.jpg":
        print("LAA")
        print(party.find('.txt-dark-red.strong.rtxt').text())
        print(party.find('.txt-red.strong.rtxt').text()+" VOTUES")
        print("----------------------")

#.parent().parent().child("txt-red strong rtxt").text
