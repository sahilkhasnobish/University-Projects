/*
-------------------------------------
File:    stack.h
Project: a6_q2
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-03-03
-------------------------------------
 */
#ifndef STACK_H
#define STACK_H

#include "common.h"

typedef struct stack {
  NODE *top;
} STACK;

void push(STACK *sp, NODE *np);
NODE *pop(STACK *sp);
void clean_stack(STACK *sp);

#endif
