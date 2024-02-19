# Price-Comparison-Tool
import requests
from bs4 import BeautifulSoup
USER_AGENT ="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0"
HEADERS = {
    "User-Agent": USER_AGENT,
    "Accept-Language": "en-US, en;q=0.5"
}
url ="https://www.amazon.ca/2021-Apple-iPad-10-2-inch-Wi-Fi/dp/B09G9BJVT6/ref=sr_1_1_sspa?crid=JH8GH92SZ3F3&dib=eyJ2IjoiMSJ9.rpni6IL_14CkVVRbzrBrSQP2iA-E7i-iCf8yoLOfdYtIgwhK2SR-CeHA6HjsY-FdNaYqLvEGHnkWhb0X8zaUqpJgFpiASOc6u8NK19WLlj4Uk3DlPgDfiRjYUe1ToRcdvwV-Uh9AqxRBa5celn5FVVCqQkHY4Rp9KTLlguCEzJqwoesIu_Ivn4sAz3fwF4ZwNUPRFfkcZzygWt3bzKTR1u0TqcYL37WsqLWvKMYsUnaj-Hb-7F3fnUcBGciCYC3ogWPePaQg7UAnVzIJmGjHFQWxLKSa1Q0xNw62XZab2QE.COam3A7jfV-pQcDlMC599-IshvNMd-9MjG_VhBpr984&dib_tag=se&keywords=ipad+10th+generation&qid=1708364536&sprefix=ipad+10th+generation%2Caps%2C193&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"
response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
title_tag = soup.find("span", id="productTitle")
title_text=title_tag.getText()
title=title_text.strip()
print(title)
price_tag=soup.find("span",class_="a-price-whole")
price_text=price_tag.getText()
price=price_text.rstrip(".")
print(price)
decimalprice_tag = soup.find("span", class_="a-price-fraction")
decimalprice_text=decimalprice_tag.getText()
decimalprice=decimalprice_text.strip()
print(decimalprice)
url ="https://www.ebay.ca/itm/175524001378?epid=28049286448&itmmeta=01HQ17DJ09TM9DX11P8KKSQWQW&hash=item28de0bb662%3Ag%3Ag3kAAOSwNcxh6LAr&itmprp=enc%3AAQAIAAAA0AxcRfbUhIIib0nsP8DIRvg3llt5e6hZOun43gdLoS%2B%2FsSYGZsxpGEPJRoLgTlLevCwES3GZSRnp8DQ1tcwdNjvBDnyeEfWGsGLy7HEYSPD3kMd3w1WBVULchv6lebN33EkH5OkuWmVbSr0ESAqgeJAGs%2FH%2B5NjIT4u2gWAshBz8lVBlY0Zm9EGLtxmEK5lYovLM1AK0hDF6fWvcGzuvfkzT3039ZWRP3Rch9Oot3suD3QP4BGjmm1qPH1hSvR6OclVTv9zenHq2Js6fUOdA6zc%3D%7Ctkp%3ABk9SR6Cgtqe4Yw&LH_BIN=1&LH_ItemCondition=1000"
response = requests.get(url, headers=HEADERS)
soup = BeautifulSoup(response.content, "lxml")
etitle_tag = soup.find("span", class_="ux-textspans ux-textspans--BOLD")
etitle_text=etitle_tag.getText()
etitle=etitle_text.strip()
print(etitle)
eprice_tag=soup.find("div",class_="x-price-primary").text
#eprice_text=eprice_tag.getText()
eprice=eprice_tag.lstrip("C $")
print(eprice)

