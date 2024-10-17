from preloaded import MORSE_CODE

def decode_morse(morse_code):
  decoded_words = []
  for word in morse_code.strip().split('   '): # 3 spaces
    decoded_word = ''
    for l in word.split(' '): # 1 space
      decoded_word += MORSE_CODE[l]
    decoded_words.append(decoded_word)
  return ' '.join(decoded_words)
