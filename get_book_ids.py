from bs4 import BeautifulSoup
import lxml.html
import pickle
import requests
import re
from urllib.request import urlopen
import pandas as pd

book_ids = []
s = requests.session()
login = s.get('https://www.goodreads.com/user/sign_in')
login_html = lxml.html.fromstring(login.text)
hidden_input = login_html.xpath(r'//div[@class="wrapper"]//div[@class="content distractionless"]//div[@class="mainContentContainer"]//div[@class="mainContent"]//div[@class="contentBox clearfix"]//div[@class="column_right"]//div[@id="emailForm"]//form//input[@type="hidden"]')
# print(hidden_input)
form = { x.attrib["name"]: x.attrib["value"] for x in hidden_input }

# for key, value in form.items():
# 	print(key.encode('utf-8'))
# 	print(value.encode('utf-8'))

form['user[email]']='abhinavdutt19@gmail.com'
form['user[password']='abhi97dutt'

response = s.post('https://www.goodreads.com/user/sign_in', data=form)

print(response.ok)

def get_book_ids(url):

	for i in range(1,7):
		page_url = url + '?page=' + str(i)
		# page_url = url + '?page={}'.format(str(i))
		print(page_url)
		page = s.get(page_url)
		# page = urlopen(page_url)  
		soup = BeautifulSoup(page.content, 'html.parser')
		content = soup.find('div',{'class':'content'})
		# print(content.encode('utf-8').decode('utf-8'))
		main_content_container = content.find('div', {'class': 'mainContentContainer'})
		main_content = main_content_container.find('div', {'class':'mainContent'})
		# print(main_content.encode('utf-8').decode())
		main_content_float = main_content.find('div', {'class':'mainContentFloat'})
		left_container = main_content_float.find('div', {'class':'leftContainer'})
		book_list = left_container.find_all('div', {'class':'elementList'})

		for books in book_list:
			book = books.find('div', {'class':'left'})
			book_span = books.find('span', {'itemprop':'author'})
			author_name = book_span.find('span', {'itemprop':'name'})
			book_author = author_name.text
			book_links = book.find_all('a')
			book_title = book_links[0].get('title')
			# print(book_title.decode('utf-8'))
			book_link = book_links[0].get('href')
			book_link = book_link.split('/')
			# print(book_link)
			book_id= book_link[-1].split('.')[0]

			book_ids.append((book_id, book_title,book_author))
		print('\n')

get_book_ids('https://www.goodreads.com/shelf/show/classics')
get_book_ids('https://www.goodreads.com/shelf/show/fiction')
get_book_ids('https://www.goodreads.com/shelf/show/mystery')
get_book_ids('https://www.goodreads.com/shelf/show/thriller')
get_book_ids('https://www.goodreads.com/shelf/show/non-fiction')
get_book_ids('https://www.goodreads.com/shelf/show/philosophy')
get_book_ids('https://www.goodreads.com/shelf/show/science-fiction')
get_book_ids('https://www.goodreads.com/shelf/show/horror')
get_book_ids('https://www.goodreads.com/shelf/show/fantasy')
get_book_ids('https://www.goodreads.com/shelf/show/young-adult')
get_book_ids('https://www.goodreads.com/shelf/show/romance')
get_book_ids('https://www.goodreads.com/shelf/show/adult')

books = []
for bookid, book, b_author in book_ids:
	# print(type(bookid))
	# print(bookid)
	bookid = re.sub(r'\D', "", bookid)
	books.append((bookid, book, b_author))
	# print(bookid)

# print([x.encode('utf-8'),y.encode('utf-8') for x,y in books])
finbook_list = (sorted(set(books), key=lambda x: books.index(x)))
print(len(finbook_list))

final_book_ids = []
final_books = []
final_book_authors = [] 

for ids, books, author in finbook_list:

	final_book_ids.append(ids)
	final_books.append(books)
	final_book_authors.append(author)

book_data = pd.DataFrame({'book_id': final_book_ids,
						  'book_title': final_books,
						   'author': final_book_authors})
book_data.to_csv('book_data.csv', index=False)

with open('book_ids.txt', 'wb') as fp:
	pickle.dump(finbook_list,fp)