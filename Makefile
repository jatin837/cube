out: main.o project.o rotate.o
	gcc -o out main.o rotate.o -lm 

main.o: main.c
	gcc -c -o main.o main.c

rotate.o: rotate.c
	gcc -c -o rotate.o rotate.c -lm

project.o: project.c
	gcc -c -o project.o project.c 

clean:
	rm *.o out
