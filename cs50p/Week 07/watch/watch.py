import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    regex = r'<iframe.*src="https?://(?:www\.)?youtube\.com/embed/(.{11})"'

    if matches := re.search(regex, s):
        return f"https://youtu.be/{matches.group(1)}"


if __name__ == "__main__":
    main()
