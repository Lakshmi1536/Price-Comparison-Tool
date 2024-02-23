import smtplib
import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import messagebox
import smtplib
import matplotlib.pyplot as plt
#import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
#Identifies the client application (e.g., browser) making the request.
HEADERS = {
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US, en;q=0.5"
    }
#HTTP headers facilitate communication between clients(such as web
#browsers or mobile apps) and servers during requests and responses.
#Amazon Ipad
amazon_ipad_url = "https://www.amazon.ca/2021-Apple-iPad-10-2-inch-Wi-Fi/dp/B09G9BJVT6/ref=sr_1_1_sspa?crid=JH8GH92SZ3F3&dib=eyJ2IjoiMSJ9.rpni6IL_14CkVVRbzrBrSQP2iA-E7i-iCf8yoLOfdYtIgwhK2SR-CeHA6HjsY-FdNaYqLvEGHnkWhb0X8zaUqpJgFpiASOc6u8NK19WLlj4Uk3DlPgDfiRjYUe1ToRcdvwV-Uh9AqxRBa5celn5FVVCqQkHY4Rp9KTLlguCEzJqwoesIu_Ivn4sAz3fwF4ZwNUPRFfkcZzygWt3bzKTR1u0TqcYL37WsqLWvKMYsUnaj-Hb-7F3fnUcBGciCYC3ogWPePaQg7UAnVzIJmGjHFQWxLKSa1Q0xNw62XZab2QE.COam3A7jfV-pQcDlMC599-IshvNMd-9MjG_VhBpr984&dib_tag=se&keywords=ipad+10th+generation&qid=1708364536&sprefix=ipad+10th+generation%2Caps%2C193&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
response = requests.get(amazon_ipad_url, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
a_ipad_title_tag = soup.find("span", id="productTitle")
a_ipad_title_text = a_ipad_title_tag.getText()
a_ipad_title = a_ipad_title_text.strip()
a_ipad_price_whole_tag = soup.find("span", class_="a-price-whole")
a_ipad_price_whole_text = a_ipad_price_whole_tag.getText()
a_ipad_whole_price = a_ipad_price_whole_text.rstrip(".")
a_ipad_decimal_price_tag = soup.find("span", class_="a-price-fraction")
a_ipad_decimal_price_text = a_ipad_decimal_price_tag.getText()
a_ipad_decimal_price = a_ipad_decimal_price_text.strip()
a_ipad_price = a_ipad_whole_price + "." + a_ipad_decimal_price

#Ebay Ipad
ebay_ipad_url = "https://www.ebay.ca/itm/175524001378?epid=28049286448&itmmeta=01HQ17DJ09TM9DX11P8KKSQWQW&hash=item28de0bb662%3Ag%3Ag3kAAOSwNcxh6LAr&itmprp=enc%3AAQAIAAAA0AxcRfbUhIIib0nsP8DIRvg3llt5e6hZOun43gdLoS%2B%2FsSYGZsxpGEPJRoLgTlLevCwES3GZSRnp8DQ1tcwdNjvBDnyeEfWGsGLy7HEYSPD3kMd3w1WBVULchv6lebN33EkH5OkuWmVbSr0ESAqgeJAGs%2FH%2B5NjIT4u2gWAshBz8lVBlY0Zm9EGLtxmEK5lYovLM1AK0hDF6fWvcGzuvfkzT3039ZWRP3Rch9Oot3suD3QP4BGjmm1qPH1hSvR6OclVTv9zenHq2Js6fUOdA6zc%3D%7Ctkp%3ABk9SR6Cgtqe4Yw&LH_BIN=1&LH_ItemCondition=1000"
response = requests.get(ebay_ipad_url, headers=HEADERS)# requests library to fetch the HTML content from a page.
#BeautifulSoup is a Python library used for parsing HTML and XML documents
soup = BeautifulSoup(response.content, "lxml")# This parser is known for its speed and leniency.
# specifies the parser to be used by BeautifulSoup
#using "lxml" as the parser in your BeautifulSoup instance
# allows you to efficiently navigate and extract data from HTML content
e_ipad_title_tag = soup.find("span", class_="ux-textspans ux-textspans--BOLD")
#method is used to locate the first occurrence of a specific HTML element
# that matches certain criteria.
#searching for the first <span> element
# with the specified classes in the parsed HTML content
e_ipad_title_text = e_ipad_title_tag.getText()
e_ipad_title = e_ipad_title_text.strip()
e_ipad_price_tag = soup.find("div", class_="x-price-primary").text
e_ipad_price = e_ipad_price_tag.lstrip("C $")

#Amazon Apple Watch
amazon_apple_watch_url ="https://www.amazon.ca/Apple-Smartwatch-Midnight-Aluminium-Water-Resistant/dp/B0CHXCWBYT/ref=sr_1_5?crid=3EL36YWSSXP41&dib=eyJ2IjoiMSJ9.38xjdLNU--pTtn-VdutIVdsWT96vu2ca5TWjysZAmaxB-q8yYSzHrPpZ_uitYFs3hS4bv63mw1T-z1v-8to_XrBhh_Kq2rWqZyaq_otgrIivZo7WGRDRo8x_EH287CGRSxWlOPd18UcQbhE8nKoNuSs28Th6wAJCE3xACs3ESr0ShfqqikHAh1Hw_ehSg93HX2IfmU9yYxGtL1ipdphVGfe5qyGfIs9FItB4PRDOXu2QkVCRHwkLWVEi2DKTkQcTPfjy4OxgaNJYYSdplNwyGOzafh8UQnYl9DMCzQZLqUw.aDyVOy347C5olVMpIaU9XdQ2i8-Lvla2x74zrQH5YCo&dib_tag=se&keywords=apple+watch&qid=1708365591&sprefix=apple+watch%2Caps%2C160&sr=8-5"
response = requests.get(amazon_apple_watch_url, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
a_apple_watch_title_tag = soup.find("span", id="productTitle")
a_apple_watch_title_text=a_apple_watch_title_tag.getText()
a_apple_watch_title=a_apple_watch_title_text.strip()
a_apple_watch_whole_price_tag=soup.find("span",class_="a-price-whole")
a_apple_watch_whole_price_text=a_apple_watch_whole_price_tag.getText()
a_apple_watch_whole_price=a_apple_watch_whole_price_text.rstrip(".")
a_apple_watch_decimal_price_tag = soup.find("span", class_="a-price-fraction")
a_apple_watch_decimal_price_text=a_apple_watch_decimal_price_tag.getText()
a_apple_watch_decimal_price=a_apple_watch_decimal_price_text.strip()
a_apple_watch_price=a_apple_watch_whole_price_text+a_apple_watch_decimal_price

#Ebay Apple Watch
ebay_apple_watch_url ="https://www.ebay.ca/itm/256371656305?itmmeta=01HQ18DWH3HAK3NG688QR6V35T&hash=item3bb0f10671%3Ag%3ArbAAAOSwIitlgjUe&itmprp=enc%3AAQAIAAAA8HzNCLK8VNCg2uzFLGTlrjF2CRrISwWWHYN3tDVvlYyK4v4V3%2FE9pVbEEnH0IBqNrTDambjjmnJRhHH0W6bR8zS3tEEctveCavNb16uXamctWd66MuPXNO5jOfIsJmbidrdQZ6zEog%2BgD5V20mLjMIYC1xP7Tfi2pzdCmBx%2FRnjXXMWbTQyOukLAIIwqdClQketxE2NTyEGS7wGICYQEMsxjDNoUj9R%2BbDS2UTcju3dmFKOoKXFwkk874T35B0M6MU1nto7jJ1vasZ6WwyTE3sC%2B6bXrXwyn96QbB3f2x%2B%2BUdweWOI4mu5c11F6kVuUO6g%3D%3D%7Ctkp%3ABk9SR9LIt6i4Yw&LH_BIN=1&LH_ItemCondition=3"
response = requests.get(ebay_apple_watch_url, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
e_apple_watch_title_tag = soup.find("span", class_="ux-textspans ux-textspans--BOLD")
e_apple_watch_title_text=e_apple_watch_title_tag.getText()
e_apple_watch_title=e_apple_watch_title_text.strip()
e_apple_watch_price_tag=soup.find("div",class_="x-price-primary").text
e_apple_watch_price=e_apple_watch_price_tag.lstrip("C $")

#Walmart Ipad
w_ipad_url=requests.get("https://www.walmart.ca/en/search?q=ipad%209th%20generation&catId=10003",headers=HEADERS)
soup=BeautifulSoup(w_ipad_url.content,'lxml')
w_ipad_product_title_tag=soup.find('span',{'class':'normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy'})
w_ipad_product_title=w_ipad_product_title_tag.text
w_ipad_price_tag = soup.find('div', {'class':'mr1 mr2-xl b black lh-copy f5 f4-l'})
w_ipad_price_text=w_ipad_price_tag.getText().lstrip("$")
w_apple_watch_url=requests.get("https://www.walmart.ca/en/search?q=apple%20watch&catId=10003",headers=HEADERS)
soup=BeautifulSoup(w_apple_watch_url.content,'lxml')
w_apple_watch_product_title_tag=soup.find('span',{'class':'normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy'})
w_apple_watch_product_title=w_apple_watch_product_title_tag.text
w_apple_watch_price_tag = soup.find('div', {'class':'f7 f6-l black mb2 mb3-l'})
w_apple_watch_price_text=w_apple_watch_price_tag.getText().lstrip("From $")

#Amazon Fitbit
a_fitbit_url=requests.get("https://www.amazon.ca/Fitbit-Advanced-Fitness-Management-Tracking/dp/B0CC62ZG1M/ref=sr_1_2?crid=10WWHDI7XIYZL&dib=eyJ2IjoiMSJ9.ZdfS4vYg92vjBbWPbevR_ifk5iRoumpjaI51It_I5JKEenNYqFUoKz1G2_t25CfHMIxZI1dHrt6D4StaEYQnMVRxLPOdFKIqd9_ThA5crtaXDCOByWbMGQd66-Tb7mqpQoUFsMXbFBPCQ8MRPzlqYnEPzYDFMtd015cPD3YF0JmlOlsfKLGGHuPECfm-GV-xKd03jWObf5XR8DqfLoEwDIeFUfEKQAgVwnE3RWQlnkXwwcSr4dbG8CE2XW_OAWtWi1R98Y0sFcErsMbFs-BYthgOzz90-ZkPykXmTXZ-I58.P3xDJEM6uwAu7-Ac8ss48Z0rhikmsrjJ7jMvMq9SISw&dib_tag=se&keywords=fitbit%2Bcharge%2B6&qid=1708365836&sprefix=fitbit%2Bc%2Caps%2C141&sr=8-2&th=1",headers=HEADERS)
soup=BeautifulSoup(a_fitbit_url.content,'lxml')
a_fitbit_product_title_tag=soup.find('span',{'id':'productTitle'})
a_fitbit_product_title=a_fitbit_product_title_tag.text
a_fitbit_price_whole_tag = soup.find('span', {'class':'a-price-whole'})
a_fitbit_price_whole_text=a_fitbit_price_whole_tag.getText().strip()
a_fitbit_price_decimal_tag = soup.find('span', {'class':'a-price-fraction'})
a_fitbit_price_decimal_text=a_fitbit_price_decimal_tag.getText()
a_fitbit_price_text = a_fitbit_price_whole_text + a_fitbit_price_decimal_text

#Amazon Pixel
a_pixel_url=requests.get("https://www.amazon.ca/Google-G9BQD-Pixel-8-128GB-Rose/dp/B0CGTD5KVT/ref=sr_1_3?crid=1CO0EGLK520ZP&dib=eyJ2IjoiMSJ9.lk88THc-ZlPzuGlpogeeK-MNW5tFY_HWA-yDy5MaaemmX9XyNDUHWKWvJ2Q62JvB5kjcgRBY3H5dr9R2YxAuft2hG0wtM-PTjD-5-h-OEsB5xHXvJ5wmRi6WRuz8pbXNk5iN9xc2XHIfaxH2JBAb2PMFFNNW9xdmLrnKgqCpVTqBx1q01NLkpNzhZvup_0E6dbZBqxo2BxS9dBhwQ3jYOkZZvzoxXpha4YVEWTPpnwXy3SfENSaAmEhUTfkxFjtM-nYSFOHD0ruT5051qsEof41W9Z4E3e4BI2GeY0u5wcA.N67w7y2eVaOoHYliY1QnnTgcfmSRe8YS3VeZG47SmPw&dib_tag=se&keywords=pixel%2B8&qid=1708366190&sprefix=pixel%2B%2Caps%2C128&sr=8-3&th=1",headers=HEADERS)
soup=BeautifulSoup(a_pixel_url.content,'lxml')
a_pixel_product_title_tag=soup.find('span',{'id':'productTitle'})
a_pixel_product_title=a_pixel_product_title_tag.text
a_pixel_price_whole_tag = soup.find('span', {'class':'a-price-whole'})
a_pixel_price_whole_text=a_pixel_price_whole_tag.getText().strip()
a_pixel_price_decimal_tag = soup.find('span', {'class':'a-price-fraction'})
a_pixel_price_decimal_text=a_pixel_price_decimal_tag.getText()
a_pixel_price_text = a_pixel_price_whole_text + a_pixel_price_decimal_text

#Ebay Fitbit
ebay_fitbit_url=requests.get("https://www.ebay.ca/itm/186290508000?epid=3063405901&itmmeta=01HQ18MW8Y8AFF9YK6BGW5NVEC&hash=item2b5fc790e0%3Ag%3AzgMAAOSwAsRlw%7ExU&itmprp=enc%3AAQAIAAAA4FzcKyueJHFAUygiX4Ztlcd%2BYEFyy2hghgKnH0td4R510N1eeOGTcDpR%2BddmzcPnJWidd2jiy0AbfmRxvChCUktCYU2d4Mw1b167P7so2bhne0HqdPzt1oS359Felf6A%2F1qhEV1EuFmsYoFRcOKN5eAoM%2FHFsr7kLmzLn%2Fzc4kARtA86ULkSQJWR7veFj9moSbFPprVSEZP6huHRztd0GTCXOTrZHSe%2FCCxDFURA%2FURs01cp6dZxqhg8xghSjkWOzAIHyDmnhsc3iJl%2BV%2Bu9VeLN5DPFk0loYdk%2FFJC2ZyyF%7Ctkp%3ABFBMxsTTqLhj&LH_BIN=1&LH_ItemCondition=1000",headers=HEADERS)
soup=BeautifulSoup(ebay_fitbit_url.content,'lxml')
ebay_fitbit_product_title_tag=soup.find('span',{'class':'ux-textspans ux-textspans--BOLD'})
ebay_fitbit_product_title=ebay_fitbit_product_title_tag.text
ebay_fitbit_price_tag = soup.find('div', {'class':'x-price-primary'})
ebay_fitbit_price_text=ebay_fitbit_price_tag.getText().lstrip("C $")

#Ebay Pixel
ebay_pixel_url=requests.get("https://www.ebay.ca/itm/116001426079?epid=20063135105&itmmeta=01HQ18ZQASS1GVNS8T3EM48VT4&hash=item1b02394a9f%3Ag%3AK0UAAOSwlcRlb6Jz&itmprp=enc%3AAQAIAAAA4DW3jEnXOsUZ%2FQyt1MYwgi3fa6rgwMko7BGeohvjgkT8Aj%2F9yP4aDpOI%2Fb%2FQsWmiNzO4DVYk3xY0tmffvKoHh5x%2FnZxay0Nkoq5WRP7s1YX%2B7O3LFgSbakvdr8FvPUf4%2BdfviYKW7MyN84YfZDFBkv2C%2BujPOgtWsNAEb5Y4qB52qN%2FJ8pqzcAHep0vssxdtNWV%2BQBpBddtc%2FgDKEwPwTUxOd5zNkB6gceVf3BljmY2YYt6pGzAwrcCeJGVk77AGPpG7sJQyn9lQpl5BW3qdzMg0NR1JB51loGVJYvOi0Hy%2B%7Ctkp%3ABk9SR7z1_qi4Yw&LH_BIN=1&LH_ItemCondition=1000",headers=HEADERS)
soup=BeautifulSoup(ebay_pixel_url.content,'lxml')
ebay_pixel_product_title_tag=soup.find('span',{'class':'ux-textspans ux-textspans--BOLD'})
ebay_pixel_product_title=ebay_pixel_product_title_tag.text
ebay_pixel_price_tag = soup.find('div', {'class':'x-price-primary'})
ebay_pixel_price_text=ebay_pixel_price_tag.getText().lstrip("C $")

#Walmart Fitbit
w_fitbit_url=requests.get("https://www.walmart.ca/en/search?q=fitbit%20charge%206&catId=10003",headers=HEADERS)
soup=BeautifulSoup(w_fitbit_url.content,'lxml')
w_fitbit_product_title_tag=soup.find('span',{'class':'normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy'})
w_fitbit_product_title=w_fitbit_product_title_tag.text
w_fitbit_price_tag = soup.find('div', {'class':'mr1 mr2-xl b black lh-copy f5 f4-l'})
w_fitbit_price_text=w_fitbit_price_tag.getText().lstrip("$")

#Walmart Pixel
w_pixel_url=requests.get("https://www.walmart.ca/en/search?q=google%20pixel%208&catId=10003",headers=HEADERS)
soup=BeautifulSoup(w_pixel_url.content,'lxml')
w_pixel_product_title_tag=soup.find('span',{'class':'normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy'})
w_pixel_product_title=w_pixel_product_title_tag.text
w_pixel_price_tag = soup.find('div', {'class':'mr1 mr2-xl b black lh-copy f5 f4-l'})
w_pixel_price_text=w_pixel_price_tag.getText().lstrip("$")
#converting test price to float
amazon_ipad_price = float(a_ipad_price)
amazon_apple_watch_price = float(a_apple_watch_price)
amazon_fitbit_price = float(a_fitbit_price_text)
amazon_pixel_price = float(a_pixel_price_text)
ebay_ipad_price = float(e_ipad_price)
ebay_apple_watch_price = float(e_apple_watch_price)
ebay_fitbit_price=float(ebay_fitbit_price_text)
ebay_pixel_price=float(ebay_pixel_price_text)
w_ipad_price = float(w_ipad_price_text)
w_apple_watch_price=float(w_apple_watch_price_text)
w_fitbit_price=float(w_fitbit_price_text)
w_pixel_price=float(w_pixel_price_text)
#storing all the product details in to csv file
fields = ['Website_Name', 'Product_Name','Product_Title', 'Price','URL']
rows = [['Amazon', 'Apple ipad',a_ipad_title, amazon_ipad_price,amazon_ipad_url],
            ['Ebay','Apple ipad', e_ipad_title, ebay_ipad_price,ebay_ipad_url],
        ['Walmart','Apple ipad',w_ipad_product_title,w_ipad_price,w_ipad_url],
        ['Amazon','Apple Watch',a_apple_watch_title,amazon_apple_watch_price,amazon_apple_watch_url],
        ['Ebay','Apple Watch',e_apple_watch_title,ebay_apple_watch_price,ebay_apple_watch_url],
        ['Walmart','Apple Watch',w_apple_watch_product_title,w_apple_watch_price,w_apple_watch_url],
        ['Amazon','Fitbit Watch',a_fitbit_product_title,amazon_fitbit_price,a_fitbit_url],
        ['Ebay','Fitbit Watch',ebay_fitbit_product_title,ebay_fitbit_price,ebay_fitbit_url],
        ['Walmart','Fitbit Watch',w_fitbit_product_title,w_fitbit_price,w_fitbit_url],
        ['Amazon', 'Pixel Phone', a_pixel_product_title, amazon_pixel_price, a_pixel_url],
        ['Ebay', 'Pixel Phone', ebay_pixel_product_title, ebay_pixel_price, ebay_pixel_url],
        ['Walmart', 'Pixel Phone', w_pixel_product_title, w_pixel_price, w_pixel_url]
        ]
filename = "Price_Details.csv"
with open(filename, 'w') as csvfile:
        # creating a csv writer object
    csvwriter = csv.writer(csvfile)
        # writing the fields
    csvwriter.writerow(fields)
        # writing the data rows
    csvwriter.writerows(rows)
#Best Ipad function is called when we click the Ipad button
def best_ipad():
    min_price = min(amazon_ipad_price, ebay_ipad_price,w_ipad_price)
    if min_price==amazon_ipad_price:
        website_name.config(text=f"Apple Ipad:You got a good deal at Amazon :C$ {min_price: }")
        #content from the website_name widget
        #website_name.config(text=amazon_ipad_url)
    elif min_price==ebay_ipad_price:
        website_name.config(text=f"Apple Ipad:You got a good deal at Ebay :C$ {min_price: }")
    else:
        website_name.config(text=f"Apple Ipad:You got a good deal at Walmart :C$ {min_price: }")
    website = ["Amazon", "Ebay","Walmart"]
    #Barchart Creation
    price = [amazon_ipad_price, ebay_ipad_price,w_ipad_price]
    fig = Figure(figsize=(5, 2), dpi=100)
    ax = fig.add_subplot(111)
    ax.bar(website, price, color='b',alpha=0.7)
    ax.set_xlabel("Website")
    ax.set_ylabel("Price")
    ax.set_title("Price comparison")
    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)
# best_apple_watch function is called when we click the Apple Watch button
def best_apple_watch():
    min_price = min(amazon_apple_watch_price, ebay_apple_watch_price, w_apple_watch_price)
    if min_price == amazon_apple_watch_price:
        website_name.config(text=f"Apple Watch:You got a good deal at Amazon :C$ {min_price: }")
        # website_name.config(text=amazon_ipad_url)
    elif min_price == ebay_apple_watch_price:
        website_name.config(text=f"Apple Watch:You got a good deal at Ebay :C$ {min_price: }")
    elif min_price==w_apple_watch_price:
        website_name.config(text=f"Apple Watch:You got a good deal at Walmart :C$ {min_price: }")
    website = ["Amazon", "Ebay","Walmart"]
    price = [amazon_apple_watch_price, ebay_apple_watch_price,w_apple_watch_price]
    fig = Figure(figsize=(5, 2), dpi=100)
    ax = fig.add_subplot(111)
    ax.bar(website, price, color='b', alpha=0.7)
    ax.set_xlabel("Website")
    ax.set_ylabel("Price")
    ax.set_title("Price comparison")
    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)
# best_fitbit_watch function is called when we click the Fitbit Watch button
def best_fitbit_watch():
    min_price = min(amazon_fitbit_price,ebay_fitbit_price,w_fitbit_price)
    if min_price==amazon_fitbit_price:
        website_name.config(text=f"Fitbit Watch:You got a good deal at Amazon :C$ {min_price: }")
        #website_name.config(text=amazon_ipad_url)
    elif min_price==ebay_fitbit_price:
        website_name.config(text=f"Fitbit Watch:You got a good deal at Ebay :C$ {min_price: }")
    else:
        website_name.config(text=f"Fitbit Watch:You got a good deal at Walmart :C$ {min_price: }")
    website = ["Amazon", "Ebay","Walmart"]
    price = [amazon_fitbit_price, ebay_fitbit_price,w_fitbit_price]
    fig = Figure(figsize=(5, 2), dpi=100)
    ax = fig.add_subplot(111)
    ax.bar(website, price, color='b', alpha=0.7)
    ax.set_xlabel("Website")
    ax.set_ylabel("Price")
    ax.set_title("Price comparison")
    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)
