from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import os

usuario = "PostsOfCats"
url = f"https://twitter.com/{usuario}"

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.get(url)

time.sleep(5)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")

posts = soup.find_all("article")

dados = []

contador = 0

for post in posts:

    if contador == 3:
        break

    autor = post.find("div", {"data-testid":"User-Name"})
    autor = autor.text if autor else "N/A"

    texto = post.find("div", {"data-testid":"tweetText"})
    texto = texto.text if texto else "N/A"

    data = post.find("time")
    data = data["datetime"] if data else "N/A"

    dados.append({
        "autor": autor,
        "texto": texto,
        "data": data
    })

    contador += 1

df = pd.DataFrame(dados)

os.makedirs("data", exist_ok=True)
df.to_csv("data/tweets.csv", index=False)

print(df)