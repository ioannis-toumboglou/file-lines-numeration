try:
    with open('output.txt', 'w') as newfile:
        with open('input.txt', 'r') as f:
            lines = f.readlines()
            count = 1
            for i in lines:
                i = i.strip()
                newline = str(count)+': '+i+'\n'
                newfile.write(newline)
                count += 1
                
except FileNotFoundError:
    print('Error: File not found...')

except:
    print('Error processing the file...')
