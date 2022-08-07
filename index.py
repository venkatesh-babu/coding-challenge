import csv,sys,time
start = time.time()
find_words_file = open('find_words.txt')
french_dictionary_file = open('french_dictionary.csv')
core_file = open('t8.shakespeare.txt')
translated_file = open('t8.shakespeare.translated.txt','w')
line = ""; word = ""; givenwords = [];wordsreplaced = [];duplicateFrequencies = {}

# storing french_dictionary.csv file as dictionary named dict_from_csv
reader = csv.reader(french_dictionary_file)
dict_from_csv = {rows[0]:rows[1] for rows in reader}

# storing find_words.csv words in list
for words in find_words_file:
    givenwords.append(words.replace("\n",""))

for line in core_file:
    for word in line.split():
        initialword = word
        exclamation = False; startdot = False; enddot = False; startcomma = False; endcommo = False; semicolon = False; openparanthesis = False; closeparanthesis = False; opensquarebracket = False; closesquaerbracket = False; startapostrophe = False; endapostrophe = False; startdoublequotes = False; enddoublequotes = False; questionmark = False; colon = False
        
        # finding and removing special characters
        if "!" in word or "," in word or "." in word or ";" in word or "(" in word or ")" in word or "[" in word or "]" in word or "'" in word or '"' in word or "?" in word or ":" in word:
            if "!" in word:
                count = word.count("!")
                word = word.replace("!","")
                exclamation = True
            elif "," in word:
                startletter = word[0]
                endletter = x = word[len(word)-1]
                if startletter == ",":
                    word = word.replace(",","")
                    startcomma = True
                if endletter == ",":
                    word = word.replace(",","")
                    endcommo = True
            elif "." in word:
                startletter = word[0]
                endletter = x = word[len(word)-1]
                if startletter == ".":
                    word = word.replace(".","")
                    startdot = True
                if endletter == ".":
                    word = word.replace(".","")
                    enddot = True
            elif ";" in word:
                word = word.replace(";","")
                semicolon = True
            elif "(" in word:
                word = word.replace("(","")
                openparanthesis = True
            elif ")" in word:
                word = word.replace(")","")
                closeparanthesis = True
            elif "[" in word:
                word = word.replace("[","")
                opensquarebracket = True
            elif "]" in word:
                word = word.replace("]","")
                closesquaerbracket = True
            elif "'" in word:
                startletter = word[0]
                endletter = x = word[len(word)-1]
                if startletter == "'":
                    word = word.replace("'","")
                    startapostrophe = True
                if endletter == "'":
                    word = word.replace("'","")
                    endapostrophe = True
            elif '"' in word:
                startletter = word[0]
                endletter = x = word[len(word)-1]
                if startletter == '"':
                    word = word.replace('"',"")
                    startdoublequotes = True
                if endletter == '"':
                    word = word.replace('"',"")
                    enddoublequotes = True
            elif "?" in word:
                word = word.replace("?","") 
                questionmark = True
            elif ":" in word:
                word = word.replace(":","") 
                colon = True
    
        # replacing words from english to french and adding special characters according to their positions then writing it in t8.shakespeare.translated.txt
        if word in dict_from_csv.keys() and word in givenwords:
            wordsreplaced.append(word)
            if opensquarebracket: translated_file.write("[")
            if openparanthesis: translated_file.write("(")
            if startapostrophe: translated_file.write("'")
            if startdoublequotes: translated_file.write('"')  
            if startcomma:  translated_file.write(',')
            if startdot: translated_file.write('.') 
            
            translated_file.write(dict_from_csv[word])
            
            if endcommo: translated_file.write(',')
            if enddot: translated_file.write('.') 
            if enddoublequotes: translated_file.write('"')  
            if endapostrophe: translated_file.write("'")
            if closeparanthesis: translated_file.write(")")
            if closesquaerbracket: translated_file.write("]")
            if exclamation: 
                if count == 2: 
                    translated_file.write("!!")
                else:
                    translated_file.write("!")
            if questionmark: translated_file.write("?")
            if semicolon: translated_file.write(";")
            if colon: translated_file.write(":")
        else:
            translated_file.write(initialword)                             
                
        translated_file.write(" ")
    translated_file.write("\n")
end = time.time()

for i in set(wordsreplaced):
    duplicateFrequencies[i] = wordsreplaced.count(i)  
wordsreplaced = list(dict.fromkeys(wordsreplaced))
memory = sys.getsizeof(dict_from_csv)/(1048576)+sys.getsizeof(word)/(1048576)+sys.getsizeof(line)/(1048576)+sys.getsizeof(givenwords)/(1048576)+sys.getsizeof(duplicateFrequencies)/(1048576)+sys.getsizeof(wordsreplaced)/(1048576)+sys.getsizeof(exclamation)/(1048576)+sys.getsizeof(startdot)/(1048576)+sys.getsizeof(enddot)/(1048576)+sys.getsizeof(startcomma)/(1048576)+sys.getsizeof(endcommo)/(1048576)+sys.getsizeof(semicolon)/(1048576)+sys.getsizeof(openparanthesis)/(1048576)+sys.getsizeof(closeparanthesis)/(1048576)+sys.getsizeof(opensquarebracket)/(1048576)+sys.getsizeof(closesquaerbracket)/(1048576)+sys.getsizeof(startapostrophe)/(1048576)+sys.getsizeof(endapostrophe)/(1048576)+sys.getsizeof(startdoublequotes)/(1048576)+sys.getsizeof(enddoublequotes)/(1048576)+sys.getsizeof(questionmark)/(1048576)+sys.getsizeof(colon)/(1048576)

# Unique list of words that was replaced with French words from the dictionary
print(wordsreplaced)
print("\n")

# Number of times a word was replace
print(duplicateFrequencies)
print("\n")

# Time taken to process
print('Time to process')
print(end - start)
print("\n")

#  Memory taken to process
print('Memory used')
print(memory)