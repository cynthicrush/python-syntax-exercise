def print_upper_words(list, must_start_with):
    '''if the words in the list start with any letters in must_start_with argument they return as uppercase letters'''

    for word in list:
      if word[0] in must_start_with:
        print(word.upper())



print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],must_start_with={"h", "y", "g"})
# this should print "HELLO", "HEY", "YO", and "YES"