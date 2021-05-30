#include <stdio.h>
#include <math.h>

void rotate(float *x , float *y, float *z, float theta);

int main(void){
	float x, y, z;
	char output[2500];
	float theta = 0.0f;
	while(1){
		//generate the cube centered at origin
		//
		for (y = -100; y <= 100; y++){
			for (z = -100; z <= 100; z++){
				x = 100;
				//rotate in all three directions
				rotate(&x, &y, &z, theta);
				printf("%f, %f, %f\n", x, y, z);
				//calculate the dot product of <x, y, z> and surface normal
				//but how do i calculate surface normal
				// ----------Potential Method-----------
				// 	1> rotate <1000, 0, 0> with same values as other points in this cube
				//	2> assuming light source at origin (<0, 0, 0>), find position vector of every point WRT origin 
				//	3> take dot product of Position vector and surface normal

				
			}
		}
		theta += 0.01f;
		
	}
	return 0;
}

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
