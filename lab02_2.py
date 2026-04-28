# Ask for Student 1 ID
# This line takes the first student's ID from the user
id1 = int(input("Enter Student 1 ID: "))

# Ask for Student 2 ID
# This line takes the second student's ID from the user
id2 = int(input("Enter Student 2 ID: "))

# Find last 2 digits of first ID
# % 100 gives only the last two digits
last1 = id1 % 100

# Find last 2 digits of second ID
# % 100 gives only the last two digits
last2 = id2 % 100

# Make one unique value for quiz
# Add both last digits and keep only one digit using % 10
unique_value = (last1 + last2) % 10

# Show the unique value
# This prints the unique number for the quiz
print("Unique value is:", unique_value)


# Create empty dictionary for students
# Dictionary will store student names and scores
students = {}

# Ask student names until user types exit
# while True means the loop will keep running
while True:

    # Ask the user to enter student name
    name = input("Enter student name (type 'exit' to stop): ")

    # Stop the loop if user types exit
    # lower() helps accept Exit, EXIT, exit etc.
    if name.lower() == "exit":
        break

    # Skip blank name
    # If no name is entered, show message
    if name == "":
        print("Name cannot be blank")
        continue

    # Save name with starting score 0
    # Every student starts with score 0
    students[name] = 0


# Start quiz for each student
# for loop runs quiz for every student
for name in students:

    # Show whose quiz is starting
    print("Quiz for", name)

    # Start score from 0
    score = 0
 
 # Question 1
    ans = int(input(f"{unique_value} + 2 = "))
    if ans == unique_value + 2:   # Check correct answer
        score += 1               # Add 1 mark if correct

    # Question 2
    ans = int(input(f"{unique_value} * 3 = "))
    if ans == unique_value * 3:
        score += 1

    # Question 3
    ans = int(input(f"{unique_value} + 5 = "))
    if ans == unique_value + 5:
        score += 1

    # Store final score in dictionary
    students[name] = score


# Step 4: Display results, performance, certificate, and stars
for name, score in students.items():
    print(f"\n{name}'s Score:", score)

    # Determine performance level
    if score == 3:
        performance = "Excellent"
    elif score == 2:
        performance = "Good"
    elif score == 1:
        performance = "Average"
    else:
        performance = "Poor"

    print("Performance:", performance)

    # Check certificate eligibility
    if score >= 2:
        print("Certificate: Eligible")
    else:
        print("Certificate: Not Eligible")

    # Step 5: Print star pattern based on score
    print("Stars:")
    if score == 0:
        print("(No stars)")   # If score is 0, print nothing or message
    else:
        for i in range(score):
            print("*" * (i + 1))   # Print increasing stars


