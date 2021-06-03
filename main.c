#include <stdio.h>
#include <unistd.h>

#include "data.h"
#include "flatten.h"
#include "rotate.h"
#include "project.h"

int main(void){
	char O_SCR[SRC_WIDTH*SRC_HEIGHT];
	memset(O_SCR, " ", SCR_WIDTH*SCR_HEIGHT);
	float x, y, z, x_temp, y_temp, z_temp;
	float theta = 0.0f;
	while(1){
		for (y = -10; y <= 10; y++){
			for (z = -10; z <= 10; z++){
				x = 10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;
				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp);
			}
		}
		for (y = -10; y <= 10; y++){
			for (z = -10; z <= 10; z++){
				x = -10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp);
			}
		}
		for (x = -10; x <= 10; x++){
			for (z = -10; z <= 10; z++){
				y = -10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp);
			}
		}
		for (x = -10; x <= 10; x++){
			for (z = -10; z <= 10; z++){
				y = 10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp);
			}
		}
		for (x = -10; x <= 10; x++){
			for (y = 10; y <= 10; y++){
				z = -10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp);
			}
		}
		for (x = -10; x <= 10; x++){
			for (y = -10; y <= 10; y++){
				z = -10;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;

				rotate(&x_temp, &y_temp, &z_temp, theta);
				project(&x_temp, &y_temp, &z_temp);
			}
		}
		theta += 1.0f;
	}
	return 0;
}
