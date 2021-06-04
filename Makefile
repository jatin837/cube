OBJ := ./obj/
HEADER := ./headers/
SRC := ./src/

out: main.o project.o rotate.o flatten.o
	gcc -o out $(OBJ)main.o $(OBJ)rotate.o $(OBJ)project.o $(OBJ)flatten.o -lm 

main.o: main.c
	gcc -c -o $(OBJ)/main.o main.c

rotate.o: $(SRC)rotate.c
	gcc -c -o $(OBJ)/rotate.o $(SRC)rotate.c -lm

flatten.o: $(SRC)flatten.c
	gcc -c -o $(OBJ)/flatten.o $(SRC)flatten.c 

project.o: $(SRC)project.c
	gcc -c -o $(OBJ)/project.o $(SRC)project.c 

clean:
	rm out ./$(OBJ)/*