#best_pixel_phone function is called when we click the Pixel Phone button
def best_pixel_phone():
    min_price = min(amazon_pixel_price,ebay_pixel_price,w_pixel_price)
    if min_price==amazon_pixel_price:
        website_name.config(text=f"Pixel-Phone:You got a good deal at Amazon :C$ {min_price: }")
        #website_name.config(text=amazon_ipad_url)
    elif min_price==ebay_pixel_price:
        website_name.config(text=f"Pixel-Phone:You got a good deal at Ebay :C$ {min_price: }")
    else:
        website_name.config(text=f"Pixel-Phone:You got a good deal at Walmart :C$ {min_price: }")
    website = ["Amazon", "Ebay","Walmart"]
    price = [amazon_pixel_price, ebay_pixel_price,w_pixel_price]
    fig = Figure(figsize=(5, 2), dpi=100)
    ax = fig.add_subplot(111)
    ax.bar(website, price, color='b', alpha=0.7)
    ax.set_xlabel("Website")
    ax.set_ylabel("Price")
    ax.set_title("Price comparison")
    canvas = FigureCanvasTkAgg(fig, master=result_frame)
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=2)

#Barchart for all product price Comparion
def show_barchart():
    Amazon = [amazon_ipad_price,amazon_apple_watch_price,amazon_fitbit_price,amazon_pixel_price]  # ipad price
    ebay = [ebay_ipad_price, ebay_apple_watch_price,ebay_fitbit_price,ebay_pixel_price]  # apple_watch price
    Walmart = [w_ipad_price, w_apple_watch_price,w_fitbit_price,w_pixel_price]
    # Product categories
    products = ["AIpad", "Apple watch","Fitbit watch","Pixel Phone"]
    # Create a bar chart
    fig, ax = plt.subplots()
    bar_width = 0.25
    index = range(len(products))
    ax.bar(index, Amazon, bar_width, label="Amazon")
    ax.bar([i + bar_width for i in index], ebay, bar_width, label="Ebay")
    ax.bar([i + 2 * bar_width for i in index], Walmart, bar_width, label="Walmart")
    ax.set_xlabel('Product')
    ax.set_ylabel('Price')
    ax.set_title('Price Comparison by Website')
    ax.set_xticks([i + bar_width for i in index])
    ax.set_xticklabels(products)
    ax.legend()
    plt.show()
