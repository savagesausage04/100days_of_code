import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage
import ssl
import smtplib

URL = "https://www.amazon.com/Herschel-Supply-Co-Classic-Backpack/dp/B078J1193K/ref=sr_1_4?crid=F7IKF2NGJFHB&keywords=herschel+backpack&qid=1657182989&sprefix=hers%2Caps%2C211&sr=8-4"

headers={"Accept-Language": "en-US,en;q=0.9",
         "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36",
         }

response = requests.get(URL, headers=headers)
data = response.text



soup = BeautifulSoup(data, "html.parser")
price = float(soup.find(name="span", class_="a-offscreen").getText().split("$")[1])
print(price)

product_name = soup.find(name="span", id="productTitle").getText().strip()
print(product_name)

email_sender = "kylieh1104@gmail.com"
email_receiver = "kyleh1104@gmail.com"
subject = f"{product_name} Price Drop!"
body = f"The product price is now ${price}, below your target price. Buy now!"
email_password = "jkismqutbbdencoi"

buy_price = 35

if price < buy_price:
    em = EmailMessage()
    em["From"] = email_sender
    em["To"] = email_receiver
    em["Subject"] = subject
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())


























