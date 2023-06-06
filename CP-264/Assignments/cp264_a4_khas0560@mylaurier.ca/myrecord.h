/*
-------------------------------------
File:    myrecord.h
Project: a4_q2
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-02-09
-------------------------------------
 */
#ifndef MYRECORD_H
#define MYRECORD_H
#include <string.h>

typedef struct {
	char name[20];
	float score;
} RECORD;

typedef struct {
	int count;
	float mean;
	float stddev;
} REPORT;

char letter_grade(float score);
int import_data(RECORD dataset[], char *filename);
REPORT report_data(RECORD dataset[], int n, char *filename);

#endif
