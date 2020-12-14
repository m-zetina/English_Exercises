import random 
from file_editor import unserialize_data as unserialize 

print("\n\n")
print("\nWelcome to your daily English Exercises, Jimena!")
print("You will find review verbs and sentences here to complete.")
print("How this will work: Verbs and sentences, written in Spanish, will appear on the screen.")
print("You are to conjugate the verbs and translate the sentences into English.")
print("For the verbs, type your answer for each individual pronoun, and this program will tell you your score and the correct answers.")
print("You will have 5 different verb exercises.")
print("For the sentences, simply retype the sentence in English.")
print("If your answer is incorrect, you may try again.")
print("Or you could have the correct answer revealed. If so, then just type \"no.\"")
print("You will have 10 different setences.")
print("Alright, let's get started!")
print("\n\n---------------------------------------------------------------------------------------\n")


# noun_dict = unserialize("nouns.pickle")
conjugation_dict = unserialize("conjugations.pickle")
verb_dict = unserialize("verbs.pickle")
sentence_dict = unserialize("sentences.pickle")

def conjugate(question_limit):
    question_wordbank = sorted(conjugation_dict)
    
    for i in range(question_limit):
        num_correct_answers = 0

        question = random.choice(question_wordbank)
        question_wordbank.remove(question)

        print(f"\n\nPlease conjugate this: {question}")

        print("\nI")
        response = input()
        if response == conjugation_dict[question][0]:
            num_correct_answers += 1

        print("\nYou")
        response = input()
        if response == conjugation_dict[question][1]:
            num_correct_answers += 1

        print("\nHe/She/It")
        response = input()
        if response == conjugation_dict[question][2]:
            num_correct_answers += 1

        print("\nWe")
        response = input()
        if response == conjugation_dict[question][3]:
            num_correct_answers += 1

        print("\nThey")
        response = input()
        if response == conjugation_dict[question][4]:
            num_correct_answers += 1
        print(f"\nCorrect Answers: I {conjugation_dict[question][0]}, You {conjugation_dict[question][1]}, He/She/It {conjugation_dict[question][2]}, We {conjugation_dict[question][3]}, They {conjugation_dict[question][4]}")
        print(f"\nTotal Score: {num_correct_answers}/5\n")

def universal(test_dict, question_limit, prompt): 
    num_correct_answers = 0
    question_wordbank = sorted(test_dict)

    for i in range(question_limit):
        question = random.choice(question_wordbank)
        question_wordbank.remove(question)

        print(f"\n\n{prompt}: {question}")
        response = input()

        if response in test_dict[question]:
            print("Correct!\n+1")
            num_correct_answers += 1

        else:
            print("Sorry, that was incorrect. Would you like to try again? (yes or no)")
            try_again = input()
            if try_again == "yes":
                print("\nEnter your response: ")
                response2 = input()

                if response2 in test_dict[question]:
                    print("Correct!\n+.5")
                    num_correct_answers += .5
                else:
                    print("The correct answer was: ")
                    for i in range(len(test_dict[question])):
                        print(f"\"{test_dict[question][i]}\"")
                        if i < len(test_dict[question]) - 1:
                            print("or")
            else:
                print("The correct answer was: ") 
                for i in range(len(test_dict[question])):
                    print(f"\"{test_dict[question][i]}\"")
                    if i < len(test_dict[question]) - 1:
                        print("or")
    
    print(f"\nTotal Score: {num_correct_answers}/{question_limit}\n\n")



conjugate(7)
universal(verb_dict, 10, "Past Tense of")
universal(sentence_dict, 10, "Please translate this")