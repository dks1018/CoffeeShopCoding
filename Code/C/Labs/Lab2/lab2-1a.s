	.file	"lab2-1a.c"
	.intel_syntax noprefix
	.text
	.def	___main;	.scl	2;	.type	32;	.endef
	.section .rdata,"dr"
	.align 4
LC0:
	.ascii "Print variables %d %d %d %d %d %d %d\0"
	.text
	.globl	_main
	.def	_main;	.scl	2;	.type	32;	.endef
_main:
LFB17:
	.cfi_startproc
	push	ebp
	.cfi_def_cfa_offset 8
	.cfi_offset 5, -8
	mov	ebp, esp
	.cfi_def_cfa_register 5
	and	esp, -16
	sub	esp, 64
	call	___main
	mov	eax, DWORD PTR [esp+60]
	mov	DWORD PTR [esp+56], eax
	sub	DWORD PTR [esp+56], 16
	mov	DWORD PTR [esp+52], 32
	mov	DWORD PTR [esp+48], 46
	mov	DWORD PTR [esp+44], 55
	mov	eax, DWORD PTR [esp+52]
	mov	DWORD PTR [esp+40], eax
	mov	eax, DWORD PTR [esp+48]
	mov	DWORD PTR [esp+36], eax
	mov	eax, DWORD PTR [esp+40]
	add	DWORD PTR [esp+36], eax
	mov	eax, DWORD PTR [esp+36]
	add	DWORD PTR [esp+44], eax
	mov	eax, DWORD PTR [esp+44]
	add	DWORD PTR [esp+36], eax
	mov	eax, DWORD PTR [esp+36]
	mov	DWORD PTR [esp+28], eax
	mov	eax, DWORD PTR [esp+40]
	mov	DWORD PTR [esp+24], eax
	mov	eax, DWORD PTR [esp+44]
	mov	DWORD PTR [esp+20], eax
	mov	eax, DWORD PTR [esp+48]
	mov	DWORD PTR [esp+16], eax
	mov	eax, DWORD PTR [esp+52]
	mov	DWORD PTR [esp+12], eax
	mov	eax, DWORD PTR [esp+56]
	mov	DWORD PTR [esp+8], eax
	mov	eax, DWORD PTR [esp+60]
	mov	DWORD PTR [esp+4], eax
	mov	DWORD PTR [esp], OFFSET FLAT:LC0
	call	_printf
	mov	eax, 0
	leave
	.cfi_restore 5
	.cfi_def_cfa 4, 4
	ret
	.cfi_endproc
LFE17:
	.ident	"GCC: (MinGW.org GCC-8.2.0-3) 8.2.0"
	.def	_printf;	.scl	2;	.type	32;	.endef
