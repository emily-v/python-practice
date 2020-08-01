import wordcloud
import sys
import os

def main(argv):
    length = len(argv)
    if length != 2:
        print(f"Incorrect number of args: {length} (need 2)!")
        return
    
    textFileName = argv[1]

    text = readTextFile(textFileName)
    words = getWordsOnly(text)
    word_frequencies = getFrequencies(words)

    generateWordCloud(word_frequencies)
    

def readTextFile(fileName):
    file = open(fileName).read()
    return file

def getWordsOnly(text):
    words = text.split()
    length = len(words)
    for w in range(length):
        for char in words[w]:
            if not char.isalpha():
                words[w] = words[w].replace(char, '')
    return words

def getFrequencies(words):
    frequencies = {}
    wordsToIgnore = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just", \
    "on", "for", "not", "in"]

    for w in words:
        word = w.lower()
        if word not in wordsToIgnore:
            if word not in frequencies.keys():
                frequencies[word] = 1
            else:
                frequencies[word] = frequencies[word] + 1
    return frequencies

def generateWordCloud(frequencies):
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    if not os.path.exists("output"):
        os.makedirs("output")
    cloud.to_file("output/wordcloud.jpg")


main(sys.argv)