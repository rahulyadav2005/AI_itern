text = input(" word: ")
count = 0

for i in text:
    if i.lower() in "aeiou":
        count += 1

print("vowels:", count)
