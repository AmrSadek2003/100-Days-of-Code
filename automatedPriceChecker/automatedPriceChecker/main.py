from bs4 import BeautifulSoup
import requests
import os
import smtplib, ssl

# email alert when price falls below certain value

amazon_url = ('https://www.amazon.com/Beats-Wireless-Noise-Cancelling-Headphones/dp/B09NYKT6XF/ref=sr_1_2?crid'
              '=1X4RT1DXZBUT5&dib=eyJ2IjoiMSJ9.Q3r2gzq'
              '-5XMWuRjF2x2W86GmK5CoNtrEPYV7DCF6GoStbR2gDxrtSoJy_0MycKckPxrHdxl0_vD'
              '-SY9fEB7v7yPdiHgV8pEDUdfeh_iNeBX4nTOSxjmJrpafsKvO94Wt0jUFc2RMozMCknxmOMojHyHa9U59coMdjIr56z9SM6UJYJLUFDKgzmV3u-V5gy8P3B50ewruCDd-Pw98graMmYC4vYqqr3VvwQB_dMynAW4.4fSst4bhbz40UVrJLPrFXuoYTO6LeD'
              'mIfYpr0SFyKHI&dib_tag=se&keywords=beats%2Bfit%2Bpro&qid=1751516467&sprefix=beats%2Bfit%2Bpr%2Caps%2C186&sr=8-2&th=1')

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
}

response = requests.get(url=amazon_url, headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

price = soup.find('span', class_="a-offscreen")

string_price = price.getText()
no_dollar = float(string_price.replace("$", ""))

my_email = "amrsadek2003@gmail.com"
# password = os.getenv("GMAIL_PASS")
password = os.getenv("GMAIL_PASS")

if no_dollar < 150.00:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    random_motivation = (f"Subject: BEATS ON SALE NOW!\n\n"
                         f"Beat Fit Pros are at a great price right now! They're selling for ${no_dollar}")
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=my_email, msg= random_motivation)
