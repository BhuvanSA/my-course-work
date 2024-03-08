import sys
from PIL import Image, ImageOps


def main():
    file_path = get_file_path()
    input_image = Image.open(file_path[0])
    cropped_image = ImageOps.fit(input_image, size=(600, 600))
    shirt_image = Image.open("shirt.png")
    # cropped_shirt = ImageOps.fit(shirt_image, size=(300, 300))
    cropped_image.paste(shirt_image, (00, 00), shirt_image)
    cropped_image.save(file_path[1])


def get_file_path() -> list[str]:
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    supported_extensions = ['jpg', 'jpeg', 'png']
    try:
        assert sys.argv[1].lower().split(".")[1] in supported_extensions
    except:
        sys.exit("Invalid input")
    try:
        assert sys.argv[2].lower().split(".")[1] in supported_extensions
    except:
        sys.exit("Invalid output")

    try:
        assert sys.argv[1].lower().split(
            ".")[1] == sys.argv[2].lower().split(".")[1]
    except:
        sys.exit("Input and output have different extensions")

    try:
        with open(sys.argv[1]) as _:
            ...
    except:
        sys.exit("Input does not exist")

    return [sys.argv[1], sys.argv[2]]


if __name__ == "__main__":
    main()
