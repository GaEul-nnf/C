#include <stdio.h>

int function_add_numbers(int a, int b, int c );

int main()
{
	int retValue;

	retValue = function_add_numbers(12, 13, 0);

	printf("Sum = %d\n",retValue);

	return 0;
}


int function_add_numbers(int a, int b, int c )
{
	int sum;
	sum = a+b+c;

	return sum;
}
