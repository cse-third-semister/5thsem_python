room_type = input("Enter room type (Standard/Deluxe/Suite): ")
nights = int(input("Enter number of nights: "))
season = input("Enter season (Peak/Off/Normal): ")
loyalty_member = input("Loyalty member? (yes/no): ")

if room_type == "Standard":
    cost_per_night = 100
elif room_type == "Deluxe":
    cost_per_night = 150
elif room_type == "Suite":
    cost_per_night = 250

total_cost = cost_per_night * nights

if nights > 7:
    total_cost *= 0.8
elif nights > 3:
    total_cost *= 0.9

if season == "Peak":
    total_cost *= 1.2
elif season == "Off":
    total_cost *= 0.85

if loyalty_member == "yes":
    total_cost *= 0.95

print("Final booking cost:", total_cost)
