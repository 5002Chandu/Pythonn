print("\nExact Centered Reverse Pyramid")

rows = 5
for i in range(rows, 0, -1):
    stars = '*' * (2 * i - 1)   # odd number of stars per row
    print(stars.center(2 * rows))  # center align within max width
