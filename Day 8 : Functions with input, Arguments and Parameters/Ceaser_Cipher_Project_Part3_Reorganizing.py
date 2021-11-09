alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 

# def caesar(arg_text,arg_shift):
#   result_text = ""
#   for letter in arg_text:
#     position = alphabet.index(letter)
#     if direction == "encode":
#       new_position = position + arg_shift
#     elif direction == "decode":
#       new_position = position - arg_shift
#     result_text += alphabet[new_position]
#   print(f"The encoded text is {result_text}")


def caesar(arg_text,arg_shift,cipher_direction):
  result_text = ""
  if cipher_direction == "decode":
      # new_position = position + arg_shift
      arg_shift *= -1
  for letter in arg_text:
    position = alphabet.index(letter)
    new_position = position + arg_shift
    result_text += alphabet[new_position]
  print(f"The {cipher_direction}d text is {result_text}")

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.

caesar(arg_text=text,arg_shift=shift,cipher_direction=direction)
