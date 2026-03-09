#Problem3.py
#Project Euler Problem 3
#Approach Description: Instead of calling the getFactors and the getPrimeFactors functions, /
#I used a prime_factorization function to directly find and outputs the largest prime factor /
#by checking every number it is divisible by to see if it is a prime factor. 
#Runtime Notes: My program efficiently runs and quickly outputs an answer. 

from NumberTests import *
#from NumberTests import getFactors 
# * grabs everything from NumberTests

def main():
  number = 600851475143
  #primeFactors = getPrimeFactors(number)
#   print(primeFactors)
  #largestPrimeFactor = max(primeFactors)
  largestPrimeFactor = prime_factorization(number)
  """outputs only the largest prime factor"""
  print("The largest prime factor of", number, "is", largestPrimeFactor)

if __name__ == '__main__':
  main()