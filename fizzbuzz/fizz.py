start = 1
while(start <= 30):
    print(start)
    start = start + 1
    if start % 3 == 0:
        print(f"{start} fizz")
    elif start % 5 == 0:
        print(f"{start} Buzz")    
    if (start % 3 == 0 and start % 5 == 0):    
        print(f"{start} Fizzbuzz")