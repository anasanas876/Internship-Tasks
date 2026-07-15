# Task 4
import time
print("Starting the program")
def start_timer():
  seconds = int(input("Enter reminder interval (seconds): "))
  while True:
   time.sleep(seconds)
   print("Walk 20 steps after 5 minutes each")
if __name__=="__main__":
  start_timer()
