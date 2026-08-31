# Module 01 Project
# Project: Text Analyzer
# Date: 08.26.2026
#
# PURPOSE:
# Taking a chunk of text and reporting on it. Applies problem decomposition
# and the counting pattern to a problem with five separate questions to answer.
# 
# RULES:
# Case-insensitive. Punctuation stripped. No imports.
# Two of these can be built on word_frequencies instead of re-reading the text.

from email.mime import text


def clean(text): # clean the text
    
    words = text.split()
    cleaned = []
    for word in words:
        cleaned.append(word.strip(".,!?").lower())
    return cleaned

def wordCount(text): # word count
    
    return len(clean(text))

def uniqueWords(text): # words used
    
    set(clean(text))
    return len(set(clean(text)))
    
def longestWord(text): # longest word
    
    longest_word = ""
    
    for word in clean(text):
        if len(word) > len(longest_word):
            longest_word = word
            
    return longest_word

def wordFrequencies(text): # How many times the words shows up
    
    wordFreqCount = {}
    
    for word in clean(text):
        if word in wordFreqCount:
            wordFreqCount[word] += 1
        else:
            wordFreqCount[word] = 1
    return wordFreqCount

def topThreeWords(text): # top three words used
    
    
    
    
    
    return
    
print(clean("The cat sat. The MAT!"))
