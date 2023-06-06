/*
-------------------------------------
File:    caseflip.c
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-01-22
-------------------------------------
 */

#include <stdio.h>

int main()
{
	char c = 0, temp;

	do {
		printf("Please enter a character\n");
		scanf("%c", &c);
		do{
			scanf("%c",&temp);
			if (temp == '\n')break;
		}while (1);
		if (c=='*'){
			printf("%c:quit\n",c); break;
		}
		if (c>='a' && c<='z'){
			printf("%c:%d,%c\n", c, c, c-32);
		}
		else if (c>='A' && c<='Z'){
					printf("%c:%d,%c\n", c, c, c+32);
				}
		else{
			printf("%c:invalid\n",c);
		}

	}while(1);
	return 0;

}
//lowecase quivaleince is -32
//uppercase to lowecase - add 32
