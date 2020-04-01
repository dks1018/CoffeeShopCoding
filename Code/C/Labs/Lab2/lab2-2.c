//main
int main(int argc, char const *argv[])
{
      //push  ebp
      int ebp;
  //mov ebp, esp
  int esp;
  ebp = esp;
  //sub esp, 16
  esp = esp - 16;
  //mov DWORD PTR [ebp-8], 10
  long *ebpPTR;
  ebpPTR[-8] = 10;
  //mov DWORD PTR [ebp-4], 14
  ebpPTR[-4]= 14;
  //mov eax, DWORD PTR [ebp-8]
  int eax = ebpPTR[-8];
  //cmp eax, DWORD PTR [ebp-4]
  //cmp compares to operands
  //compares source to destination
  eax == ebpPTR[-4];
  //jge .L2
  //the jge performs an unconditional jump
  

  //mov eax, 1
  eax = 1;
  //jmp .L3
goto L3;
//.L2:
  
  //mov eax, 2
eax = 2;
//.L3:
L3:
  //leave
  //ret
    return 0;
}
