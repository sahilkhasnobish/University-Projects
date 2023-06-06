/*
-------------------------------------
File:    tree.c
Project: a7_q1
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-03-12
-------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include "tree.h"

TPROPS get_props(TNODE *root) {
	TPROPS r = {0};
	TNODE *tp = root;
	int count = 0,height=1;
	if (root==NULL) return r;
	else{
		r->count = get_props_aux(tp,count);
		r->height = get_props_height_aux(tp,height);
	}
}
get_props_aux(TNODE*root, int count){
	if (root){
		get_props_aux(root->left,count+=1);
		get_props_aux(root->right,count+=1);
	}
}
get_props_height_aux(TNODE*root,height){
	TNODE *tp = root;
	int height_left = 1;
	int height_right = 1;
	while (tp->left!=NULL){
		tp = tp->left;
		height_left+=1;
	}
	while (tp->right!=NULL){
		tp = tp->right;
		height_right+=1;
	}
	if (height_right>height_left){
		return height_right;
	}else{
		return height_left;
}


void display_preorder(TNODE *root) {
	if (root){
		printf("%d",root->data);
		display_preorder(root->left);
		display_preorder(root->right);
	}
}

void display_inorder(TNODE *root) {
	if (root){
		display_inorder(root->left);
		printf("%d",root->data);
		display_inorder(root->right);
		}
}

void display_postorder(TNODE *root) {
	if (root){
		display_inorder(root->left);
		display_inorder(root->right);
		printf("%d",root->data);
		}
}

TNODE *iterative_bf_search(TNODE *root, int val) {
}


TNODE *iterative_df_search(TNODE *root, int val) {

}


/* basic functions */
TNODE *new_node(int value) {
  TNODE *np = (TNODE *) malloc(sizeof(TNODE));
  if (np == NULL) return NULL;
  np->data = value;
  np->left = NULL;
  np->right = NULL;
  return np;
}

void display_tree(TNODE *root, int prelen) {
  if (root) {
    int i;
    for (i = 0; i < prelen; i++)
      printf("%c", ' ');
    printf("%s", "|___");
    printf("%c\n", root->data);
    display_tree(root->right, prelen + 4);
    display_tree(root->left, prelen + 4);
  }
}

void clean_tree(TNODE **rootp) {
  TNODE *root = *rootp;
  if (root) {
    if (root->left)
      clean_tree(&root->left);
    if (root->right)
      clean_tree(&root->right);
    free(root);
  }
  *rootp = NULL;
}


// queue functions adapted and modified from a6
void enqueue(QUEUE *qp, void *data) {
   QNODE *p = (QNODE*) malloc(sizeof(QNODE));
   if (p == NULL) return;
   else {
     p->data = data;
     p->next = NULL;

     if (qp->front == NULL) {
      qp->front = p;
      qp->rear = p;
     } else {
      (qp->rear)->next = p;
      qp->rear = p;
    }
  }
}
void *dequeue(QUEUE *qp) {
  void *temp = NULL;
  if (qp->front) {
    QNODE *p = qp->front;
    temp = p->data;
    if (qp->front == qp->rear) {
      qp->front = NULL;
      qp->rear = NULL;
    } else {
      qp->front = p->next;
    }
    free(p);
    return temp;
  }
  return NULL;
}
void clean_queue(QUEUE *qp) {
  QNODE *temp, *p = qp->front;
  while (p != NULL) {
    temp = p;
    p = p->next;
    free(temp);
  }
}

// stack functions adapted and modified from a6
void push(STACK *sp, void *data) {
  SNODE *p = (SNODE*) malloc(sizeof(SNODE));
  p->data = data;
  p->next = NULL;
  if (sp->top == NULL) {
    sp->top = p;
  } else {
    p->next = sp->top;
    sp->top = p  ;
  }
}
void pop(STACK *sp) {
  if (sp->top != NULL) {
    SNODE *p = sp->top;
    sp->top = p->next;
    free(p);
  }
}
void *peek(STACK *sp) {
  if (sp->top != NULL) {
     return sp->top->data;
  }
  return NULL;
}
void clean_stack(STACK *sp) {
  SNODE *temp, *p = sp->top;
  while (p) {
    temp = p;
    p = p->next;
    free(temp);
  }
  sp->top = NULL;
}
