/*
 -------------------------------------
 File:    190990560_200291740_a04.c
 Project: A4
 file description
 -------------------------------------
 Author:  Sahil Khasnobish
 ID:      190990560
 Version  2022-07-15

 Author:  Jaini Patel
 ID:      200291740
 Version  2022-07-15
 -------------------------------------
 */
#include <stdio.h>
#include <string.h>
#define MAX = 1048565//max memory as passed when program starts
//int partitions[3]; //each index represents a parition, the value in the index is the mem size

typedef struct process {
	int pid;
	int size;
	char mem_alg;
} Process;

int main() {
	//int count = 0;
	//Process process_list[3];

	int exit = 0;
	//char command[100];

	while (!exit) {
		char command[100];
		//extract data from user input
		scanf("%s", command);
		char *d = " ";
		char *token = strtok(command, d);
		/*
		 char R[2];
		 strcpy(R, token);

		 token = strtok(NULL, d);
		 char p[2];
		 strcpy(p, token);

		 token = strtok(NULL, d);
		 char pid[6];
		 strcpy(pid, token);

		 token = strtok(NULL, d);
		 char mem_alg[1];
		 strcpy(mem_alg, token);

		 printf("%s", p);
		 */
		//printf(token);
		while (token != NULL) {
			printf(token);
			token = strtok(NULL, d);
		}
		//printf("%s", command);

		//for (int i = 0; i < 2; i++) {
		//	printf("%c", command[i]);
		//}

		//for (int i = 3; i < 5; i++) {
		//printf("%c", command[i]);
		//}

		//printf("%c", command[13]);

		//create process
		/*
		 Process p;
		 p.pid = pid;
		 p.size = size;
		 p.mem_alg = mem_alg;

		 //add process to process_list
		 if (count == 0)
		 process_list[count] = p;
		 count += 1;
		 if (count == 1)
		 process_list[count] = p;
		 count += 1;
		 if (count == 1)
		 process_list[count] = p;

		 //call appropriate algorithm function
		 if (mem_alg == 'B') {
		 best_fit(p);
		 }
		 if (mem_alg == 'W') {
		 worst_fit();
		 }
		 if (mem_alg == 'F') {
		 first_fit();
		 }
		 */

	}
}
/*
 void best_fit(Process p) {
 int best_space = 0;
 for (int i = 0; i < 3; i++) {
 if (partitions[i] <= MAX-p.size)
 best_space = i;
 }
 partitions[best_space] = p.size;
 }

 void worst_fit(Process p) {
 int worst_space = 0;
 for (int i = 0; i < 3; i++) {
 if (partitions[i] > MAX-p.size)
 worst_space = i;
 }
 partitions[worst_space] = p.size;
 }

 void first_fit(Process p) {
 for (int i = 0; i < 3; i++) {
 if (partitions[i] >= MAX-p.size)
 partitions[i] = p.size;
 break;
 }
 }
 */
