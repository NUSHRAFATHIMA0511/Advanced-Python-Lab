f = open("input.txt", "r")
data = f.read()
f.close()

lines = data.count('\n') + 1
words = len(data.split())
chars = len(data)

print("Lines:", lines)
print("Words:", words)
print("Characters:", chars)
