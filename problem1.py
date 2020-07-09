import re


Input_str = "With the recent uptick to the COVID-19 positive cases and many states in various phases of restarting the economy; the food service industry and the restaurant sector have been strongly impacted. DMS Coalition is proud to announce the Facemasks For Restaurants Donation Initiative with a target of $2M in donation."
validat = ["food", "face", "the", "donation", "coalition", "economy", "sector"]

new_input = Input_str.lower()

pattern= r'[a-zA-Z]+'
match= re.findall(pattern,new_input)


print("This is the input list : ", match)

print(validat)

def check(i):
	

	for i in validat:
		
		y=match.count(i)
		print("{} : {}".format(i,y))
		



check(match)





