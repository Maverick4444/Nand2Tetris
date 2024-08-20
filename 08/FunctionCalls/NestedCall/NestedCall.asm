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
(Sys.init)
// push constant
@4000
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer
@0
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
@5000
D=A
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
// push return address
@Sys.main$ret.0
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
@Sys.main
0;JMP
(Sys.main$ret.0)
// pop temp
@6
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
// label
(Sys.init$LOOP)
// goto
@Sys.init$LOOP
0;JMP
(Sys.main)
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// push constant
@4001
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer
@0
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
@5001
D=A
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
@200
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local
@1
D=A
@LCL
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
@40
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local
@2
D=A
@LCL
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
@6
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local
@3
D=A
@LCL
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
@123
D=A
@SP
A=M
M=D
@SP
M=M+1
// push return address
@Sys.add12$ret.1
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
@Sys.add12
0;JMP
(Sys.add12$ret.1)
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
// push local
@0
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local
@1
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local
@2
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local
@3
D=A
@LCL
A=M+D
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local
@4
D=A
@LCL
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
(Sys.add12)
// push constant
@4002
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop pointer
@0
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
@5002
D=A
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
@12
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
