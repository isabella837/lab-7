# Non-Square 2D Array Investigation

# --- Personalization values ---
d1 = 5 # last digit of student ID
d2 = 6 # second-last digit

k = (d1 + d2) % 4 + 2
shift = d1 - d2
rows_keep = (d1 % 2) + 2

# Component A

print("=== Component A ===")

# Create a 2D list (4 rows, 3 colums)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 11, 12]
]

# 1. Print dimensions
print("Matrix dimensions: 4 rows and 3 columns")

# 2. Print each row
print("Rows:")
for row in matrix:
    print(row)

# 3. Print last column
print("Last column:")
for row in matrix:
    print(row[-1])

# 4. Sub-array (all rows, first 3 columns)
sub_array = [row[:3] for row in matrix]
print("Sub-array (first 3 columns):")
for row in sub_array:
    print(row)

# Component B

print("\n=== Component B ===")

# Choose row using d1 % number_of_rows
row_index = d1 % len(matrix)

# Save old row
old_row = matrix[row_index]

# Create new row (each value increased by k)
new_row = [value + k for value in old_row]

# Replace row
matrix[row_index] = new_row

# Show old vs new
print("Old row:", old_row)
print("New row:", new_row)

# Choose starting column using d2 % 2
col_start = d2 % 2

# Print sliced sub-array
print(f"Sliced sub-array from column {col_start}:")
for row in matrix:
    print(row[col_start:])

    




