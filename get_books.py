import urllib.request
from xml.etree import ElementTree
import xmltodict
from xml.dom import minidom
import pickle

# get books reviewed by a user 

with open('user_ids.txt', 'rb') as fp:
	user_ids = pickle.load(fp)
print(user_ids)
url = 'https://www.goodreads.com/review/list/1.xml?key=XpoGVm4lYBMCQceTmmw&v=2&shelf=read&per_page=200&page=4'
xml_code = urllib.request.urlopen(url)

# print(xml_code)
data = ElementTree.parse(xml_code)
# print(data.encode('utf-8'))
reviews_list = data.find('reviews')
print(reviews_list)
reviews = reviews_list.findall('review')
print(len(reviews))
for review in reviews:

	shelf = review.find('shelves')
	shelf_status = shelf.find('shelf')
	if shelf_status.attrib['name'] != 'read':
		continue

	book = review.find('book')
	book_title = book.find('title').text

	rating = review.find('rating').text
	print((book_title.encode('utf-8'),rating))





