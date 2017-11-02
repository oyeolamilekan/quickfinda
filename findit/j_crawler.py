from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import re
import requests
import tempfile
from .models import Products
from django.core import files
from django.core.files.base import ContentFile
import time
import threading
from django.utils.crypto import get_random_string

def jumia_crawler():
	# for urls in range(1,25):
	# 	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	# 	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	# 	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	# 	       'Accept-Encoding': 'none',
	# 	       'Accept-Language': 'en-US,en;q=0.8',
	# 	       'Connection': 'keep-alive'}
	# 	html = Request('https://www.jumia.com.ng/smartphones/?page=%s'%urls,headers=hdr)
	# 	htmll = urlopen(html).read()
	# 	bsObj = BeautifulSoup(htmll,'html.parser')
	# 	namelist = bsObj.findAll('div',{'class':'-gallery'})
	# 	for news in namelist:
	# 		product_link = news.find('a',{'class':'link'})
	# 		product_link = product_link.attrs['href']
	# 		image = news.find('img',{'class':'image'})
	# 		images = image.attrs['data-src']
	# 		product_named = news.find('h2',{'class':'title'})
	# 		product_price = news.find('span', {'class','price'}).find_all('span')
	# 		product_price = product_price[1]
	# 		product_price = bytes(str(product_price.text),'UTF-8')
	# 		product_price = product_price.decode('ascii','ignore')
	# 		namelst = bytes(str(product_named.text), 'UTF-8')
	# 		namelst = namelst.decode('ascii','ignore')
	# 		htl = Request(images,headers=hdr)
	# 		httl = urlopen(htl).read()
	# 		print(namelst,product_price)
	# 		if Products.objects.filter(name=namelst,shop='jumia').exists():
	# 			produc = Products.objects.get(name=namelst,shop='jumia')
	# 			# Checks the price
	# 			if produc.price != product_price:
	# 				produc.old_price = produc.price
	# 				produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
	# 				# Updates the price
	# 				produc.price = product_price
	# 				# Saves the price
					
	# 				produc.save()
	# 		else:
	# 			request = requests.get(images, stream=True)
	# 			if request.status_code != requests.codes.ok:
	# 				continue
	# 			randd_ne = get_random_string(length=10)
	# 			file_name = images.split('/')[-1]
	# 			point_finder = file_name.find('.')
	# 			file_name = file_name[:point_finder] + randd_ne
	# 			lf = tempfile.NamedTemporaryFile()
	# 			for block in request.iter_content(1024*8):
	# 				if not block:
	# 					break
	# 				lf.write(block)
	# 			lf = ContentFile(httl)
	# 			product = Products(name=namelst,price=product_price,source_url=product_link,shop='jumia')
	# 			product.image.save(file_name[:20],lf)

	# for urls in range(1,25):
	# 	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	# 	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	# 	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	# 	       'Accept-Encoding': 'none',
	# 	       'Accept-Language': 'en-US,en;q=0.8',
	# 	       'Connection': 'keep-alive'}
	# 	html = Request('https://www.jumia.com.ng/laptops/?page=%s'%urls,headers=hdr)
	# 	htmll = urlopen(html).read()
	# 	bsObj = BeautifulSoup(htmll,'html.parser')
	# 	namelist = bsObj.findAll('div',{'class':'-gallery'})
	# 	for news in namelist:
	# 		product_link = news.find('a',{'class':'link'})
	# 		product_link = product_link.attrs['href']
	# 		image = news.find('img',{'class':'image'})
	# 		images = image.attrs['data-src']
	# 		product_named = news.find('h2',{'class':'title'})
	# 		product_price = news.find('span', {'class','price'}).find_all('span')
	# 		product_price = product_price[1]
	# 		product_price = bytes(str(product_price.text),'UTF-8')
	# 		product_price = product_price.decode('ascii','ignore')
	# 		namelst = bytes(str(product_named.text), 'UTF-8')
	# 		namelst = namelst.decode('ascii','ignore')
	# 		htl = Request(images,headers=hdr)
	# 		httl = urlopen(htl).read()
	# 		if Products.objects.filter(name=namelst,shop='jumia').exists():
				
	# 			produc = Products.objects.get(name=namelst,shop='jumia')
	# 			# Checks the price
	# 			if produc.price != product_price:
	# 				produc.old_price = produc.price
	# 				produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
	# 				# Updates the price
	# 				produc.price = product_price
	# 				# Saves the price
					
	# 				produc.save()
	# 		else:
	# 			request = requests.get(images, stream=True)
	# 			if request.status_code != requests.codes.ok:
	# 				continue
	# 			randd_ne = get_random_string(length=10)
	# 			file_name = images.split('/')[-1]
	# 			point_finder = file_name.find('.')
	# 			file_name = file_name[:point_finder] + randd_ne
	# 			lf = tempfile.NamedTemporaryFile()
	# 			for block in request.iter_content(1024*8):
	# 				if not block:
	# 					break
	# 				lf.write(block)
	# 			lf = ContentFile(httl)
	# 			product = Products(name=namelst,price=product_price,source_url=product_link,shop='jumia',genre='laptops')
	# 			product.image.save(file_name[:20],lf)

	# for urls in range(1,25):
	# 	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	# 	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	# 	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	# 	       'Accept-Encoding': 'none',
	# 	       'Accept-Language': 'en-US,en;q=0.8',
	# 	       'Connection': 'keep-alive'}
	# 	html = Request('https://www.jumia.com.ng/televisions/?page=%s'%urls,headers=hdr)
	# 	htmll = urlopen(html).read()
	# 	bsObj = BeautifulSoup(htmll,'html.parser')
	# 	namelist = bsObj.findAll('div',{'class':'-gallery'})
	# 	for news in namelist:
	# 		product_link = news.find('a',{'class':'link'})
	# 		product_link = product_link.attrs['href']
	# 		image = news.find('img',{'class':'image'})
	# 		images = image.attrs['data-src']
	# 		product_named = news.find('h2',{'class':'title'})
	# 		product_price = news.find('span', {'class','price'}).find_all('span')
	# 		product_price = product_price[1]
	# 		product_price = bytes(str(product_price.text),'UTF-8')
	# 		product_price = product_price.decode('ascii','ignore')
	# 		namelst = bytes(str(product_named.text), 'UTF-8')
	# 		namelst = namelst.decode('ascii','ignore')
	# 		htl = Request(images,headers=hdr)
	# 		httl = urlopen(htl).read()
	# 		print(namelst,product_price)
	# 		if Products.objects.filter(name=namelst,shop='jumia').exists():
				
	# 			produc = Products.objects.get(name=namelst,shop='jumia')
	# 			# Checks the price
	# 			if produc.price != product_price:
	# 				produc.old_price = produc.price
	# 				produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
	# 				# Updates the price
	# 				produc.price = product_price
	# 				# Saves the price
					
	# 				produc.save()
	# 		else:
	# 			request = requests.get(images, stream=True)
	# 			if request.status_code != requests.codes.ok:
	# 				continue
	# 			randd_ne = get_random_string(length=10)
	# 			file_name = images.split('/')[-1]
	# 			point_finder = file_name.find('.')
	# 			file_name = file_name[:point_finder] + randd_ne
	# 			lf = tempfile.NamedTemporaryFile()
	# 			for block in request.iter_content(1024*8):
	# 				if not block:
	# 					break
	# 				lf.write(block)
	# 			lf = ContentFile(httl)
	# 			product = Products(name=namelst,price=product_price,source_url=product_link,genre='televisions',shop='jumia')
	# 			product.image.save(file_name[:20],lf)
				
	# for urls in range(1,25):
	# 	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	# 	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	# 	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	# 	       'Accept-Encoding': 'none',
	# 	       'Accept-Language': 'en-US,en;q=0.8',
	# 	       'Connection': 'keep-alive'}
	# 	html = Request('https://www.jumia.com.ng/mens-shirts/page=%s'%urls,headers=hdr)
	# 	htmll = urlopen(html).read()
	# 	bsObj = BeautifulSoup(htmll,'html.parser')
	# 	namelist = bsObj.findAll('div',{'class':'-gallery'})
	# 	for news in namelist:
	# 		product_link = news.find('a',{'class':'link'})
	# 		product_link = product_link.attrs['href']
	# 		image = news.find('img',{'class':'image'})
	# 		images = image.attrs['data-src']
	# 		product_named = news.find('h2',{'class':'title'})
	# 		product_price = news.find('span', {'class','price'}).find_all('span')
	# 		product_price = product_price[1]
	# 		product_price = bytes(str(product_price.text),'UTF-8')
	# 		product_price = product_price.decode('ascii','ignore')
	# 		namelst = bytes(str(product_named.text), 'UTF-8')
	# 		namelst = namelst.decode('ascii','ignore')
	# 		htl = Request(images,headers=hdr)
	# 		httl = urlopen(htl).read()
	# 		print(namelst,product_price)
	# 		if Products.objects.filter(name=namelst,shop='jumia').exists():
				
	# 			produc = Products.objects.get(name=namelst,shop='jumia')
	# 			# Checks the price
	# 			if produc.price != product_price:
	# 				produc.old_price = produc.price
	# 				produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
	# 				# Updates the price
	# 				produc.price = product_price
	# 				# Saves the price
					
	# 				produc.save()
	# 		else:
	# 			request = requests.get(images, stream=True)
	# 			if request.status_code != requests.codes.ok:
	# 				continue
	# 			randd_ne = get_random_string(length=10)
	# 			file_name = images.split('/')[-1]
	# 			point_finder = file_name.find('.')
	# 			file_name = file_name[:point_finder] + randd_ne
	# 			lf = tempfile.NamedTemporaryFile()
	# 			for block in request.iter_content(1024*8):
	# 				if not block:
	# 					break
	# 				lf.write(block)
	# 			lf = ContentFile(httl)
	# 			product = Products(name=namelst,price=product_price,source_url=product_link,genre='shirts',shop='jumia')
	# 			product.image.save(file_name[:20],lf)
	# 			print('helloo')

	# for urls in range(1,25):
	# 	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	# 	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	# 	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	# 	       'Accept-Encoding': 'none',
	# 	       'Accept-Language': 'en-US,en;q=0.8',
	# 	       'Connection': 'keep-alive'}
	# 	html = Request('https://www.jumia.com.ng/womens-dresses/page=%s'%urls,headers=hdr)
	# 	htmll = urlopen(html).read()
	# 	bsObj = BeautifulSoup(htmll,'html.parser')
	# 	namelist = bsObj.findAll('div',{'class':'-gallery'})
	# 	for news in namelist:
	# 		product_link = news.find('a',{'class':'link'})
	# 		product_link = product_link.attrs['href']
	# 		image = news.find('img',{'class':'image'})
	# 		images = image.attrs['data-src']
	# 		product_named = news.find('h2',{'class':'title'})
	# 		product_price = news.find('span', {'class','price'}).find_all('span')
	# 		product_price = product_price[1]
	# 		product_price = bytes(str(product_price.text),'UTF-8')
	# 		product_price = product_price.decode('ascii','ignore')
	# 		namelst = bytes(str(product_named.text), 'UTF-8')
	# 		namelst = namelst.decode('ascii','ignore')
	# 		htl = Request(images,headers=hdr)
	# 		httl = urlopen(htl).read()
	# 		print(namelst,product_price)
	# 		if Products.objects.filter(name=namelst,shop='jumia').exists():
				
	# 			produc = Products.objects.get(name=namelst,shop='jumia')
	# 			# Checks the price
	# 			if produc.price != product_price:
	# 				produc.old_price = produc.price
	# 				produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
	# 				# Updates the price
	# 				produc.price =product_price
	# 				# Saves the price
					
	# 				produc.save()
	# 		else:
	# 			request = requests.get(images, stream=True)
	# 			if request.status_code != requests.codes.ok:
	# 				continue
	# 			randd_ne = get_random_string(length=10)
	# 			file_name = images.split('/')[-1]
	# 			point_finder = file_name.find('.')
	# 			file_name = file_name[:point_finder] + randd_ne
	# 			lf = tempfile.NamedTemporaryFile()
	# 			for block in request.iter_content(1024*8):
	# 				if not block:
	# 					break
	# 				lf.write(block)
	# 			lf = ContentFile(httl)
	# 			product = Products(name=namelst,price=product_price,source_url=product_link,genre='women-dresses',shop='jumia')
	# 			product.image.save(file_name[:20],lf)

	# hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	# 	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	# 	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	# 	       'Accept-Encoding': 'none',
	# 	       'Accept-Language': 'en-US,en;q=0.8',
	# 	       'Connection': 'keep-alive'}
	# html = Request('https://istore.jumia.com.ng/',headers=hdr)
	# htmll = urlopen(html).read()
	# bsObj = BeautifulSoup(htmll,'html.parser')
	# namelist = bsObj.findAll('div',{'class':'-gallery'})
	# for news in namelist:
	# 	product_link = news.find('a',{'class':'link'})
	# 	product_link = product_link.attrs['href']
	# 	image = news.find('img',{'class':'image'})
	# 	images = image.attrs['data-src']
	# 	product_named = news.find('h2',{'class':'title'})
	# 	product_price = news.find('span', {'class','price'}).find_all('span')
	# 	product_price = product_price[1]
	# 	product_price = bytes(str(product_price.text),'UTF-8')
	# 	product_price = product_price.decode('ascii','ignore')
	# 	namelst = bytes(str(product_named.text), 'UTF-8')
	# 	namelst = namelst.decode('ascii','ignore')
	# 	htl = Request(images,headers=hdr)
	# 	httl = urlopen(htl).read()
	# 	print(namelst,product_price)
	# 	if Products.objects.filter(name=namelst,shop='jumia').exists():
		
	# 		produc = Products.objects.get(name=namelst,shop='jumia')
	# 		# Checks the price
	# 		if produc.price != product_price:
	# 			produc.old_price = produc.price
	# 			produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
	# 			# Updates the price
	# 			produc.price = product_price
	# 			# Saves the price
				
	# 			produc.save()
	# 	else:
	# 		request = requests.get(images, stream=True)
	# 		if request.status_code != requests.codes.ok:
	# 			continue
	# 		randd_ne = get_random_string(length=10)
	# 		file_name = images.split('/')[-1]
	# 		point_finder = file_name.find('.')
	# 		file_name = file_name[:point_finder] + randd_ne
	# 		lf = tempfile.NamedTemporaryFile()
	# 		for block in request.iter_content(1024*8):
	# 			if not block:
	# 				break
	# 			lf.write(block)
	# 		lf = ContentFile(httl)
	# 		product = Products(name=namelst,price=product_price,source_url=product_link,shop='jumia')
	# 		product.image.save(file_name,lf)
	# https://www.jumia.com.ng/womens-watches/
	# for urls in range(1,25):
	# 	hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
	# 	       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	# 	       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
	# 	       'Accept-Encoding': 'none',
	# 	       'Accept-Language': 'en-US,en;q=0.8',
	# 	       'Connection': 'keep-alive'}
	# 	html = Request('https://www.jumia.com.ng/mens-watches/?page=%s'%urls,headers=hdr)
	# 	htmll = urlopen(html).read()
	# 	bsObj = BeautifulSoup(htmll,'html.parser')
	# 	namelist = bsObj.findAll('div',{'class':'-gallery'})
	# 	for news in namelist:
	# 		product_link = news.find('a',{'class':'link'})
	# 		product_link = product_link.attrs['href']
	# 		image = news.find('img',{'class':'image'})
	# 		images = image.attrs['data-src']
	# 		product_named = news.find('h2',{'class':'title'})
	# 		product_price = news.find('span', {'class','price'}).find_all('span')
	# 		product_price = product_price[1]
	# 		product_price = bytes(str(product_price.text),'UTF-8')
	# 		product_price = product_price.decode('ascii','ignore')
	# 		namelst = bytes(str(product_named.text), 'UTF-8')
	# 		namelst = namelst.decode('ascii','ignore')
	# 		htl = Request(images,headers=hdr)
	# 		httl = urlopen(htl).read()
	# 		print(namelst,product_price)
	# 		if Products.objects.filter(name=namelst,shop='jumia',genre='men-watches').exists():
				
	# 			produc = Products.objects.get(name=namelst,shop='jumia',genre='men-watches')
	# 			# Checks the price
	# 			if produc.price != product_price:
	# 				produc.old_price = produc.price
	# 				produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
	# 				# Updates the price
	# 				produc.price =product_price
	# 				# Saves the price
					
	# 				produc.save()
	# 		else:
	# 			request = requests.get(images, stream=True)
	# 			if request.status_code != requests.codes.ok:
	# 				continue
	# 			randd_ne = get_random_string(length=10)
	# 			file_name = images.split('/')[-1]
	# 			point_finder = file_name.find('.')
	# 			file_name = file_name[:point_finder] + randd_ne
	# 			lf = tempfile.NamedTemporaryFile()
	# 			for block in request.iter_content(1024*8):
	# 				if not block:
	# 					break
	# 				lf.write(block)
	# 			lf = ContentFile(httl)
	# 			product = Products(name=namelst,price=product_price,source_url=product_link,genre='men-watches',shop='jumia')
	# 			product.image.save(file_name[:20],lf)

	for urls in range(1,25):
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		       'Accept-Encoding': 'none',
		       'Accept-Language': 'en-US,en;q=0.8',
		       'Connection': 'keep-alive'}
		html = Request('https://www.jumia.com.ng/womens-watches/?page=%s'%urls,headers=hdr)
		htmll = urlopen(html).read()
		bsObj = BeautifulSoup(htmll,'html.parser')
		namelist = bsObj.findAll('div',{'class':'-gallery'})
		for news in namelist:
			product_link = news.find('a',{'class':'link'})
			product_link = product_link.attrs['href']
			image = news.find('img',{'class':'image'})
			images = image.attrs['data-src']
			product_named = news.find('h2',{'class':'title'})
			product_price = news.find('span', {'class','price'}).find_all('span')
			product_price = product_price[1]
			product_price = bytes(str(product_price.text),'UTF-8')
			product_price = product_price.decode('ascii','ignore')
			namelst = bytes(str(product_named.text), 'UTF-8')
			namelst = namelst.decode('ascii','ignore')
			htl = Request(images,headers=hdr)
			httl = urlopen(htl).read()
			print(namelst,product_price)
			if Products.objects.filter(name=namelst,shop='jumia',genre='women-watches').exists():
				
				produc = Products.objects.get(name=namelst,shop='jumia',genre='women-watches')
				# Checks the price
				if produc.price != product_price:
					produc.old_price = produc.price
					produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
					# Updates the price
					produc.price =product_price
					# Saves the price
					
					produc.save()
			else:
				request = requests.get(images, stream=True)
				if request.status_code != requests.codes.ok:
					continue
				randd_ne = get_random_string(length=10)
				file_name = images.split('/')[-1]
				point_finder = file_name.find('.')
				file_name = file_name[:point_finder] + randd_ne
				lf = tempfile.NamedTemporaryFile()
				for block in request.iter_content(1024*8):
					if not block:
						break
					lf.write(block)
				lf = ContentFile(httl)
				product = Products(name=namelst,price=product_price,source_url=product_link,genre='women-watches',shop='jumia')
				product.image.save(file_name[:20],lf)

