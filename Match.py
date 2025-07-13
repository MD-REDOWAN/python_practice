

# The match statements is used to perorm different acttions based on different conditons

# Many if..else statements, you can use the match statement.

# The match expressin is evaluated once
# The value of the expressin is compared with the valurs each case
# If therre sis a match , the associated block of code is executed

# example:

Off_day = 7
match Off_day:
    case 1:
        print("Staturday")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case 4:
        print("Tuesday")
    case 5:
        print("Wednesday")
    case 6:
        print("Thursday")
    case 7:
        print("Friday")
    
# Output: 'Friday'


# Default Value
# Use the underscore character _ as the last case value if you want a code block to execute when there are not other matches:

Off_day = 7
match Off_day:
    case 1:
        print("Staturday")
    case 2:
        print("Sunday")
    case 3:
        print("Monday")
    case 4:
        print("Tuesday")
    case 5:
        print("Wednesday")
    case 6:
        print("Thursday")
    case _:
        print("Friday")


# Combine Values

# Use the pipe character | as an or operatoe in the case evaluation to check for more than one value match in one case:

day = 3
match day:
    case 1| 2| 3| 4| 5:
        print("today is Monday")
day = 7
match day:
    case 4 | 5 | 6 | 7:
        print("To day is weekends")



# If Statements as Guards:
# You can add if statements in the case evaluation as an extra condition-check

day = 12
month = 7
match day:
    case 7|8|9|10|11|12|13 if month == 7:
        print("This is my birthday")
    case 1|2|3|4|5|6|7|8 if month != 7:
        print("It's not my birthday")


