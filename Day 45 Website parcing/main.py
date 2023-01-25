from bs4 import BeautifulSoup

# Don't forget to add the encoding.
with open("website.html", encoding="UTF-8") as file:
    data = file.read()

soup = BeautifulSoup(data, 'html.parser')
# # Print out the title tag
# print(soup.title)
#
# # Print out the name of the tag
# print(soup.title.name)
#
# # Print out the value in the tag
# print(soup.title.string)

# entire HTML file
# print(soup.prettify())

# print out the first anchor tag, li tag, paragraph tag
# print(soup.li)

# prints all of the tags in your website using the find all option
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# Loop through all the returned tags
# for tags in all_anchor_tags:
#     # to get the text from the tags
#     print(tags.getText())
#     # to get the href attr from the tag
#     print(tags.get("href"))


# find by ID or CLass
"""FInd_all returns everything but Find returns just the first item"""

heading = soup.find(name="h1", id="name")
print(heading)
section_heading = soup.find(name="h3", class_="heading")

# HOW to select specifc tags from the HTML document by html selectors e.g p tag then a tag
company_url = soup.select_one(selector="p a")
print(company_url)

# select by id(#) or class(.)
h3_heading= soup.select_one(selector=".heading")
h1_name = soup.select_one(selector="#name")

print(h1_name, h3_heading)

