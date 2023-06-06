/*
-------------------------------------
File:    edgelist.c
Project: a10_q1
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
#include "edgelist.h"

EDGELIST *new_edgelist() {
	EDGELIST *e =  malloc(sizeof(EDGELIST));
	return e;
}

void add_edge_end(EDGELIST *g, int from, int to, int weight) {
	EDGE *e = malloc(sizeof(EDGE));
	e->from = from;
	e->to = to;
	e->weight = weight;
	e = g->end->next;
	g->end = e;
}

void add_edge_start(EDGELIST *g, int from, int to, int weight) {
	EDGE *e = malloc(sizeof(EDGE));
		e->from = from;
		e->to = to;
		e->weight = weight;
		g->start->next = g->start;
		g->start = e;
}

int weight_edgelist(EDGELIST *g) {
	int size = g->size;
	int weight = 0;
	for(int i=0;i<size;i++){
		//int edge_weight = g[i]->weight;
		weight += g[i].start->weight;
	}

	return weight;
}

void clean_edgelist(EDGELIST **gp) {
  EDGELIST *g = *gp;
  EDGE *temp, *p = g->start;
  while (p) {
    temp = p;
    p = p->next;
    free(temp);
  }
  free(g);
  *gp = NULL;
}

void display_edgelist(EDGELIST *g) {
  if (g == NULL) return;
  printf("size:%d\n", g->size);
  printf("(from to weight):");
  EDGE *p = g->start;
  while (p) {
    printf("(%d %d %d) ", p->from, p->to, p->weight);
    p = p->next;
  }
}

