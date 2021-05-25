out: main.c
	gcc -o out main.c -lm -Wimplicit-function-declaration -Wincompatible-pointer-types

clean:
	rm ./out
