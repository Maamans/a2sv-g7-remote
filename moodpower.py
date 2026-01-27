# Read input
a, b, m = map(int, input().split())

# Print a^b
print(pow(a, b))

# Print (a^b) % m
print(pow(a, b, m))
