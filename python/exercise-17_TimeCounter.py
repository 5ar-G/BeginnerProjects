import time

def counter(end, start= 0):
    for x in range(start, end+1):
        print(x)
        time.sleep(1)
    print("Done!")

end= int(input("Enter the number of seconds: "))
counter(end)


    