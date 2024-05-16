def to_jaden_case(string):
    # Split the string into words
    words = string.split()
    
    # Capitalize each word and handle contractions
    jaden_cased_words = [word.capitalize() for word in words]
    
    # Join the words back into a single string
    jaden_cased_string = ' '.join(jaden_cased_words)
    
    return jaden_cased_string

# Example usage
input_string = "How can mirrors be real if our eyes aren't real"
jaden_cased_string = to_jaden_case(input_string)
print(jaden_cased_string)
