def func(month):
    if month == "february":
        print("28/29")
    elif month in ["june", "september", "april", "november"]:
        print(30)
    else:
        print(31)

month = input("Enter a month").lower()
func(month)


# Enter a month june
# 31