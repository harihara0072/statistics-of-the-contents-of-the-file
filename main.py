#prompting the user to enter the file name
file_name = input("What is the file name:")

#checking of the file name is valid or not
try:
    
    #opening the file in read mode
    file = open(file_name, 'r')
    
    #reading the lines in the file using readlines()
    lines = file.readlines()
    
    #counting the number of lines
    lines_count = len(lines)
    word_count = 0
    char_count = 0
    
    #iterating through each line
    for line in lines:
        
        #spliting the line for words
        words = line.split()
        word_count += len(words)
        
        #checking the length of each line for the number of charecters
        for word in words:
            char_count += len(word)
            
    #Calculating the average number of charecters per word and printing.        
    average = char_count / word_count
    print(f'Number of lines: {lines_count}')
    print(f'Number of words: {word_count} ')
    print(f'Number of characters: {char_count}')
    print(f'Average length of a word: {average}')
    
except:
    print("Please enter the valid file name")
