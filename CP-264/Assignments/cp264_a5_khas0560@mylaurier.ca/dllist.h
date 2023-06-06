/*
-------------------------------------
File:    dllist.h
Project: a5_q2
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-02-25
-------------------------------------
 */
#ifndef DLLIST_H_
#define DLLIST_H_
typedef struct node{
	struct node*prev;
	char data;
	struct node*next;
}NODE;
NODE *new_node(char data);
void display_forward(NODE *np);
void display_backward(NODE *np);
void insert_start(NODE **startp, NODE **endp, NODE *new_np);
void insert_end(NODE **startp, NODE **endp, NODE *new_np);
void delete_start(NODE **startp, NODE **endp);
void delete_end(NODE **startp, NODE **endp);
void clean(NODE **startp, NODE **endp);


#endif /* DLLIST_H_ */
