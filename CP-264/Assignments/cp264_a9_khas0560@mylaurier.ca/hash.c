/*
-------------------------------------
File:    hash.c
Project: a9_q1
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-03-29
-------------------------------------
 */
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "hash.h"

int hash(char* word) {
  unsigned int hash = 0, i;
  for (i = 0; word[i] != '\0'; i++) {
    hash = 31 * hash + word[i];
  }
  return hash % htsize;
}

HTNODE *new_hashnode(char *name, int value) {
	HTNODE* node = (HTNODE*)malloc(sizeof(HTNODE));
	//node->name = name;
	strcpy(node->name,name);
	node->value = value;
	return node;
}

HASHTABLE *new_hashtable(int size) {
	HASHTABLE *ht = (HASHTABLE*)malloc(sizeof(HASHTABLE));
	ht->hnp = (HTNODE**)malloc(sizeof(HTNODE**));
	int i;
	for (i=0;i<size;i++) *(ht->hnp+i) = NULL;
	ht->size = size;
	ht->count = 0;
	return ht;
}

HTNODE *search(HASHTABLE *ht, char *name) {
	int size = ht->size;
	int n = hash(name);
	int i=0;
	HTNODE *node = ht->hnp[n];

	while(i<size){
		if (ht->hnp[i]->name==node->name){
			return node;
			break;
		}
		i++;
	}
	return NULL;
}

int insert(HASHTABLE *ht, HTNODE *np) {
	int n = hash(np);
	HTNODE *node = np;
	int i=0;
	int a=0;
	for (int i=0;i<n;i++){
		HTNODE *node = np;
		ht->hnp[i] = node;
		node->next  = ht->hnp[i+1];
	}

	ht->count+=1;
	return 1;
}

int delete(HASHTABLE *ht, char *name) {
	int n = hash(name);
	HTNODE *node = ht->hnp[n];
	for (int i=0;i<n;i++) node  = node->next;
	node->value = -1;
	return 0;
}


// you can use this function in your program
void clean_hash(HASHTABLE **htp) {
  if (*htp == NULL) return;
  HASHTABLE *ht = *htp;
  HTNODE *sp = ht->hnp[0], *p, *temp;
  int i;
  for (i = 0; i < ht->size; i++) {
    p = ht->hnp[i];
    while (p) {
      temp = p;
      p = p->next;
      free(temp);
    }
  ht->hnp[i] = NULL;
  }
  free(ht->hnp);
  ht->hnp = NULL;
  *htp = NULL;
}

// you can use this function in your program
void display_hashtable(HASHTABLE *ht, int option) {
  int i = 0;
  HTNODE *p;
  if (option == 0) {
  printf("size:  %d\n", ht->size);
  printf("count: %d\n", ht->count);
  printf("hash data:\nindex: list of the data elements");
  for (i = 0; i < ht->size; i++) {
    p = *(ht->hnp + i);
    if (p)
      printf("\n%2d: ", i);

    while (p) {
      printf("(%s, %d) ", p->name, p->value);
      p = p->next;
    }
  }
  printf("\n");
  }
  else {

  for (i = 0; i < ht->size; i++) {
    p = *(ht->hnp + i);
    while (p) {
      printf("%s=%d\n", p->name, p->value);
      p = p->next;
    }
  }

  }

}

