#include <stdio.h>

void project(float *x, float *y, float *z){
	printf("\033[{%d};{%d}H", (int)*x, (int)*y);
	printf(".");
}
