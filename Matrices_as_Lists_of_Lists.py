# Matrices as Lists of Lists
# A simple introduction to handling matrices as lists of lists in Python
# Patrick Honner 9/21/22

# Need this to deepcopy lists
import copy

# Makes presenting a table of data easier
from tabulate import tabulate

# We'll hardcode the matrix as a list of lists
# The nested lists function as the rows of the matrix

row_1 = [3, -4, 0, 5]
row_2 = [-1, -2, 3, 10]
row_3 = [4, 1, 1, 3]

M = [ row_1, row_2, row_3]


print("Here is matrix M shown as a table in Python:\n")
print(tabulate(M))


# Helper: Perform a row operation on the matrix passed into this function
def perform_row_operation(matrix):
  print("1: Multiply a row by a scalar")
  print("2: Swap two rows")
  print("3: Add a multiple of one row to another row")
  operation = input("Enter your choice: ")

  if operation == "1":
    row = int(input("Choose a row to multiply: ")) - 1
    scalar = float(input("Enter a scalar: "))
    for i in range(len(matrix[row])):
      matrix[row][i] = scalar * matrix[row][i]

  elif operation == "2":
    first_row = int(input("Enter the first row to swap: ")) - 1
    second_row = int(input("Enter the second row to swap: ")) - 1
    matrix[first_row], matrix[second_row] = matrix[second_row], matrix[first_row]

  elif operation == "3":
    target_row = int(input("Enter the row you want to change: ")) - 1
    source_row = int(input("Enter the row to use: ")) - 1
    scalar = float(input("Enter the scalar: "))
    for i in range(len(matrix[target_row])):
      matrix[target_row][i] += scalar * matrix[source_row][i]

  else:
    print("Invalid operation.")


# Easy Task Part 1: Return a row or column selected by the user
def easy_task_part_1():
  choice = input("Do you want a row or column? ").lower()

  if choice == "no":
    print("No row or column selected.")
    return

  number = int(input("Enter its number: ")) - 1

  if choice == "row":
    print("Selected row:", M[number])
  elif choice == "column":
    selected_column = []
    for row in M:
      selected_column.append(row[number])
    print("Selected column:", selected_column)
  else:
    print("Please enter row or column.")


# Easy Task Part 2: Let the user change one entry in the matrix
def easy_task_part_2():
  row_number = int(input("Enter the row of the entry to change: ")) - 1
  column_number = int(input("Enter the column of the entry to change: ")) - 1
  new_value = float(input("Enter the new value: "))
  M[row_number][column_number] = new_value
  print("Entry changed.")


# Easy Task Part 3: Perform any elementary row operation
def easy_task_part_3():
  perform_row_operation(M)
  print("Row operation complete.")


# Medium Task Part 1: Let the user enter a custom matrix
def create_custom_matrix():
  custom_row_count = int(input("How many rows are in your matrix? "))
  custom_column_count = int(input("How many columns are in your matrix? "))
  custom_matrix = []

  for i in range(custom_row_count):
    values = input(
      f"Enter {custom_column_count} values for row {i + 1}, separated by spaces: "
    ).split()
    while len(values) != custom_column_count:
      values = input(
        f"Please enter exactly {custom_column_count} values for row {i + 1}: "
      ).split()
    custom_matrix.append([float(value) for value in values])

  print("Your custom matrix:")
  print(tabulate(custom_matrix))
  return custom_matrix


# Medium Task Part 2: Perform a chosen row operation on the custom matrix
def medium_task_part_2():
  custom_matrix = create_custom_matrix()
  perform_row_operation(custom_matrix)
  print("Custom matrix after the row operation:")
  print(tabulate(custom_matrix))


# Task Menu: Choose one task at a time, or enter q to exit
while True:
  print("\nCurrent matrix M:")
  print(tabulate(M))
  print("\nChoose a task:")
  print("1: Easy Task Part 1 - Select a row or column")
  print("2: Easy Task Part 2 - Change an entry")
  print("3: Easy Task Part 3 - Row operations on M")
  print("4: Medium Tasks - Custom matrix and row operation")
  print("q: Quit")

  task_choice = input("Enter your choice: ").lower()

  if task_choice == "1":
    easy_task_part_1()
  elif task_choice == "2":
    easy_task_part_2()
  elif task_choice == "3":
    easy_task_part_3()
  elif task_choice == "4":
    medium_task_part_2()
  elif task_choice == "q":
    break
  else:
    print("Please enter 1, 2, 3, 4, or q.")



# A function to print out a list of lists, i.e. a matrix
# tabulate is nicer, so I didn't use this, but left as an example
def print_matrix(A):
  for i in range(len(A)):
    for j in range(len(A[i])):
      # M[i][j] is the jth entry in the ith list
      # in other words, it's exactly the ij-th entry in the matrix M
      print (A[i][j], "\t", end="")
    print("\n")
