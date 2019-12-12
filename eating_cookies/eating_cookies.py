#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n):
  cache=[1, 1, 2]
  if n == 0:
      return cache[0]
  if n == 1:
      return cache[1]
  if n == 2:
      return cache[2]
  if n == 3:
      return sum(cache)

  for i in range(3, n):
      cache.append(sum(cache))
      del cache[0]
  
  return sum(cache)


  

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')