#Email Configuration
def send_email():
    # Get the user's email from the input field
    user_email = email_text.get()# retrieving the user’s email from an input field.

    # Set up your email credentials
    sender_email = 'Mailid@outlook.com' #(sender’s email address and password).
    sender_password = 'Password'

    # Compose the email message
    subject = 'Hello You Got a Good Deal!'
    #body = 'This is the email content. You can customize it.'
    body=(website_name.cget("text"))# content from the website_name widget
          #,'Here is the link : ',amazon_ipad_url)
    message = f'Subject: {subject}\n\n{body}'

    try:
        # Connect to the SMTP server
        #connecting to an SMTP (Simple Mail Transfer Protocol)
        # server hosted by Outlook (smtp-mail.outlook.com) on port 587.
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        # using TLS (Transport Layer Security) encryption for secure communication.
        server.starttls()
        #logging in with your sender email and password.
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, user_email, message)
        server.quit()

        # Show a success message
        messagebox.showinfo('Success', 'Email sent successfully!')
    except Exception as e:
        # Show an error message
        messagebox.showerror('Error', f'Error sending email: {str(e)}')
#Gui
window = tk.Tk()
window.title("Price Comparison Tool")
#window.geometry('400x400')
window.configure(bg='Blanched Almond')

frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

user_input_frame=tk.LabelFrame(frame,text='Select your product and get the best deal',fg="blue")
user_input_frame.grid(row=0,column=0,sticky='news')
user_input_frame.configure(bg='Honeydew')

