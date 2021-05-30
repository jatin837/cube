out: main.c
	gcc -o out main.c -lm -Wimplicit-function-declaration -Wincompatible-pointer-types

compile: main.c
	gcc -c -o out main.c -lm

clean:
	rm ./out
