
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

    def get_next_td(label):
        label_td = soup.find("td", string=label)
        return label_td.find_next_sibling("td").text.strip() if label_td else ""

    name = get_text("h1[itemprop='name'] span.fn") or get_text("h1 span.fn")
    nickname = get_text("span.nickname em")

    data = {
        "name": name,
        "nickname": nickname,
        "age": get_next_td("AGE"),
        "birthdate": get_text("span[itemprop='birthDate']"),
        "height": get_next_td("HEIGHT"),
        "weight": get_next_td("WEIGHT"),
        "association": get_text("div.association-class"),
        "weight_class": get_next_td("CLASS"),
        "wins": get_text("div.winsloses-holder .wins .pl"),
        "losses": get_text("div.winsloses-holder .losses .pl")
    }

    return data
