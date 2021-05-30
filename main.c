#include <stdio.h>
#include <math.h>

void rotate(float *x , float *y, float *z, float theta);

int main(void){
	int x, y, z;
	char output[2500];
	float theta = 0.0f;
	while(1){
		//generate the cube centered at origin
		//
		for (y = -1000; y <= 1000; y++){
			for (z = -1000; z <= 1000; z++){
				x = 1000;
				//rotate in all three directions
				rotate(&x, &y, &z, theta);
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
