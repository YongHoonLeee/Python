from bs4 import BeautifulSoup
import requests

# 전체 html 긁어오기
html = requests.get('https://www.python.org')
# print(html.text)

# soup 안에 넣기 , lxml 는 파서 
soup = BeautifulSoup(html.text, 'lxml')

# title 찾아서 넣기 여러개면 다 담김 지금은 하나.
titles = soup.find_all('title')
print(titles)

# div 중에서 class 이름이 introduction 인거 따오기 신기하다.
intro = soup.find_all('div', {'class': 'introduction'})
print(intro)


#응용하면 재밋는 프로그램 만들수 있겠다.