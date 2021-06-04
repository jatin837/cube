#include "../headers/project.h"

int* project(float x, float y, float z){
	int *zo = (O_POINT + 2);
	int res[2];
	x =(int) x*(*zo)/z;
	y = (int) y*(*zo)/z;
	res[0] = x;
	res[1] = y;
	return res;
}
