from datetime import date
from .models import Ads,View
# Checks the ads expiry date and deletes it if it has expired
def landlord(request,ads):
	# Checks todays date
	today = date.today()
	
	# Loops over the queryset
	for ad in ads:
		
		# Calculate the days btw
		time_notice = today - ad.date_adder
		
		print(ad.date_adder,ad,time_notice)
		# If the days btw is greater than the allocated time
		if time_notice.days >= int(ad.time_wait):
			
			# Stop the ad
			ad.expired = 'True'

			# Save to the database
			ad.save()

# For the user ad owner
def admin_landlord(request,ad):
	# Checks todays date
	today = date.today()
	
	# Calculate the days btw
	time_notice = today - ad.date_adder

	# Day remaining
	days = int(ad.time_wait) - time_notice.days
	
	# If the days btw is greater than the allocated time
	if time_notice.days >= int(ad.time_wait):
		
		# Stop the ad
		ad.expired = 'True'

		# Save to the database
		ad.save()

	return days

# Calculates the number of users that saw it
def seen_by(request,ads):
	# Lops over the ads
	for ad in ads:
		# Gets the one that is currently being seen
		adsee = Ads.objects.get(id=ad.id)
		# Increments the ads views
		ad.views = ad.views + 1
		# Creates a view object for date analytics
		ad_me = View.objects.create(ads=adsee,views_cal='v')
		# Saves the view object being created 
		ad_me.save()
		# Saves th
		ad.save()