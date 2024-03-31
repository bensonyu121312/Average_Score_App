# This program average test scores. It asks the user for the number of students and the number of test scores per student
# Make it as streamlit web application
# deploy your application to the github and streamlit.io (extra point)
import streamlit as st

# Get the number of students
num_student = st.number_input("How many students do you have?", min_value=1, step=1, value=1, key="num_student")
# Get the number of test scores per student
num_test_scores = st.number_input("How many quizzes are you running per student?", min_value=1, step=1, value=1, key="num_test_scores")

# Input validation for num_student
if num_student < 1:
    st.error("Number of students must be at least 1.")
elif num_test_scores < 1:
    st.error("Number of test scores per student must be at least 1.")
else:
    # Initialize an accumulator for test score
    total = 0.0
    # Determine each student's average test score
    for student in range(num_student):
        # Display the student number
        st.write(f"Student number {student + 1}")
        st.write("-------------------------------")
        for test_number in range(num_test_scores):
            # Get a student's test score
            score = st.number_input(f"Test number {test_number + 1} for student {student + 1}:",
                                    key=f"score_{student}_{test_number}",
                                    min_value=1.0, max_value=100.0, value=1.0, step=0.1)
            total += score
        st.write("")  # Add a blank line for separation between students
    # Calculate the average test score for all students
    average = total / (num_student * num_test_scores)
    # Display the average
    st.write(f"The average score for all students is {average}")