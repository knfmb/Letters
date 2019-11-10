char = input("Enter a letter in the English alphabet: ")
if (char == 'a'or char == 'e'or char == 'i'or char == 'o'or char == 'u'or char == 'A'or char == 'E'or char == 'I'or char == 'O'or char == 'U' ):
    print ("Letter ", char, "is a vowel!")
elif char in ('b','c','d','f','g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z', 'B','C','D','F','G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z'):
    print ("Letter ", char, "is a consonant!")
else:
    print ("Invalid character!")