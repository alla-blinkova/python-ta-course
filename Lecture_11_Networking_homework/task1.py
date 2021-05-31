import re

import requests
from bs4 import BeautifulSoup


def get_sites(url) -> set[str]:
    content = requests.get(url).text
    soup = BeautifulSoup(content)
    links = [link.attrs["href"] for link in soup.findAll("a")]
    domain_names = set()
    for link in links:
        search_result = re.search("^(.*//)?([A-Za-z0-9.]+)([/:])", link)
        if search_result:
            domain_names.add(search_result.group(2))
    return domain_names
