PROGRAM = graphdb
OBJS	= main.o
CC		= g++
CFLAGS	= -Wall -O2

all: $(OBJS)
	$(CC) -o $(PROGRAM) main.cc node.o $(CFLAGS)

%.o: %.cc
	$(CC) -c -o %.o $(CFLAGS) $<