
#Bibliotecas
import requests
from bs4 import BeautifulSoup
import json
import os
from datetime import datetime

# Primeira função (Buscar página)

def buscar_pagina(url):
    """Baixa o HTML de uma URL e retorna o conteúdo como texto."""
    try:
        reposta = requests.get(url, timeout =30)
        reposta.raise_for_status()
        return reposta.text
    except Exception as erro:
        print(f"[ERRO] Falha ao acessar {url}: {erro}")
        return None