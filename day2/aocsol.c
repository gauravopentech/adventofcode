#include "aoc.h"
#include <stdio.h>
#include <stdlib.h>

#define READ_FILE FILE *fp = getFilePointer("./input.txt");
#define DEFINE_READ_FIRST_LINE char *line = getNextLine(fp);

void partOne() {
  READ_FILE
  DEFINE_READ_FIRST_LINE
  while (line != NULL) {
    printf("%s", line);
    line = getNextLine(fp);
  }
  fclose(fp);
}

void partTwo() {
  READ_FILE
  DEFINE_READ_FIRST_LINE
  while (line != NULL) {
    printf("%s", line);
    line = getNextLine(fp);
  }
  fclose(fp);
}

int main(int argc, char *argv[]) {
  partOne();
  // partTwo();

  return 0;
}
