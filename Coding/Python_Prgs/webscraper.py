from requests_html import HTML, HTMLSession

session = HTMLSession()
r = session.get('https://www.pythonanywhere.com/')

heading_block = r.html.find('div.row', first=True)
heading = heading_block.find('h1', first=True)

image = r.html.find('#id_main_screenshot', first=True)

# to get the arrtibutes of a temlpate tag
# print(image.attrs)


# just extracting the content from the website
content_block = r.html.find('div.details-stripe', first=True)
content_mid_block = content_block.find('div.row')[0]
content = content_mid_block.find('div.col-md-3')


for c, cont in enumerate(content):
    head = cont.find('h3')[0].text
    txt = cont.find('p')[0].text
    print(f'heading {c} : {head}')
    print(f'Content {c} : {txt}')



# getting all the links from a website
all_links = r.html.links
for  i in all_links:
    print(i)

# Getting relative links
all_links = r.html.absolute_links
for  i in all_links:
    print(i)