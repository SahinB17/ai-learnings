n = int(input("Enter the amount of numbers :"))
numbers = []
def fizzbuzz(n):
    for i in range(1,n+1) :
        if i % 15 == 0:
            numbers.append("FizzBuzz")
        elif i % 3 == 0:
            numbers.append("Fizz")
        elif i % 5 == 0:
            numbers.append("Buzz")
        else :
            numbers.append(str(i))
    return numbers
        
fizzbuzz(n)
print(numbers)



