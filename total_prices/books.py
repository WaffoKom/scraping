from selectolax.parser import HTMLParser
# from bs4 import BeautifulSoup
from loguru import logger
import sys
import requests
import re

logger.remove()
logger.add("books.log", rotation="600kb", level="WARNING")

logger.add(sys.stderr, level="INFO")

# First method with BeautifulSoup

# soup = BeautifulSoup(req.text, "html.parser")

# Second method With selectolax


# example

# soup.select("a")
# soup.select_one("a")

# tree.css("a")
# tree.css_first("a")

BASE_URL = "https://books.toscrape.com"


def get_all_books_urls(url: str) -> list[str]:
    """
    Recuperer les URLS  des livres sur toutes les pages a partir d'une URL
    :param url: URL de depart
    :return:Liste de toutes les URLS de toutes les pages
    """


def get_next_page_url(tree: HTMLParser) -> str:
    """Recuper l'URL de la page suivante a partir du HTML d'une page donnee

    :param tree:Objet HTMLParser de la page
    :return:URL de la page suivante
    """
    pass


def get_all_books_urls_on_page(tree: HTMLParser) -> list[str]:
    """
    Recupere toutes les URLS  des livres present sur une page
    :param tree: Objet HTMLParser de la page
    :return: Liste des URLS de tous les livres sur toute la page
    """
    pass


def get_book_price(url: str) -> float:
    """
    Recupere le prix d'un livre a partir de son URL
    :param url: URL de la page du livre
    :return: Prix du livre multiplier par le nombre de livre en stock
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        tree = HTMLParser(response.text)
        price = extract_price_from_page(tree=tree)
        stock = extract_stock_quantity_from_page(tree=tree)
        return price * stock

    except requests.exceptions.RequestException as e:
        logger.error(f"Erreur lors de la requette HTTP : {e}")
        return 0.0


def extract_price_from_page(tree: HTMLParser) -> float:
    """ Extrait le prix du livre depuis le code HTML  de la page

    :param tree: Objet HTMLParser de la page du livre
    :return: Prix unitaire du livre
    """
    price_node = tree.css_first("p.price_color")
    if price_node:
        price_string = price_node.text()

    else:
        print(f"Aucun noeuds ne comprenant le prix n'a ete trouve")
        return 0.0
    try:
        price = (re.search(r"\d+(?:\.\d+)?", price_string).group())
    except (IndexError, ValueError, TypeError, AttributeError) as e:
        logger.error(f"Aucun nombre n'a ete trouve {e}")
        return 0.0
    else:
        print(float(price))
        return float(price)


def extract_stock_quantity_from_page(tree: HTMLParser) -> int:
    """
    Extrait la quantite de livre en stock depuis le code HTML  de la page

    :param tree:
    :return: Le nombre de livre en stock
    """
    return 1


def main():
    all_books_urls = get_all_books_urls(url=BASE_URL)
    total_price = 0
    for book_url in all_books_urls:
        price = get_book_price(url=book_url)
        total_price += price

    return total_price


if __name__ == "__main__":
    get_book_price(url=BASE_URL)
