a = str(input("Enter time (24-hours format): "))
hour = int(a[:2])
minute = int(a[3:])
ap = "pm"
if hour == 12:
    ap = "pm"
elif hour == 0:
    ap = "am"
    hour = 12
elif hour>12:
    ap = "pm"
    hour = hour - 12
elif 0 < hour < 12:
    ap = "am"

print(f'Time in 12-hour format: {hour}:{minute}{ap}')

