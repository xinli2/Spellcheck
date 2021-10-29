###
### Author: Xin Li.
### Description: In this short PA, I will be writing
### The spell checking program should be named
### spellcheck.py. The spell check program that
### you will write should accept two inputs from the
### console. The first input will be the name of a text
### file, which will contain the text that the user
### wants to be spell-checked. The second input will
### be the mode that the program should operate in.
### The user can select to operate in one of two modes:
### suggest or replace mode. In suggest mode, the program
### should not actually make any changes to the text.
### Rather, it should annotate the text with suggestions
### for how to spell words differently. In replace mode,
### it should print out the contents of the input file
### with the spelling already fixed.
###
def get_word_conversions():
    file = open('misspellings.txt', 'r')
    conversions = { }
    lines = file.readlines()
    for line in lines:
        line = line.split(':')
        words = line[1].split(',')
        for word in words:
            conversions[word.strip()] = line[0]
    return conversions

def replace_mode(word, conversions):
    print(' ')
    print('--- OUTPUT ---')
    file_word = open(word, 'r')
    lines = file_word.readlines()
    new_word = []
    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        for i in range(len(line)):
            if line[i].lower() in conversions:
                if line[i][0].isupper():
                    new_word.append(conversions[line[i].lower()].capitalize())
            else:
                new_word.append(line[i])
        for i in new_word:
            print(i+' ', end='')
        print('')
        new_word=[]

def suggest_mode(word, conversions):
    print()
    print('--- OUTPUT ---')
    file_word = open(word, 'r')
    lines = file_word.readlines()
    new_word=[]
    suggest= []
    q = 1
    for line in lines:
        line = line.strip('\n')
        line = line.split(' ')
        for i in range(len(line)):
            if line[i].lower() in conversions:
                if line[i][0].isupper():
                    suggest.append('('+str(q)+') '+conversions[line[i].lower()].capitalize())
                    new_word.append(line[i]+' '+'('+str(q)+')')
                    q+=1
                else:
                    suggest.append('('+str(q)+') '+conversions[line[i]])
                    new_word.append(line[i]+' '+'('+str(q)+')')
                    q+=1
            else:
                new_word.append(line[i])
        for i in new_word:
            print(i+' ', end='')
        new_word=[]
        print('')
    print()
    print('--- LEGEND ---')
    for i in suggest:
        print(i)

def main():
    word = input('Enter input file:\n')
    conversions = get_word_conversions()
    method = input('Enter spellcheck mode (replace or suggest):\n')
    if method =='replace':
        replace_mode(word, conversions)
    if method =='suggest':
        suggest_mode(word, conversions)

main()
