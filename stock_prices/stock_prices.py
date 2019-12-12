#!/usr/bin/python

import argparse


def find_max_profit(prices):
  prices.reverse()
  i = 0
  profit = None
  while i < len(prices) - 1:
    for j in prices[i+1:]:
      if profit == None:
        profit = prices[i] - j
      else:
        profit = max(profit, prices[i] - j)
    i += 1
    
  return profit


if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
