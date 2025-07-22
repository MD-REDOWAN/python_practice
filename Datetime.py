

# Python Dates
# A date in pythob is not a data type of its own, byt we can import named datetime to work with date as date objects


import datetime

x = datetime.datetime.now()
print(x)
print(x.year)

# Output: 2025-07-22 11:25:13.138388
# Output : 2025


# Creating date objects


import datetime

y = datetime.datetime(2002,7,12)
print(y)

# Output: 2020-05-17 00:00:00


# The strftime() Method

import datetime

z = datetime.datetime(2002,7,12)
print(z.strftime("%B"))

# Output: July

# There are so much %B this type of legal formate . Cann we follow w3 school


