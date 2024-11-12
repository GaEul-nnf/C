#include <stdio.h>
#include <stdint.h>

void wait_for_user_input(void);

int main(void)
{
	int8_t code;
	float r, b, h, a;
	float area;


	printf("Area calculation program\n");
	printf("Circle    --> c\n");
	printf("Triangle  --> t\n");
	printf("Rectangle --> r\n");
	printf("Square    --> s\n");
	printf("Trapezoid --> z\n");
	printf("Enter the code here:");
	scanf("%c",&code);

	switch(code)
	{
	case 'c':
		printf("Circle Area calculation\n");
		printf("Enter radius(r) value:");
		scanf("%f",&r);
		if(r<0){
			printf("Radius cannot be -ve\n");
			area = -1;
		}else{
			area = 3.1415 * r * r;
		}
		break;
	case 't':
		printf("Triangle Area calculation\n");
		printf("Enter base(b) value:");
		scanf("%f",&b);
		printf("Enter height(h) value:");
		scanf("%f",&h);
		if((b<0)||(h<0)){
			printf("base or height cannot be -ve\n");
			area = -1;
		}else{
			area = (b * h)/2;
		}
		break;
	case 'r':
		printf("Rectangle Area calculation\n");
		printf("Enter width(w) value:");
		scanf("%f",&a);
		printf("Enter length(l) value:");
		scanf("%f",&b);
		if((a<0)||(b<0)){
			printf("width or length cannot be -ve\n");
			area = -1;
		}else{
			area = a * b;
		}
		break;
	case 's':
		printf("Square Area calculation\n");
		printf("Enter side(a) value:");
		scanf("%f",&a);
		if(a<0){
			printf("side cannot be -ve\n");
			area = -1;
		}else{
			area = a * a;
		}

		break;
	case 'z':
		printf("Triangle Area calculation\n");
		printf("Enter base1(a) value:");
		scanf("%f",&a);
		printf("Enter base2(b) value:");
		scanf("%f",&b);
		printf("Enter height(h) value:");
		scanf("%f",&h);
		if((a<0)||(b<0)||(h<0)){
			printf("base1 or base2 or height cannot be -ve\n");
			area = -1;
		}else{
			area = ((a + b)/2) * h;
		}
		break;
	default:
		printf("Invalid input\n");
		area = -1;
	}

	if(area < 0)
	{
		;
	}
	else
	{
		printf("Area = %f\n",area);
	}

	wait_for_user_input();
}

void wait_for_user_input(void)
{
	printf("Press enter key to exit application\n");
	while(getchar() != '\n')
		{

		}
	getchar();
}
