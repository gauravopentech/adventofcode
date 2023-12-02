#include <stdio.h>
#include <stdlib.h>

FILE *getFilePointer(char *filename) {
  FILE *fp = fopen(filename, "r");
  if (fp == NULL) {
    printf("Error opening file %s\n", filename);
    exit(1);
  }
  return fp;
}

char *getNextLine(FILE *fp) {
  char *line = NULL;
  size_t len = 0;
  ssize_t read;
  read = getline(&line, &len, fp);
  if (read == -1) {
    return NULL;
  }
  return line;
}
