print("All answers should be in lower case")
one = input("What is an action word or a doing word? ")
two = input("I am something, I kiss my mother before I die, What am I? ")
three = input("Processed data is called? ")
four = input("People cry as they kill me, what am I? ")

def check_correct(question, answer):
    if question == answer:
        return 1
    else:
        return 0

print("Your score is ", check_correct(one, "verb")+check_correct(two, "matches")+check_correct(three, "information")+check_correct(four, "onoins"))