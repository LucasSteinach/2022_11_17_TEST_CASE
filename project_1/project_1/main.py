import requests
import re
from bs4 import BeautifulSoup
from pprint import pprint
# from time import sleep

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
def get_domains():
    url = 'http://www.tigir.com/domains.htm'
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    result = [tag.text[1:] for tag in soup.find_all('dt') if tag.text[0] == '.']
    return result, resp.status_code


def edit_link(code: str, ink: str) -> str:
    if code == 'none':
        return 'https://www.' + ink
    if code == 'www':
        return 'https://' + ink
    if code == 'http':
        return 'https://www.' + ink.split('//')[-1]
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


def get_data(filename) -> list:
    with open(filename) as file:
        str_list = ''.join(file.readlines()).split('\n')
    return str_list


def execute(filename: str) -> dict:
    domains_list = get_domains()[0]
    res_dict = dict()
    strings_list = get_data(filename)

    for line in strings_list:
        link = is_link(line, domains_list)
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
    return res_dict


if __name__ == '__main__':
    pprint(execute('input_strings.txt'))



