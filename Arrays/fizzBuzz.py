"""
FizzBuzz:
Write a program that outputs the string representation of numbers from 1 to n.
But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”.
For numbers which are multiples of both three and five output “FizzBuzz”.

"""

def fizzBuzz(self, n):
    results = []
    for num in range(1, n + 1):
        if num % 3 == 0 and num % 5 == 0:
            results.append('FizzBuzz')
        elif num % 5 == 0:
            results.append('Buzz')
        elif num % 3 == 0:
            results.append('Fizz')
        else:
            results.append(str(num))
    return results
