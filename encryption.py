import hashlib

# Caesar Cipher
def caesar_cipher(text, shift=3, decrypt=False):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            shift_dir = -shift if decrypt else shift
            result += chr((ord(char) - shift_base + shift_dir) % 26 + shift_base)
        elif char.isdigit():
            shift_dir = -shift if decrypt else shift
            result += chr((ord(char) - 48 + shift_dir) % 10 + 48)
        else:
            result += char
    return result

# Reverse Text
def reverse_text(text):
    return text[::-1]

# Super Secure — Random Special Symbols
def super_secure_encrypt(text):
    map_table = {chr(i): chr(33 + (i % 15)) for i in range(32, 127)}
    return ''.join(map_table.get(c, c) for c in text)

def super_secure_decrypt(text):
    reverse_table = {chr(33 + (i % 15)): chr(i) for i in range(32, 127)}
    return ''.join(reverse_table.get(c, c) for c in text)

# Emoji Cipher
emoji_map = {
    'a': '😀', 'b': '😁', 'c': '😂', 'd': '🤣', 'e': '😅', 'f': '😊', 'g': '😎',
    'h': '😍', 'i': '😘', 'j': '😜', 'k': '🤪', 'l': '😏', 'm': '🥲', 'n': '😱',
    'o': '😳', 'p': '🤯', 'q': '🛸', 'r': '👻', 's': '🎃', 't': '👽', 'u': '💀',
    'v': '🤖', 'w': '🧠', 'x': '🕹️', 'y': '⚡', 'z': '🔥', ' ': '🌌'
}
reverse_emoji_map = {v: k for k, v in emoji_map.items()}

def emoji_encrypt(text):
    return ''.join(emoji_map.get(c.lower(), c) for c in text)

def emoji_decrypt(text):
    return ''.join(reverse_emoji_map.get(c, c) for c in text)

# Morse Code
morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..',
    'E': '.',  'F': '..-.', 'G': '--.',  'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-',  'L': '.-..',
    'M': '--', 'N': '-.',   'O': '---',  'P': '.--.',
    'Q': '--.-','R': '.-.', 'S': '...',  'T': '-',
    'U': '..-', 'V': '...-','W': '.--',  'X': '-..-',
    'Y': '-.--','Z': '--..',
    '1': '.----','2': '..---','3': '...--','4': '....-','5': '.....',
    '6': '-....','7': '--...','8': '---..','9': '----.','0': '-----',
    ' ': '/'
}
reverse_morse_dict = {v: k for k, v in morse_code_dict.items()}

def morse_encrypt(text):
    return ' '.join(morse_code_dict.get(char.upper(), char) for char in text)

def morse_decrypt(text):
    return ''.join(reverse_morse_dict.get(code, '') for code in text.strip().split())

# Hash Encrypt (One way only)
def hash_encrypt(text):
    return hashlib.sha256(text.encode()).hexdigest()

# Router
def encrypt_text(text, method):
    if method == "Caesar":
        return caesar_cipher(text)
    elif method == "Reverse":
        return reverse_text(text)
    elif method == "SuperSecure":
        return super_secure_encrypt(text)
    elif method == "Emoji":
        return emoji_encrypt(text)
    elif method == "Morse":
        return morse_encrypt(text)
    elif method == "Hash":
        return hash_encrypt(text)
    elif method == "Barcode":
        return text
    else:
        return "❌ Unknown method!"

def decrypt_text(text, method):
    if method == "Caesar":
        return caesar_cipher(text, decrypt=True)
    elif method == "Reverse":
        return reverse_text(text)
    elif method == "SuperSecure":
        return super_secure_decrypt(text)
    elif method == "Emoji":
        return emoji_decrypt(text)
    elif method == "Morse":
        return morse_decrypt(text)
    elif method == "Barcode":
        return "❌ Barcode decryption not supported!"
    elif method == "Hash":
        return "❌ Hash can't be decrypted!"
    else:
        return "❌ Unknown method!"
