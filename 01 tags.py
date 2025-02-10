import requests
from bs4 import BeautifulSoup

with open("sample.html", "r", encoding="utf-8") as f:
    html_doc = f.read()
soup=BeautifulSoup(html_doc, 'html.parser')

#About Beautiful Soup ~{ Just remove the hashtag # to see the working of each command}

#print(soup.prettify()) show us the entire sample.html file

#print(soup.title, type(soup.title))

#title will show us the title , type will show is bs4.element.Tag

#print(soup.div) #will show the first division tag

#print(soup.find_all("div"))#will show all the divisions tags in the code

#if i want to specify which division I wanna display then i can use:

#print(soup.find_all("div")[0])
#This will show us the first div

#for link in soup.find_all("a"):
    #print(link.get("href"))
    #print(link.get_text())

#Kiti child aahet te check karaychy asel tar
#for child in soup.find(class_="container").children:
    #print(child)

#If we want to see the parent:

#for parent in soup.find(class_="box").parent:
    #print(parent)

# cont= soup.find(class_="container")
# cont.name="span"
# cont["class"]="my class"
# cont.string="I am a string"
# print(cont)

# ulTag=soup.new_tag("ul")

# liTag= soup.new_tag("li")
# liTag.string ="Home"
# ulTag.append(liTag)

# liTag= soup.new_tag("li")
# liTag.string ="About"
# ulTag.append(liTag)

# soup.html.body.insert(0,ulTag)
# with open("modified.html", "w") as f:
#     f.write(str(soup))

