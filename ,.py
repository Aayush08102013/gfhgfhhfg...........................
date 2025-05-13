import calendar
y = 1

# Using calendar.month_name
print("All months of the year:")
for month in range(1, 13):
    print(f"{y}.", calendar.month_name[month])
    y += 1