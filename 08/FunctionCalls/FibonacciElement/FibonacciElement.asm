// BOOTSTRAP
// SP equals 256
@256
D=A
@SP
M=D
// push return address
@Sys.init$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push lcl
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push arg
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// reposition arg
@5
D=A
@SP
D=M-D
@0
D=D-A
@ARG
M=D
// lcl eq sp
@SP
D=M
@LCL
M=D
// goto function
@Sys.init
0;JMP
(Sys.init$ret.0)
// END BOOTSTRAP
(Main.fibonacci)
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
// lt
@SP
M=M-1
A=M
D=M
@SP
M=M-1
A=M
D=M-D
@TRUE0
D;JLT
D=0
@SP
A=M
M=D
@SP
M=M+1
@END0
0;JMP
(TRUE0)
D=-1
@SP
A=M
M=D
@SP
M=M+1
(END0)
// if goto
@SP
M=M-1
A=M
D=M
@Main.fibonacci$IF_TRUE
D;JNE
// goto
@Main.fibonacci$IF_FALSE
0;JMP
// label
(Main.fibonacci$IF_TRUE)
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
// set frame
@LCL
D=M
@R13
M=D
// set return address
@5
D=A
@R13
A=M-D
D=M
@R14
M=D
// arg equals pop
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// restore SP
@ARG
D=M+1
@SP
M=D
// restore that
@R13
A=M-1
D=M
@THAT
M=D
// restore this
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
// restore arg
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
// restore lcl
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
// goto return address
@R14
A=M
0;JMP
// label
(Main.fibonacci$IF_FALSE)
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
// push return address
@Main.fibonacci$ret.0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push lcl
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push arg
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// reposition arg
@5
D=A
@SP
D=M-D
@1
D=D-A
@ARG
M=D
// lcl eq sp
@SP
D=M
@LCL
M=D
// goto function
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.0)
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
// push return address
@Main.fibonacci$ret.1
D=A
@SP
A=M
M=D
@SP
M=M+1
// push lcl
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push arg
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// reposition arg
@5
D=A
@SP
D=M-D
@1
D=D-A
@ARG
M=D
// lcl eq sp
@SP
D=M
@LCL
M=D
// goto function
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.1)
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
// set frame
@LCL
D=M
@R13
M=D
// set return address
@5
D=A
@R13
A=M-D
D=M
@R14
M=D
// arg equals pop
@SP
M=M-1
A=M
D=M
@ARG
A=M
M=D
// restore SP
@ARG
D=M+1
@SP
M=D
// restore that
@R13
A=M-1
D=M
@THAT
M=D
// restore this
@R13
D=M
@2
A=D-A
D=M
@THIS
M=D
// restore arg
@R13
D=M
@3
A=D-A
D=M
@ARG
M=D
// restore lcl
@R13
D=M
@4
A=D-A
D=M
@LCL
M=D
// goto return address
@R14
A=M
0;JMP
(Sys.init)
// push constant
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// push return address
@Main.fibonacci$ret.2
D=A
@SP
A=M
M=D
@SP
M=M+1
// push lcl
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// push arg
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// reposition arg
@5
D=A
@SP
D=M-D
@1
D=D-A
@ARG
M=D
// lcl eq sp
@SP
D=M
@LCL
M=D
// goto function
@Main.fibonacci
0;JMP
(Main.fibonacci$ret.2)
// label
(Sys.init$WHILE)
// goto
@Sys.init$WHILE
0;JMP
