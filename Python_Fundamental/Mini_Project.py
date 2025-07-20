# Project 1: Travel Suggestion based on distance

distance = float(input("How far would you like to travel in miles? "))

if distance < 3:
    print("I suggest Bicycle to your destination.")
elif distance < 300:
    print("I suggest Motor-Cycle to your destination.")
else:
    print("I suggest Super-Car to your destination.")



# Project 2: Cloud Server Cost Calculation

cost_per_hour = 0.51


cost_per_day = cost_per_hour * 24
cost_per_week = cost_per_day * 7
cost_per_month = cost_per_day * 30 
budget = 918
days_possible = budget / cost_per_day

print("Cost to operate one server:")
print(f"- Per Day   : ${cost_per_day:.2f}")
print(f"- Per Week  : ${cost_per_week:.2f}")
print(f"- Per Month : ${cost_per_month:.2f}")
print(f"\nWith ${budget}, you can run one server for about {days_possible:.2f} days.")
