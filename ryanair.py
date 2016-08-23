#!/usr/bin/python
 
import requests, json

print "1. Stansted - STN"
print "2. Szymany - SZY"
print "3. Lodz - LCJ"


choices = input("Fly from: ")
if choices == 1:
   ORG = "STN"
elif choices == 2:
   ORG = "SZY"
elif choices == 3:
   ORG = "LCJ"
 
choiced = input("Fly to: ")
if choiced == 1:
   DST = "STN"
elif choiced == 2:
   DST = "SZY"
elif choiced == 3:
   DST = "LCJ"

dateout = raw_input("Start date: ")
datein = raw_input("Return date: ")

URL = "https://desktopapps.ryanair.com/en-gb/availability?ADT=1&CHD=0&DateIn=%s&DateOut=%s&Destination=%s&FlexDaysIn=6&FlexDaysOut=6&INF=0&Origin=%s&RoundTrip=true&TEEN=0"  % (datein, dateout, DST, ORG)


r = requests.get(URL, data={'Origin': 'https://www.ryanair.com', 'Referer': 'https://www.ryanair.com/gb/en/booking/home'})
data = json.loads(r.content)
 
#print data

curency = data["currency"]
for trip in data["trips"]:
  destination = trip["destination"]
  origin = trip["origin"]
  print "*---------"
  for date in trip["dates"]:
     for flight in date["flights"]:
          flightKey = flight["flightKey"]
          faresLeft = flight["faresLeft"]
          infantsLeft = flight["infantsLeft"]
          RFamount = flight["regularFare"]["fares"][0]["amount"]
          fareclass = flight["regularFare"]["fareClass"]
          farekey = flight["regularFare"]["fareKey"]
          
          print  "|%s-%s | flightKey : %s | FaresLeft : %s | InfantLeft : %s | amount : %s %s | FareClass : %s | FareKey : %s" % (origin, destination, flightKey, faresLeft, infantsLeft, RFamount, curency, fareclass, farekey)

