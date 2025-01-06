file = input("File name: ").lower().strip()

file_extension = file.split(".")[-1]

match file_extension:
    case "gif":
        print("image/gif")
    case "jpg"| "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")
