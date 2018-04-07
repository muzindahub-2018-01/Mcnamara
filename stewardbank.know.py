#make a list that can hold on to your items
banking_services =[]
def show_help():
	#print a  set of instruction on how to use the app
	print("Welcome to STEWARD BANK Agent anking")
	print("What would you like to know")
	print("""
Enter 'DONE' to stop adding items.
Enter 'HELP' for this help.
Enter 'SHOW' to see your current list.
Enter 'KWENGA' for kwenga application requirements
Enter 'iSave' for iSave requirements
Enter 'VISA' for VISA requirements
Enter 'BRANCH' for nearest Harare branch
""")

def show_list():	
	#print out your list    
	print("Contact customer services on 0772191191 or email customer.service@stewardbak.co.zw: ")
	
	for item in banking_services:
		print(item)
		
def show_kwenga():
	#print out kwenga requirements
	print("""
	Thank you for your interest in our Kwenga device!Bring:
	copy of id
	proof of residence bill with 3 months
	two colored passport photo
	or valid trading licence
	duly completed merchant application form
	duly completed kwenga contact form
	""")
def show_visa():
    #print out visa requirement
	print("""
	Thank you for your interest in our Globetrotter Account!Bring:
	upto 3000 USD a month
	$10
	copy of ID
	upto 10000 USD a month
	plus
	proof of residence bill within 3 month
	colored passport photo
	""")
def show_branch():
	print("""
	Eastgate
	Avodale
	Joina City
	LIvingstone
	Chisipiti
	Borrowdale
	Airport
	First Street
	Chitepo
	""")

def show_queeries():
	queery =[
	"lost card",
	"new pin",
	"missing credit",
	"Failed POS but account was debited", 
	"duplicate transaction",
	"missing charges",
	"missing commissions",
	"ecocash banking services",
	"mobile app",
	"ussd baking",
	"sms alerts",
	]
	for item in queeries:
		try:
			queeries.append(new_item)
			if new items == po
	
	
def add_to_list(new_item):
	#add new items to your list
	banking_services.append(new_item)
	print("Added {}. List now has {} items.".format(new_item, len(banking_services)))
		
show_help()


while True:
	#ask for new items
		new_item = input("< ")
		
		if new_item == 'HELP':
			show_help()
			continue
		elif new_item == 'KWENGA':
			show_kwenga()
			continue
		elif new_item =='VISA':
			show_visa()
			continue
		elif new_item =='BRANCH':
			show_branch()
			continue
		elif new_item == 'QUERRIES':
			show_querries()
			continue
		elif new_item == 'SHOW':
			show_list()
			continue
		add_to_list(new_item)	

#be able to quit the app
else:
		#format querries and direct to relevant department or at leas guide customrer giv e contact umbers
		print("Contact customer services on 0772191191 or email customer.service@stewardbak.co.zw!"
		print("Your queery is {}".queeries.append(new_item))
	play_again = input("Do you want to play again? Y/n ")
	if game.lower() != n:
		game()
	else:
		print("bye!")

		
show_kwenga()

show_visa()

show_branch()

show_list()

