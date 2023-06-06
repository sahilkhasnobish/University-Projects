/*
-------------------------------------
File:    factorial.c
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-01-22
-------------------------------------
 */

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *args[])
{
  int i, n = 0, f = 1, prev, is_overflow = 0;

  if ( argc > 1 ) {
    n = atoi( args[1] );  // convert command line argument to an integer
    printf("factorial %d\n",n);
    if (n >= 1) {         // the conversion is successful
    	if (n>=13){
    		is_overflow = 1;

    	}
			for(i=1;i<=n;i++){
				f*=i;
				if (i==13){
					break;
				}
				printf("%11d",f);
				if (i % 4 == 0){
					printf("\n");
				}
			}if (is_overflow == 1){
				printf("overflow:13!\n");
			}else{
				printf("\n%d!:%d",n,f);
			}

    } else {
       printf("%s:invalid argument\n",args[1]);
    }
  }
  else {
    printf("no argument");
  }
  return 0;
}
