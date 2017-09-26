import urllib.request
from xml.etree import ElementTree
import xmltodict
from xml.dom import minidom
import pickle

# get books reviewed by a user 

# d = {}
# with open('book_reviews.txt', 'wb') as fp:
# 	pickle.dump(d,fp)

with open('book_reviews.txt', 'rb') as fp:
	book_dict = pickle.load(fp)
	fp.close()

with open('user_ids.txt', 'rb') as fp:
	user_ids = pickle.load(fp)
# print(user_ids)
print(book_dict)
print(len(book_dict))

def get_books(user_id):
	book_dict[user_id] = {}
	for i in range(1, 25):

		url = 'https://www.goodreads.com/review/list/'+ str(user_id)+'.xml?key=XpoGVm4lYBMCQceTmmw&v=2&shelf=read&per_page=200&page='+str(i)
		print(url)
		try:
			xml_code = urllib.request.urlopen(url)
		except:
			break
		# print(xml_code)
		data = ElementTree.parse(xml_code)
		# print(data.encode('utf-8'))
		reviews_list = data.find('reviews')
		print(reviews_list)
		reviews = reviews_list.findall('review')
		if len(reviews) == 0:
			break
		for review in reviews:

			# shelf = review.find('shelves')
			# shelf_status = shelf.find('shelf')
			# if shelf_status.attrib['name'] != 'read':
			# 	continue

			book = review.find('book')
			book_title = book.find('title').text
			book_id = book.find('id').text
			rating = review.find('rating').text
			book_dict[user_id][int(book_id)] = int(rating)
			print((book_id,rating))
	# print(book_dict)
	with open('book_reviews.txt', 'wb') as fp:
		pickle.dump(book_dict,fp)

for i in range(75,100):
	print(i)
	get_books(user_ids[i])
# print(book_dict)
# get_books(user_ids[1])


