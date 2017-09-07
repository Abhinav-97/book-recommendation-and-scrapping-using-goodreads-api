from bs4 import BeautifulSoup
import lxml.html
import pickle
import requests
import re
from urllib.request import urlopen

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

def get_book_ids():

	for i in range(1,5):
		page_url = 'https://www.goodreads.com/shelf/show/classics?page={}'.format(str(i))
		# page_url = url + '?page={}'.format(str(i))
		print(page_url)
		page = s.get(page_url)
		# page = urlopen(page_url)  
		soup = BeautifulSoup(page.content, 'html.parser')
		content = soup.find('div',{'class':'content'})
		# print(content.encode('utf-8'))
		main_content_container = content.find('div', {'class': 'mainContentContainer'})
		main_content = main_content_container.find('div', {'class':'mainContent'})
		# print(main_content.encode('utf-8'))
		main_content_float = main_content.find('div', {'class':'mainContentFloat'})
		left_container = main_content_float.find('div', {'class':'leftContainer'})
		book_list = left_container.find_all('div', {'class':'elementList'})

		for books in book_list:
			book = books.find('div', {'class':'left'})
			book_link = book.find('a', {'class':'bookTitle'})
			book_title = book_link.text
			print(book_title)
			book_link = book_link.get('href')
			book_link = book_link.split('/')
			# print(book_link)
			book_id= book_link[-1].split('.')[0]

			book_ids.append((book_id.encode('utf-8'), book_title.encode()))
		print('\n')

get_book_ids()#'https://www.goodreads.com/shelf/show/classics')
books = []
for bookid, book in book_ids:
	# print(type(bookid))
	# print(bookid)
	bookid = re.sub(r'\D', "", bookid)
	books.append((bookid,book))
	# print(bookid)

# print([x.encode('utf-8'),y.encode('utf-8') for x,y in books])
print(len(books))
print((set(books)))