import bs4
import requests
from operator import itemgetter
response = requests.get("https://news.ycombinator.com/front")
yc_website = response.text

soup = bs4.BeautifulSoup(yc_website, "html.parser")

article_tags = soup.find_all(name="span", class_="titleline")

results = []
for i, tag in enumerate(article_tags):

    if i == 0:
        score = soup.findAll(name="span", class_="score")

    article_link = tag.find_next(name="a")
    article_text = article_link.getText()
    article_url = article_link.get("href")
    plain_points = score[i].getText().split(" ")
    result = {
        "article_url": article_url,
        "article_text": article_text,
        "score":  int(plain_points[0])
    }
    results.append(result)

results = sorted(results, key=itemgetter('score'), reverse=True)

for result in results:
    print(result)

# article_text = article_tag.getText()
# print(article_text)
# with open("website.html", "r") as file:
#     content = file.read()

# # print(content)

# soup = bs4.BeautifulSoup(content, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.a)

# all_achor_tags = soup.find_all(name="a")

# for tag in all_achor_tags:
#     print(tag.get("href"))


# heading = soup.find(name="h1", id="name")
# print(heading)

# company_url = soup.select_one(selector="")
