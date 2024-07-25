import requests
from bs4 import BeautifulSoup
BASE_URL = "https://books.toscrape.com"

req = requests.get(BASE_URL)
# with open("test.txt", "w", encoding="utf-8") as f:
#     f.write(req.text)
# with open("books.html", "r") as f:
#     html = f.read()

soup = BeautifulSoup(req.text, 'html.parser')

aside = soup.find("div", class_="side_categories")
categories = aside.find("ul").find("li").find("ul").find_all("li")
with open("test.txt", "w", encoding="utf-8") as f:
    for category in categories:
        f.write(category.text.strip() + "\n")
        print(category.text.strip(), category.name)


# images = soup.find("section").find_all("img")
# for image in images:
#     print(image.get("src"))

# Nous avons la deux facons de proceder pour obtenir des nom d'articles a partir de l'url

# titles = soup.find("section")
# titles_articles = titles.find_all("h3")
# for title_article in titles_articles:
#     for title in title_article:
#         totals_articles = title.get("title")
#         print(totals_articles)
limit_book: int = 20
titles_tags = soup.find_all("a", title=True)
result = [a["title"] for a in titles_tags]
if len(result) <= limit_book:
    print(result)
else:
    print("Update a number of your book !", len(result))


