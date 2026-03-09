#NumberTests.py

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False

def getFactors(num):
  """Returns a list of all factors of a given integer"""
  factors = []
  for f in range(1, num//2):
    if num % f == 0: 
      factors.append(f)
  return factors 

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  if p == 2: 
    return True 
  if isEven(p):
    return False
  for div in range(3, int(p ** 0.5) + 1): 
    """Calculates square root and accounts for rounding of integer."""
    if p % div == 0:
      return False 
  return True

def getPrimeFactors(num):
  factors = getFactors(num) 
  primeFactors = []
  """Stores prime factors in an array"""
  for factor in factors: 
    if isPrime(factor):
        primeFactors.append(factor)
        """Appends prime factors to list in array"""

  return primeFactors 

def getPrimeSum(num): 
  primeSum = 0
  """Prime variable"""
  for prime in range(2,num): 
    if isPrime(prime):
      primeSum += prime 
        # primes.append(prime)
      """Sums prime numbers below input number"""
  return primeSum

def prime_factorization(num):
  factor = 2
  while factor * factor <= num:
    while num % factor == 0:
      num //= factor
    factor += 1
  
  if num > 1:
    return num
  else:
    return None


def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums

#Test your new functions in this main
def main():
  knownPrimes = [3, 7, 11, 13, 17]

  num = int(input("Enter a number: "))

  if isPrime(num):
    print("%d is a prime number" %(num))

  if isEven(num):
    print("%d is an even number" %(num))


if __name__ == '__main__':
    main()
