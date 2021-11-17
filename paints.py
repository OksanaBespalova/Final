import requests
from bs4 import BeautifulSoup

source_paints = requests.get('https://www.senukai.lt/c/apdailos-prekes/dazai-dazu-priedai/dazai/emulsiniai-dazai/emulsiniai-dazai-isores-darbams/bry').text
soup_paints = BeautifulSoup(source_paints, 'html.parser')
blokai_paints = soup_paints.find_all('div', class_='catalog-taxons-product catalog-taxons-product--grid-view')

paints = []
for blokas in blokai_paints:
    item = blokas.find('a', class_='catalog-taxons-product__name').text.strip()
    remove = ('l', 'kg')
    tmp_volume = item
    for x in remove:
        tmp_volume = tmp_volume.replace(x, '')
    tmp_volume1 = tmp_volume.split()
    volume = 0
    for x in tmp_volume1:
        try:
            volume += float(x)
        except ValueError:
            pass
    tmp_kaina = blokas.find('span', class_='catalog-taxons-product-price__item-price').span.text.strip()
    tmp_kaina1 = tmp_kaina.replace(',', '.')
    kaina = float(tmp_kaina1)
    spalva = blokas.find('strong', class_='catalog-taxons-product-key-attribute-list__item-value').next_element.next_element.next_element.next_element.strong.text.strip()
    paints.append([item, spalva, volume, kaina])

dazai = []
for x in paints:
    dazai.append(x[0])

dazo_norma = 0.3



