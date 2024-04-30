from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    from bs4 import BeautifulSoup as BS
    import requests
    from random import random
    divs = []
    url = 'https://www.anekdot.ru/random/anekdot/?ysclid=lvjlgczctm675877123'
    page = requests.get(url)
    html_page = BS(page.content, "html.parser")
    div = html_page.find_all("div", attrs={"class": "topicbox"})
    div1 = []
    for i in div:
        y = i.text
        print(y)
        div1 += [y]
        return ' '.join(div1)


app.run()
