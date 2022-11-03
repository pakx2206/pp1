import time
def countdown(time_sec):
    while time_sec:

        mins, secs = divmod(time_sec, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        time.sleep(1)
        time_sec -= 1
pin = "0805"
proby = 3
pr = 2
while proby > 0:
        x = input("Enter the PIN code:")
        if x == pin:
            print("Correct!")
            break
        elif x != pin:
            print("Incorrect...")
            proby -= 1
            if proby == 0:
                print("Sorry, your payment card has been blocked.")
                countdown(15*pr)
                pr=pr**2 
                accept = input("Do want to try again? (Write yes or no):")
                if accept=="yes": proby=3
                else: break

