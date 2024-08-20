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
(Class1.set)
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
// pop static
@Class1.0
D=A
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
// pop static
@Class1.1
D=A
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
(Class1.get)
// push static
@Class1.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static
@Class1.1
D=M
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
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant
@8
D=A
@SP
A=M
M=D
@SP
M=M+1
// push return address
@Class1.set$ret.0
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
@2
D=D-A
@ARG
M=D
// lcl eq sp
@SP
D=M
@LCL
M=D
// goto function
@Class1.set
0;JMP
(Class1.set$ret.0)
// pop temp
@5
D=A
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
@23
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant
@15
D=A
@SP
A=M
M=D
@SP
M=M+1
// push return address
@Class2.set$ret.1
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
@2
D=D-A
@ARG
M=D
// lcl eq sp
@SP
D=M
@LCL
M=D
// goto function
@Class2.set
0;JMP
(Class2.set$ret.1)
// pop temp
@5
D=A
@R13
M=D
@SP
M=M-1
A=M
D=M
@R13
A=M
M=D
// push return address
@Class1.get$ret.2
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
@Class1.get
0;JMP
(Class1.get$ret.2)
// push return address
@Class2.get$ret.3
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
@Class2.get
0;JMP
(Class2.get$ret.3)
// label
(Sys.init$WHILE)
// goto
@Sys.init$WHILE
0;JMP
(Class2.set)
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
// pop static
@Class2.0
D=A
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
// pop static
@Class2.1
D=A
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
(Class2.get)
// push static
@Class2.0
D=M
@SP
A=M
M=D
@SP
M=M+1
// push static
@Class2.1
D=M
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
