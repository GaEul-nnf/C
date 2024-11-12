#include <stdio.h>
#include <stdint.h>

uint8_t const data = 10;

int main(void)
{

	printf("Value = %u\n",data);

	uint8_t *ptr = &data; // uint8_t const *

	*ptr = 50;

	printf("Value = %u\n",data);

	getchar();

}
