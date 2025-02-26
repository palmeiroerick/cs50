text = input("Text: ").strip()

words = sum(c == " " for c in text) + 1
letters = sum(c.isalpha() for c in text)
sentences = sum(c in ".!?" for c in text)

l, s = letters / words * 100, sentences / words * 100

grade = 0.0588 * l - 0.296 * s - 15.8

if grade < 1:
    print("Before Grade 1")
elif grade > 15:
    print("Grade 16+")
else:
    print(f"Grade {round(grade)}")
