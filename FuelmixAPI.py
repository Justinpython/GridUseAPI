import requests
import json


response = requests.get('https://api.carbonintensity.org.uk/regional/scotland', params={})

info= []

pie = response.json()["data"][0]["data"][0]

for i in pie["generationmix"]:
	info.append(i)


print("Energy production, Scotland")
for i in info:
	print(i["fuel"],": ", i["perc"],"%")
