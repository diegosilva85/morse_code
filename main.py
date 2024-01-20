hash_map_morse_code = {
    "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
    "j": ".---", "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.",
    "s": "...", "t": "-", "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--", "z": "--..", "0": "-----",
    "1": ".----", "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..",
    "9": "----.", ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.", "!": "-.-.--", "/": "-..-.",
    "(": "-.--.", ")": "-.--.-", "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-", "-": "-....-",
    "_": "..--.-", "$": "...-...-", "@": ".--.-.", " ": "/", "é": "..-.."
}


def morse_code_generator(text: str) -> str:
    text_to_decode = text.lower()
    text_converted = ""
    for char in text_to_decode:
        if char in hash_map_morse_code:
            text_converted += f"{hash_map_morse_code[char]} "
    return text_converted


if __name__ == "__main__":
    input_text = input("Write the text to be converted:")
    morse_code = morse_code_generator(input_text)
    print(morse_code)
