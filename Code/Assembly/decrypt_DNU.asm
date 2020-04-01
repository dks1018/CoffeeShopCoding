Encrypt Function
push ebp
mov ebp,esp
pop ebp
ret

Decrypt Function
push ebp
mov ebp,esp
add dword [arg_8h], 0x26
xor dword [arg_8h], 0x37
xor dword [arg_8h], 0x11e61
not dword [arg_8h]
xor dword [arg_8h], 0x7a69
sub dword [arg_8h], 0x18
mov eax, dword [arg_8h]
pop ebp
ret

push ebp
mov ebp,esp
mov eax, 4
add eax, 0x26
xor eax, 0x37
xor eax, 0x11e61
not eax
xor eax, 0x7a69
sub eax, 0x18
pop ebp
ret

e asm.arch=x86 # Set architecture to x86
e asm.bits=32 # Set bits to 32
waf encrypt.asm # Read assembly from file
aei # Initialize VM State
aeim # Initialize VM Stack
aeip # Initialize VM EIP to current seek
dr
aes
aes
aes
dr

