

# CC = clang
CC = gcc
CFLAGS = -g -Wall -std=c99
BIN = aocsol

all: $(BIN)

libaoc.o: ../lib/libaoc.c ../include/aoc.h
	$(CC) $(CFLAGS) -c ../lib/libaoc.c 

aocsol: aocsol.c libaoc.o
	$(CC) $(CFLAGS) -o $@ $^ -I../include

clean:
	rm -rf *.o *.dSYM $(BIN)
