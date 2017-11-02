from django.shortcuts import render,redirect,get_object_or_404
from .models import Ads,Click,AdsBuy
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse,Http404
from accounts.forms import LoginForm
import datetime
from django.db.models.aggregates import Count
from .forms import AdsForm,ProdAdsForm
import datetime
from .analytics import admin_landlord
from django.contrib.auth.decorators import login_required
# Create your views here.
# Calculations of number clicks

# Home page View
def home_page(request):
	# Modal Login form
	form = LoginForm()
	# Well i think it renders it
	return render(request,'index.html',{'form':form})

def index(request):
	# Well i think it renders it
	ad_1 = AdsBuy.objects.filter(ad_owner=request.user,ad_type='Products').exists()
	return render(request,'cat_index.html',{'ad_1':ad_1})

def ad_type_detector(added_p):
	if added_p == 'Products':
		return added_p
	elif added_p == 'Banner':
		return added_p
	else:
		return ''

@login_required
# Dashboard View
def dash(request):
	#######################################################
	section = request.GET.get('type',None)
	sector = ad_type_detector(section)

	# get the get ad belonging to a user
	ad_1 = Ads.objects.filter(ad_owner=request.user,ad_type=sector).exists()
	# Checks if the user has bought any ads
	
	ad_credit = AdsBuy.objects.filter(ad_owner=request.user,ad_type=sector).exists()

	time_remaining = None
	# Confirms the boolean statement for the above code
	if ad_1:
		# Gets the ads belonging to that particular user
		ad_1 = Ads.objects.get(ad_owner=request.user,ad_type=sector)
		time_remaining = admin_landlord(request,ad_1)
	# Checks if the user has ad credit
	if ad_credit:
		# Gets the credit belonging to that particular user
		ad_credit = AdsBuy.objects.get(ad_owner=request.user,ad_type=sector)

	# Renders the queries to the html page ;)
	return render(request,'home.html',{'ad':ad_1,
			'ad_credit':ad_credit,
			'type':sector,
			'time_remaining':time_remaining})

@login_required
# Validates the user account after payment
def payment_val(request):
	section = request.GET.get('type',None)
	sector = ad_type_detector(section)
	# Gets the boolean token from ajax 
	bool_me = request.GET.get('confirm',None)

	# Gets the reference number from ajax
	ref_number = request.GET.get('ref_num',None)

	# Approves or gives the user ad credit
	ad_credit = AdsBuy.objects.create(ad_owner=request.user,as_ad_credit=True,ad_type=sector)

	# Saves the token for later validation of transaction
	ad_credit.save()

	# Just to lazy to write a JsonResponse
	return HttpResponse('hi')

@login_required
# Validates the user account after payment
def reactivate_payment_val(request):
	section = request.GET.get('type',None)
	sector = ad_type_detector(section)
	# Gets the boolean token from ajax 
	bool_me = request.GET.get('confirm',None)

	# Gets the reference number from ajax
	ref_number = request.GET.get('ref_num',None)

	# Approves or gives the user ad credit
	ad_credit = Ads.objects.get(ad_owner=request.user,ad_type=sector)

	# Add todays date to the date added
	ad_credit.date_adder = datetime.datetime.today().strftime('%Y-%m-%d')

	# Change the experation to false
	ad_credit.expired = 'False'

	# Saves the token for later validation of transaction
	ad_credit.save()

	# Just to lazy to write a JsonResponse
	return HttpResponse('hi')