apple_ipad = tk.Label(user_input_frame, text="Products",fg='blue')
apple_ipad.grid(row=0, column=1,padx=10,pady=10)

apple_ipad = tk.Button(user_input_frame, text="Apple iPad",command=best_ipad)
apple_ipad.grid(row=1, column=1,padx=10,pady=10)

apple_watch = tk.Button(user_input_frame, text="Apple Watch",command=best_apple_watch)
apple_watch.grid(row=2, column=1,padx=10,pady=10)

fitbit_watch = tk.Button(user_input_frame, text="Fitbit Watch",command=best_fitbit_watch)
                         #,command=best_fitbit_watch)
fitbit_watch.grid(row=3, column=1,padx=10,pady=10)

pixel_phone = tk.Button(user_input_frame, text="Pixel Phone",command=best_pixel_phone)
                        #,command=best_pixel_phone)
pixel_phone.grid(row=4, column=1,padx=10,pady=10)

e_website_frame=tk.Label(user_input_frame,text='Ecommerce Websites ',fg="blue")
e_website_frame.grid(row=0,column=14,sticky='news')

amazon_label = tk.Label(user_input_frame, text="Amazon")
amazon_label.grid(row=1, column=14)

ebay_label = tk.Label(user_input_frame, text="EBAY")
ebay_label.grid(row=2, column=14)

