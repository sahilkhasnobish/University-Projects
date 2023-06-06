/*
-------------------------------------
File:    dllist.c
Project: a5_q2
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-02-25
-------------------------------------
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "dllist.h"

NODE *new_node(char data) {
	NODE *p = (NODE*) malloc(sizeof(NODE));
	if (p==NULL){
		printf("malloc fails");
		return NULL;
	}
	p->data = data;
	p->prev = NULL;
	p->next = NULL;
	return p;
}

void display_forward(NODE *np) {
	if (np==NULL) return;
	NODE *p = np;
	while(p!=NULL){
		printf("%c",p->data);
		p = p->next;
	}
}

void display_backward(NODE *np) {
	if (np==NULL) return;
		NODE *p = np;
		while(p!=NULL){
			printf("%c",p->data);
			p = p->prev;
		}
}

void insert_start(NODE **startp, NODE **endp, NODE *new_np) {
	if (*startp == NULL){
		*startp = new_np;
		*endp = new_np;
	}else{
		NODE *start_p = *startp;
		NODE *prev = NULL;
		new_np->next = start_p;
		start_p->prev = new_np;
		*startp= new_np;
	}
	NODE *start_p = *startp;
}

void insert_end(NODE **startp, NODE **endp, NODE *new_np) {
	if (*endp == NULL){
			*endp = new_np;
			*startp = new_np;
		}else{
			NODE *end_p = *endp;
			new_np->prev = end_p;
			end_p->next= new_np;
			*endp= new_np;
		}
}

void delete_start(NODE **startp, NODE **endp) {
	NODE*p = *startp;
	*startp = p->next;
	free(p);
}

void delete_end(NODE **startp, NODE **endp) {
	NODE*p = *endp;
	NODE*prev_p = p->prev;
	prev_p->next = NULL;
	*endp = prev_p;
	free(p);
}

void clean(NODE **startp, NODE **endp) {
	NODE*prev = NULL;
	NODE*p = *startp;
	prev = p;
	p = p->next;
	while(p!=NULL){
		free(prev);
		prev = p;
		p = p->next;
	}
	*startp = NULL;
	*endp = NULL;
}
