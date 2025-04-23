
import requests
from bs4 import BeautifulSoup

def parse_fighter(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/113.0.0.0 Safari/537.36"
    }
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')

    def get_text(css_selector):
        el = soup.select_one(css_selector)
        return el.text.strip() if el else ""

    data = {
        "name": get_text("span.fn[itemprop='name']"),
        "nickname": get_text("span[itemprop='alternateName']").replace('"', ''),
        "age": get_text("div.fighter-data td:contains('AGE') + td"),
        "birthdate": get_text("span[itemprop='birthDate']"),
        "height": get_text("div.fighter-data td:contains('HEIGHT') + td"),
        "weight": get_text("div.fighter-data td:contains('WEIGHT') + td"),
        "association": get_text("div.association-class"),
        "weight_class": get_text("div.fighter-data td:contains('CLASS') + td"),
        "wins": get_text("div.winsloses-holder .wins .pl"),
        "losses": get_text("div.winsloses-holder .losses .pl")
    }

    return data
