/*
 * main.c
 *
 *  Created on: Nov 7, 2024
 *      Author: OWNER
 */

#include <stdio.h>

#define AREA_CIR
#define AREA_TRI

int main()
{
#if define(AREA_CIR) && define(AREA_TRI)
		printf("This is circle area calculation program\n");
#endif

	float radius = 0;
	fflush(stdout);
	printf("Enter the radius :");
	fflush(stdout);
	scanf("%f", &radius);
	printf("Area of circle  = %f\n",(3.1415 * radius * radius));
	fflush(stdout);

	printf("This is Triangle area calculation program\n");
	float base, height;
	fflush(stdout);
	printf("Enter base and height: ");
	fflush(stdout);
	scanf("%f%f",&base, &height);
	printf("Area of triangle = %f\n", (0.5 * base * height));

	return 0;

}
