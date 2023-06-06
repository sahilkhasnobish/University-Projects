/*
 -------------------------------------
 File:    z_terminator.c
 Project: a1
 file description
 -------------------------------------
 Author:  Sahil Khasnobish
 ID:      190990560
 Email:   khas0560@mylaurier.ca
 Version  2022-05-29
 -------------------------------------
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
 * we can start a loop, in the loop we
 * do the ps -l command which lists a process
 * we then identify if it is a zombie, if it is,
 * then we kill it
 */
int main() {
	int ppid;
	int x = 0;
	while (x) {
		//list all running processes
		char command_listprocess[100];
		strcpy(command_listprocess, "ps -l");
		//get the parent of the zombie
		char command_ppid[100];
		strcpy(command_ppid, "ps -el | grep -wZ|tr -s''|cut -d''-f5");
		ppid = system(command_ppid);
		//kill the parent process
		char command_kill[100];
		char ppid_string[100];
		//strcpy(command_kill, "kill -9 <%d>", ppid);
		strcpy(command_kill, "kill -9 <");
		sprintf(ppid_string, "%d", ppid);
		strcpy(command_kill, ">");
		system(command_kill);

	}
}

