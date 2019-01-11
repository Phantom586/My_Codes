if __name__ == '__main__':
    # A List for Storing the names and corresponding marks in form of a nested list.
    students = []
    # Another list to store the Scores for the students.
    scores = []
    # for loop to input the names and the score of N Students.
    for _ in range(int(input())):
        # Variable to hold the name of the student.
        name = input()
        # Variable to hold the score of the student.
        score = float(input())
        # Appending the score of the student to the scores list
        scores.append(score)
        # Appending a list of each students ,name and score( [name, score] ) into students list.
        students.append([name, score])
    # Removing the Repeated Values.
    scores = list(set(scores))
    # Sorting the Scores List
    scores.sort()
    # Reversing the list in order to calculate the second lowest score.
    scores.reverse()
    # A list to store the names of the Students having the second lowest score.
    stud = []
    for i in students:
        # Matching from the second lowest score from the score list to the students list.
        if scores[-2] == i[1]:
            # Append the matched names to the stud list.
            stud.append(i[0])
    # Sorting the names of the students scores second lowest scores Alphabetically.
    stud.sort()
    # Printing the Result.
    for i in stud:
        print(i)