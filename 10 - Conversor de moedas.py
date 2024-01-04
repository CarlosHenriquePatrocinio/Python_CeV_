import requests
from bs4 import BeautifulSoup

headers = {'User-Agent':'User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
page = requests.get('https://www.google.com/search?q=dolar&sca_esv=583177807&sxsrf=AM9HkKkIPpUM3x3hFNZAN2eJNdNDuKsFiw%3A1700182884369&ei=ZLtWZYyUFvuc1sQP8PWr2AE&ved=0ahUKEwiM1oDn6smCAxV7jpUCHfD6ChsQ4dUDCBA&uact=5&oq=dolar&gs_lp=Egxnd3Mtd2l6LXNlcnAaAhgDIgVkb2xhcjIOEAAYgAQYsQMYgwEYiwMyEBAAGIoFGLEDGIMBGEMYiwMyCxAAGIAEGLEDGIMBMg0QABiKBRixAxiDARhDMhAQABiKBRixAxiDARhDGIsDMgoQABiKBRhDGIsDMgoQABiKBRhDGIsDMgoQABiKBRhDGIsDMg4QABiABBixAxiDARiLAzIOEAAYgAQYsQMYgwEYiwNIxwdQAFiBBnAAeAGQAQCYAeUBoAHLB6oBBTAuMy4yuAEDyAEA-AEBwgIEECMYJ8ICBxAjGIoFGCfCAg4QABiKBRixAxiDARiLA8ICCxAAGIAEGLEDGIsD4gMEGAAgQYgGAQ&sclient=gws-wiz-serp', headers = headers)

soup = BeautifulSoup(page.content,'html.parser')

atributos = {'class':'g'}

valor_dolar = soup.find_all('span', class_='DFlfde SwHCTb')[0]
valor_dolar = float((valor_dolar['data-value']))
real = float(input('Qual valor em REAL(R$) você quer converter? '))

print(f'O Dólar no momento está US${valor_dolar:.2f} e com R${real:.2f} você pode comprar US${real / valor_dolar:.2f}.')
