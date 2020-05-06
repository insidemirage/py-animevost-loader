from mirrors import look_for_mirror
import requests
from bs4 import BeautifulSoup
import json
import re
from pprint import pprint
from multiprocessing import Pool
PAGE_TEMPLATE = "{}/page/{}/"
mirror = ""


def get_titles_from_page(link):
    global mirror
    response = requests.get(link)
    soup = BeautifulSoup(response.text, "html.parser")
    titles = soup.find_all("div", class_="shortstory")
    result_titles = []
    for title in titles:
        name = title.find("div", class_="shortstoryHead").text
        title_link = title.find("a").get("href")
        image = mirror + title.find("img").get("src")
        title_content = title.find("div", class_="shortstoryContent")
        title_data = title.find_all("p")
        date = re.search(r"\d.*",title_data[0].text)
        if date:
            date = date.group(0)
        else:
            date = ""
        genre = re.sub(r"Жанр: +","", title_data[1].text)
        author = re.sub(r"Режиссёр: +","", title_data[4].text)
        text = re.sub(r"Описание: +","", title_data[-1].text)
        result_titles.append({
            "name":name,
            "link":title_link,
            "image":image,
            "date":date,
            "genre":genre,
            "author":author,
            "text":text
        })
    print(f"Page {link} done!")
    return result_titles



def main():
    global mirror
    mirror = look_for_mirror(40,50)
    response = requests.get(mirror)
    soup = BeautifulSoup(response.text, 'html.parser')
    pagination = soup.find("td", class_="block_4")
    last_page = int(pagination.find_all("a")[-1].text)
    page_links = []
    pool = Pool(25)
    for i in range(1, last_page+1):
        if i == 1:
            page_links.append(mirror)
        else:
            page_links.append(PAGE_TEMPLATE.format(mirror,i))
    result = pool.map(get_titles_from_page, page_links)
    pool.close()
    pool.join()
    with open("temp.json", "w+", encoding="utf8") as file:
     json.dump(result, file, ensure_ascii=False, indent=2)

main()
