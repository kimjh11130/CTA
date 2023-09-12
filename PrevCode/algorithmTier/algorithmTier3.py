import requests
from bs4 import BeautifulSoup
import numpy as np
import json


def takeLevel(number):
    url = f'https://solved.ac/api/v3/search/problem'
    headers = {'Content-Type': 'application/json'}
    querystring = {"query": number}

    req = requests.get(url, headers=headers, params=querystring)

    if req.status_code == 200:
        data = json.loads(req.text)
        items = data.get("items")
        if items:
            return items[0]['level']

    return None


def getUrlFromPage(algorithm, page):
    print(f"하는중, {page}\n")
    problem_levels = np.zeros((31,), dtype=int)
    url = f'https://www.acmicpc.net/problemset?sort=ac_desc&algo={algorithm}&algo_if=and&page={page}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    number_list = soup.select('.list_problem_id')
    print(number_list)

    for item in number_list:
        level = takeLevel(item.get_text())
        if level is not None:
            problem_levels[level] += 1

    return problem_levels


if __name__ == '__main__':
    array = np.array(getUrlFromPage(175, 30))
    tmep = array.tolist()
    print(tmep)




