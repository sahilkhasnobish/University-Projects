/*
-------------------------------------
File:    polynomial.h
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
#include<math.h>

#define EPSILON 1e-6

void display_polynomial(float p[], int n, float x)
{
    //printf("P(%f)=",x);
    int i,count = n-1;
    //printf("%d\n",num_elements);
    for (i=0;i<n;i++){
        printf("%.2f*%.2f^%d",p[i],x,count);
        count -=1;
        if (i != n-1){
            printf("+");
        }
    }
}

float horner(float p[], int n, float x)
{
    int i;
    float result = p[0],count = n-1; 
    for (i=1;i<n;i++){
        if (count == 0) result = p[i];
        else result = result * x + p[i];
        count-=1;
    }
    return result;
}

float bisection(float p[], int n, float a, float b)
{   
    float c = 0.0,result = 0.0;
    do{
        c = (a+b)/2;
        if (fabs(horner(p,n,c)) < EPSILON) break;
        else if (horner(p,n,c) * horner(p,n,a)<0.0) b = c;
        else if (horner(p,n,c) * horner(p,n,a)>0.0) a = c;

    }while (1);
    return c;
    
}

