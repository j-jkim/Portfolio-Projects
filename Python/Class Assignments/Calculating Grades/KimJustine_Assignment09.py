# Name: Justine Kim     # Date: 5/5/19
# NetID: jk5565         # Section: CSCI-UA.0002-1
# Assignment 9          # Program: Part 1 - 4 + Extra Credit


# try-except-else to open the file
while True:
    try:
        filename = input("Enter a class to grade (i.e. class1 for class1.txt): ")
        filenametxt = filename + ".txt"
        f = open(filenametxt,"r")
    except:
        print("File cannot be found.")
        print()   
    else:
        print("Successfully opened",filenametxt)
        print()
        break

fout = open(filename.split(".")[0]+"_grades.txt", "w")  # to create grades file (Part.4)
answerkey = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D".split(",")

# accumulator variables 
no_students = 0
highest_score = 0
lowest_score = 0
mean_score = 0
list_scores = []
list_id = []

# to read every line separately
for s in f.readlines():
    s = s.strip().split(",")
    s_id = s[0]
    del s[0]
    list_id.append(s_id)

    # to check scores for each student ( per line )
    score = 0
    for i in range(len(s)): 
        if not s[i]:
            continue
        elif s[i] == answerkey[i]:
            score+=4
        else:
            score-=1

    # overwriting new grade file
    fout.write(s_id + "," + format(score,".2f") + "\n")

    if no_students == 0:
        highest_score = score
        lowest_score = score
    if highest_score < score:
        highest_score = score
    if lowest_score > score:
        lowest_score = score
    mean_score += score
    list_scores += [score]
    no_students+=1
    
# to calculate median, mode, range...
import statistics
median_score = statistics.median(list_scores)
mode_score = statistics.mode(list_scores)
range_score = highest_score - lowest_score
mean_score = mean_score / no_students

# printing output to user
print('Grade Summary')
print('Total students:',no_students)
print('Highest score:', highest_score)
print('Lowest score:',lowest_score)
print('Mean score:', format(mean_score,".2f"))
print('Median score:',format(median_score,".2f"))
print('Mode:',mode_score)
print('Range:',range_score)

# to ask if user wants to curve (Extra Credit)
curve = input("Would you like to curve the exam? 'y' or 'n': ")
while curve == 'y':
    desired_mean = float(input("Enter a desired mean (i.e. 75.0 to raise mean score\
to 75.0): "))
    if desired_mean < 0:
        print("Invalid curve, try again.")
        print()
    else:
        fout = open(filename.split(".")[0]+"_grades.txt", "w")
        diff = desired_mean - mean_score

        for j in range(len(list_id)):
            new_score = list_scores[j] + diff
            fout.write(list_id[j] +"," + format(list_scores[j],".2f") \
                       + "," + format(new_score,".2f") +"\n")
        
        print("Done! Check your grade file!")
        break

# closing all files
f.close()
fout.close()


