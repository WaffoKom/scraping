import requests
from bs4 import BeautifulSoup

BASE_URL = "https://books.toscrape.com"
with requests.Session() as session:
    response = session.get(BASE_URL)
    # req = requests.get(BASE_URL)
    soup = BeautifulSoup(response.text, 'html.parser')


    def main():
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
            # print(book_link)
            # Separons l'url en plusieurs parties
            parts = book_link.split("/")

            #Obtenons les differentes informations
            directory = parts[0]
            product_id = parts[1].split('_')[1]
            file_name = parts[-1]

            #fesons un print des resultats

            # print(f"Répertoire : {directory}")
            print(f"ID du produit : {product_id}")
            # print(f"Nom du fichier : {file_name}")

if __name__ == '__main__':
    main()
