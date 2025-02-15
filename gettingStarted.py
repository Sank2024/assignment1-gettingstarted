### welcome_assignment_answers
### Input - All nine questions given in the assignment.
### Output - The right answer for the specific question.

def welcome_assignment_answers(question):
    # Students do not have to follow the skeleton for this assignment.
    # Another way to implement is using a "case" statements similar to C.

    if question.strip() == "Are encoding and encryption the same? - Yes/No":
        answer = "No"
    elif question.strip() == "Is it possible to decrypt a message without a key? - Yes/No":
        answer = "No"
    elif question.strip() == "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
        answer = 5
    elif question.strip() == "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
        answer = "pcap"
    elif question.strip()== "Is it possible to decode a message without a key? - Yes/No":
        answer = "Yes"
    elif question.strip() =="Is a hashed message supposed to be un-hashed? - Yes/No":
        answer = "No"
    elif question.strip() == "What is the SHA256 hashing value of your NYU email and use the answer in your code -":
        answer = "c504dc6362e24f920b065bbb5c5249104108ae530bd47b573213db898e2177fc"
    elif question.strip() == "Is MD5 a secured hashing algorithm? - Yes/No":
        answer = "No"
    elif question.strip() == "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
        answer = 3
    else:
        question = question.strip()
        answer = f"'{question.strip()}' does not match any predefined questions."
    return answer

# Complete all the questions.


if __name__ == "__main__":
    # use this space to debug and verify that the program works
    debug_question = "Is MD5 a secured hashing algorithm? - Yes/No"
    print(welcome_assignment_answers(debug_question))

# Questions:
# "In Slack, what is the secret passphrase posted in the #lab-python-getting-started channel posted by a TA?":
# "Are encoding and encryption the same? - Yes/No":
# "Is it possible to decrypt a message without a key? - Yes/No":
# "Is it possible to decode a message without a key? - Yes/No":
# "Is a hashed message supposed to be un-hashed? - Yes/No":
# "What is the SHA256 hashing value of your NYU email and use the answer in your code - ":
# "Is MD5 a secured hashing algorithm? - Yes/No":
# "What layer of the TCP/IP model does the protocol DNS belong to? - The answer should be an integer number":
# "What layer of the TCP/IP model does the protocol ICMP belong to? - The answer should be an integer number":
