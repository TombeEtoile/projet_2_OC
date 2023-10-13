import requests
from bs4 import BeautifulSoup


def get_data_book():

    r = requests.get("http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html")
    soup = BeautifulSoup(r.content, 'html.parser')

    product_information = []
    breadcrumb = []
    breadcrumb_list = []
    all_p = []
    review = []
    list_2 = []

    url = r.url
    title = soup.title.text.strip()
    img = soup.find("img", src_="")
    product_information = soup.find_all("td")
    upc = product_information[0].text
    ht = product_information[2].text
    ttc = product_information[3].text
    breadcrumb = soup.find("ul", class_="breadcrumb")
    breadcrumb_list = breadcrumb.find_all("a", href_="")
    categorie = breadcrumb_list[2].text
    all_p = soup.find_all("p")
    availability = product_information[5].text
    description = all_p[3].text
    class_name = soup.find("p", class_="star-rating")


get_data_book()
