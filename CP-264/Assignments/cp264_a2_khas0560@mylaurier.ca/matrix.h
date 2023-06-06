/*
-------------------------------------
File:    matrix.h
Project: A2
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-01-29
-------------------------------------
 */
#include<stdio.h>
//#include "matrix.h"


void display_matrix(int *m, int n) {
  int *p = m, i, j;
  for (i = 0; i < n; i++) {
    printf("\n");
    for (j = 0; j < n; j++) printf("%4d", *p++); 
  }
  printf("\n");
}

int sum(int *m, int n) {
  int sum_matrix = 0,i,j,*p=m;
  for (i=0;i<n;i++){
    for (j=0;j<n;j++) sum_matrix += *p++;
  }
  return sum_matrix;
}

int is_magic_square(int *m, int n) {
  int prev_sum_row = 0, current_sum_row = 0;
  int prev_sum_column = 0, current_sum_column = 0;
  int prev_sum_diagonal = 0, current_sum_diagonal = 0;
  int i, j,*p=m,result=1;

  for (i=0;i<n;i++){
    current_sum_column += *p++;
    prev_sum_column = current_sum_column;
    for (j=0;j<n;j++){
      if (i==0){
        current_sum_row += *p++;
        prev_sum_row = current_sum_row;
      }else{

        current_sum_row += *p++;
        if (prev_sum_row != current_sum_row){
          result = 0;
          break;
        }else prev_sum_row = current_sum_row; 
      }
      }
      if (i!=0){
        if (prev_sum_column!=current_sum_column){
          result = 0;
          break;
    } 
    }
  }
  if (prev_sum_row == current_sum_row) result = 1;
  return result;
}

void transpose_matrix(int *m1, int *m2, int n) {
  int i,j,*p1 = m1, *p2 = m2;
    for (i=0;i<n;i++){
      for (j=0;j<n;j++)*(p2+j*n+i)=*(p1+i*n+j);
    }
}
/*
void multiply_matrix(int *m1, int *m2, int *m3, int n) {  
  int i,j,*p1 = m1,*p2 = m2, *p3 = m3;
  for (i=0;i<n;i++){
    for (j=0;j<n;j++){
      *(p3+j*n+i) = (*(p2+j*n+i)*(*(p1+(i)*n+(j))+(*(p2+(j+1)*n+(i+1)*(*(p1+(i+1)*n+(j+1))+(*(p2+(j+1)*n+(i+1)*(*(p1+(i+1)*n+(j+1))));
    }
}
*/