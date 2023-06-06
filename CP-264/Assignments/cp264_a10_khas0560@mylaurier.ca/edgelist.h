/*
-------------------------------------
File:    edgelist.h
Project: a10_q1
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-04-08
-------------------------------------
 */
#ifndef EDGELIST_H
#define EDGELIST_H

// your code document
typedef struct edge {
  int from;
  int to;
  int weight;
  struct edge *next;
} EDGE;

// your code document
typedef struct edgelist {
  int size;
  EDGE *start;
  EDGE *end;
} EDGELIST;


// your code document
EDGELIST *new_edgelist();

// your code document
void add_edge_end(EDGELIST *g, int from, int to, int weight);

// your code document
void add_edge_start(EDGELIST *g, int from, int to, int weight);

// your code document
int weight_edgelist(EDGELIST *g);

// your code document
void display_edgelist(EDGELIST *g);

// your code document
void clean_edgelist(EDGELIST **gp);

#endif
