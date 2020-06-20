import requests
from bs4 import BeautifulSoup

url = 'https://programmers.co.kr/learn/challenges?tab=all_challenges'

def get_max_page():
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    ret = soup.find_all("li", {"class":"page-item"})[-2].string
    return ret

def get_problems(page):
    ret = []    
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    get_max_page()
    all_problems = soup.find("div",{"class":"algorithm-list"}).find_all("div",{"class":"col-item"})

    # id, title, level
    for problem in all_problems:
        # id  
        prob_num = problem.find("a")["href"].split("/")[-1]

        # title  
        title = problem.find("h4",{"class":"title"}).string

        # level
        level = problem.find("div",{"class":"card-algorithm"})["class"][1]

        prob_obj = {
            "prob_num":prob_num,
            "title":title,
            "level":level,
        }
    return ret

def get_problems_data():
    data = []
    max_page = int(get_max_page())
    for page in range(max_page):
        data += get_problems(page)

get_problems_data()
