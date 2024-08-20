import sys
import re

def convert_to_binary16(dec_input):
    return format(dec_input, '016b')

def A_INSTRUCTION_DIGIT_to_binary(instruction):
    return str(convert_to_binary16(int(instruction[1:len(instruction)]))) #take out @, convert to 16 bit binary

def A_INSTRUCTION_VARIABLE_to_binary(instruction):
    value = symbols[instruction[1:len(instruction)]] #get value from symbol table with @ removed
    return str(convert_to_binary16(int(value)))

def remove_comments(text):
    x = re.search('//', text) #search for //
    start_end = x.span() #start_end becomes a tuple for the start and end of the comment
    start_of_comment = int(start_end[0]) #transform tuple into single int for start
    text = text[0:start_of_comment] #remove comment
    text = text.strip() #remove whitespace
    return text

def dest (dest_input):
    if dest_input == 'M':
        return '001'
    elif dest_input == 'D':
        return '010'
    elif dest_input == 'DM' or dest_input == 'MD':
        return '011'
    elif dest_input == 'A':
        return '100'
    elif dest_input == 'AM' or dest_input == 'MA':
        return '101'
    elif dest_input == 'AD' or dest_input == 'DA':
        return '110'
    elif dest_input == 'ADM' or dest_input == 'AMD' or dest_input == 'MAD' or dest_input == 'MDA' or dest_input == 'DMA' or dest_input ==  'DAM':
        return '111'

def jump (jump_input):
    if jump_input == 'JGT':
        return '001'
    elif jump_input == 'JEQ':
        return '010'
    elif jump_input == 'JGE':
        return '011'
    elif jump_input == 'JLT':
        return '100'
    elif jump_input == 'JNE':
        return '101'
    elif jump_input == 'JLE':
        return '110'
    elif jump_input == 'JMP':
        return '111'

def comp (comp_input):
    if comp_input == '0':
        return '0101010'
    elif comp_input == '1':
        return '0111111'
    elif comp_input == '-1':
        return '0111010'
    elif comp_input == 'D':
        return '0001100'
    elif comp_input == 'A':
        return '0110000'
    elif comp_input == '!D':
        return '0001101'
    elif comp_input == '!A':
        return '0110001'
    elif comp_input == '-D':
        return '0001111'
    elif comp_input == '-A':
        return '0110011'
    elif comp_input == 'D+1':
        return '0011111'
    elif comp_input == 'A+1':
        return '0110111'
    elif comp_input == 'D-1':
        return '0001110'
    elif comp_input == 'A-1':
        return '0110010'
    elif comp_input == 'D+A':
        return '0000010'
    elif comp_input == 'D-A':
        return '0010011'
    elif comp_input == 'A-D':
        return '0000111'
    elif comp_input == 'D&A':
        return '0000000'
    elif comp_input == 'D|A':
        return '0010101'
    elif comp_input == 'M':
        return '1110000'
    elif comp_input == '!M':
        return '1110001'
    elif comp_input == '-M':
        return '1110011'
    elif comp_input == 'M+1':
        return '1110111'
    elif comp_input == 'M-1':
        return '1110010'
    elif comp_input == 'D+M':
        return '1000010'
    elif comp_input == 'D-M':
        return '1010011'
    elif comp_input == 'M-D':
        return '1000111'
    elif comp_input == 'D&M':
        return '1000000'
    elif comp_input == 'D|M':
        return '1010101'

def instructionType (instruction_type_input):
    if not instruction_type_input.strip(): #if blank
        return 'NO INSTRUCTION'
    elif instruction_type_input[0] == '@':
         return 'A_INSTRUCTION'
    elif instruction_type_input[0] == "(":
        return 'L_INSTRUCTION'
    else:
        return 'C_INSTRUCTION'

first_pass_counter = 0
second_pass_counter = 16

def first_pass(instruction):
    global first_pass_counter
    type_of_instruction = instructionType(instruction)
    if type_of_instruction == 'L_INSTRUCTION':
        parenthesis_removed = instruction[1:len(instruction)-1]
        if parenthesis_removed not in symbols:
            symbols[parenthesis_removed] = first_pass_counter #add to symbol table
    else:
        first_pass_counter += 1

