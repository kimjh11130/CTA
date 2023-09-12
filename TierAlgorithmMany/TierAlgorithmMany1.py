import requests
from bs4 import BeautifulSoup
import numpy as np
import json


# spoiler-link
def takeLevel(number):
    url = f'https://solved.ac/api/v3/problem/show'
    headers = {'Content-Type': 'application/json'}
    querystring = {"problemId": number}

    req = requests.get(url, headers=headers, params=querystring)
    if req.status_code == 200:
        data = json.loads(req.text).get("tags")
        if data:
            return len(data)

def getUrlFromPage(tier, page):
    print(f"하는중, {page}\n")
    problem_levels = np.zeros((31,), dtype=int)
    url = f'https://www.acmicpc.net/problemset?sort=no_asc&tier={tier}&page={page}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}

    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.text, 'lxml')
    number_list = soup.select('.list_problem_id')

    for item in number_list:
        level = takeLevel(item.get_text())
        if level is not None:
            problem_levels[level] += 1

    return problem_levels


if __name__ == '__main__':
    array = np.array(getUrlFromPage(21, 9))
    tmep = array.tolist()
    print(tmep)
