#!/usr/bin/env python

from __future__ import division
import argparse


"""
===============================================================================
  Please complete the following function.
===============================================================================
"""

def solve(P, M, N, C, items, constraints):
  """
  Write your amazing algorithm here.

  Return: a list of strings, corresponding to item names.
  """
  # item = (name, class, weight, cost, resale_val)
  constr = {}
  #constr = {item_class: incompatible classes to it}
  for s in constraints:
    for item_class in s: 
      if item_class not in constr: 
        constr[item_class] = set()
      for other_class in s: 
        if other_class != s and other_class not in constr[item_class]:
          constr[item_class].add(other_class)
  def violates_constraint(current_sack, item):
    for i in current_sack: 
      if item[1] in constr[i[1]]: 
        return True
    return False 

  def total_resale_val(current_sack): 
    total = 0
    for i in range(0, len(current_sack)): 
      total += current_sack[i][4]
    return total
  def bound_zero(num): 
    if num < 0: 
      return 0 
    else: 
      return num 

  table = []
  for i in range(0, N + 1): 
    table.append([])
    for j in range(0, P + 1): 
      table[i].append[[]]
      for k in range(0, M + 1): 
        table[i][j].append((0, []))

  for i in range(1, N + 1): #num items 
    for j in range(1, P + 1): #weight capacity
      for k in range(1, M + 1): #how much money
        if items[i][2] > j or items[i][3] > k:  #
          table[i][j][k] = (total_resale_val(current_sack) + k, current_sack[:])
        else: 
          if table[bound_zero(i - 1)][j][k][0] > table[i][bound_zero(j - items[i][2])][bound_zero(k - item[i][3])] + item[i][4]: 
            table[i][j][k] = (total_resale_val(current_sack) + k, current_sack[:])
          elif violates_constraint(current_sack, items[i]) == False: 
            updated_sack = current_sack[:]
            updated_sack.append(items[i][0])
            table[i][j][k] = (total_resale_val(updated_sack) + k, updated_sack)
  max_val = (float('-inf'), [])
  for i in range(1, N + 1): #num items 
    for j in range(1, P + 1): 
      for k in range(1, M + 1): 
        if table[i][j][k][0] > max_val[0]:
          max_val = table[i][j][k]
  return max_val[1]

  #table values look like (total resale of sack + leftover cash, current_sack)

  # def k(p, m, current_sack, remaining_items): 
  #   if p <= 0 or m <= 0: 
  #     return 0
  #   elif violates_constraint(current_sack, remaining_items[0]) == False: 
  #     if remaining_items[0][2] > p: 
  #       return k(p, m, current_sack, remaining_items[1:])
  #     else: 
  #       return max(k())
  


"""
===============================================================================
  No need to change any code below this line.
===============================================================================
"""

def read_input(filename):
  """
  P: float
  M: float
  N: integer
  C: integer
  items: list of tuples
  constraints: list of sets
  """
  with open(filename) as f:
    P = float(f.readline())
    M = float(f.readline())
    N = int(f.readline())
    C = int(f.readline())
    items = []
    constraints = []
    for i in range(N):
      name, cls, weight, cost, val = f.readline().split(";")
      items.append((name, int(cls), float(weight), float(cost), float(val)))
    for i in range(C):
      constraint = set(eval(f.readline()))
      constraints.append(constraint)
  return P, M, N, C, items, constraints

def write_output(filename, items_chosen):
  with open(filename, "w") as f:
    for i in items_chosen:
      f.write("{0}\n".format(i))

if __name__ == "__main__":

  parser = argparse.ArgumentParser(description="PickItems solver.")
  parser.add_argument("input_file", type=str, help="____.in")
  parser.add_argument("output_file", type=str, help="____.out")
  args = parser.parse_args()

  P, M, N, C, items, constraints = read_input(args.input_file)
  items_chosen = solve(P, M, N, C, items, constraints)
  write_output(args.output_file, items_chosen)
