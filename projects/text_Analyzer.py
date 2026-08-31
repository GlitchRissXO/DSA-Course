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

def clean(text):
    words = text.split()
    cleaned = []
    for word in words:
        cleaned.append(word.strip(".,!?").lower())
    return cleaned

def wordCount(text):
    return len(clean(text))

def uniqueWords(text):
   return
    
def longestWord(text):
    return

def wordFrequencies(text):
    return
    
def topThreeCommonWords(text):
    return
    
print(clean("The cat sat. The MAT!"))
