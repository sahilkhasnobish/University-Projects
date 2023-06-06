/*
-------------------------------------
File:    queue.h
Project: a6_q1
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-03-03
-------------------------------------
 */
#ifndef QUEUE_H
#define QUEUE_H

#include "common.h"

typedef struct queue {
  NODE *front;
  NODE *rear;
} QUEUE;

void enqueue(QUEUE *qp, NODE *np);
NODE *dequeue(QUEUE *qp);
void clean_queue(QUEUE *qp);

#endif
