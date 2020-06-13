from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen
import re

print("\n")
print("Let's Find Mobile with suitable range")
print("-----------------------------------------------------------------------------------------------------")
print("\n")

lrange = str(input("Enter Lowest Amount of your budget = "))
hrange = str(input("Enter Highest Amount of  your budget = "))

print("\n")
print("Please wait while computer is doing your work")
print("Your results will be displayed here")
print("\n")


url = urlopen("https://www.91mobiles.com/list-of-phones/mobile-phones-in-range-of-"+lrange+"-to-"+hrange)

name = []
price = []

soup = BeautifulSoup(url , 'html.parser')

for i in soup.findAll('a' , attrs={'class' : ("hover_blue_link name gaclick") }):
	mname = re.search('>(.+?)<',str(i))
	name.append(mname.group(1))

for j in soup.findAll('span' , attrs={'class' : ("price price_padding") }):
	mprice = re.search('span>(.+?)</',str(j))
	price.append(mprice.group(1))


for mobile in range(10):
	print(name[mobile]+" ------> "+price[mobile])

print("\n Thank You")
