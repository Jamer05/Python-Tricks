from PyDictionary import PyDictionary

dictionary=PyDictionary(input("Enter a word: "))

print(dictionary.printMeanings()) 
print ("\nSynonyms:",dictionary.getSynonyms())

print(dictionary.translateTo(dictionary)) 