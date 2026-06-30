def palindrome():
    word = input("Word: ").lower()

    if word == word[::-1]:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

palindrome()