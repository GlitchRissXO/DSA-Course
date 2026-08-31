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

TEXT = """
The cat sat on the mat. The mat was extraordinary, or so the cat believed.
Every morning the cat would sit, and every morning the mat would hold.
A dog once questioned the arrangement. The cat did not respond. The dog left.
"""

def clean(text): # clean the text
    
    words = text.split()
    cleaned = []
    for word in words:
        cleaned.append(word.strip(".,!?").lower())
    return cleaned

def wordCount(text): # word count
    
    return len(clean(text))

def uniqueWords(text): # words used
    
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

def topThreeWords(text, n=3): # top three words used
    
    topThree = []
    counts = wordFrequencies(text).copy()
    
    for _ in range(n):
        
        best_word = None
        best_count = 0
        
        for word, count in counts.items():
            if count > best_count:
                best_word = word
                best_count = count
                
        topThree.append((best_word, best_count))
        del counts[best_word]
    
    return topThree
    
print("Words: ", wordCount(TEXT))
print("Unique Words: ", uniqueWords(TEXT))
print("Longest Word: ", longestWord(TEXT))
print("Word Frequencies: ", wordFrequencies(TEXT))
print("Top Three Words: ", topThreeWords(TEXT))