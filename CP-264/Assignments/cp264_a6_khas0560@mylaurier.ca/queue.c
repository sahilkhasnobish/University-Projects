/*
-------------------------------------
File:    queue.c
Project: a6_q1
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
#include "common.h"
#include "queue.h"

void enqueue(QUEUE *qp, NODE *np) {
	if ((qp->front) == NULL){
		qp->front = np;
		qp->rear = np;
	}else{
		qp->rear->next = np;
		qp->rear = np;
	}
}

NODE *dequeue(QUEUE *qp) {
	NODE *ptr = qp->front;
	if ((qp->front != NULL)){
		if (qp->front == qp->rear){
			qp->front = NULL;
			qp->rear = NULL;
		}else{
			qp->front = qp->front->next;
		}
	}
	return ptr;
}

void clean_queue(QUEUE *qp) {
	if ((qp->front != NULL)){
		while (qp->front!=qp->rear){
			NODE *ptr = qp->front;
			qp->front = qp->front->next;
			free(ptr);
		}
		qp->front = NULL;
		qp->rear = NULL;
	}
}