@login_required
# Handles the image upload
def upload_ads(request):
	# Checks if the user has bought an ad
	section = request.GET.get('type',None)
	sector = ad_type_detector(section)

	ad_1 = AdsBuy.objects.filter(ad_owner=request.user,ad_type=sector).exists()

	# Value to give template if the user has not bought any ads
	ade = None

	time_remaining = None

	# If the user has bought an ad
	if ad_1:

		# Checks if the user has uploaded there banner
		ade = Ads.objects.filter(ad_owner=request.user,ad_type=sector).exists()
		
		# IF the ads exist in the database 
		if ade:

			# Get the owner 
			ade = Ads.objects.get(ad_owner=request.user,ad_type=sector)

			# Calculates the time remaining to run ads
			time_remaining = admin_landlord(request,ade)

	# If the request sending to the server is post show them the banner form
	if request.method != 'POST':
		if sector == 'Banner':
			form = AdsForm()
		else:
			form = ProdAdsForm()

	# Else save the banner the to the server 
	else:
		if sector == 'Banner':
		# Accept the data being sent
			form = AdsForm(request.POST,request.FILES or None)
		else:
			form = ProdAdsForm(request.POST,request.FILES or None)

		# Check if the form is valid
		if form.is_valid():

			# Don't save yet
			new_form = form.save(commit=False)

			# Add the creator of the add
			new_form.ad_owner = request.user

			# The days the ad is supposed to spend on the web site
			new_form.time_wait = '7'

			new_form.ad_type = sector
			print(sector)
			# Save the data
			new_form.save()

		# Redirect to the preview page
		return redirect('/adengine/ads_upload/'+'?type=%s'%sector)
	context = {'form':form,
				'ad_1':ad_1,
				'type':sector,
				'ade':ade,
				'time_remaining':time_remaining}
	return render(request,'ads_upload.html',context)

@login_required
# It's loaded data for particular ad
def loaded(request):
	# Gets the user ads
	section = request.GET.get('type',None)
	sector = ad_type_detector(section)
	ad_1 = Ads.objects.filter(ad_owner=request.user,ad_type=sector).exists()

	# if it exists
	if ad_1:

		# Get the ad
		ad_1 = Ads.objects.get(ad_owner=request.user,ad_type=sector)

		# Get the views
		items = ad_1.view_set.extra({'date_added':"date(date_added)"}).values('date_added').annotate(date_added_count=Count('id'))
		
		# Get the clicks
		items_2 = ad_1.click_set.extra({'date_added':"date(date_added)"}).values('date_added').annotate(date_added_count=Count('id')) 
		
		# Create an empty list to contain the view
		data_set = []

		# Create an empty list to contain the clicks
		data_set_2 = []

		# Create an empty list to contain the days the ads has been running
		days = []

		# Loop through the Views list
		for item in items:

			# Append each view item to the data set list
			data_set.append(item['date_added_count'])

			# Append each days the ads has being running
			days.append(datetime.datetime.strptime(item['date_added'], '%Y-%m-%d').strftime('%a'))
		# Loop through the click list
		for item in items_2:

			# Append each click item to the data set list
			data_set_2.append(item['date_added_count'])

		# Return a Json response to the ajax server
		return JsonResponse({'data_set':data_set,'data_set_2':data_set_2,'days':days})

	# Return the Httpresonse inother not crash(i am lazy)
	return HttpResponse('nothing')

@login_required
def edit_ads(request,id):
	# Gets the ad supposed to be edited
	section = request.GET.get('type',None)
	sector = ad_type_detector(section)
	ads = get_object_or_404(Ads,id=id)

	# Gets the title
	ads_title = ads.title

	# Compares if user is the owner of the ads
	if ads.ad_owner != request.user:

		# If not raise a 404 error
		raise Http404

	# If the user request the edit form
	if request.method != 'POST':

		# Display the edit form to the user
		if sector == 'Banner':

			form = AdsForm(instance=ads)
		else:
			form = ProdAdsForm(instance=ads)
	# If the user is Submiting the form
	else:

		# Process the form data being saved
		if sector == 'Banners':
			form = AdsForm(instance=ads,data=request.POST,files=request.FILES)
		else:
			form = ProdAdsForm(instance=ads,data=request.POST,files=request.FILES)

		# Check if the form is valid
		if form.is_valid():

			# If the form is valid save it
			form.save()

			# Redirect the user back to the Complete page
			return redirect('/adengine/ads_upload/?type='+sector)
	# Display the form 
	context = {'form':form,'type':sector,'ads':ads}

	# Return and render the form
	return render(request,'edit_ads.html',context)

# Calculates the analytics
def click_by(request,ads):

	# Get the ads being clicked
	ad = Ads.objects.get(id=int(ads))

	# Add 1 to the click counter
	ad.clicks = ad.clicks + 1

	# Crete a click object for daily referal
	ad_me = Click.objects.create(ads=ad,click_cal='c')

	# Save the click object
	ad_me.save()

	# Save the ad counter
	ad.save()

	# Redirect them to the ad website
	return redirect('http://'+ad.website)
