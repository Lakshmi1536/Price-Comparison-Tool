import requests
from bs4 import BeautifulSoup
import csv
import tkinter as tk
from tkinter import messagebox
import plotly.express as px


def best_ipad():
    USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
    HEADERS = {
        "User-Agent": USER_AGENT,
        "Accept-Language": "en-US, en;q=0.5"
    }
    amazon_url = "https://www.amazon.ca/2021-Apple-iPad-10-2-inch-Wi-Fi/dp/B09G9BJVT6/ref=sr_1_1_sspa?crid=JH8GH92SZ3F3&dib=eyJ2IjoiMSJ9.rpni6IL_14CkVVRbzrBrSQP2iA-E7i-iCf8yoLOfdYtIgwhK2SR-CeHA6HjsY-FdNaYqLvEGHnkWhb0X8zaUqpJgFpiASOc6u8NK19WLlj4Uk3DlPgDfiRjYUe1ToRcdvwV-Uh9AqxRBa5celn5FVVCqQkHY4Rp9KTLlguCEzJqwoesIu_Ivn4sAz3fwF4ZwNUPRFfkcZzygWt3bzKTR1u0TqcYL37WsqLWvKMYsUnaj-Hb-7F3fnUcBGciCYC3ogWPePaQg7UAnVzIJmGjHFQWxLKSa1Q0xNw62XZab2QE.COam3A7jfV-pQcDlMC599-IshvNMd-9MjG_VhBpr984&dib_tag=se&keywords=ipad+10th+generation&qid=1708364536&sprefix=ipad+10th+generation%2Caps%2C193&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
    response = requests.get(amazon_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "lxml")
    a_title_tag = soup.find("span", id="productTitle")
    a_title_text = a_title_tag.getText()
    a_title = a_title_text.strip()
    #print(a_title)
    price_tag = soup.find("span", class_="a-price-whole")
    price_text = price_tag.getText()
    price = price_text.rstrip(".")
    decimal_price_tag = soup.find("span", class_="a-price-fraction")
    decimal_price_text = decimal_price_tag.getText()
    decimal_price = decimal_price_text.strip()
    a_price = price + "." + decimal_price
    #print(a_price)
    ebay_url = "https://www.ebay.ca/itm/175524001378?epid=28049286448&itmmeta=01HQ17DJ09TM9DX11P8KKSQWQW&hash=item28de0bb662%3Ag%3Ag3kAAOSwNcxh6LAr&itmprp=enc%3AAQAIAAAA0AxcRfbUhIIib0nsP8DIRvg3llt5e6hZOun43gdLoS%2B%2FsSYGZsxpGEPJRoLgTlLevCwES3GZSRnp8DQ1tcwdNjvBDnyeEfWGsGLy7HEYSPD3kMd3w1WBVULchv6lebN33EkH5OkuWmVbSr0ESAqgeJAGs%2FH%2B5NjIT4u2gWAshBz8lVBlY0Zm9EGLtxmEK5lYovLM1AK0hDF6fWvcGzuvfkzT3039ZWRP3Rch9Oot3suD3QP4BGjmm1qPH1hSvR6OclVTv9zenHq2Js6fUOdA6zc%3D%7Ctkp%3ABk9SR6Cgtqe4Yw&LH_BIN=1&LH_ItemCondition=1000"
    response = requests.get(ebay_url, headers=HEADERS)
    soup = BeautifulSoup(response.content, "lxml")
    e_title_tag = soup.find("span", class_="ux-textspans ux-textspans--BOLD")
    e_title_text = e_title_tag.getText()
    e_title = e_title_text.strip()
    #print(e_title)
    e_price_tag = soup.find("div", class_="x-price-primary").text
    e_price = e_price_tag.lstrip("C $")
    #print(e_price)
    fields = ['Website_Name', 'Product_Name', 'Price']
    rows = [['Amazon', a_title, a_price],
            ['ebay', e_title, e_price]]
    filename = "Price_Details.csv"
    with open(filename, 'w') as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)

        # writing the fields
        csvwriter.writerow(fields)

        # writing the data rows
        csvwriter.writerows(rows)

    amazon_ipad_price = float(a_price)
    ebay_ipad_price = float(e_price)
    min_price = min(amazon_ipad_price, ebay_ipad_price)
    if min_price==amazon_ipad_price:
        website_name.config(text=f"You got a good deal at Amazon :C$ {min_price: }")
    else:
        website_name.config(text=f"You got a good deal at Ebay :C$ {min_price: }")
    def show_bmi_barchart():
        data = [
            {"Website": "Amazon", "Price": a_price},
            {"Website": "Ebay", "Price": e_price}]

        fig = px.bar(data, x="Website", y="Price", title="Price Comparison")
        fig.show()

window = tk.Tk()
window.title("Price Comparison Tool")
#window.geometry('400x400')

frame = tk.Frame(window)
frame.pack(padx=20, pady=20)

user_input_frame=tk.LabelFrame(frame,text='Select your product and get the best deal',fg="blue")
user_input_frame.grid(row=0,column=0,sticky='news')

apple_ipad = tk.Button(user_input_frame, text="Apple iPad",command=best_ipad)
apple_ipad.grid(row=0, column=3,padx=10,pady=10)

samsungwatch = tk.Button(user_input_frame, text="Samsung Watch")
samsungwatch.grid(row=1, column=3,padx=10,pady=10)

iphone = tk.Button(user_input_frame, text="Iphone")
iphone.grid(row=2, column=3,padx=10,pady=10)

iwatch = tk.Button(user_input_frame, text="Iwatch")
iwatch.grid(row=3, column=3,padx=10,pady=10)

fitbitwatch = tk.Button(user_input_frame, text="Fitbit Watch")
fitbitwatch.grid(row=4, column=3,padx=10,pady=10)

e_website_frame=tk.LabelFrame(frame,text='Ecommerce websites ')
e_website_frame.grid(row=0,column=1,sticky='news')

amazon_label = tk.Label(e_website_frame, text="THE SOURCE")
amazon_label.grid(row=0, columnspan=1)

ebay_label = tk.Label(e_website_frame, text="STAPLES")
ebay_label.grid(row=1, columnspan=1)

bestbuy_label = tk.Label(e_website_frame, text="BEST BUY")
bestbuy_label.grid(row=2, columnspan=1)

walmart_label = tk.Label(e_website_frame, text="WALMART")
walmart_label.grid(row=3, columnspan=1)

email_frame=tk.LabelFrame(frame,text='send me an email')
email_frame.grid(row=1,column=0,sticky='news')

email_text_label = tk.Label(email_frame, text="Please enter your email:")
email_text_label.grid(row=0, column=0,padx=10,pady=10)

email_text=tk.Entry(email_frame)
email_text.grid(row=0, column=1,padx=10,pady=10)

email_button = tk.Button(email_frame, text="Press me")
email_button.grid(row=1, column=0,padx=10,pady=10)

email_label = tk.Label(email_frame, text="You will get an email notification")
email_label.grid(row=1, column=1,padx=10,pady=10)

price_visualization_frame=tk.LabelFrame(frame,text='Price visualization')
price_visualization_frame.grid(row=1,column=1,sticky='news')

bar_chart = tk.Button(price_visualization_frame, text="Barchart",command=show_bmi_barchart)
bar_chart.grid(row=0, column=0,padx=10,pady=10)

result_frame=tk.LabelFrame(frame,text='Best Price')
result_frame.grid(row=2,column=0,sticky='news')

website_name = tk.Label(result_frame, text="")
website_name.grid(row=0, columnspan=2)

window.mainloop()
