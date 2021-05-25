#include <stdio.h>
#include <math.h>
#include <unistd.h>
#include <signal.h>

typedef struct {
	float x, y, z;
}Co3;

typedef struct {
	float x, y;
} Co2;

Co2 project(Co3 Coordinate){
	Co2 res;
	res.x = Coordinate.x;		
	res.y = Coordinate.y;		
	return res;
}

Co3 rotate_X(Co3 Coordinate){
	//impl rotation matrix
}

Co3 rotate_Y(Co3 Coordinate){
	//impl rotation matrix
}

Co3 rotate_Z(Co3 Coordinate){
	//impl rotation matrix
}

Co2 rotate(Co2 Coordinates, float theta){
	float temp_x, temp_y;
	temp_x = Coordinates.x*cos(theta) - Coordinates.y*sin(theta);	
	temp_y = Coordinates.y*cos(theta) + Coordinates.x*sin(theta);	
	Co2 aux_coordinate = {temp_x, temp_y};
	return aux_coordinate;
}

void handle_sig(void){
	printf("\033[?25h");
	printf("bye\n");
	exit(0);
}

int main(void){
	float theta = 0.0f; 
	Co3 A = {8.0f, 8.0f, 8.0f};
	Co3 B = {8.0f, 16.0f, 8.0f};
	Co3 C = {16.0f, 16.0f, 8.0f};
	Co3 D = {16.0f, 8.0f, 8.0f};
	Co3 E = {8.0f, 8.0f,  16.0f};
	Co3 F = {8.0f, 16.0f, 16.0f};
	Co3 G = {16.0f, 16.0f,16.0f};
	Co3 H = {16.0f, 8.0f, 16.0f};
	Co2 a = project(A);
	Co2 b = project(B);
	Co2 c = project(C);
	Co2 d = project(D);
	while(1){
		signal(SIGINT, handle_sig);
		printf("\033[2J");
		printf("\033[H");
		printf("\033[?25l");
		usleep(200000);
		theta += M_PI/180;
		a = rotate(a, theta);
		b = rotate(b, theta);
		c = rotate(c, theta);
		d = rotate(d, theta);
		printf("a = (%f, %f), b = (%f, %f), c = (%f, %f), d = (%f, %f)\n\n\n", a.x, a.y, b.x, b.y, c.x, c.y, d.x, d.y);
	}
	return 0;
}
