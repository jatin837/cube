OBJ := ./obj/
out: main.o project.o rotate.o flatten.o
	gcc -o out $(OBJ)main.o $(OBJ)rotate.o $(OBJ)project.o $(OBJ)flatten.o -lm 

main.o: main.c
	gcc -c -o obj/main.o main.c

rotate.o: rotate.c
	gcc -c -o obj/rotate.o rotate.c -lm

flatten.o: flatten.c
	gcc -c -o obj/flatten.o flatten.c 

project.o: project.c
	gcc -c -o obj/project.o project.c 

clean:
	rm out ./obj/*
