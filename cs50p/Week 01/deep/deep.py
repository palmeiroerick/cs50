answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()

correct = [
    "42",
    "forty-two",
    "forty two"
]

if answer in correct:
    print("Yes")
else:
    print("No")
