n = int(input("Enter the number of subjects: "))

marks = []
for i in range(n):
    m = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(m)

# Calculate average
average = sum(marks) / n

print("\nMarks entered:", marks)
print("Average marks =", average)
