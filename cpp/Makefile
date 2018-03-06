PROGRAM = graphdb
SRCDIR	= ./src
SOURCES = $(wildcard $(SRCDIR)/*.cc)
OBJECTS = $(subst ./obj/./src, ./obj, $(addprefix $(OBJDIR)/, $(SOURCES:.cc=.o)))
OBJDIR  = ./obj
INCLUDE = -I./include/
CC		= g++
CFLAGS	= -Wall -O2 -std=c++14

$(PROGRAM): $(OBJECTS)
	$(CC) -o $@ $^

$(OBJDIR)/%.o: $(SRCDIR)/%.cc
	$(CC) -c -o $@ $(CFLAGS) $(INCLUDE) $<

echo: 
	echo $(SOURCES)

clean:
	rm $(OBJDIR)/*.o
	rm ./$(PROGRAM)
