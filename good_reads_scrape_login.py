import requests
import lxml.html
from bs4 import BeautifulSoup
import pickle

user_ids = []

def get_user_ids(page):

	soup = BeautifulSoup(page.text, 'html.parser')

	content = soup.find('div',{'class':'content'})
	main_content_container = content.find('div', {'class': 'mainContentContainer'})
	main_content = main_content_container.find('div', {'class':'mainContent'})
	# print(main_content.encode('utf-8'))
	main_content_float = main_content.find('div', {'class':'mainContentFloat'})
	left_container = main_content_float.find('div', {'class':'leftContainer'})
	# print(left_container.encode('utf-8'))
	table_elements = left_container.find('table')
	# print(table_elements.encode('utf-8'))
	# left_table_rows = leftContainer.find('table').find('tbody')
	table_rows = table_elements.find_all('tr')
	for rows in table_rows:
		td = rows.find('td',{'valign':'top', 'width':None})
		links = td.find_all('a')
		id_link = links[0].get('href')
		id_link = id_link.split('/')
		user_ids.append(int(id_link[-1]))


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
# print(response.url)

top_librarians_url = 'https://www.goodreads.com/librarian/top_librarians?country=all&duration=a'
url_client = s.get(top_librarians_url)
top_librarians_page = url_client
get_user_ids(top_librarians_page)

top_librarians_year_url = 'https://www.goodreads.com/librarian/top_librarians?country=all&duration=y'
url_client = s.get(top_librarians_year_url)
top_librarians_year_page = url_client
get_user_ids(top_librarians_year_page)

top_readers_url = 'https://www.goodreads.com/user/top_readers?country=all&duration=a'
url_client = s.get(top_readers_url)
top_readers_page = url_client
get_user_ids(top_readers_page)

top_readers_us_url = 'https://www.goodreads.com/user/top_readers?utf8=%E2%9C%93&country=US&duration=a'
url_client = s.get(top_readers_us_url)
top_readers_us_page = url_client
get_user_ids(top_readers_us_page)


top_readers_ca_url = 'https://www.goodreads.com/user/top_readers?utf8=%E2%9C%93&country=CA&duration=a'
url_client = s.get(top_readers_ca_url)
top_readers_ca_page = url_client
get_user_ids(top_readers_ca_page)


popular_reviewers_url = 'https://www.goodreads.com/user/best_reviewers?country=all&duration=a'
url_client = s.get(popular_reviewers_url)
popular_reviewers_page = url_client
get_user_ids(popular_reviewers_page)

popular_reviewers_year_url = 'https://www.goodreads.com/user/best_reviewers?country=all&duration=y'
url_client = s.get(popular_reviewers_year_url)
popular_reviewers_year_page = url_client
get_user_ids(popular_reviewers_year_page)

popular_reviewers_us_year_url = 'https://www.goodreads.com/user/best_reviewers?country=US&duration=y'
url_client = s.get(popular_reviewers_us_year_url)
popular_reviewers_us_year_page = url_client
get_user_ids(popular_reviewers_us_year_page)

popular_reviewers_ca_year_url = 'https://www.goodreads.com/user/best_reviewers?country=CA&duration=y'
url_client = s.get(popular_reviewers_ca_year_url)
popular_reviewers_ca_year_page = url_client
get_user_ids(popular_reviewers_ca_year_page)

popular_reviewers_uk_year_url = 'https://www.goodreads.com/user/best_reviewers?country=GB&duration=y'
url_client = s.get(popular_reviewers_uk_year_url)
popular_reviewers_uk_year_page = url_client
get_user_ids(popular_reviewers_uk_year_page)

popular_reviewers_us_url = 'https://www.goodreads.com/user/best_reviewers?country=US&duration=a'
url_client = s.get(popular_reviewers_us_url)
popular_reviewers_us_page = url_client
get_user_ids(popular_reviewers_us_page)

popular_reviewers_ca_url = 'https://www.goodreads.com/user/best_reviewers?country=CA&duration=a'
url_client = s.get(popular_reviewers_ca_url)
popular_reviewers_ca_page = url_client
get_user_ids(popular_reviewers_ca_page)

popular_reviewers_uk_url = 'https://www.goodreads.com/user/best_reviewers?country=GB&duration=a'
url_client = s.get(popular_reviewers_uk_url)
popular_reviewers_uk_page = url_client
get_user_ids(popular_reviewers_uk_page)

popular_reviewers_url_year = 'https://www.goodreads.com/user/best_reviewers?country=all&duration=y'
url_client = s.get(popular_reviewers_url_year)
popular_reviewers_page_year = url_client
get_user_ids(popular_reviewers_page_year)

top_reviewers_url = 'https://www.goodreads.com/user/top_reviewers?country=all&duration=a'
url_client = s.get(top_reviewers_url)
top_reviewers_page = url_client
get_user_ids(top_reviewers_page)

top_reviewers_year_url = 'https://www.goodreads.com/user/top_reviewers?country=all&duration=y'
url_client = s.get(top_reviewers_year_url)
top_reviewers_year_page = url_client
get_user_ids(top_reviewers_year_page)


top_reviewers_year_us_url = 'https://www.goodreads.com/user/top_reviewers?country=US&duration=y'
url_client = s.get(top_reviewers_year_us_url)
top_reviewers_year_us_page = url_client
get_user_ids(top_reviewers_year_us_page)

top_reviewers_year_ca_url = 'https://www.goodreads.com/user/top_reviewers?country=CA&duration=y'
url_client = s.get(top_reviewers_year_ca_url)
top_reviewers_year_ca_page = url_client
get_user_ids(top_reviewers_year_ca_page)

top_reviewers_year_uk_url = 'https://www.goodreads.com/user/top_reviewers?country=GB&duration=y'
url_client = s.get(top_reviewers_year_uk_url)
top_reviewers_year_uk_page = url_client
get_user_ids(top_reviewers_year_uk_page)

top_reviewers_us_url = 'https://www.goodreads.com/user/top_reviewers?country=US&duration=a'
url_client = s.get(top_reviewers_us_url)
top_reviewers_us_page = url_client
get_user_ids(top_reviewers_us_page)

top_reviewers_ca_url = 'https://www.goodreads.com/user/top_reviewers?country=CA&duration=a'
url_client = s.get(top_reviewers_ca_url)
top_reviewers_ca_page = url_client
get_user_ids(top_reviewers_ca_page)

top_reviewers_uk_url = 'https://www.goodreads.com/user/top_reviewers?country=GB&duration=a'
url_client = s.get(top_reviewers_uk_url)
top_reviewers_uk_page = url_client
get_user_ids(top_reviewers_uk_page)

print(len(user_ids))
print(len(set(user_ids)))

with open('user_ids.txt','wb') as fp:
	pickle.dump(user_ids,fp)

# with open('user_ids.txt', 'rb') as fp:
# 	u = pickle.load(fp)

# print(u)