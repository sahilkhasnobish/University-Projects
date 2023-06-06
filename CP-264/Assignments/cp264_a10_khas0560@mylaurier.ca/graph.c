/*
-------------------------------------
File:    graph.c
Project: a10_q2
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-04-08
-------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>
#include "graph.h"


GRAPH *new_graph(int order) {
	GRAPH *g = malloc(sizeof(GRAPH));
	g->order = order;

	g->nodes = malloc(order*sizeof(GNODE*));
	for(int n=0;n<order;n++){
		g->nodes[n] = malloc(sizeof(GNODE));
		g->nodes[n]->neighbor = NULL;
		g->nodes[n]->nid = n;
	}

	return g;
}

void add_edge(GRAPH *g, int from, int to, int weight) {
	int i;
	int size = g->order;
	for(i=0;i<size;i++){
		if (g->nodes[i] == from) break;
	}
	ADJNODE *e = malloc(sizeof(ADJNODE));
	e->weight = weight;
	e->nid = i;
	e->next = to;

	e->next = g->nodes[i]->neighbor;
	g->nodes[i]->neighbor = e;
}


void bf_traverse(GRAPH *g, int nid) {
	QUEUE *q = {0};
	int status[g->order];
	QUEUE *out = {0};
	int start = g->nodes[nid];
	for(int i=0;i<g->order;i++) status[i] = 1;
	GNODE *gn = NULL;
	ADJNODE *an = NULL;
	enqueue(&q,start);
	status[nid] = 2;
	if (q->front == NULL){
		printf(out);
	}else{
		while(q->front){
			gn = (GNODE*) dequeue(&q);
			printf("%d",gn->nid);
		}
		/*
		int n = dequeque(q);
		status[n] = 3;
		enqueque(out,n);
		*/
	}
	clean_queue(q);
}

//use auxiliary stack data structure for the algorithm
void df_traverse(GRAPH *g, int nid) {
	STACK *q = {0};
	int status[g->order];
	STACK *out = {0};
	int start = g->nodes[nid];
	for(int i=0;i<g->order;i++) status[i] = 1;
	GNODE *gn = NULL;
	ADJNODE *an = NULL;
	push(&q,start);
	status[nid] = 2;
	if (q->top == NULL){
		printf(out);
	}else{
		while(q->top){
			gn = (GNODE*) dequeue(&q);
			printf("%d",gn->nid);
		}
		/*
		int n = dequeque(q);
		status[n] = 3;
		enqueque(out,n);
		*/
	}
	clean_stack(q);
}




int get_weight(GRAPH *g, int from, int to) {
  ADJNODE *p = g->nodes[from]->neighbor;
  int result = INFINITY;
  while (p) {
    if (p->nid == to) {
        result = p->weight;
        break;
    }
    p = p->next;
  }
  return result;
}

void clean_graph(GRAPH **gp) {
  int i;
  GRAPH *g = *gp;
  ADJNODE *temp, *ptr;
  for (i = 0; i < g->order; i++) {
    ptr = g->nodes[i]->neighbor;
    while (ptr != NULL) {
      temp = ptr;
      ptr = ptr->next;
      free(temp);
    }
    free(g->nodes[i]);
  }
  free(g->nodes);
  free(g);
  *gp = NULL;
}

void display_graph(GRAPH *g) {
  if (g == NULL) return;
  printf("order:%d\n", g->order);
  printf("size:%d\n", g->size);
  printf("from:(to weight)");
  int i;
  ADJNODE *ptr;
  for (i = 0; i < g->order; i++) {
    printf("\n%d:", g->nodes[i]->nid);
    ptr = g->nodes[i]->neighbor;
    while (ptr != NULL) {
      printf("(%d %d) ", ptr->nid, ptr->weight);
      ptr = ptr->next;
    }
  }
}


// queue functions adapted and modified from a7
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

// stack functions adapted and modified from a6q3
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
