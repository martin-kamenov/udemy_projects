with open("file1.txt") as f:
    file1 = f.readlines()
    file1 = [int(n.strip()) for n in file1]

with open("file2.txt") as file:
    file2 = file.readlines()
    file2 = [int(n.strip()) for n in file2]

result = [x for x in file1 if x in file2]

print(result)