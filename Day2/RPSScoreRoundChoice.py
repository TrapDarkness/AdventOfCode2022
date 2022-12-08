total_score = 0 #check back against this variable for finding the most calories
selection_score = {"X":1, "Y":2, "Z":3}
match_score = {
    "A":{"X":3,"Y":6,"Z":0 },
    "B":{"X":0,"Y":3,"Z":6 },
    "C":{"X":6,"Y":0,"Z":3 }
}
with open("input.txt", "r") as open_file:
    for line in open_file:
        my_choice = line[2]
        their_choice = line[0]
        total_score += selection_score[my_choice] + match_score[their_choice][my_choice]

print(total_score)
