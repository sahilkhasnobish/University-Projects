/*
-------------------------------------
File:    myrecord.c
Project: a4_q2
file description
-------------------------------------
Author:  Sahil Khasnobish
ID:      190990560
Email:   khas0560@mylaurier.ca
Version  2021-02-09
-------------------------------------
 */

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include "myrecord.h"

#define MAX_LINE 100

char letter_grade(float s){
	char grade;
	if ((s>=90)&&(s<=100)){
		grade = 'S';
	}
	if ((s>=80)&&(s<90)){
			grade = 'A';
	}
	if ((s>=70)&&(s<80)){
			grade = 'B';
	}
	if ((s>=60)&&(s<70)){
			grade = 'C';
	}
	if ((s>=50)&&(s<60)){
			grade = 'D';
	}
	if ((s>=0)&&(s<50)){
			grade = 'F';
	}
	return grade;
}

int import_data(RECORD dataset[], char *filename) {
	char buf[100],name2[100],score_str[100],c[100];char* end;
	int i=0,result=0,num_records=0,n=0,k=0,type=0;

	FILE *filename2 = fopen(filename,"r");
	if (filename2 == NULL){
		perror("Error opening file");
	}else{
		char * token;

				while(fgets(buf, sizeof(buf), filename2)){
					token = strtok(buf,",");
					char* token2 = token;
					if (*token!='\n'){
					while ((token != NULL)){

						if (type == 0){
							strcpy(name2,token);
							type = 1;
						}else{
							strcpy(score_str,token);
							type = 0;
						}

						token = strtok(NULL,",");
						token2++;
					}


					if (name2!=""){

					RECORD student;
					float score2 = strtof(score_str, &end);
					strcpy(student.name,name2);
					student.score = score2;
					dataset[num_records] = student;
					num_records+=1;

					}
					strcpy(name2,"");
					strcpy(score_str,"");

				}
				}

	}
	return num_records;
}

REPORT report_data(RECORD dataset[], int n, char *filename) {
  REPORT report = {};
  FILE *fp = fopen(filename,"w");
  int i,count=n,x=0;
  float mean = 0;
  float stddev;

  if (n < 1) return report;
  while (x!=count){
	  mean += dataset[x].score;
	  x++;
  }
  mean = mean/count;
  x = 0;
  while (x!=count){

	  stddev +=((dataset[x].score)-mean)*((dataset[x].score)-mean);
	  fwrite(dataset[x].name, strlen(dataset[x].name), 1, fp);
	  fputc(',',fp);
	  fputc(letter_grade(dataset[x].score),fp);
	  fputc('\n',fp);
	  x+=1;
  }
  	  stddev = sqrt(stddev/(count));
  	  report.count = (count);
  	  report.mean = mean;
  	  report.stddev = stddev;


  	  fclose(fp);


  return report;
}
