from tkinter import *
from PIL import Image, ImageTk

asl_fingerspelling = {
    'a': 'a2.png',
    'b': 'b2.png',
    'c': 'c3.png',
    'd': 'd2.png',
    'e': 'e2.png',
    'f': 'f2.png',
    'g': 'g5.png',
    'h': 'h4.png',
    'i': 'i2.png',
    'j': 'j.png',
    'k': 'k2.png',
    'l': 'l2.png',
    'm': 'm2.png',
    'n': 'n2.png',
    'o': 'o2.png',
    'p': 'p5.png',
    'q': 'q1.png',
    'r': 'r2.png',
    's': 's2.png',
    't': 't2.png',
    'u': 'u2.png',
    'v': 'v2.png',
    'w': 'w2.png',
    'x': 'x2.png',
    'y': 'y2.png',
    'z': 'z2.png',
    ' ': ' ',
}

def display_image(image_filename, row, col):
    image = Image.open(image_filename)
    image.thumbnail((100, 100))
    photo = ImageTk.PhotoImage(image)
    label = Label(root, image=photo)
    label.photo = photo
    label.grid(row=row, column=col)

def text_to_asl(text):
    text = text.lower()
    asl_translation = ""
    row, col = 0, 0

    for char in text:
        translation = asl_fingerspelling.get(char, char)

        if translation.endswith('.png'):
            display_image(translation, row, col)
            col += 1

            # Check if it's time to move to the next row (e.g., after 5 images)
            if col == 10:
                col = 0
                row += 1
        else:
            asl_translation += translation + " "
            col = 0
            row += 1

    return asl_translation

def main():
    print("Text-to-ASL Fingerspelling Translator")
    while True:
        user_input = input("Enter a phrase or type 'exit' to quit:")

        if user_input.lower() == "exit":
            break

        asl_translation = text_to_asl(user_input)
        if asl_translation:
            print("ASL Fingerspelling Translation:", asl_translation)

if __name__ == "__main__":
    root = Tk()
    root.title("ASL Fingerspelling Translator")

    main()
    root.mainloop()
