// push argument
@1
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// pop pointer
@1
D=A
@THIS
D=A+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push constant
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that
@0
D=A
@THAT
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push constant
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop that
@1
D=A
@THAT
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push argument
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1
// pop arg
@0
D=A
@ARG
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
(MAIN_LOOP_START)
// push argument
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// if goto
@SP
M=M-1
A=M
D=M
@COMPUTE_ELEMENT
D;JNE
@END_PROGRAM
0;JMP
(COMPUTE_ELEMENT)
// push that
@0
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push that
@1
D=A
@THAT
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D+M
@SP
A=M
M=D
@SP
M=M+1
// pop that
@2
D=A
@THAT
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push pointer
@1
D=A
@THIS
A=A+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=D+M
@SP
A=M
M=D
@SP
M=M+1
// pop pointer
@1
D=A
@THIS
D=A+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push argument
@0
D=A
@ARG
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@SP
A=M
M=D
@SP
M=M+1
// pop arg
@0
D=A
@ARG
D=M+D
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
@MAIN_LOOP_START
0;JMP
(END_PROGRAM)