bestbuy_label = tk.Label(user_input_frame, text="Walmart")
bestbuy_label.grid(row=3, column=14)

email_frame=tk.LabelFrame(frame,text='Email',fg="blue")
email_frame.grid(row=0,column=1,sticky='news')
email_frame.configure(bg='Honeydew')

email_text_label = tk.Label(email_frame, text='Email Notification',fg='blue')
email_text_label.grid(row=0, column=0,padx=10,pady=10)

email_text_label = tk.Label(email_frame, text="Please enter your email:")
email_text_label.grid(row=1, column=0,padx=10,pady=10)

email_text=tk.Entry(email_frame)
email_text.grid(row=1, column=1,padx=10,pady=10)

email_button = tk.Button(email_frame, text="Press me",command=send_email)
email_button.grid(row=2, column=0,padx=10,pady=10)

email_label = tk.Label(email_frame, text="You will get an email notification",fg='blue')
email_label.grid(row=2, column=1,padx=10,pady=10)

result_frame=tk.LabelFrame(frame,text='Best Price',fg="blue")
result_frame.grid(row=1,column=0,sticky='news')
result_frame.configure(bg='Honeydew')

website_name = tk.Label(result_frame, text="",fg='Green')
website_name.grid(row=0, column=2)


price_visualization_frame=tk.LabelFrame(frame,text='Price Visualization of All Products',fg="blue")
price_visualization_frame.grid(row=1,column=1,sticky='news')
price_visualization_frame.configure(bg='Honeydew')

bar_chart = tk.Button(price_visualization_frame, text="Barchart",command=show_barchart)
bar_chart.grid(row=4, column=0,padx=10,pady=10)

window.mainloop()
