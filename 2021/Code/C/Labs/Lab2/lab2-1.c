#include <stdio.h>
#include <stdlib.h>

int main()
{

    //push  ebp
        //save the value of ebp
        //push the the value stored in ebp onto the stack
        int ebp;
        
    //mov ebp, esp
        //ebp now points to the top of the stack
        //store the value in esp in ebp
        int esp;
        ebp = esp;

    //sub esp, 16
        //subtract the value in esp by 16
        esp = esp - 16;

    //mov DWORD PTR [ebp-12], 32
        //store the value 32 to the address [ebp-12] only taking up 4 bytes
        //Move the 32-bit integer representation of 32 into 12 minus the value in memory location ebp
        int *ebpPTR;
        ebpPTR[-12] = 32;

    //mov DWORD PTR [ebp-8], 46
        //store the value 46 to the address [ebp-8] only taking up 4 bytes
        //Move the 32-bit integer representation of 46 into 8 minus the value in memory location ebp
        //int *ebp2 = (ebp - 8 ) + 46;
        ebpPTR[-8] = 46;

    //mov DWORD PTR [ebp-4], 55
        //store the value 55 to the address [ebp-12] only taking up 4 bytes
        //Move the 32-bit integer representation of 55 into 4 minus the value in memory location ebp
        ebpPTR[-4] = 55;

    //mov edx, DWORD PTR [ebp-12]
        //store the value 32 to the address [ebp-12] only taking up 4 bytes
        //Move the 32-bit integer representation of the value at ebp into 12 minus the value in memory location ebp
        ebpPTR[-12]=65;
        int edx = ebpPTR[-12];

    //mov eax, DWORD PTR [ebp-8]
        //store the value in the memory location ebp-8 to the address eax only taking up 4 bytes
        //Move the 32-bit integer representation of the value at memory location ebp-8 into eax
        int eax = ebpPTR[-8];


    //add eax, edx
        //add the value of edx to eax and store it in eax
        eax = eax + edx;

    //add DWORD PTR [ebp-4], eax
        //add the value at eax to the value at memory location ebp - 4 and store it at ebp-4
        ebpPTR[-4] = ebpPTR[-4] + eax;

    //mov eax, DWORD PTR [ebp-4]
        //copy and store the value of ebp - 4 in eax
        eax = ebpPTR[-4];

    //leave

    //ret
    return 0;
}
