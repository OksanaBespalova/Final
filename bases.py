import requests
from bs4 import BeautifulSoup

source_base = requests.get('https://www.senukai.lt/c/apdailos-prekes/dazai-dazu-priedai/dazai/emulsiniai-dazai/emulsiniai-dazai-isores-darbams/bry?f=kje5').text
soup_base = BeautifulSoup(source_base, 'html.parser')
blokas_base = soup_base.find('div', class_='catalog-taxons-product__hover')

item_base = blokas_base.find('a', class_='catalog-taxons-product__name').text.strip()

tmp_kaina_base = blokas_base.find('span', class_='catalog-taxons-product-price__item-price').span.text.strip()
tmp_kaina_base1 = tmp_kaina_base.replace(',', '.')
kaina_base = float(tmp_kaina_base1)

tmp_volume_base = item_base.replace('l', '')
tmp_volume_base1 = tmp_volume_base.split()
volume_base = float(tmp_volume_base1[-1])

bases_norma = 0.2
