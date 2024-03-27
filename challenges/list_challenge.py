#!/usr/bin/env python3


def main():
    wordbank= ["indentation", "spaces"]
    tlgstudents= ["Aaron", "Ahmed", "Andy", "Brent", "Cedric", "Chris", "Dom", "Franco", "John", "Nicolas", "Joey", "Jordan", "JC", "Louis", "Samuel", "Sanam", "Zach"]

    wordbank.append(4)
    # print(wordbank)

    num = int(input("Enter a number between 0 and 17: "))

    student_name = tlgstudents[num]

    print(f"{student_name} always uses {num} {wordbank[1]} to indent")

if __name__=="__main__":
    main()




