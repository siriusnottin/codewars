def DNA_strand(dna):
  complementary_dna = ""
  for l in dna:
    # for each letter, if its a A convert it into T
    # if its a C->G
    if l == 'A':
      complementary_dna += 'T'
    elif l == 'T':
        complementary_dna += 'A'
    elif l == 'C':
      complementary_dna += 'G'
    elif l == 'G':
        complementary_dna += 'C'
  return complementary_dna
