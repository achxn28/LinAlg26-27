# Load Data into a Matrix, Patrick Honner 10/1/2022
# Simple example of reading a csv file in and converting to a list of lists

# Challenge 2
# Import the csv module for handling data
import csv

choice = input("Enter 1 to enter a matrix or 2 to read matrix.txt: ")

if choice == "1":
  number_of_rows = int(input("Enter the number of rows: "))
  number_of_columns = int(input("Enter the number of columns: "))
  d = []

  for i in range(number_of_rows):
    row = input("Enter row " + str(i + 1) + ", separated by commas: ").split(",")
    for j in range(number_of_columns):
      row[j] = float(row[j])
    d.append(row)

else:
  # This reads in the comma separated values as a list of lists of strings.
  with open("matrix.txt") as f:
    reader = csv.reader(f)
    d = list(reader)

  # By default lists have strings as entries, so convert them to floats.
  for i in range(len(d)):
    for j in range(len(d[i])):
      d[i][j] = float(d[i][j])


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


# This RREF code was copied from Matrices_as_Lists_of_Lists.py.
def rref(matrix):
  number_of_rows = len(matrix)
  number_of_columns = len(matrix[0])
  pivot_row = 0

  for pivot_column in range(number_of_columns):
    swap_row = pivot_row
    while swap_row < number_of_rows and matrix[swap_row][pivot_column] == 0:
      swap_row += 1

    if swap_row == number_of_rows:
      continue

    if swap_row != pivot_row:
      matrix[pivot_row], matrix[swap_row] = matrix[swap_row], matrix[pivot_row]

    pivot_value = matrix[pivot_row][pivot_column]
    for column in range(number_of_columns):
      matrix[pivot_row][column] /= pivot_value

    for row in range(number_of_rows):
      if row != pivot_row:
        factor = matrix[row][pivot_column]
        for column in range(number_of_columns):
          matrix[row][column] -= factor * matrix[pivot_row][column]

    for row in range(number_of_rows):
      for column in range(number_of_columns):
        if abs(matrix[row][column]) < 0.0000000001:
          matrix[row][column] = 0

    pivot_row += 1
    if pivot_row == number_of_rows:
      break

  return matrix


print("Reduced row echelon form:")
print_matrix(rref(d))
