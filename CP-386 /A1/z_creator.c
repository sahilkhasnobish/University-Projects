/*
 -------------------------------------
 File:    z_creator.c
 Project: a1
 file description
 -------------------------------------
 Author:  Sahil Khasnobish
 ID:      190990560
 Email:   khas0560@mylaurier.ca
 Version  2022-05-27
 -------------------------------------
 */

#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int main_creator(void) {
	pid_t pid;
	int x = 10;
	pid = fork();
	if (pid < 0) {
		fprintf(stderr, "could not create process");
		return 1;
	} else if (pid == 0) {
		sleep(x);
		return 0;
	} //we dont call wait meaning the above child process becomes a zombie
	return 0;
}
