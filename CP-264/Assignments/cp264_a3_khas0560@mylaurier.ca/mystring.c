/*
-------------------------------------
File:    mystring.c
Project: A3
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-02-05
-------------------------------------
 */
#include <stdio.h>
#include "mystring.h"
int str_length(char*s){
    char *n=s;
    int count = 0,i;
    while (*n!='\0'){
        count+=1;
        n++;
    }
    return count;
}

int word_count(char*s){
    int word_count=0,count=0;
    char *n=s,*prev=s;
    while(*n!='\0'){
        if (count==0){
            prev++;
        }
        if ((*n!=' ') && ((*prev) == ' ')) word_count ++;
        n++;
        prev++;
        count=1;
    }
    return word_count;
}

void lower_case(char*s){
    char *n=s;
    int i = 0;
    while (i<str_length(s)){
        if (*n>='A' && *n<='Z'){
            *n+=32;
        }
        n++;
        i+=1;
    }
}

void trim(char *s){
    char *n=s,*prev=s,*trimmed;
    int i=0,count=0;
    while (i<str_length(s)){
        if (count==0){
            prev++;
        }
        if (((*n==' ')&&(*prev!=' '))||(*n!=' ')){
            *trimmed = *n;
            *n = *trimmed;
        }
        n++;
        prev++,
        trimmed++;
        i+=1;
        count = 1;
    }
    s = trimmed;
}