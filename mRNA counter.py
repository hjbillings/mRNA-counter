mRNA = "AUGAUGCCCGGGUAACCC"
aa = 0
start = False

for i in range(0, len(mRNA)):
    if start:
        break
    if mRNA[i:(i+3)] == "AUG":
        start = True
        j = i
        while j < len(mRNA):
            if (mRNA[j:(j+3)] == "UAA") or (mRNA[j:(j+3)] == "UAG") or (mRNA[j:(j+3)] == "UGA"):
                break
            else:
                aa += 1
                j += 3
print(aa)
