from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd

options = webdriver.ChromeOptions()

# evita detecção de automação
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option("useAutomationExtension", False)

driver = webdriver.Chrome(options=options)

# abre o X
driver.get("https://twitter.com/login")

print("Faça login manualmente e depois pressione ENTER no terminal para armazenar os três tweets mais recentes do usuário escolhido...")
input()

# Escolha o usuário aqui!
driver.get("https://twitter.com/choquei")

time.sleep(5)



dados = []

contador = 0
while contador < 3:
    tweets = driver.find_elements(By.XPATH, "//article")

    for tweet in tweets:
        if contador >= 3:
            break
        texto_total = tweet.text.lower()

        # ignorar fixado
        if "pinned" in texto_total:
            continue
        # ignorar anuncio
        if "promoted" in texto_total:
            continue
        # ignorar repost
        if "reposted" in texto_total:
            continue

        try:
            autor = tweet.find_element(By.XPATH, './/span').text
        except:
            autor = ""

        try:
            texto = tweet.find_element(By.XPATH, './/div[@lang]').text
        except:
            texto = ""

        try:
            data = tweet.find_element(By.XPATH, './/time').get_attribute("datetime")
        except:
            data = ""
        dados.append({
            "Autor": autor,
            "Data": data,
            "Texto": texto
        })  
        contador += 1

df = pd.DataFrame(dados)
df.to_csv("tweets.csv", index=False, encoding="utf-8")

print("Tweets salvos em tweets.csv")

# NÃO fecha o navegador
input("Pressione ENTER para encerrar o script...")
