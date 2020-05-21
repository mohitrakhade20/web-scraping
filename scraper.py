import pip._vendor.requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.amazon.in/Sony-IhttpsLCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp/B07DPSQRFF/ref=sr_1_2?dchild=1&keywords=sony+a7&qid=1590058835&sr=8-2'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}


def check_price():
    page = pip._vendor.requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    price1 = price[2:3]
    price2 = price[4:6]
    price3 = price[7:10]
    converted_price = float(price1+price2+price3)

    if(converted_price < 150000):
        send_mail()

    print(converted_price)

    print(title.strip())

    if(converted_price > 150000):
        send_mail()


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('mohitrakhade20@gmail.com', 'rschxqguvfhixyth')

    subject = 'Price fell down my dear friend!'
    body = 'Check the amazon link https://www.amazon.in/Sony-IhttpsLCE-7M3K-Full-Frame-Mirrorless-Interchangeable/dp/B07DPSQRFF/ref=sr_1_2?dchild=1&keywords=sony+a7&qid=1590058835&sr=8-2'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'mohitrakhade20@gmail.com', 'mohitrakhade20@gmail.com',
        msg
    )

    print('HEY, email has been sent! cool ')

    server.quit()


while(1):
    check_price()
    time.sleep(60)
