x, y, z = input("Expression: ").split(" ")

x, z = float(x), float(z)

match y:
    case "+":
        print(x + z)
    case "-":
        print(x - z)
    case "*":
        print(x * z)
    case "/":
        print(x / z)
