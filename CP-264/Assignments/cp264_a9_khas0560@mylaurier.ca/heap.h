/*
-------------------------------------
File:    heap.h
Project: a9_q3
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-03-30
-------------------------------------
 */
#ifndef HEAP_H
#define HEAP_H

#define MIN_CAPACITY 4

typedef int KEYTYPE;  // key type
typedef int DATA;     // data type

typedef struct heap_node { // data element ds for binary heap
  KEYTYPE key;
  DATA data;
} HNODE;

typedef struct heap {
  unsigned int capacity; // the MAX length of array
  unsigned int size;     // the current heap size, i.e., heap node count
  HNODE *hnap;  // pointer pointing the heap node array
} HEAP;

// add your code documentation
HEAP *new_heap(int capacity);

// add your code documentation
int find_index(HEAP *heap, DATA d);

// add your code documentation
void insert(HEAP *heap, HNODE a);

// add your code documentation
HNODE extract_min(HEAP *heap);

// add your code documentation
void decrease_key(HEAP *heap, int index, KEYTYPE new_key_value);


void display_heap(HEAP *heap);
int cmp(KEYTYPE a, KEYTYPE b);

#endif
