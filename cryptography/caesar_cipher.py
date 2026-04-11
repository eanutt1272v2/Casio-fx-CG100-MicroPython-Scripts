def caesar(text, shift, decode=False):
    if decode: shift = -shift
    result = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            result += chr((ord(ch) - base + shift) % 26 + base)
        else:
            result += ch
    return result

mode = input("e=encode, d=decode: ")
text = input("Text: ")
shift = int(input("Shift: "))
out = caesar(text, shift, decode=(mode=="d"))
print("Result:", out)

# input("\nPress any key to exit: ")

