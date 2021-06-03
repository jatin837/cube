#include <stdio.h>
#include <unistd.h>

void rotate(float *x , float *y, float *z, float theta);
void project(float *x , float *y, float *z, float theta);
// TESTING
// --------
// 	project function should take inputs and print '.' at projected x and projected y
//
int main(void){
	float x, y, z, x_temp, y_temp, z_temp;
	char output[100];
	float theta = 0.0f;
	while(1){
		for (y = -10; y <= 10; y++){
			for (z = -10; z <= 10; z++){
				x = 10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;
				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		for (y = -10; y <= 10; y++){
			for (z = -10; z <= 10; z++){
				x = -10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		for (x = -10; x <= 10; x++){
			for (z = -10; z <= 10; z++){
				y = -10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		for (x = -10; x <= 10; x++){
			for (z = -10; z <= 10; z++){
				y = 10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		for (x = -10; x <= 10; x++){
			for (y = 10; y <= 10; y++){
				z = -10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		for (x = -10; x <= 10; x++){
			for (y = -10; y <= 10; y++){
				z = -10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		theta += 1.0f;
	}
	return 0;
}
