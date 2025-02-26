while True:
    try:
        change = int(float(input("Change: ")) * 100)
    except ValueError:
        pass
    else:
        if change > 0:
            break


coins = change // 25 + change % 25 // 10 + \
    change % 25 % 10 // 5 + change % 25 % 10 % 5 // 1

print(coins)
