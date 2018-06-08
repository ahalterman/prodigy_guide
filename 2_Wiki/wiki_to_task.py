import requests
import jsonlines
from bs4 import BeautifulSoup

def cat_to_links(category_url):
    category = BeautifulSoup(requests.get(category_url).content, "lxml")
    links = category.find("div", {"id": "mw-pages"}).find_all("a", href = True)
    links = ['https://en.wikipedia.org' + i['href'] for i in links][1:]
    return links

def results_to_task(links)
    output = []
    for l in links:
        html = "<iframe width='960' height='415' src='{0}'></iframe>".format(l),
        task = {
            "html": html,
            "text": l
        }
        output.append(task)
    return links

if __name__ == "__main__":
    links = cat_to_links("https://en.wikipedia.org/wiki/Category:Towns_in_Oklahoma")
    output = results_to_tasks(links)
    with jsonlines.open("wiki_tasks.jsonl", mode='w') as writer:
        writer.write_all(output)
