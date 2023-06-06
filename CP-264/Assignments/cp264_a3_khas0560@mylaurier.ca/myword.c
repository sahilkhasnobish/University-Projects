#include <stdio.h>
#include <string.h>
#include "mystring.h"
#include "myword.h"

void set_stopword(char *filename, char *stopwords[])
{
  FILE *fp=fopen("common-english-words.txt","r");
  char buf[128];
  if (fp==NULL){
    perror("Error openning file");
  }
  while(!feof(fp)){
    fgets(buf, sizeof(buf),fp);

    }
  }

// your implementation, refer to class code example 22 -- csv file read with string value
}

// this function check if word is a word in string str, 
// returns 1 if yes, 0 otherwise
int contain_word(char *str, char *word)
{
  char word_list[30];
  char *n = str;
  int i=0;
  if (str == NULL || word == NULL) return 0; 
  lower_case(str);
  trim(str);
  while (i<str_length(str)){
    

  }

  return 0;
}

// this function check if the word is contained in directory stopwords[] 
// returns 1 if yes, 0 otherwise. It use function contain_word()
int is_stopword(char *stopwords[], char *word)
{
// your code
}


int process_word(char *filename, WORDSUMMARY *ws, char *stopwords[])
{
  const char delimiters[] = " .,;:!()&?-\n\t\r\"\'"; 
  // your implementation
  
}

int save_to_file(char *filename, WORDSUMMARY *ws)
{
// your implementation
}