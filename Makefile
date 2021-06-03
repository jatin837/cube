out: main.o project.o rotate.o flatten.o
	gcc -o out main.o rotate.o -lm 

main.o: main.c
	gcc -c -o main.o main.c

rotate.o: rotate.c
	gcc -c -o rotate.o rotate.c -lm

flatten.o: flatten.c
	gcc -c -o flatten.o flatten.c 

project.o: project.c
	gcc -c -o flatten.o flatten.c 

clean:
	rm *.o out
