/*
 -------------------------------------
 File:    Question_2.c
 Project: A3
 file description
 -------------------------------------
 Author:  Sahil Khasnobish
 ID:      190990560
 Version  2022-06-30

 Author:  Jaini Patel
 ID:      200291740
 Version  2022-06-30
 -------------------------------------
 */
#include <stdio.h>
#include <pthread.h>
#include <unistd.h>
#include <stdlib.h>
void inc_dec();

pthread_mutex_t lock;
//initialize global variables
int a = 5;
int b = 7;
int count = 1;

int main() {
	pthread_t tid_1;
	pthread_t tid_2;
	pthread_t tid_3;

	//initialize mutex lock
	pthread_mutex_init(&lock, NULL);

	pthread_create(&tid_1, NULL, inc_dec, NULL);

	pthread_create(&tid_2, NULL, inc_dec, NULL);

	pthread_create(&tid_3, NULL, inc_dec, NULL);

	pthread_mutex_destroy(&lock);

	pthread_exit(NULL);
	return 0;
}
//critical section
void inc_dec() {

	pthread_mutex_lock(&lock);
	printf("Read value of 'a' global variable is: %d\n", a);
	printf("Read value of 'b' global variable is: %d\n", b);

	if (count == 1) {
		a = 6;
		b = 6;
	} else if (count == 2) {
		a = 7;
		b = 5;
	} else if (count == 3) {
		a = 8;
		b = 4;
	}

	count++;

	printf("Updated Value of 'a' variable is: %d\n", a);
	printf("Updated Value of 'b' variable is: %d\n\n", b);
	pthread_mutex_unlock(&lock);
}

