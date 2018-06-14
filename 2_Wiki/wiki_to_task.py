import requests
import jsonlines
from bs4 import BeautifulSoup
import plac

def cat_to_links(category_url):
    """
    Find all the page urls linked to from a Wikipedia category page

    Parameters
    ----------
    category_url: str
        URL of a Wikipedia category page

    Returns
    -------
    links: list
        list of Wikipedia page URLs
    """
    category = BeautifulSoup(requests.get(category_url).content, "lxml")
    links = category.find("div", {"id": "mw-pages"}).find_all("a", href = True)
    links = ['https://en.wikipedia.org' + i['href'] for i in links][1:]
    return links

def results_to_tasks(links):
    """
    Take in URLs and return Prodigy-formatted tasks with an iframe displaying the page.

    Parameters
    ---------
    links: list
        list with URLs (not necessarily wikipedia) to display in Prodigy as iframes

    Returns
    -------
    tasks: list
        Prodigy formatted JSON with iframes
    """
    tasks = []
    for l in links:
        html = "<iframe width='900' height='415' src='{0}'></iframe>".format(l),
        task = {
            "html": html,
            "text": l
        }
        tasks.append(task)
    return tasks

@plac.annotations(
    cat_url=("Wikipedia category URL", "option", "i", str),
    output_file=("File to write Prodigy JSONL to", "option", "o", str))
def main(cat_url, output_file):
    """
    Go from Wikipedia category page to Prodigy JSONL
    """
    links = cat_to_links(cat_url)
    output = results_to_tasks(links)
    with jsonlines.open(output_file, mode='w') as writer:
        writer.write_all(output)


if __name__ == '__main__':
    plac.call(main)
