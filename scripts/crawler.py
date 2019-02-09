from bs4 import BeautifulSoup
import requests

url = 'https://ponisha.ir/search/projects/skill-c++-programming/currency-IRR/sort-newest/page'
limit = 2
for page in range(1, limit + 1):
    html_doc = requests.get('{}/{}'.format(url, page)).content
    soup = BeautifulSoup(html_doc, 'html.parser')
    ul = soup.find_all('ul', {"class": "projects"})[0]
    lis = ul.find_all('li')
    projects = []

    for li in lis:
        project = {'skills': []}

        a = li.find('a', {'class': 'no-link'})
        project['title'] = a['title']
        project['url'] = a['href']

        div = li.find('div', {'class': 'height-50px'})
        project['description'] = div.text.strip()

        a_tags = li.select('div.labels a')
        for a_tag in a_tags:
            project['skills'].append(a_tag.find('div').text.strip())

        price = li.select('div.budget span')[0]['amount']
        project['budget'] = price[:-1]

        print(project)
