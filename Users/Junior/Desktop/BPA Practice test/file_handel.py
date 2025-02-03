#makes two parameters the input file and the output file
def count_lines_in_file(input_file, output_file):
   #try except block to make it so if an error happens the except block goes just incase but it alwas works i had issues earlier.
    try:
        with open(input_file) as f:
            lines = f.readlines()
        line_count = len(lines) #counts the lines
    except FileNotFoundError:
        print("error: cant find file")
        return

    with open(output_file, 'w') as f:
        f.write(f'number of lines: {line_count}\n') #writes the amount of lines in the output file

count_lines_in_file('data.txt', 'output.txt')
