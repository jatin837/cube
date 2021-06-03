#include <stdio.h>
#include <unistd.h>

void rotate(float *x , float *y, float *z, float theta);

int main(void){
	float x, y, z, x_temp, y_temp, z_temp;
	char output[2500];
	float theta = 0.0f;
	while(1){
		printf("working");
		for (y = -30; y <= 30; y++){
			for (z = -30; z <= 30; z++){
				x = 30;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;
				rotate(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		for (y = -30; y <= 30; y++){
			for (z = -30; z <= 30; z++){
				x = -30;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		for (x = -30; x <= 30; x++){
			for (z = -30; z <= 30; z++){
				y = -30;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		for (x = -30; x <= 30; x++){
			for (z = -30; z <= 30; z++){
				y = 30;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		for (x = -30; x <= 30; x++){
			for (y = -30; y <= 30; y++){
				z = 30;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		for (x = -30; x <= 30; x++){
			for (y = -30; y <= 30; y++){
				z = -30;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
			}
		}
		theta += 1.0f;
	}
	return 0;
}
