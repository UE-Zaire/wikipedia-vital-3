import os
import json

links = []

for filename in os.listdir(os.getcwd() + '\\pages'):
    print('pages/' + filename)
    page_links = open('pages/' + filename, 'r')

    for line in page_links:
        links.append([filename[:-4].replace(' ', '_'), line])

print(len(links))

links_file = open('links.txt', 'w')
for link in links:
    links_file.write(','.join(link))
links_file.close()

links_json = open('links.json', 'w')
links_json.write(json.dumps(links))
