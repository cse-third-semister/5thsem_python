"""
 Create a program that reads duration from the user as a number of days, hours, minutes, and seconds.
 Compute and display the total number of seconds represented by this duration
"""


days = int(input("Enter the number of days: "))
hours = int(input("Enter the number of hours: "))
minutes = int(input("Enter the number of minutes: "))
seconds = int(input("Enter the number of seconds: "))


total_seconds = (days * 24 * 60 * 60) + (hours * 60 * 60) + (minutes * 60) + seconds


print(f"The total duration in seconds is: {total_seconds}")


# Enter the number of days: 2
# Enter the number of hours: 3
# Enter the number of minutes: 1
# Enter the number of seconds: 1
# The total duration in seconds is: 183661