# Task 1 Midrand speedster

your_speed = int(input("What was your average speed in km/h: "))
average_speed: int = int(input("What was the speed limit: "))
diff = your_speed - average_speed

if your_speed <= average_speed:
    print("OK!")
else:
    point = diff/5
    point =int(point)
    print(point)
    if point > 12:
        print("Time to go to jail!!")
