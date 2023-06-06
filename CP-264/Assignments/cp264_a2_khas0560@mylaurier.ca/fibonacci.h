/*
-------------------------------------
File:    fibonacci.h
Project: A2
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-01-29
-------------------------------------
 */
#include <stdio.h> 
extern int *la;
int recursive_fibonacci(int n){
    if ((n==1)||(n==2)) return 1;
    if (n==0) return 0;
    else{
        return recursive_fibonacci(n-2) + recursive_fibonacci(n-1);
    }
}
int iterative_fibonacci(int n){
    if (&n < la) la = &n;
    int i,previous1=0,previous2=0,current=1;
    for (i=1;i<n;i++){
        previous2 = previous1;
        previous1 = current;
        current = previous1+previous2;

        /*if (n==1||n==2){
            ptr = 1;
        }else{
            ptr = (i-1)+(i-2);
        }*/
    }//printf("%d",current);
return current;
}