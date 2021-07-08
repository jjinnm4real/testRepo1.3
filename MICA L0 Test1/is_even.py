import sys, time

def is_even(num):
    if (num % 2) == 0:
        return True
    else:
        return False

if __name__ == "__main__":
    # parse the first argument as number
    num = int(sys.argv[1])

    # look for 2nd argument as seconds (default to 10)
    try:
        seconds = int(sys.argv[2])
    except:
        seconds = 10

    # sleep for {seconds}
    print(f"waiting {seconds} seconds")
    time.sleep(seconds)
    
    # pass or fail if even or odd
    if is_even(num):
        print(f"{num} is even: ")
        print(True)
        exit(0) #pass (even)
    else:
        print(f"{num} is even: ")
        print(False)
        exit(1) #fail (odd)
