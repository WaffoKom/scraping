import requests
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

BASE_URL = "https://books.toscrape.com"
with requests.Session() as session:
    response = session.get(BASE_URL)
    # req = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')


    def main() -> list[int]:
        book_ids = []
        try:
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"IL a eu un probleme lors de la requette :{e} !")
            raise requests.exceptions.RequestException from e

        one_star_books = soup.select("p.star-rating.One")
        print(len(one_star_books))
        for book in one_star_books:
            try:
                book_link = book.find_next("h3").find("a")["href"]

            except AttributeError as e:
                print(f"Impossible de trouver la balise ' <h3> ' ! {e}")
                raise AttributeError from e
            except TypeError as e:
                print(f"Impossible de trouver la balise ' <a> ' {e}")
                raise TypeError from e
            except KeyError as e:
                print(f"Impossible de trouver la clef 'href'{e} !")
                raise KeyError from e
            print(book_link)
            try:
                book_id = re.findall(r"_\d+", book_link)[0][1:]
                # print(book_id)
            except IndexError as e:
                print(f"Impossible de trouver l'ID du livre")
                raise IndexError from e
            else:
                book_ids.append(int(book_id))

        return book_ids

if __name__ == '__main__':
    print(main())
