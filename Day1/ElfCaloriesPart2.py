top3_calories = (0,0,0)
with open("input.txt", "r") as open_file:
    current_elf_calories = 0
    for line in open_file:
        #print(line.strip('\n'))
        if (line.strip('\n').isnumeric()):
            current_elf_calories += int(line.strip('\n'))
            #print(line)
        else:
            top1,top2,top3 = top3_calories
            if current_elf_calories > top3:
                if current_elf_calories > top2:
                    if current_elf_calories > top1:
                        top3 = top2
                        top2 = top1
                        top1 = current_elf_calories
                    else:
                        top3 = top2
                        top2 = current_elf_calories
                else:
                    top3 = current_elf_calories
            top3_calories = (top1,top2,top3)
            current_elf_calories = 0
        
print(top3_calories)
top1,top2,top3 = top3_calories
print(top3+top2+top1)
