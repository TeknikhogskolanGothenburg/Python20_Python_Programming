def main():
    result = input("Enter result: ")
    if int(result) > 80:
        letter_grade = "A"
    elif int(result) > 70:
        letter_grade = "B"
    elif int(result) > 60:
        letter_grade = "C"
    elif int(result) > 50:
        letter_grade = "D"
    elif int(result) > 40:
        letter_grade = "E"
    else:
        letter_grade = "F"

    print(letter_grade)


if __name__ == '__main__':
    main()
