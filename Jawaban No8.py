def analyze_sentence(sentence):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0
    word_count = 0

    for char in sentence:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    words = sentence.split()
    word_count = len(words)

    return vowel_count, consonant_count, word_count

# Get input from the user
input_sentence = input("Masukkan kalimat: ")

# Analyze the sentence
vowel_count, consonant_count, word_count = analyze_sentence(input_sentence)

# Print the results
print("Jumlah huruf vokal:", vowel_count)
print("Jumlah huruf konsonan:", consonant_count)
print("Jumlah kata:", word_count)
