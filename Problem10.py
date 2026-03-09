#Problem10.py
#Project Euler Problem 10
#Approach Description: I altered the getPrimeFactors function I had made to output all the prime numbers instead of just prime /
#factors and then added all of those numbers together. 
#Runtime Notes: Program outputs sum for prime numbers lower than 2,000,000 in about a minute. 

from NumberTests import getPrimeSum

def main():
  number = 2000000
  primeSum = getPrimeSum(number)
  print("The sum of all prime numbers lower than", number, "is", primeSum)

if __name__ == '__main__':
  main()