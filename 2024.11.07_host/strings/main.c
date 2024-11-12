/*
 * main.c
 *
 *  Created on: Nov 7, 2024
 *      Author: OWNER
 */

#include <stdint.h>
#include <stdio.h>
//
//int main(void)
//{
//	char msg1[] = "Hello how are you?";
//	char const *pmsg2 = "fastbitlab.com";
//
//	msg1[0] = 'b';
////	pmsg2[0] = 'b';
//
//    printf("Message is : %s\n",msg1);
//    printf("Message is : %s\n",pmsg2);
//    printf("Address of 'pmsg2' variable = %p\n",&pmsg2);
//    printf("Value of 'pmsg2' variable = %p\n",pmsg2);
//
//	return 0;
//}

int main()
{
    char name[30];
    printf("Enter your name :");
    fflush(stdout);
    scanf("%s",name);

    printf("Hi,%s\n",name);
    fflush(stdout);

//    for(int i=0 ; i<30 ; i++)
//    {
//        printf("%x\n",name[i]);
//    }

    return 0;
}
