import re

txt = 'S@nd!wara419'

x = re.search("(^\D)(?=.*[a-zA-Z])(?=.*[0-9])(\D{2})(?=[@$!%*#?&])[A-Za-z\d@$!#%*?&]{8,32}$", txt)

if x :
	print('yes')
else :
	print('No')
