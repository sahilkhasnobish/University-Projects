/*
-------------------------------------
File:    heap.c
Project: a9_q3
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-03-30
-------------------------------------
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "heap.h"

HEAP *new_heap(int capacity)
{
	HEAP* hp = (HEAP*)malloc(sizeof(HEAP));
	hp->capacity = capacity;
	hp->size = 0;
	hp->hnap = (HNODE*)malloc(sizeof(HNODE)*capacity);
	return hp;

}
/* this inserts the given node data a into the heap; When the heap
 * size is equal to the capacity, the inserting process needs
 * first to expand data array by doubling its amount.
 * This may need to copy the data of old array to new array,
 * secondly insert the new data element into the end of the array, heapify and update size.*/
void insert(HEAP *heap, HNODE new_node)
{
	//HNODE *np = (HNODE *) malloc(sizeof(HNODE) * 10);
	if (heap->size<=heap->capacity){
		HNODE *n = heap->hnap;
		int temp;
		int size = heap->size;
		n[size] = new_node;

		int i = 0;
		int parent = (i-1)/2;
		int swap_temp;
		int smallest = parent;
		while (i<size){
			int left = (2*i)+1;
			int right = (2*i)+2;
			i+=1;
			if (n+left<=n+parent) smallest = left;
			if (n+right<=n+parent) smallest = right;
			if (smallest!=parent){
				swap_temp = n+parent;
				n[parent].data = smallest;
				smallest = swap_temp;
			}
		}
		heap->size+=1;
	}else{
		heap->capacity*=2;
		HNODE *temp = realloc(heap->hnap,sizeof(HNODE)*heap->capacity); //reallocating num of nodes equal to the capacity, doubling by multplying
		if (temp){
			heap->hnap=temp;
		}else{
			temp = malloc(sizeof(HNODE)*heap->capacity);
			if (temp){
				memcpy(temp,heap->hnap,sizeof(HNODE)*heap->size);
				free(heap->hnap);
				heap->hnap = temp;
			}else{
				printf("array resize failed\n");
			}
		}
	}

}
/* this gets the data element of minimum key and delete the element from the binary heap.
 * When the heap size  is no more than a quarter of the capacity,
 * it needs to shrink the data array by half to free the unused memory space. */
HNODE extract_min(HEAP *heap)
{
	int i;
	int last_node = heap->size-1;
	HNODE *temp = (HNODE*)malloc(sizeof(HNODE));
	temp = &(heap->hnap[0]);
	HNODE *temp_resize = (HNODE*)malloc(sizeof(HNODE));
	heap->hnap[0] = heap->hnap[last_node];
	heap->hnap[last_node] = *temp; //defrences pointers to get node
	heap->size = heap->size-1;

	int  *n = heap->hnap;
	int size = heap->size;
	int parent = (i-1)/2;
	int swap_temp;
	while (i<size){
		int smallest = parent;
		int left = (2*i)+1;
		int right = (2*i)+2;
		if (n+left<=n+parent) smallest = left;
		if (n+right<=n+parent) smallest = right;
		if (smallest!=parent){
			swap_temp = n+parent;
			n[parent] = smallest;
			smallest = swap_temp;
		}
	}
	if ((heap->size)<=(heap->size/4)){
		heap->capacity = heap->capacity/2;

		heap->capacity/=2;
		temp_resize=realloc(heap->hnap,sizeof(HNODE)*heap->capacity);
		if (temp_resize){
			heap->hnap=temp_resize;
		}else{
			temp_resize = malloc(sizeof(HNODE)*heap->capacity);
			if (temp_resize){
				memcpy(temp_resize,heap->hnap,sizeof(HNODE)*heap->size);
				free(heap->hnap);
				heap->hnap=temp_resize;
			}else{
				printf("array resize failed\n");
			}
		}

	}
	return *temp;
}
/* this decreases the key value of given element by index to new_key_value */
void decrease_key(HEAP *heap, int node_index, KEYTYPE key_value)
{
	heap->hnap[node_index].key = key_value;

	int  *n = heap->hnap;
	int i=0;
	int size = heap->size;
	int parent = (i-1)/2;
	int swap_temp;
	while (i<size){
		int smallest = parent;
		int left = (2*i)+1;
		int right = (2*i)+2;
		if (n+left<=n+parent) smallest = left;
		if (n+right<=n+parent) smallest = right;
		if (smallest!=parent){
			swap_temp = n+parent;
			n[parent] = smallest;
			smallest = swap_temp;
		}
	}
}

int find_index(HEAP *heap, DATA value) {
	int i = 0;
	int index = 0;
	int size = heap->size;
	HNODE *node = heap->hnap;
	for (i=0;i<size;i++){
		if (heap->hnap[i].data == value){
			index = i;
			break;
		}
	}
	return index;
}

void display_heap(HEAP *hp) {
  printf("\nsize:%d\ncapacity:%d\n", hp->size, hp->capacity);
    printf("(index, key, data):\n");
    int i;
    for (i=0; i < hp->size; i++) {
    printf("(%d %d %d) ", i, hp->hnap[i].key, hp->hnap[i].data);
    if (i % 10 == 9) printf("\n");
  }
    printf("\n");
}

int cmp(KEYTYPE a, KEYTYPE b) {
  if (a < b)
     return -1;
  else if (a==b)
     return 0;
  else
     return 1;
}
