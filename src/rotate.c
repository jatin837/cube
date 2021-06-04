#include "../headers/rotate.h"
#include <math.h>

void rotate(float *X, float *Y, float *Z, float theta){
	float x = *X, y = *Y, z = *Z;
	float a, b, c;
	float sinT = sin(theta*M_PI/180);
	float cosT = cos(theta*M_PI/180);
	a = cosT*(x*cosT - y*sinT) + z*sinT;
	b = cosT*(x*sinT + y*cosT) - sinT*(z*cosT - sinT*(x*cosT - y*sinT));
	c = sinT*( x*sinT + y*cosT ) + cosT*( z*cosT - sinT*( x*cosT - y*sinT ) );
	*X = a;
	*Y = b;
	*Z = c;	
}