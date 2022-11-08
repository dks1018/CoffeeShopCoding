    ;Encrypt Function 
push ebp
mov ebp,esp
mov eax, 4;this can be any number and will encrypt the number then store it in ebx
sub eax, 0x18
xor eax, 0x7a69
not eax
xor eax, 0x11e61
xor eax, 0x37
add eax, 0x26
mov ebx, eax
    ;Decrypt
sub eax, 0x26;this takes the encrypted number from eax and decrpts it, in the registers you can can compare the number as it is being decrypted and the decrypted number is stored in eax
xor eax, 0x37
xor eax, 0x11e61
not eax
xor eax, 0x7a69
add eax, 0x18
pop ebp
ret

