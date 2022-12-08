total_score = 0 #check back against this variable for finding the most calories
selection_score = {"X":1, "Y":2, "Z":3}
match_score = {
    "A X":3, "A Y":4, "A Z":8,
    "B X":1, "B Y":5, "B Z":9,
    "C X":2, "C Y":6, "C Z":7,

}
with open("input.txt", "r") as open_file:
    for line in open_file:
        total_score += match_score[line.strip()]

print(total_score)
