from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")

# Get all the tags
all_anchor_tags = soup.find_all(name="a", class_="titlelink")
all_scores = soup.find_all(name="span", class_="score")


article_title = []
article_link = []
article_scores = []


for tags in all_anchor_tags:
    title = tags.getText()
    article_title.append(title)
    link = tags.get("href")
    article_link.append(link)
    # print(title, link)

number = 0
for scores in all_scores:
    score = int(scores.getText().split()[0])
    if score > number:
        number = score
        # print(number)
    article_scores.append(score)

index = article_scores.index(number)
# print(index)


title = article_title[index]
link = article_link[index]
score = article_scores[index]

print(title,"\n",link,"\n",score)