def second_pass(instruction):
    global second_pass_counter
    type_of_instruction = instructionType(instruction)
    if type_of_instruction == 'A_INSTRUCTION':
        instruction_at_removed = instruction[1:len(instruction)]
        if not instruction_at_removed.isnumeric():
            if instruction_at_removed not in symbols:
                symbols[instruction_at_removed] = second_pass_counter
                second_pass_counter +=1

def parse(instruction):
    type_of_instruction = instructionType(instruction)
    if type_of_instruction == 'A_INSTRUCTION':
        # remove the @ symbol
        at_removed = instruction[1:len(instruction)]
        if at_removed.isnumeric():
            list_of_instructions_binary.append(A_INSTRUCTION_DIGIT_to_binary(instruction))
        else:
            list_of_instructions_binary.append(A_INSTRUCTION_VARIABLE_to_binary(instruction))
    elif type_of_instruction == 'C_INSTRUCTION':
        c_output = ['111', '0000000', '000', '000']
        search_for_equal = re.search('=', instruction)
        search_for_semi = re.search(';', instruction)

        # just a comp
        if search_for_equal == None and search_for_semi == None:
            comp_instruction = instruction
            c_output[1] = comp(comp_instruction)
            output = ''.join(c_output)
            list_of_instructions_binary.append(output)

            # comp and dest
        elif search_for_semi == None:
            start_end_equal = search_for_equal.span()
            start_of_equal = int(start_end_equal[0])
            dest_instruction = instruction[0:start_of_equal]
            comp_instruction = instruction[start_of_equal + 1:len(instruction)]
            c_output[1] = comp(comp_instruction)
            c_output[2] = dest(dest_instruction)
            output = ''.join(c_output)
            list_of_instructions_binary.append(output)

            # comp and jump
        elif search_for_equal == None:
            start_end_semi = search_for_semi.span()
            start_of_semi = int(start_end_semi[0])
            comp_instruction = instruction[0:start_of_semi]
            jump_instruction = instruction[start_of_semi + 1:len(instruction)]
            c_output[1] = comp(comp_instruction)
            c_output[3] = jump(jump_instruction)

            output = ''.join(c_output)
            list_of_instructions_binary.append(output)

# Initialization
symbols = {'R0': 0, 'R1': 1, 'R2': 2, 'R3': 3, 'R4': 4, 'R5': 5, 'R6': 6, 'R7': 7, 'R8': 8, 'R9': 9, 'R10': 10, 'R11': 11,
           'R12': 12, 'R13': 13, 'R14': 14, 'R15': 15, 'SP': 0, 'LCL': 1, 'ARG': 2, 'THIS': 3,'THAT': 4,'SCREEN': 16384,
           'KBD': 24576}
list_of_instructions_binary = []

#first pass
with open('Prog.asm', 'r+', encoding="utf-8") as assembly_file:
    for line in assembly_file:
        current_instruction = line.strip() #strip white space before and after
        if not current_instruction.strip(): #if blank, go next line
            continue
        elif current_instruction[0] == '/': #if it is just a comment
            continue
        else:
            search_for_comments = re.search("//", current_instruction)
            if search_for_comments == None: ##lines
                first_pass(current_instruction)
            else:
                current_instruction = remove_comments(current_instruction)
                first_pass(current_instruction)

#second pass
with open('Prog.asm', 'r+', encoding="utf-8") as assembly_file:
    for line in assembly_file:
        current_instruction = line.strip() #strip white space before and after
        if not current_instruction.strip(): #if blank, go next line
            continue
        elif current_instruction[0] == '/': #if it is just a comment
            continue
        else:
            search_for_comments = re.search("//", current_instruction)
            if search_for_comments == None: ##lines
                second_pass(current_instruction)
            else:
                current_instruction = remove_comments(current_instruction)
                second_pass(current_instruction)

#parse
with open('Prog.asm', 'r+', encoding="utf-8") as assembly_file:
    for line in assembly_file:
        current_instruction = line.strip() #strip white space before and after
        if not current_instruction.strip(): #if blank, go next line
            continue
        elif current_instruction[0] == '/': #if it is just a comment
            continue
        else:
            search_for_comments = re.search("//", current_instruction)
            if search_for_comments == None:
                parse(current_instruction)
            else:
                current_instruction = remove_comments(current_instruction)
                parse(current_instruction)

with open("Prog1.hack", "w") as output:
    for x in list_of_instructions_binary:
        output.write(str(x))
        output.write('\n')




