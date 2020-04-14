#Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), 
#and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

import requests
from bs4 import BeautifulSoup
import parser

url = 'http://www.practicepython.org/'
r = requests.get(url)
r_html = r.text

soup = BeautifulSoup(r_html,'html.parser')

#asks the user what they want to call the file they want to save
fileExtension = ".txt"
userFileName = str(input("Enter the name of the file:")) + fileExtension
f = open(userFileName,"w+")

for link in soup.find_all('a'):
    f.write("{}\n".format(link.get('href')))

f.close()