import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint
from time import sleep

METHODS = [
    'CONNECT',
    'DELETE',
    'GET',
    'HEAD',
    'OPTIONS',
    'POST',
    'PUT',
    'TRACE',
    'PATCH',
]


#  parses top-level domains from internet
def get_domains() -> list:
    url = 'http://www.tigir.com/domains.htm'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    result = [tag.text[1:] for tag in soup.find_all('dt') if tag.text[0] == '.']
    return result


def edit_link(code: str, ink: str) -> str:
    if code == 'none':
        return 'https://www.' + ink
    if code == 'www':
        return 'https://' + ink
    if code == 'http':
        return 'https://' + ink.split('//')[-1]
    return ink


def domain_check(link_check: str, domains: list) -> bool:
    return link_check.split('.')[-1] in domains


def is_link(inp: str, domains):
    link_patterns = {'full': r"(http|https):\/\/www.([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])",
                     'http': r"(http|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])",
                     'www': r"www\.[\w_-]+\.\w{2,}",
                     'none': r"[\w_-]+\.\w{2,}",
                     }
    for code, pattern in link_patterns.items():
        result = re.search(pattern, inp)
        if result and len(result[0]) == len(inp) and domain_check(inp, domains):
            return True, edit_link(code, inp)
    return False, None


if __name__ == '__main__':
    DOMAINS = get_domains()
    res_dict = dict()

    with open('input_strings.txt') as file:
        lines = ''.join(file.readlines()).split('\n')

    # print(lines, '\n-----------\n')

    for line in lines:

        link = is_link(line, DOMAINS)
        # print('(', link[0], ' ', link[1], ' )')
        if not link[0]:
            print(f"The string '{line}' is not a link")
        else:
            res_dict.update({link[1]: dict()})
            for method in METHODS:
                response = requests.request(
                    method=method,
                    url=link[1],
                    allow_redirects=True,
                )
                if response.status_code != 405:
                    res_dict[link[1]].update({method: response.status_code})
                # sleep(2)
    pprint(res_dict)
