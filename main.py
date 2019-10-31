import requests
from lxml import html
import json

with requests.session() as session:
    req = session.get('https://www.flippa.com/search?filter%5Bproperty_type%5D=app&search_template=apps_ending_soon')
    # with open('teste.html', 'w') as file:
    #     file.write(req.text)
    page = req.text
    page = html.fromstring(page)
    itens = page.xpath("//*[contains(@class, 'Basic___propertyName')]/text()")

    for item in itens:
        dictio = {'nome': item}
        print(dictio)
