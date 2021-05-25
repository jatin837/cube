#include <stdio.h>

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

int main(void){
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
	Co2 e = project(E);
	Co2 f = project(F);
	Co2 g = project(G);
	Co2 h = project(H);
	printf("%f %f %f\n", A.x, A.y, A.z);
	printf("%f %f %f\n", B.x, B.y, B.z);
	printf("%f %f %f\n", C.x, C.y, C.z);
	printf("%f %f %f\n", D.x, D.y, D.z);
	printf("%f %f %f\n", E.x, E.y, E.z);
	printf("%f %f %f\n", F.x, F.y, F.z);
	printf("%f %f %f\n", G.x, G.y, G.z);
	printf("%f %f %f\n", H.x, H.y, H.z);
	printf("%f %f\n", a.x, a.y);
	printf("%f %f\n", b.x, b.y);
	printf("%f %f\n", c.x, c.y);
	printf("%f %f\n", d.x, d.y);
	printf("%f %f\n", e.x, e.y);
	printf("%f %f\n", f.x, f.y);
	printf("%f %f\n", g.x, g.y);
	printf("%f %f\n", h.x, h.y);
	return 0;
}
