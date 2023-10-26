import requests
from bs4 import BeautifulSoup


def get_data_book(url):

    r = requests.get(url)
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
    img_url = img["src"]
    valid_img_url = img_url.replace("../..", "https://books.toscrape.com/")
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
    class_name = soup.find("p", class_="star-rating Two")
    class_rating = class_name["class"]
    product_rating = class_rating[1]

    all_information = {
        "url": url,
        "title": title,
        "image produit": valid_img_url,
        "UPC": upc,
        "prix HT": ht,
        "prix TTC": ttc,
        "categorie parente": categorie,
        "nombre en stock": availability,
        "avis (sur 5)": product_rating,
        "description": description
    }

    return all_information


print(get_data_book())


"""
    return url, title, valid_img_url, upc, ht, ttc, categorie, availability, product_rating, description
"""
