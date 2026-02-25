import sys

n = int(input())
phone_book = {}

# Read phone book entries
for _ in range(n):
    name, number = input().split()
    phone_book[name] = number

# Read queries until EOF
for line in sys.stdin:
    query = line.strip()
    if query in phone_book:
        print(f"{query}={phone_book[query]}")
    else:
        print("Not found")
