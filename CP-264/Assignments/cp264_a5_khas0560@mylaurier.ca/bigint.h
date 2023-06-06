/*
-------------------------------------
File:    bigint.h
Project: a5_q3
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-02-27
-------------------------------------
 */
// add your code signature

#ifndef BIGINT_H
#define BIGINT_H
#include "dllist.h"
typedef struct node{
	struct node*prev;
	char data;
	struct node*next;
}NODE;

typedef struct bigint{
	NODE **start;
	NODE**end;

}BIGINT;

#endif
