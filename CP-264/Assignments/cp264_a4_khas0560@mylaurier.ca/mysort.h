/*
-------------------------------------
File:    mysort.h
Project: a4_q1
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-02-09
-------------------------------------
 */

#ifndef MYSORT_H
#define MYSORT_H

enum BOOLEAN{
	 false = 0,
	 true = 1,
};
void select_sort(int *a, int left, int right);
void quick_sort(int *a, int left, int right);
void swap(int *first, int *second);
enum BOOLEAN is_sorted(int *a, int left, int right);

#endif
