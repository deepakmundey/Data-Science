a=int(input("Please insert the value of 'a': "))
num_to_word = {
    0: "Zero",
    1: "One",
    2: "Two",
    3: "Three"
}

if a in num_to_word:
    print(num_to_word[a])
