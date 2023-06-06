/*
-------------------------------------
File:    quadratic.c
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-01-22
-------------------------------------
 */


#include <stdio.h>
#include <math.h>

#define EPSILON 0.000001
// or #define EPSILON 1e-6

int main()
{
  //setvbuf(stdout, NULL, _IONBF, 0);
  //setvbuf(stderr, NULL, _IONBF, 0);

  float a, b, c, d, x1, x2;
  int inn;
  char temp;

  do {// do-while for new input problem
    // do-while loop to get correct input of three floating numbers,
    do {
      printf("Please enter the coefficients a,b,c\n");
      inn = scanf("%f,%f,%f", &a,&b,&c);

      if (inn != 3 ) {
         printf("input:Invalid input\n");
      } else
        break;



    } while (1);
    do {  // flush the input buffer
    	scanf("%c", &temp);
    	if (temp == '\n') break;
      } while (1);

    if (fabs(a) < EPSILON && fabs(b) < EPSILON && fabs(c) < EPSILON) {
      printf("input:quit\n");
      break;
    }
    else if (fabs(a) < EPSILON) {
      printf("input:not a quadratic equation\n");break;
    } else {

      d = (b * b) - (4 * a * c);  // compute the discriminant
    }if (d == 0){
        printf("The equation has two equal real roots\n");
        x1 = (-b+(sqrt(d)))/(2*a);
        printf("x1:%f\n",x1);
    }if (d<0){ printf("The equation has no real roots\n");
    	x1 = (-b)/(2*a);
    	x2 = (sqrt(fabs(d)))/(2*a);
        printf("%f,%f,%f",a,b,c);
		printf("real:%f\n",x1);
		printf("imaginary:%f\n",x2);
    }if (d>0){
    	  printf("The equation has two distinct real roots\n");
        x1 = (-b+(sqrt(d)))/(2*a);
        x2 = (-b-(sqrt(d)))/(2*a);
        printf("x1:%f\n",x1);
        printf("x2:%f\n",x2);
      }


    } while (1);
  return 0;
}
