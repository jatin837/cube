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
		for (y = 0; y <= CUBE_WIDTH; y++){
			for (z = -10; z <= CUBE_WIDTH; z++){
				x = CUBE_SIZE;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;
				rotate(&x_temp, &y_temp, &z_temp);
				int x_p, y_p = project(&x_temp, &y_temp, &z_temp);
				OUT_SCR[flatten(x_p, y_p)] = '.';
			}
		}
		for (y = 0; y <= CUBE_WIDTH; y++){
			for (z = -10; z <= CUBE_WIDTH; z++){
				x = 0;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;
				rotate(&x_temp, &y_temp, &z_temp);
				int x_p, y_p = project(&x_temp, &y_temp, &z_temp);
				OUT_SCR[flatten(x_p, y_p)] = '.';
			}
		}
		for (y = 0; y <= CUBE_WIDTH; y++){
			for (z = -10; z <= CUBE_WIDTH; z++){
				x = CUBE_WIDTH;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;
				rotate(&x_temp, &y_temp, &z_temp);
				int x_p, y_p = project(&x_temp, &y_temp, &z_temp);
				OUT_SCR[flatten(x_p, y_p)] = '.';
			}
		}
		for (y = 0; y <= CUBE_WIDTH; y++){
			for (z = -10; z <= CUBE_WIDTH; z++){
				x = CUBE_WIDTH;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;
				rotate(&x_temp, &y_temp, &z_temp);
				int x_p, y_p = project(&x_temp, &y_temp, &z_temp);
				OUT_SCR[flatten(x_p, y_p)] = '.';
			}
		}
		for (y = 0; y <= CUBE_WIDTH; y++){
			for (z = -10; z <= CUBE_WIDTH; z++){
				x = CUBE_WIDTH;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;
				rotate(&x_temp, &y_temp, &z_temp);
				int x_p, y_p = project(&x_temp, &y_temp, &z_temp);
				OUT_SCR[flatten(x_p, y_p)] = '.';
			}
		}
		for (y = 0; y <= CUBE_WIDTH; y++){
			for (z = -10; z <= CUBE_WIDTH; z++){
				x = CUBE_WIDTH;
				x_temp = (float) x;
				y_temp = (float) y;
				z_temp = (float) z;
				rotate(&x_temp, &y_temp, &z_temp);
				int x_p, y_p = project(&x_temp, &y_temp, &z_temp);
				OUT_SCR[flatten(x_p, y_p)] = '.';
			}
		}
	}
		theta += 1.0f;
	return 0;
}
