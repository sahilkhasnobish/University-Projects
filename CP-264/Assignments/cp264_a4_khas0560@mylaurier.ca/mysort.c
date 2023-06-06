/*
-------------------------------------
File:    mysort.c
Project: a4_q1
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-02-09
-------------------------------------
 */

#include <stdio.h>
#include "mysort.h"

enum BOOLEAN is_sorted(int *a, int left, int right)
{
	int *p = a;
	int i, count = 0,l=left,r=right;
	enum BOOLEAN result = true;
	while (l<=r){
		if (*p>=*(p+1)){
			return false;
		}else return true;
		p++;
		count++;
		l++;
	}
	//return result;
}

void select_sort(int *a, int left, int right)
{

	char *p=a,*sorted=a,*n=a,*l=a,*r=a;
	l+=left;
	r+=right;
	int i,count=0;
	int *min;
	while(left<right){

		min = (a+left);
		i=left+1;
		while(i<=right){
			if (*(a+i)<*min) min = (a+i);
			i++;
		}
		swap(min,(a+left));
		left++;
	}
}

void quick_sort(int *a, int left, int right)
{
	char *l=a;
	l+=left;
	int key,i,j,k;
	if (left<right){
		k=(left+right)/2;
		key = *(a+k);

		for (j=left;j<right;j++){

			if (a<=key){
				swap(key,a);
				//a++;
				quick_sort(a,left,j-1);
				quick_sort(a,j+1,right);
				a++;
			}
			if (a>key){
				swap(key,a);
				//a++;
				quick_sort(a,left,j-1);
				quick_sort(a,j+1,right);
				a++;
			}
		}
		left++;
	}

}

void swap(int *first, int *second)
{
  int temp = *first;
  *first = *second;
  *second = temp;
}
