/*
-------------------------------------
File:    expression.c
Project: a6_q3
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-03-04
-------------------------------------
 */
#include <stdio.h>
#include <stdlib.h>
#include "common.h"
#include "queue.h"
#include "stack.h"
#include "expression.h"

/*
 * auxiliary function
*/
int get_priority(char op) {
  if (op == '/' || op == '*' || op == '%')
    return 1;
  else if (op == '+' || op == '-')
    return 0;
  else
    return -1;
}

/*
 * auxiliary function
*/
int type(char c) {
  if (c >= '0' &&  c <= '9' )
     return 0;
  else if (c == '/' || c == '*' || c == '%' || c == '+' || c == '-')
    return 1;
  else if (c == '(')
    return 2;
  else if ( c == ')')
    return 3;
  else
    return 4;
}

QUEUE infix_to_postfix(char *infixstr) {
	char*p = infixstr,n;
	QUEUE queue = {0};
	STACK stack = {0};
	int sign = 1,num = 0;

	while(*p){
		if (*p == '-'&&(p==infixstr||*(p-1)=="(")){
			sign = -1;
		}
		else if (*p>='0'&&*p<='9'){
			num = *p-'0';
			while((*(p+1)>='0'&&*(p+1)<='9')){
				num = num*10+*(p+1)-'0';
				p++;
			}
			enqueue(&queue,new_node(sign*num,0));
			sign = 1;
		}
		else if(*p=='('){
			push(&stack,*p);
		}
		else if(*p==')'){
			n = stack.top;
			if (n!='('){
				pop(&stack);
				enqueue(&queue,n);
			}else{
				pop(&stack);
			}

		}
		else if(type(*p)==1){
			n = stack.top;
			if (get_priority(n)>get_priority(*p)){
				enqueue(&queue,n);
				pop(&stack);
				if (stack.top!=NULL){
					n = stack.top;
					enqueue(&queue,n);
					pop(&stack);
				}
			}
		}
		else{
			p++;
		}
		while(stack.top){
			enqueue(&queue,pop(&stack));
		}
	}
	return queue;
}

int evaluate_postfix(QUEUE queue) {
	NODE* ptr = queue.front;
	STACK stack = {0};
	int type = 0,B,A,C,result;
	while(ptr){
		type = ptr->type;
		if (type == 0){
			new_node(ptr->data,0);
			push(&stack,*new_node);
		}
		else if(type == 1){
			B = pop(&stack);
			A = pop(&stack);
			C = A*B;
			push(&stack,C);
		}
		ptr = ptr->next;
	}
	result = stack.top->data;
	clean_stack(&stack);
	return result;
}


int evaluate_prefix(char *infixstr) {
	int n;
	n = evaluate_postfix(infix_to_postfix(infixstr));
	return n;

}
