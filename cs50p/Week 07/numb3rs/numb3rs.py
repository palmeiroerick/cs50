import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    regex = r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$"

    if matches := re.search(regex, ip):
        for n in matches.groups():
            if 0 <= int(n) <= 255:
                continue
            else:
                return False
        return True
    else:
        return False


if __name__ == "__main__":
    main()
