print("Enter the time and convert it to seconds")
print("Please enter your desired time: ")
hour = int(input('enter your hour:'))
minute = int(input('enter your minute:'))
second = int(input('enter your second:'))
sec = hour*3600 + minute*60 + second
print('seconds = ', sec)