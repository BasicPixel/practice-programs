# dna2mrna-v2.py
# Program that converts a DNA sample to an mRNA one (v2)

import re

conversions = {
    "A": "U",
    "T": "A",
    "C": "G",
    "G": "C",
}

dna = input("Enter the DNA sample: ").upper()
mrna = ""

# Check if the DNA sample contains any invalid characters
if re.search(r"[^atcg]", dna):
    print("Invalid DNA sample!")
    quit()

# Loop over DNA sample, adding the corresponding Nucleotide to mRNA
for i in dna:
    mrna += conversions[i]

""" Other solution:

for i in dna:
    match i:
        case "a":
            mrna += "U"
        case "t":
            mrna += "A"
        case "c":
            mrna += "G"
        case "g":
            mrna += "C"

 """

print(mrna)
