#  File: Triangle.py

#  Description: Applies four different approaches to find the max sum given a triangle of numbers

#  Student's Name: Rakshana Govindarajan

#  Student's UT EID: rg38236	

#  Course Name: CS 313E 

#  Unique Number: 50945

#  Date Created: 15 April 2016

#  Date Last Modified: 16 April 2016




# returns the greatest path sum using exhaustive search
def exhaustive_search (grid):
  triangle = grid
  possible_paths = []

  for decisions in product((0,1), repeat = len(triangle) - 1):
    pos = 0
    path = [triangle[0][0]]
    for lr, row in zip(decisions, triangle[1:]):
      pos += lr
      path.append(row[pos])
    possible_paths.append(path)

  possible_sums = []
  sum = 0
  for i in range(len(possible_paths)):
    for j in range(len(possible_paths[i])):
      sum += possible_paths[i][j]
    possible_sums.append(sum)
    sum = 0

  max_sum = max(possible_sums)
  return max_sum   
        
  

    
      

# returns the greatest path sum using greedy approach
def greedy (grid):
  m = 0
  sum = grid[0][m]
  for i in range(1, len(grid)):
    # Checking the adjacent two numbers in the next row
    x = grid[i][m]
    y = grid[i][m + 1]
   
    # If number in the same position is the greater of the two, then add to sum
    if(x >= y):
      sum += x
    # If number in the position next to it is the greater of the two, then add to sum
    elif(x < y):
      sum += y
      m = m + 1

  return(sum)

# returns the greatest path sum using divide and conquer (recursive) approach
def rec_search (grid):
 
  # Finding the length of the grid
  n = len(grid)

  # Starting with the second row of the triangle (first row is base case) and working up
  for i in reversed(range(n - 1)):
    # For each number in the row, checking the two sub triangles and comparing the sum to see which is greater
    # Then adding it to the starting number
    for j in range(len(grid[i])):
      grid[i][j] += max(grid[i + 1][j], grid[i + 1][j + 1])

  # Coming to the top, the top most number will be added to the sub triangle with the greatest sum
  return(grid[0][0])



# returns the greatest path sum using dynamic programming
def dynamic_prog (grid):
  # Creating an empty list to store the partial sums along the way
  m = []
  
  # Finding the length of the grid to calculate length of loop
  bounds = len(grid)
  n = -1 * bounds
  
  # Going from the bottom to the top of the triangle
  for j in range(-1, n, -1):
    
    for i in range(len(grid[j]) - 1):
      x = grid[j][i] + grid[j - 1][i]
      y = grid[j][i + 1] + grid[j - 1][i]

      # Comparing the partial sums x and y and appending the greater of the two to the list m
      if(x >= y):
        
        m.append(x)
     
      
      elif(x < y):
        
        m.append(y)

    # Replacing the row above with the new partial sums calculated
    for k in range(len(grid[j - 1])):
      grid[j - 1][k] = m[k]
    # Emptying out the list m
    m = []
      
  # The greatest sum is now at the top of the triangle
  sum = grid[0][0]
  return sum

    




# reads the file and returns a 2-D list that represents the triangle
def readFile ():
  in_file = open("triangle.txt", "r")
  num_rows = in_file.readline()
  num_rows = num_rows.split()
  num_rows = int(num_rows[0])

  triangle = []
  for i in range(num_rows):
    line = in_file.readline()
    
    line = line.rstrip("\n")
    line = line.split()
    numbers = [int(n) for n in line]
    triangle.append(numbers)

  return(triangle)


from itertools import product

def main ():
  # read triangular grid from file
  grid = readFile()
  #print(grid)

  # output greatest path from exhaustive search
  exhaustive_sum = exhaustive_search(grid)
  print("The greatest path sum through exhaustive search is " + str(exhaustive_sum) + ".")

  # output greatest path from greedy approach
  greedy_sum = greedy(grid)
  print("The greatest path sum through greedy search is " + str(greedy_sum) + ".")

  # output greatest path from divide-and-conquer approach
  divcon_sum = rec_search(grid)
  print("The greatest path sum through recursive search is " + str(divcon_sum) + ".")

  # output greatest path from dynamic programming
  grid2 = readFile()
  dynamic_sum = dynamic_prog(grid2)
  print("The greatest path sum through dynamic programming is " + str(dynamic_sum) + ".")

main()