#!/usr/bin/env python

from __future__ import division
import argparse
import heapq

"""
===============================================================================
  Please complete the following function.
===============================================================================
"""
def run_tests(): 
  for i in range(1, 22): 
    filename = "project_instances/problem" + str(i) + ".in"
    tup = read_input(filename)
    items_chosen = solve(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5])
    write_output("out/problem" + str(i) + ".out", items_chosen)
def run(filename): 
  tup = read_input(filename)
  return solve(tup[0], tup[1], tup[2], tup[3], tup[4], tup[5])
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
        constr[item_class] = []
      for other_class in s: 
        if other_class != item_class and other_class not in constr[item_class]:
          constr[item_class].append(other_class)
  # for k, v in constr.items(): 
  #   print(k, v)
  def violates_constraint(current_sack, item):
    if len(constr) == 0 or item[1] not in constr: 
      return False
    else: 
      for i in current_sack: 
        if i[1] in constr: 
          if item[1] in constr[i[1]]: 
            return True
      return False 
  def total_resale_val(current_sack): 
    total = 0
    for i in range(0, len(current_sack)): 
      total += current_sack[i][4]
    return total

  pq = []
  current_sack = []
  weight = P
  money = M
  for item in items: 
    # heapq.heappush(pq, (priority(current_sack, item, money), item))
    pq.append(item)
  pq = sorted(pq, key = lambda item: item[4] - item[3], reverse = True)
  while len(pq) > 0: 
    next_item = pq.pop(0)
    if next_item[2] < weight and next_item[3] < money and violates_constraint(current_sack, next_item) == False: 
      current_sack.append(next_item)
      weight = weight - next_item[2]
      money = money - next_item[3]
    #update the pq by creating a new one 
    # new_pq = []
    # for i in range(0, len(pq)): 
    #   item = heapq.heappop(pq)[1]
    #   heapq.heappush(new_pq, (priority(current_sack, item, money), item))
    # pq = new_pq

  print(money + total_resale_val(current_sack))
  ans = []
  for item in current_sack: 
    ans.append(item[0])
  return ans

  # def priority(current_sack, item, money): 
  #   return -(item[4] - item[3])
  #   # return -(total_resale_val(current_sack) + money + item[4] - item[3])
  # def compare_priotiry(item1, item2): 
  #   if (item1[4] - item1[3]) > (item1[4] - item1[3]): 
  #     return 1
  #   elif (item1[4] - item1[3]) == (item1[4] - item1[3]): 
  #     return 0
  #   else: 
  #     return -1 
  # def total_cost(current_sack): 
  #   total = 0
  #   for i in range(0, len(current_sack)): 
  #     total += current_sack[i][3]
  #   return total
  # def bound_zero(num): 
  #   if num < 0: 
  #     return int(0)
  #   else: 
  #     return int(num) 
  """DP ALGORITHM""" 
  # table = []
  # #table values look like(total resale val of sack + leftover money, list of items in the sack)
  # for i in range(0, int(N + 1)): 
  #   table.append([])
  #   for j in range(0, int(P + 1)): 
  #     table[i].append([])
  #     for k in range(0, int(M + 1)): 
  #       table[i][j].append((0, []))
  # max_val = (float('-inf'), [])
  # for i in range(1, int(N + 1)): #num items 
  #   for j in range(1, int(P + 1)): #weight capacity
  #     for k in range(1, int(M + 1)): #how much money
  #       if items[i - 1][2] > j or items[i - 1][3] > k:  
  #         table[i][j][k] = table[i - 1][j][k]
  #       else: 
  #         if table[bound_zero(i - 1)][j][k][0] > table[i][bound_zero(j - items[i- 1][2])][bound_zero(k - items[i - 1][3])][0] + items[i - 1][4]: 
  #           table[i][j][k] = table[i - 1][j][k]
  #         elif violates_constraint(table[i - 1][j][k][1], items[i - 1]) == False: 
  #           updated_sack = table[i - 1][j][k][1][:]
  #           updated_sack.append(items[i - 1]) 
  #           table[i][j][k] = (total_resale_val(updated_sack) - total_cost(updated_sack) + k, updated_sack)
  #       if table[i][j][k][0] > max_val[0]:
  #         max_val = table[i][j][k]
  
  # ans = []
  # for i in range(1, int(N + 1)): #num items 
  #   for j in range(1, int(P + 1)): 
  #     for k in range(1, int(M + 1)):  
  # for i in range(0, len(max_val[1])): 
  #   ans.append(max_val[1][i][0])
  # print(max_val[0])
  # return ans
  # print("done")
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
