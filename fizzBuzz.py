#fizz buzz game with upper range hard coded for n
n=200

for j in range (1,n):
    if j%3==0 and j%5==0:
        print("FizzBuzz")
    elif j%3==0:
        print("Fizz")
    elif j%5==0:
        print("Buzz")
    else:
        print(j)

#FizzBuzz game with user entering upper range
max_number= input("Enter maximum number to count up to:")

for j in range (1,max_number):
    if j%3==0 and j%5==0:
        print("FizzBuzz")
    elif j%3==0:
        print("Fizz")
    elif j%5==0:
        print("Buzz")
    else:
        print(j)