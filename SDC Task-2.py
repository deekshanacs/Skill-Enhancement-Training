#SDC Task-2
# To cover the concepts of functions and control statements
#Here's my task-2 "Quiz game"
#create a quiz game consisiting of desired question also by checking the answers.

def q1():
    print("Q1.What is the color of blood when it's inside your body?\na)Yellow\nb)White\nc)Red\nd)Green")
    ans=input("Enter your answer(only options in lowercase) : ")
    if ans=='c':
        print("Correct Answer!")
        return 1
    else:
        print("Incorrect Answer try agian.")
def q2():
    print("Q2.Which is the fastest bird in the world?\na)bald Eagle\nb)Peregrine falcon\nc)Hummingbird\nd)Raven")
    ans=input("Enter your answer(only options in lowercase) : ")
    if ans=='b':
        print("Correct Answer!")
        return 1
    else:
        print("Incorrect Answer try agian.")
def q3():
    print("Q3.What is the tallest waterfall in the world?\na)Angel falls, Venezuela\nb)Niagara falls,NewYork\nc)Wailua falls,Hawaii\nd)Sutherland Falls,New Zealand")
    ans=input("Enter your answer(only options in lowercase) : ")
    if ans=='a':
        print("Correct Answer!")
        return 1
    else:
        print("Incorrect Answer try agian.")
def q4():
    print("Q4.Which planet is known as the RED Planet?\na)Venus\nb)Saturn\nc)Mars\nd)Mercury")
    ans=input("Enter your answer(only options in lowercase) : ")
    if ans=='c':
        print("Correct Answer!")
        return 1
    else:
        print("Incorrect Answer try agian.")
def q5():
    print("Q5.Which food item never gets spoiled down?\na)Honey\nb)Beef Jerky\nc)Cereal\nd)Beans")
    ans=input("Enter your answer(only options in lowercase) : ")
    if ans=='a':
        print("Correct Answer!")
        return 1
    else:
        print("Incorrect Answer try agian.")

score=0
score += q1() or 0
score += q2() or 0
score += q3() or 0
score += q4() or 0
score += q5() or 0
print("Total Score is : ",score)


