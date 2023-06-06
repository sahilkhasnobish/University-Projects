/*
-------------------------------------
File:    stack.c
Project: a6_q2
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-03-03
-------------------------------------
 */
#include <stdio.h>
#include <stdlib.h>
#include "stack.h"

void push(STACK *sp, NODE *np) {
	if (sp->top == NULL){
		sp->top = np;
	}else{
		np->next = sp->top;
		sp->top = np;
	}
}

NODE *pop(STACK *sp) {
	NODE*np;
	np = sp->top;
	if (sp->top != NULL){
		sp->top = sp->top->next;
	}
	return np;
}

void clean_stack(STACK *sp) {
	while (sp->top->next!=NULL){
		NODE *np;
		np = sp->top;
		sp->top = sp->top->next;
		free(np);
	}
}
