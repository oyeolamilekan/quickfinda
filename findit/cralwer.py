from urllib.request import urlopen,Request
from bs4 import BeautifulSoup
import re
import requests
import tempfile
from .models import Products
from django.core import files
import threading

def payporte_crawler():
	for url in range(1,26):
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		       'Accept-Encoding': 'none',
		       'Accept-Language': 'en-US,en;q=0.8',
		       'Connection': 'keep-alive'}
		html = Request('https://www.payporte.com/phones-accessories/mobile-phones-tablets/all-phones.html?p=%s'%url,headers=hdr)
		html = urlopen(html).read()
		bsObj = BeautifulSoup(html,'html.parser')
		namelist = bsObj.findAll('div',{'class':'product-card'})
		for news in namelist:
			product_name = news.find('a', {'class': 'product-image'})['style']
			image = re.findall('url\((.*?)\)', product_name)
			images = ' '.join(image)
			# Does the name and image magic
			product_named = news.find('div',{'class':'product-name'})[:299]
			# Find the price box
			price = news.find('div',{'class':'price-box'})
			# Checks if the special vlaue exists
			if price.find('span',{'class':'special-price'}) != None:
				# If it does exist it find the price
				price = price.find('span',{'class':'special-price'})
			else:
				# If does not exist it finds the original price
				price = price.find('span',{'class':'price'})

			# Finds the link
			links = news.a.attrs['href']

			# Finds the product price
			e_price = bytes(str(price.text),'UTF-8')
			e_price = e_price.decode('ascii','ignore')

			# Finds the product name
			namelst = bytes(str(product_named.text), 'UTF-8')
			namelst = namelst.decode('ascii','ignore')

			# Does the image magic
			print(namelst)
			if Products.objects.filter(name=namelst,shop='payporte').exists():
				produc = Products.objects.get(name=namelst,shop='payporte')
				# Checks the price
				if produc.price != e_price:
					# Updates the price
					produc.price = e_price
					# Saves the price
					produc.old_price = e_price
					produc.old_price_digit = int(e_price.replace(',','').replace('\n','').replace('.00',''))
					produc.save()
			else:
				request = requests.get(images, stream=True)
				if request.status_code != requests.codes.ok:
					continue
				file_name = images.split('/')[-1]
				lf = tempfile.NamedTemporaryFile()
				for block in request.iter_content(1024*8):
					if not block:
						break
					lf.write(block)
				product = Products(name=namelst,price=e_price,source_url=links,shop='payporte')
				product.image.save(file_name[:20],files.File(lf))

	for url in range(1,5):
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		       'Accept-Encoding': 'none',
		       'Accept-Language': 'en-US,en;q=0.8',
		       'Connection': 'keep-alive'}
		html = Request('https://www.payporte.com/electronics-and-gadgets/computer/laptops.html?p=%s'%url,headers=hdr)
		html = urlopen(html).read()
		bsObj = BeautifulSoup(html,'html.parser')
		namelist = bsObj.findAll('div',{'class':'product-card'})
		for news in namelist:
			product_name = news.find('a', {'class': 'product-image'})['style']
			image = re.findall('url\((.*?)\)', product_name)
			images = ' '.join(image)
			# Does the name and image magic
			product_named = news.find('div',{'class':'product-name'})[:299]
			# Find the price box
			price = news.find('div',{'class':'price-box'})
			# Checks if the special vlaue exists
			if price.find('span',{'class':'special-price'}) != None:
				# If it does exist it find the price
				price = price.find('span',{'class':'special-price'})
			else:
				# If does not exist it finds the original price
				price = price.find('span',{'class':'price'})

			# Finds the link
			links = news.a.attrs['href']

			# Finds the product price
			e_price = bytes(str(price.text),'UTF-8')
			e_price = e_price.decode('ascii','ignore')

			# Finds the product name
			namelst = bytes(str(product_named.text), 'UTF-8')
			namelst = namelst.decode('ascii','ignore')

			# Does the image magic
			print(namelst)
			if Products.objects.filter(name=namelst,shop='payporte').exists():
				produc = Products.objects.get(name=namelst,shop='payporte')
				# Checks the price
				if produc.price != e_price:
					# Updates the price
					produc.price = e_price
					# Saves the price
					produc.old_price = e_price
					produc.old_price_digit = int(e_price.replace(',','').replace('\n','').replace('.00',''))
					produc.save()
			else:
				request = requests.get(images, stream=True)
				if request.status_code != requests.codes.ok:
					continue
				file_name = images.split('/')[-1]
				lf = tempfile.NamedTemporaryFile()
				for block in request.iter_content(1024*8):
					if not block:
						break
					lf.write(block)
				product = Products(name=namelst,price=e_price,source_url=links,shop='payporte',genre='laptops')
				product.image.save(file_name[:20],files.File(lf))

	for url in range(1,27):
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		       'Accept-Encoding': 'none',
		       'Accept-Language': 'en-US,en;q=0.8',
		       'Connection': 'keep-alive'}
		html = Request('https://www.payporte.com/men/clothings/shirts.html?p=%s'%url,headers=hdr)
		html = urlopen(html).read()
		bsObj = BeautifulSoup(html,'html.parser')
		namelist = bsObj.findAll('div',{'class':'product-card'})
		for news in namelist:
			product_name = news.find('a', {'class': 'product-image'})['style']
			image = re.findall('url\((.*?)\)', product_name)
			images = ' '.join(image)
			# Does the name and image magic
			product_named = news.find('div',{'class':'product-name'})[:299]
			# Find the price box
			price = news.find('div',{'class':'price-box'})
			# Checks if the special vlaue exists
			if price.find('span',{'class':'special-price'}) != None:
				# If it does exist it find the price
				price = price.find('span',{'class':'special-price'})
			else:
				# If does not exist it finds the original price
				price = price.find('span',{'class':'price'})

			# Finds the link
			links = news.a.attrs['href']

			# Finds the product price
			e_price = bytes(str(price.text),'UTF-8')
			e_price = e_price.decode('ascii','ignore')

			# Finds the product name
			namelst = bytes(str(product_named.text), 'UTF-8')
			namelst = namelst.decode('ascii','ignore')

			# Does the image magic
			print(namelst)
			if Products.objects.filter(name=namelst,shop='payporte').exists():
				produc = Products.objects.get(name=namelst,shop='payporte')
				# Checks the price
				if produc.price != e_price:
					# Updates the price
					produc.price = e_price
					# Saves the price
					produc.old_price = e_price
					produc.old_price_digit = int(e_price.replace(',','').replace('\n','').replace('.00',''))
					produc.save()
			else:
				request = requests.get(images, stream=True)
				if request.status_code != requests.codes.ok:
					continue
				file_name = images.split('/')[-1]
				lf = tempfile.NamedTemporaryFile()
				for block in request.iter_content(1024*8):
					if not block:
						break
					lf.write(block)
				product = Products(name=namelst,price=e_price,source_url=links,shop='payporte',genre='shirts')
				product.image.save(file_name[:20],files.File(lf))
	for url in range(1,87):
		hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
		       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
		       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
		       'Accept-Encoding': 'none',
		       'Accept-Language': 'en-US,en;q=0.8',
		       'Connection': 'keep-alive'}
		html = Request('https://www.payporte.com/women/womens-clothing/dresses.html?p=%s'%url,headers=hdr)
		html = urlopen(html).read()
		bsObj = BeautifulSoup(html,'html.parser')
		namelist = bsObj.findAll('div',{'class':'product-card'})
		for news in namelist:
			product_name = news.find('a', {'class': 'product-image'})['style']
			image = re.findall('url\((.*?)\)', product_name)
			images = ' '.join(image)
			# Does the name and image magic
			product_named = news.find('div',{'class':'product-name'})[:299]
			# Find the price box
			price = news.find('div',{'class':'price-box'})
			# Checks if the special vlaue exists
			if price.find('span',{'class':'special-price'}) != None:
				# If it does exist it find the price
				price = price.find('span',{'class':'special-price'})
			else:
				# If does not exist it finds the original price
				price = price.find('span',{'class':'price'})

			# Finds the link
			links = news.a.attrs['href']

			# Finds the product price
			e_price = bytes(str(price.text),'UTF-8')
			e_price = e_price.decode('ascii','ignore')

			# Finds the product name
			namelst = bytes(str(product_named.text), 'UTF-8')
			namelst = namelst.decode('ascii','ignore')

			# Does the image magic
			if Products.objects.filter(name=namelst,shop='payporte').exists():
				produc = Products.objects.get(name=namelst,shop='payporte')
				# Checks the price
				if produc.price != e_price:
					produc.old_price = produc.price
					produc.old_price_digit = int(produc.price.replace(',','').replace('\n','').replace('.00',''))
					# Updates the price
					produc.price = e_price
					# Saves the price
					
					produc.save()
			else:
				request = requests.get(images, stream=True)
				if request.status_code != requests.codes.ok:
					continue
				file_name = images.split('/')[-1]
				lf = tempfile.NamedTemporaryFile()
				for block in request.iter_content(1024*8):
					if not block:
						break
					lf.write(block)
				product = Products(name=namelst,price=e_price,source_url=links,shop='payporte',genre='women-dresses')
				product.image.save(file_name[:20],files.File(lf))
				print(namelst,e_price)