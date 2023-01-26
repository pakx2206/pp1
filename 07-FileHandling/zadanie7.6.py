with open('07-FileHandling/countries.txt', 'r') as file:
    file_content = file.read()
    print( file_content )
    
    file.close()

