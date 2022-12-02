most_calories = 0 #check back against this variable for finding the most calories
with open("input.txt", "r") as open_file:
    current_elf_calories = 0
    for line in open_file:
        #print(line.strip('\n'))
        if (line.strip('\n').isnumeric()):
            current_elf_calories += int(line.strip('\n'))
            #print(line)
        else:
            if current_elf_calories > most_calories:
                most_calories = current_elf_calories
            current_elf_calories = 0
print(most_calories)
