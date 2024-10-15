def is_pangram(st):
  for l in range(ord('a'), ord('z')):
    if chr(l) not in st.lower():
      return False
  return True

