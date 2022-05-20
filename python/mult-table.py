# Python program to print a multiplication table

print("\t1\t2\t3\t4\t5\t6\t7\t8\t9\t10")

for n in range(1, 11):
    print(n, end="\t")
    for x in range(1, 11):
        print(n * x, end="\t")
    print()
