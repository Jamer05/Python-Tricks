#if you are using google collab "!pip install pyqrcode" && "!pip install pypng"
#@author Hemerson G. Ramiro Jr.

import pyqrcode 
import png 
from pyqrcode import QRCode 
  
def to_url():
    s = input("Enter URL: ")
    url = pyqrcode.create(s) 

    url.svg("myqr.svg", scale = 8) 
    url.png('myqr.png', scale = 6) 


def information(n,a,ad):

          return "Name: n"+"\nAge: a"+"\nAddress: ad"

print ('''>>Press 1 to create qr urls
>>Press 2 to create qr information 
''')
sel = int(input("Select mode: "))

if sel == 1:
         to_url()
elif sel == 2:
      n,a,ad = input("Enter name: "),input("Enter age: "), input("Enter Address: ")
      myQR = pyqrcode.create(information(n,a,ad))
      myQR.png('myqrcode.png', scale=8)
         