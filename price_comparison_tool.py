import smtplib
import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import messagebox
import smtplib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
HEADERS = {
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US, en;q=0.5"
    }
amazon_ipad_url = "https://www.amazon.ca/2021-Apple-iPad-10-2-inch-Wi-Fi/dp/B09G9BJVT6/ref=sr_1_1_sspa?crid=JH8GH92SZ3F3&dib=eyJ2IjoiMSJ9.rpni6IL_14CkVVRbzrBrSQP2iA-E7i-iCf8yoLOfdYtIgwhK2SR-CeHA6HjsY-FdNaYqLvEGHnkWhb0X8zaUqpJgFpiASOc6u8NK19WLlj4Uk3DlPgDfiRjYUe1ToRcdvwV-Uh9AqxRBa5celn5FVVCqQkHY4Rp9KTLlguCEzJqwoesIu_Ivn4sAz3fwF4ZwNUPRFfkcZzygWt3bzKTR1u0TqcYL37WsqLWvKMYsUnaj-Hb-7F3fnUcBGciCYC3ogWPePaQg7UAnVzIJmGjHFQWxLKSa1Q0xNw62XZab2QE.COam3A7jfV-pQcDlMC599-IshvNMd-9MjG_VhBpr984&dib_tag=se&keywords=ipad+10th+generation&qid=1708364536&sprefix=ipad+10th+generation%2Caps%2C193&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
response = requests.get(amazon_ipad_url, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
a_title_tag = soup.find("span", id="productTitle")
a_title_text = a_title_tag.getText()
a_title = a_title_text.strip()
price_tag = soup.find("span", class_="a-price-whole")
price_text = price_tag.getText()
price = price_text.rstrip(".")
decimal_price_tag = soup.find("span", class_="a-price-fraction")
decimal_price_text = decimal_price_tag.getText()
decimal_price = decimal_price_text.strip()
a_price = price + "." + decimal_price
ebay_ipad_url = "https://www.ebay.ca/itm/175524001378?epid=28049286448&itmmeta=01HQ17DJ09TM9DX11P8KKSQWQW&hash=item28de0bb662%3Ag%3Ag3kAAOSwNcxh6LAr&itmprp=enc%3AAQAIAAAA0AxcRfbUhIIib0nsP8DIRvg3llt5e6hZOun43gdLoS%2B%2FsSYGZsxpGEPJRoLgTlLevCwES3GZSRnp8DQ1tcwdNjvBDnyeEfWGsGLy7HEYSPD3kMd3w1WBVULchv6lebN33EkH5OkuWmVbSr0ESAqgeJAGs%2FH%2B5NjIT4u2gWAshBz8lVBlY0Zm9EGLtxmEK5lYovLM1AK0hDF6fWvcGzuvfkzT3039ZWRP3Rch9Oot3suD3QP4BGjmm1qPH1hSvR6OclVTv9zenHq2Js6fUOdA6zc%3D%7Ctkp%3ABk9SR6Cgtqe4Yw&LH_BIN=1&LH_ItemCondition=1000"
response = requests.get(ebay_ipad_url, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
e_title_tag = soup.find("span", class_="ux-textspans ux-textspans--BOLD")
e_title_text = e_title_tag.getText()
e_title = e_title_text.strip()
e_price_tag = soup.find("div", class_="x-price-primary").text
e_price = e_price_tag.lstrip("C $")
amazon_apple_watch_url ="https://www.amazon.ca/Apple-Smartwatch-Midnight-Aluminium-Water-Resistant/dp/B0CHXCWBYT/ref=sr_1_5?crid=3EL36YWSSXP41&dib=eyJ2IjoiMSJ9.38xjdLNU--pTtn-VdutIVdsWT96vu2ca5TWjysZAmaxB-q8yYSzHrPpZ_uitYFs3hS4bv63mw1T-z1v-8to_XrBhh_Kq2rWqZyaq_otgrIivZo7WGRDRo8x_EH287CGRSxWlOPd18UcQbhE8nKoNuSs28Th6wAJCE3xACs3ESr0ShfqqikHAh1Hw_ehSg93HX2IfmU9yYxGtL1ipdphVGfe5qyGfIs9FItB4PRDOXu2QkVCRHwkLWVEi2DKTkQcTPfjy4OxgaNJYYSdplNwyGOzafh8UQnYl9DMCzQZLqUw.aDyVOy347C5olVMpIaU9XdQ2i8-Lvla2x74zrQH5YCo&dib_tag=se&keywords=apple+watch&qid=1708365591&sprefix=apple+watch%2Caps%2C160&sr=8-5"
response = requests.get(amazon_apple_watch_url, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
awatch_title_tag = soup.find("span", id="productTitle")
awatch_title_text=awatch_title_tag.getText()
awatch_title=awatch_title_text.strip()
awatch_price_tag=soup.find("span",class_="a-price-whole")
awatch_price_text=awatch_price_tag.getText()
awatch_price=awatch_price_text.rstrip(".")
awatch_decimal_price_tag = soup.find("span", class_="a-price-fraction")
awatch_decimal_price_text=awatch_decimal_price_tag.getText()
awatch_decimal_price=awatch_decimal_price_text.strip()
awatch_totalprice=awatch_price+"."+awatch_decimal_price
ebay_apple_watch_url ="https://www.ebay.ca/itm/256371656305?itmmeta=01HQ18DWH3HAK3NG688QR6V35T&hash=item3bb0f10671%3Ag%3ArbAAAOSwIitlgjUe&itmprp=enc%3AAQAIAAAA8HzNCLK8VNCg2uzFLGTlrjF2CRrISwWWHYN3tDVvlYyK4v4V3%2FE9pVbEEnH0IBqNrTDambjjmnJRhHH0W6bR8zS3tEEctveCavNb16uXamctWd66MuPXNO5jOfIsJmbidrdQZ6zEog%2BgD5V20mLjMIYC1xP7Tfi2pzdCmBx%2FRnjXXMWbTQyOukLAIIwqdClQketxE2NTyEGS7wGICYQEMsxjDNoUj9R%2BbDS2UTcju3dmFKOoKXFwkk874T35B0M6MU1nto7jJ1vasZ6WwyTE3sC%2B6bXrXwyn96QbB3f2x%2B%2BUdweWOI4mu5c11F6kVuUO6g%3D%3D%7Ctkp%3ABk9SR9LIt6i4Yw&LH_BIN=1&LH_ItemCondition=3"
response = requests.get(ebay_apple_watch_url, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
eawatch_title_tag = soup.find("span", class_="ux-textspans ux-textspans--BOLD")
eawatch_title_text=eawatch_title_tag.getText()
eawatch_title=eawatch_title_text.strip()
eawatch_price_tag=soup.find("div",class_="x-price-primary").text
eawatch_price=eawatch_price_tag.lstrip("C $")
w_ipad_url=requests.get("https://www.walmart.ca/en/search?q=ipad%209th%20generation&catId=10003",headers=HEADERS)
soup=BeautifulSoup(w_ipad_url.content,'lxml')
w_ipad_product_title_tag=soup.find('span',{'class':'normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy'})
w_ipad_product_title=w_ipad_product_title_tag.text
w_ipad_price_tag = soup.find('div', {'class':'mr1 mr2-xl b black lh-copy f5 f4-l'})
w_ipad_price_text=w_ipad_price_tag.getText().lstrip("$")
w_applewatch_url=requests.get("https://www.walmart.ca/en/search?q=apple%20watch&catId=10003",headers=HEADERS)
soup=BeautifulSoup(w_applewatch_url.content,'lxml')
w_apple_watch_product_title_tag=soup.find('span',{'class':'normal dark-gray mb0 mt1 lh-title f6 f5-l lh-copy'})
w_apple_watch_product_title=w_apple_watch_product_title_tag.text
w_apple_watch_price_tag = soup.find('div', {'class':'f7 f6-l black mb2 mb3-l'})
w_apple_watch_price_text=w_apple_watch_price_tag.getText().lstrip("From $")
amazon_ipad_price = float(a_price)
ebay_ipad_price = float(e_price)
w_ipad_price=float(w_ipad_price_text)
amazon_apple_watch_price = float(awatch_totalprice)
ebay_apple_watch_price = float(eawatch_price)
w_apple_watch_price=float(w_apple_watch_price_text)
fields = ['Website_Name', 'Product_Name','Product_Title', 'Price','URL']
rows = [['Amazon', 'Apple ipad',a_title, a_price,amazon_ipad_url],
            ['ebay','Apple ipad', e_title, e_price,ebay_ipad_url],
        ['Walmart','Apple ipad',w_ipad_product_title,w_ipad_price_text,w_ipad_url],
        ['Amazon','Apple Watch',awatch_title,awatch_totalprice,amazon_apple_watch_url],
        ['ebay','Apple Watch',eawatch_title,eawatch_price,ebay_apple_watch_url],
        ['Walmart','Apple Watch',w_apple_watch_product_title,w_apple_watch_price_text,w_applewatch_url]]
filename = "Price_Details.csv"
with open(filename, 'w') as csvfile:
        # creating a csv writer object
    csvwriter = csv.writer(csvfile)
        # writing the fields
    csvwriter.writerow(fields)
        # writing the data rows
    csvwriter.writerows(rows)
def best_ipad():
    min_price = min(amazon_ipad_price, ebay_ipad_price,w_ipad_price)
    if min_price==amazon_ipad_price:
        website_name.config(text=f"You got a good deal at Amazon :C$ {min_price: }")
        #website_name.config(text=amazon_ipad_url)
    elif min_price==ebay_ipad_price:
        website_name.config(text=f"You got a good deal at Ebay :C$ {min_price: }")
    else:
        website_name.config(text=f"You got a good deal at Walmart :C$ {min_price: }")
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
def best_apple_watch():
    min_price = min(amazon_apple_watch_price,ebay_apple_watch_price,w_apple_watch_price)
    if min_price==amazon_apple_watch_price:
        website_name.config(text=f"You got a good deal at Amazon :C$ {min_price: }")
        #website_name.config(text=amazon_ipad_url)
    elif min_price==ebay_apple_watch_price:
        website_name.config(text=f"You got a good deal at Ebay :C$ {min_price: }")
    else:
        website_name.config(text=f"You got a good deal at Ebay :C$ {min_price: }")
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
def show_bmi_barchart():
    Amazon = [amazon_ipad_price,amazon_apple_watch_price]  # ipad price
    ebay = [ebay_ipad_price, ebay_apple_watch_price]  # apple_watch price
    Walmart = [w_ipad_price, w_apple_watch_price]
    # Product categories
    products = ["Ipad", "Applewatch"]

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
def send_email():
    # Get the user's email from the input field
    user_email = email_text.get()

    # Set up your email credentials
    sender_email = 'lakshmi.cheenu1@outlook.com'
    sender_password = 'ZXcv12#$'

    # Compose the email message
    subject = 'Hello You Got a Good Deal!'
    #body = 'This is the email content. You can customize it.'
    body=(website_name.cget("text"))
          #,'Here is the link : ',amazon_ipad_url)
    message = f'Subject: {subject}\n\n{body}'

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP('smtp-mail.outlook.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, user_email, message)
        server.quit()

        # Show a success message
        messagebox.showinfo('Success', 'Email sent successfully!')
    except Exception as e:
        # Show an error message
        messagebox.showerror('Error', f'Error sending email: {str(e)}')


window = tk.Tk()
window.title("Price Comparison Tool")
#window.geometry('400x400')

frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

user_input_frame=tk.LabelFrame(frame,text='Select your product and get the best deal',fg="blue")
user_input_frame.grid(row=0,column=0,sticky='news')

apple_ipad = tk.Button(user_input_frame, text="Apple iPad",command=best_ipad)
apple_ipad.grid(row=0, column=3,padx=10,pady=10)

apple_watch = tk.Button(user_input_frame, text="Apple Watch",command=best_apple_watch)
apple_watch.grid(row=1, column=3,padx=10,pady=10)

fitbit_watch = tk.Button(user_input_frame, text="Fitbit Watch")
                         #,command=best_fitbit_watch)
fitbit_watch.grid(row=2, column=3,padx=10,pady=10)

pixel_phone = tk.Button(user_input_frame, text="Pixel Phone")
                        #,command=best_pixel_phone)
pixel_phone.grid(row=3, column=3,padx=10,pady=10)

e_website_frame=tk.LabelFrame(frame,text='Ecommerce Websites ',fg="blue")
e_website_frame.grid(row=0,column=1,sticky='news')

amazon_label = tk.Label(e_website_frame, text="Amazon")
amazon_label.grid(row=0, columnspan=1)

ebay_label = tk.Label(e_website_frame, text="EBAY")
ebay_label.grid(row=1, columnspan=1)

bestbuy_label = tk.Label(e_website_frame, text="Walmart")
bestbuy_label.grid(row=2, columnspan=1)

email_frame=tk.LabelFrame(frame,text='Send me an email',fg="blue")
email_frame.grid(row=1,column=0,sticky='news')

email_text_label = tk.Label(email_frame, text="Please enter your email:")
email_text_label.grid(row=0, column=0,padx=10,pady=10)

email_text=tk.Entry(email_frame)
email_text.grid(row=0, column=1,padx=10,pady=10)

email_button = tk.Button(email_frame, text="Press me",command=send_email)
email_button.grid(row=1, column=0,padx=10,pady=10)

email_label = tk.Label(email_frame, text="You will get an email notification")
email_label.grid(row=1, column=1,padx=10,pady=10)

price_visualization_frame=tk.LabelFrame(frame,text='Price Visualization',fg="blue")
price_visualization_frame.grid(row=1,column=1,sticky='news')

bar_chart = tk.Button(price_visualization_frame, text="Barchart",command=show_bmi_barchart)
bar_chart.grid(row=0, column=0,padx=10,pady=10)

result_frame=tk.LabelFrame(frame,text='Best Price',fg="blue")
result_frame.grid(row=2,column=0,sticky='news')

website_name = tk.Label(result_frame, text="")
website_name.grid(row=0, columnspan=2)

window.mainloop()
