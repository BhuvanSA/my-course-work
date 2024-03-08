# Taking input and processing the data
data = input("File name: ").strip().lower().split(".")

# Cheking the extension part of the list for matching types
match data[-1]:
    case "gif" | "png":
        print("image/" + data[-1])
    case "jpeg" | "jpg":
        print("image/jpeg")
    case "pdf" | "zip":
        print("application/" + data[-1])
    case "txt":
        print("text/plain")
    case _:
        print("application/octet-stream")
