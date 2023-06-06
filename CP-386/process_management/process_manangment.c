#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>

/*
 -------------------------------------
 File:    z_creator.c
 Project: a1
 file description
 -------------------------------------
 Author:  Sahil Khasnobish
 ID:      190990560
 Version  2022-05-27

 Author:  Jaini Patel
 ID:      200291740
 Version  2022-05-27
 -------------------------------------
 */

//info_c strucutre is created
typedef struct info_c {
	char commandAll[100];
	char command[50];
} INFO_C;

void writeOutput(char *command, char *output, int opened) {
	FILE *fp;
	fp = fopen("output.txt", "a");
	fprintf(fp, "The output of: %s : is\n", command);
	fprintf(fp, ">>>>>>>>>>>>>>>\n%s<<<<<<<<<<<<<<<\n", output);
	fclose(fp);
}

void read_write(char *args[], INFO_C info, int opened) {
	int fd[2];
	// pipe is created here and checks if it is done correctly
	if (pipe(fd) == -1) {
		fprintf(stderr, "There's an error so pipe can not be opened. \n");
		exit(-1);
	}
	// fork
	pid_t pid_2 = fork();

	//checks if forking is done correctly
	if (pid_2 < 0) {
		fprintf(stderr, "There's an error in forking.");
		exit(1);
	} else if (pid_2 == 0) {
		// the child proccess is created
		close(fd[0]);

		//writes the contents into the output.txt file
		if (dup2(fd[1], STDOUT_FILENO) == -1) {
			fprintf(stderr, "There's an error while redirecting the outputs.");
			exit(1);
		};
		//writes the content into the output.txt
		execvp(args[0], args);

	}
	// parent proccess is created here
	char buffer[1500];

	//the buffer is set to 0 agina
	memset(buffer, 0, sizeof(buffer));

	if (read(fd[0], buffer, sizeof(buffer)) == -1) {
		printf("There's an error so pipe can not be opened. \n");
		exit(-1);
	}

	// write the output from the buffer to the output.txt file
	writeOutput(info.commandAll, buffer, opened);
}

//void string_to_command(){

void convert_string_command( *mptr) {
	//initialize variables
	int num = 0;
	int n = 0;
	int count = 0;
	int size = 1;
	int file_open = 0;

	char *current_command; //the current command that needs to be converted
	const char whitespace1[2] = "\r\n"; //whitespaces that need to be removed

	char command_from_shared_memory[100]; //stores the command saved in shared memory

	strcpy(command_from_shared_memory, mptr); //copies command in shared memory
	current_command = strtok(command_from_shared_memory, whitespace1); //current command with whitespaces removed

	INFO_C *commands = malloc(size * sizeof(INFO_C)); //dynamically allocates more space as commands array has increased

	while (current_command) { // add the current command to the list of all commands
		if (size >= num) { // if the total size of the array is not large enough, doubles the size and then reallocates more memory
			size *= 2;
			commands = realloc(commands, size * sizeof(INFO_C));
		}

		strcpy(commands[num].commandAll, current_command);
		strcpy(commands[num].command, current_command);
		current_command = strtok(NULL, whitespace1);
		num++;
	}
	//this time we need to remove the spaces in between
	const char whitespace2[2] = " ";
	char *second_command;

	while (n < num) {
		if (n != num - 1) {
			commands[n].commandAll[strlen(commands[n].commandAll)] = '\0';
			commands[n].command[strlen(commands[n].command)] = '\0';
		}

		char *args[50];
		//removes the spaces from the command
		second_command = strtok(commands[n].command, whitespace2);

		while (second_command) {
			args[count] = second_command;
			second_command = strtok(NULL, whitespace2);
			count++;
		}
		args[count] = NULL;

		count = 0;

		if (n == 0) {
			file_open = 0;
		} else {
			file_open = 1;
		}

		read_write(args, commands[n], file_open);
		n++;
	}

	free(commands);
}

int main() {
	//initlized requiered varibles
	char l[50];
	int sfd;
	void *mptr;

	// fork is used so that the first child can read and write contents of the file to the shared memory
	pid_t pid = fork();

	//array is created

	if (pid < 0)
		exit(1);

	else if (pid == 0) {
		// child is created here
		FILE *fp = fopen("sample_in_process.txt", "r");

		//shared memory is created
		sfd = shm_open("OS", O_CREAT | O_RDWR, 0644);
		ftruncate(sfd, 5000);
		mptr = mmap(0, 5000, PROT_WRITE, MAP_SHARED, sfd, 0);

		// contents of the file is read and written to the shared memory
		while (fgets(l, 100 - 1, fp) != NULL) {
			sprintf(mptr, "%s", l);
			mptr += strlen(l);
		}

		//close file and shared memory
		close(sfd);
		fclose(fp);

		exit(0);
	}
	// parent porccess is created here
	wait(NULL);

	//shared memory is created
	sfd = shm_open("OS", O_RDONLY, 0666);
	//ftruncate(sfd, 5000);
	mptr = mmap(0, 5000, PROT_READ, MAP_SHARED, sfd, 0);
	convert_string_command(mptr);
	//shared memory is closed
	close(sfd);

	return 0;
}
