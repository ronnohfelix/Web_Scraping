from bs4 import BeautifulSoup

with open('index.html') as html_file:
    content = html_file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    
    tags = soup.find_all('h1')
    print(tags)
    for tag in tags:
        print(tag.text)