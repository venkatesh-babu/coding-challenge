import csv
find_words_file = open('find_words.txt')
french_dictionary_file = open('french_dictionary.csv')
frequency_added_file = open('french_dictionary_frequency.csv')
core_file = open('t8.shakespeare.txt')
line = ""; word = ""; initial_count = ''; count = 0; c = ',';givenwords = [];frequency_count = {}

# storing french_dictionary.csv file as dictionary named dict_from_csv
reader = csv.reader(french_dictionary_file)
dict_from_csv = {rows[0]:rows[1] for rows in reader}

# storing find_words.csv words in list
for words in find_words_file:
    givenwords.append(words.replace("\n",""))

# getting values from french_dictionary_frequency.csv and storing it in dictionary named frequency_count
reader2 = csv.reader(frequency_added_file)
for w in reader2:
    frequency_count[w[0]] = {'french':w[1],'count':w[2]}

for line in core_file:
    for word in line.split():
        exclamation = False; dot = False; comma = False

        ## finding and removing special characters
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

        # calculating the number of times the word was replaced.
        if word in dict_from_csv.keys() and word in givenwords:
            if word in frequency_count.keys():
                initial_count = (frequency_count[word])["count"]
                count = int(initial_count)+1
                (frequency_count[word])["count"] = str(count)

# writing dictionary named dict_from_csv key and values in frequency.csv
headerList = ['English word','French word','Frequency']
with open('frequency.csv', 'w') as frequency_file:
    dw = csv.DictWriter(frequency_file, delimiter=',',fieldnames=headerList)
    dw.writeheader()
    for key in frequency_count.keys():
        frequency_file.write("%s, %s %s %s\n" %(key,frequency_count[key]["french"],',',frequency_count[key]["count"]))
    print("successfully calculated frequency and added in frequency.csv file")

