#!/usr/bin/python3

def text_indentation(text):
    """Prints a text with 2 new lines after each of these
    characters: ., ? and :.

    Args:
        text: The text to be printed. Must be a string.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in range(len(text)):
        print(text[i], end="")
        if text[i] in ".?:":
            print("\n\n", end="")
        if i < len(text) - 1 and text[i + 1] == " ":
            continue
