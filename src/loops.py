for i in range(10):
    print(i)

#  element can be of different type
names = ["Alice", "Bob", "Charlie", True] # list
for name in names:
    print(name)

s = set()
s.add(1)
s.add(2)
s.add(3)
print(s)


ages = {"Alice":22, "Bob":27}
ages["Charlie"] = 30
ages["Alice"] += 1
print(ages)

## NameError 
## IndexError

def main():
    pass

if __name__ == "__main__":
    main()

