import glob
import os


def get_last_component(path):
    # Normalize the path to handle different OS-specific path separators
    path = os.path.normpath(path)
    # Get the last component of the path
    return os.path.basename(path)


def command_type(command):
    if command.split()[0] in arithmetic_commands:
        return 'C_ARITHMETIC'
    elif command.split()[0] == 'push':
        return 'C_PUSH'
    elif command.split()[0] == 'pop':
        return 'C_POP'
    elif command.split()[0] == 'label':
        return 'label'
    elif command.split()[0] == 'if-goto':
        return 'if-goto'
    elif command.split()[0] == 'goto':
        return 'goto'
    elif command.split()[0] == 'function':
        return 'declare_function'
    elif command.split()[0] == 'return':
        return 'return'
    elif command.split()[0] == 'call':
        return 'call'


def arg1(command):
    if command_type(command) == 'C_ARITHMETIC':
        return command.split()[0]
    else:
        return command.split()[1]


def arg2(command):
    return command.split()[2]


def constant_to_d(arg2):  # appending instructions for adding a constant to D register
    constant_to_d_instructions = ['@' + arg2, 'D=A']
    for instruction in constant_to_d_instructions:
        list_of_assembly_instructions.append(instruction)


def push_d_onto_stack():
    list_of_instructions_for_d_onto_stack = ['@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    for instruction in list_of_instructions_for_d_onto_stack:
        list_of_assembly_instructions.append(instruction)


def set_a_to_top_stack():
    list_of_instructions_set_a_to_top_stack = ['@SP', 'M=M-1', 'A=M']
    for instruction in list_of_instructions_set_a_to_top_stack:
        list_of_assembly_instructions.append(instruction)


def sp_plus_one():
    list_of_instructions_sp_plus_one = ['@SP', 'M=M+1']
    for instruction in list_of_instructions_sp_plus_one:
        list_of_assembly_instructions.append(instruction)


def sp_minus_one():
    list_of_instructions_sp_plus_one = ['@SP', 'M=M-1']
    for instruction in list_of_instructions_sp_plus_one:
        list_of_assembly_instructions.append(instruction)


def pop_storeD_pop():
    list_of_instructions_pop_storeD_pop = ['@SP', 'M=M-1', 'A=M', 'D=M', '@SP', 'M=M-1', 'A=M']
    for instruction in list_of_instructions_pop_storeD_pop:
        list_of_assembly_instructions.append(instruction)


def true_false():
    #  after the comparison test, contains branches for false, tue and ends the comp
    list_of_instructions_true_false = ['D=0', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1', '@END' + str(comp_counter), '0;JMP',
                                       '(TRUE' + str(comp_counter) + ')', 'D=-1', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1',
                                       '(END' + str(comp_counter) + ')']
    for instruction in list_of_instructions_true_false:
        list_of_assembly_instructions.append(instruction)


def add():
    pop_storeD_pop()
    list_of_assembly_instructions.append('D=D+M')  # add current popped valued to previous popped value, set to D
    push_d_onto_stack()


def sub():
    pop_storeD_pop()
    list_of_assembly_instructions.append('D=M-D')  # add current popped valued to previous popped value, set to D
    push_d_onto_stack()


def f_and():
    pop_storeD_pop()
    list_of_assembly_instructions.append('D=M&D')
    push_d_onto_stack()


def f_or():
    pop_storeD_pop()
    list_of_assembly_instructions.append('D=M|D')
    push_d_onto_stack()


def f_not():
    set_a_to_top_stack()
    list_of_assembly_instructions.append('M=!M')  # set D to neg popped value
    sp_plus_one()


def neg():
    set_a_to_top_stack()
    list_of_assembly_instructions.append('M=-M')  # set D to neg popped value
    sp_plus_one()


def eq():
    pop_storeD_pop()
    eq_test = ['D=D-M', '@TRUE' + str(comp_counter), 'D;JEQ']  # subtracts top two; jumps if 0
    for instruction in eq_test:
        list_of_assembly_instructions.append(instruction)
    true_false()


def lt():
    pop_storeD_pop()
    lt_test = ['D=M-D', '@TRUE' + str(comp_counter), 'D;JLT']  # subtracts top two; jumps if 0
    for instruction in lt_test:
        list_of_assembly_instructions.append(instruction)
    true_false()


def gt():
    pop_storeD_pop()
    gt_test = ['D=M-D', '@TRUE' + str(comp_counter), 'D;JGT']
    for instruction in gt_test:
        list_of_assembly_instructions.append(instruction)
    true_false()


def set_r13_pop():
    set_r13_pop_instr = ['D=M+D', '@R13', 'M=D', '@SP', 'M=M-1', 'A=M', 'D=M', '@R13', 'A=M', 'M=D']
    for instruction in set_r13_pop_instr:
        list_of_assembly_instructions.append(instruction)


def temp_r13_pop():
    temp_r13_pop_instr = ['@R13', 'M=D', '@SP', 'M=M-1', 'A=M', 'D=M', '@R13', 'A=M', 'M=D']
    for instruction in temp_r13_pop_instr:
        list_of_assembly_instructions.append(instruction)


def pop_static():
    static_var = '@' + file_name + '.' + arg2(current_command)
    list_of_assembly_instructions.append(static_var)
    pop_static_instr = ['D=A', '@R13', 'M=D', '@SP', 'M=M-1', 'A=M', 'D=M', '@R13', 'A=M', 'M=D']
    for instruction in pop_static_instr:
        list_of_assembly_instructions.append(instruction)


def push_static():
    static_var = '@' + file_name + '.' + arg2(current_command)
    list_of_assembly_instructions.append(static_var)
    list_of_assembly_instructions.append('D=M')
    push_d_onto_stack()


def label():
    list_of_assembly_instructions.append('// label')
    list_of_assembly_instructions.append('(' + current_function + '$' + arg1(current_command) + ')')


def if_goto():
    set_a_to_top_stack()
    list_of_assembly_instructions.append('D=M')
    list_of_assembly_instructions.append('@' + current_function + '$' + arg1(current_command))
    list_of_assembly_instructions.append('D;JNE') # jump if D is not 0, i.e. if not false


def goto():
    list_of_assembly_instructions.append('// goto')
    list_of_assembly_instructions.append('@' + current_function + '$' + arg1(current_command))
    list_of_assembly_instructions.append('0;JMP') # jump if D is not 0, i.e. if not false


def declare_function():
    list_of_assembly_instructions.append('(' + arg1(current_command) + ')')
    counter = 0
    while counter < int(arg2(current_command)):
        constant_to_d(str(0))
        push_d_onto_stack()
        counter += 1


def frame_eq_lcl():
    instruction_list = ['// set frame', '@LCL', 'D=M', '@R13', 'M=D']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def ret_addr():
    instruction_list = ['// set return address', '@5', 'D=A', '@R13', 'A=M-D', 'D=M', '@R14', 'M=D']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def arg_eq_pop():
    instruction_list = ['// arg equals pop', '@SP', 'M=M-1', 'A=M', 'D=M', '@ARG', 'A=M', 'M=D']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def restore_sp():
    instruction_list = ['// restore SP', '@ARG', 'D=M+1', '@SP', 'M=D']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def restore_that():
    instruction_list = ['// restore that', '@R13', 'A=M-1', 'D=M', '@THAT', 'M=D']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def restore_this():
    instruction_list = ['// restore this', '@R13', 'D=M', '@2', 'A=D-A', 'D=M', '@THIS', 'M=D']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def restore_arg():
    instruction_list = ['// restore arg', '@R13', 'D=M', '@3', 'A=D-A', 'D=M', '@ARG', 'M=D']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def restore_lcl():
    instruction_list = ['// restore lcl', '@R13', 'D=M', '@4', 'A=D-A', 'D=M', '@LCL', 'M=D']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def goto_retaddr():
    instruction_list = ['// goto return address', '@R14', 'A=M', '0;JMP']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def return_assembly():
    frame_eq_lcl()
    ret_addr()
    arg_eq_pop()
    restore_sp()
    restore_that()
    restore_this()
    restore_arg()
    restore_lcl()
    goto_retaddr()


def push_ret_addr():
    instruction_list = ['// push return address', '@' + arg1(current_command) +
                        "$ret." + str(return_counter), 'D=A', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def push_lcl():
    instruction_list = ['// push lcl', '@LCL', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def push_arg():
    instruction_list = ['// push arg', '@ARG', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def push_this():
    instruction_list = ['// push THIS', '@THIS', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def push_that():
    instruction_list = ['// push THAT', '@THAT', 'D=M', '@SP', 'A=M', 'M=D', '@SP', 'M=M+1']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def reposition_arg():
    instruction_list = ['// reposition arg', '@5', 'D=A', '@SP', 'D=M-D', '@' + arg2(current_command), 'D=D-A', '@ARG',
                        'M=D']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def lcl_eq_sp():
    instruction_list = ['// lcl eq sp', '@SP', 'D=M', '@LCL', 'M=D']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def goto_f():
    instruction_list = ['// goto function', '@' + arg1(current_command), '0;JMP']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


def return_address_label():
    list_of_assembly_instructions.append('(' + arg1(current_command) + "$ret." + str(return_counter) + ')')


def call_function():
    push_ret_addr()
    push_lcl()
    push_arg()
    push_this()
    push_that()
    reposition_arg()
    lcl_eq_sp()
    goto_f()
    return_address_label()


def sp_eq_256():
    instruction_list = ['// SP equals 256', '@256', 'D=A', '@SP', 'M=D']
    for instruction in instruction_list:
        list_of_assembly_instructions.append(instruction)


#  Initialization
arithmetic_commands = ('add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not')  # tuple i.e. unchangeable
list_of_assembly_instructions = []
current_function = '' # variable for current function to for label, goto, if-goto
return_counter = 0 # counter for every return
comp_counter = 0  # counter for every comparison done so that there are unique branching RAM locations

# bootstrap
list_of_assembly_instructions.append('// BOOTSTRAP')
sp_eq_256()
current_command = 'call Sys.init 0'
call_function()
list_of_assembly_instructions.append('// END BOOTSTRAP')

# Specify the directory containing your files
directory = '/Users/eric/PycharmProjects/Nand2Tetris/StaticsTest'
folder = 'StaticsTest'
file_pattern = os.path.join(directory, '*.vm')
file_list = glob.glob(file_pattern)

for file_path in file_list:
    if os.path.isfile(file_path):  # Ensure it's a file
        with open(file_path, 'r+', encoding="utf-8") as vm_file:
            file_name = get_last_component(file_path).split('.', 1)[0]

            for line in vm_file:
                current_command = line.strip()  # strip white space before and after
                if not current_command.strip():  # if blank, go next line
                    continue
                elif current_command[0] == '/':  # if it is just a comment because / is the first letter, go to next line
                    continue
                else:
                    if command_type(current_command) == 'C_ARITHMETIC':
                        if arg1(current_command) == 'add':
                            list_of_assembly_instructions.append('// add')
                            add()
                        elif arg1(current_command) == 'sub':
                            list_of_assembly_instructions.append('// sub')
                            sub()
                        elif arg1(current_command) == 'neg':
                            list_of_assembly_instructions.append('// neg')
                            neg()
                        elif arg1(current_command) == 'not':
                            list_of_assembly_instructions.append('// not')
                            f_not()
                        elif arg1(current_command) == 'and':
                            list_of_assembly_instructions.append('// and')
                            f_and()
                        elif arg1(current_command) == 'or':
                            list_of_assembly_instructions.append('// or')
                            f_or()
                        elif arg1(current_command) == 'eq':
                            list_of_assembly_instructions.append('// eq')
                            eq()
                            comp_counter += 1
                        elif arg1(current_command) == 'lt':
                            list_of_assembly_instructions.append('// lt')
                            lt()
                            comp_counter += 1
                        elif arg1(current_command) == 'gt':
                            list_of_assembly_instructions.append('// gt')
                            gt()
                            comp_counter += 1
                    elif command_type(current_command) == 'C_PUSH':
                        if arg1(current_command) == 'constant':
                            list_of_assembly_instructions.append('// push constant')
                            constant_to_d(arg2(current_command))
                            push_d_onto_stack()
                        elif arg1(current_command) == 'local':
                            list_of_assembly_instructions.append('// push local')
                            constant_to_d(arg2(current_command))
                            list_of_assembly_instructions.append('@LCL')
                            list_of_assembly_instructions.append('A=M+D')
                            list_of_assembly_instructions.append('D=M')
                            push_d_onto_stack()
                        elif arg1(current_command) == 'that':
                            list_of_assembly_instructions.append('// push that')
                            constant_to_d(arg2(current_command))
                            list_of_assembly_instructions.append('@THAT')
                            list_of_assembly_instructions.append('A=M+D')
                            list_of_assembly_instructions.append('D=M')
                            push_d_onto_stack()
                        elif arg1(current_command) == 'argument':
                            list_of_assembly_instructions.append('// push argument')
                            constant_to_d(arg2(current_command))
                            list_of_assembly_instructions.append('@ARG')
                            list_of_assembly_instructions.append('A=M+D')
                            list_of_assembly_instructions.append('D=M')
                            push_d_onto_stack()
                        elif arg1(current_command) == 'this':
                            list_of_assembly_instructions.append('// push this')
                            constant_to_d(arg2(current_command))
                            list_of_assembly_instructions.append('@THIS')
                            list_of_assembly_instructions.append('A=M+D')
                            list_of_assembly_instructions.append('D=M')
                            push_d_onto_stack()
                        elif arg1(current_command) == 'temp':
                            list_of_assembly_instructions.append('// push temp')
                            temp_value = 5 + int(arg2(current_command))
                            list_of_assembly_instructions.append('@' + str(temp_value))
                            list_of_assembly_instructions.append('D=M')
                            push_d_onto_stack()
                        elif arg1(current_command) == 'pointer':
                            list_of_assembly_instructions.append('// push pointer')
                            constant_to_d(arg2(current_command))
                            list_of_assembly_instructions.append('@THIS')
                            list_of_assembly_instructions.append('A=A+D')
                            list_of_assembly_instructions.append('D=M')
                            push_d_onto_stack()
                        elif arg1(current_command) == 'static':
                            list_of_assembly_instructions.append('// push static')
                            push_static()
                    elif command_type(current_command) == 'C_POP':
                        if arg1(current_command) == 'local':
                            list_of_assembly_instructions.append('// pop local')
                            constant_to_d(arg2(current_command))
                            list_of_assembly_instructions.append('@LCL')
                            set_r13_pop()
                        elif arg1(current_command) == 'argument':
                            list_of_assembly_instructions.append('// pop arg')
                            constant_to_d(arg2(current_command))
                            list_of_assembly_instructions.append('@ARG')
                            set_r13_pop()
                        elif arg1(current_command) == 'this':
                            list_of_assembly_instructions.append('// pop this')
                            constant_to_d(arg2(current_command))
                            list_of_assembly_instructions.append('@THIS')
                            set_r13_pop()
                        elif arg1(current_command) == 'that':
                            list_of_assembly_instructions.append('// pop that')
                            constant_to_d(arg2(current_command))
                            list_of_assembly_instructions.append('@THAT')
                            set_r13_pop()
                        elif arg1(current_command) == 'temp':
                            list_of_assembly_instructions.append('// pop temp')
                            temp_value = 5 + int(arg2(current_command))
                            list_of_assembly_instructions.append('@' + str(temp_value))
                            list_of_assembly_instructions.append('D=A')
                            temp_r13_pop()
                        elif arg1(current_command) == 'pointer':
                            list_of_assembly_instructions.append('// pop pointer')
                            constant_to_d(arg2(current_command))
                            list_of_assembly_instructions.append('@THIS')
                            list_of_assembly_instructions.append('D=A+D')
                            temp_r13_pop()
                        elif arg1(current_command) == 'static':
                            list_of_assembly_instructions.append('// pop static')
                            pop_static()
                    elif command_type(current_command) == 'label':
                        label()
                    elif command_type(current_command) == 'if-goto':
                        list_of_assembly_instructions.append('// if goto')
                        if_goto()
                    elif command_type(current_command) == 'goto':
                        goto()
                    elif command_type(current_command) == 'declare_function':
                        current_function = arg1(current_command)  # set current function for loop, goto, if-goto
                        declare_function()
                    elif command_type(current_command) == 'return':
                        return_assembly()

                    elif command_type(current_command) == 'call':
                        call_function()
                        return_counter += 1


with open(folder + '.asm', "w") as output:
    for x in list_of_assembly_instructions:
        output.write(str(x))
        output.write('\n')


