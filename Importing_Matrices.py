# Load Data into a Matrix, Patrick Honner 10/1/2022
# Simple example of reading a csv file in and converting to a list of lists


# Import the csv module for handling data
import csv

# This reads in the comma separated values as a list of lists of strings
#                                               Each line is a list

with open("matrix.txt") as f:
  reader = csv.reader(f)
  d = list(reader)

print("The original lists of lists:")
print(d)
print("\n")

# By default lists have strings as entries, so convert them to floats

for i in range(len(d)):
  for j in range(len (d[i])):
    d[i][j]=float(d[i][j])


print("The list of lists of floats")
print (d)
print("\n")

# A function to print out a list of lists, i.e. a matrix
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      # M[i][j] is the jth entry in the ith list
      # in other words, it's exactly the ij-th entry in the matrix M
      print (A[i][j], "\t", end="")
    print("\n")

print("In a 'matrix' format:")
print_matrix(d)

# Challenge 1: Determine if a matrix is in row echelon form

def is_row_echelon(A):
  previous_leading_entry = -1
  zero_row = False

  for i in range(len(A)):
    leading_entry = -1

    for j in range(len(A[i])):
      if A[i][j] != 0:
        leading_entry = j
        break

    if leading_entry == -1:
      zero_row = True
    else:
      if zero_row:
        return False
      if leading_entry <= previous_leading_entry:
        return False
      previous_leading_entry = leading_entry

  return True

if is_row_echelon(d):
  print("This matrix is in row echelon form.")
else:
  print("This matrix is not in row echelon form.")
