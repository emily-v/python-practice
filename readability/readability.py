def main():
    text = input("Text: ")
    letters = 0
    words = 1
    sentences = 0

    for c in text:
        if ord(c.lower()) >= ord("a") and ord(c.lower()) <= ord("z"):
            letters += 1
        if c == " ":
            words += 1
        if(c == '.' or c == '?' or c == '!'):
            sentences += 1
    
    print(f"letters: {letters} words: {words} sentences: {sentences}")       
    level = calculateLevel(letters, words, sentences)
    
    printGrade(level)
    
def calculateLevel(letters, words, sentences):
    lettersPer100Words = float(letters) / float(words) * 100
    sentencesPer100Words = float(sentences) / float(words) * 100
    level = 0.0588 * lettersPer100Words - 0.296 * sentencesPer100Words - 15.8
    return round(level)
    
def printGrade(level):
    if level < 1:
        print("Before Grade 1")
    elif level > 16:
        print("Grade 16+")
    else:
        print(f"Grade: {level}")

    
    
main()