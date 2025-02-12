/**
 ******************************************************************************
 * @file           : main.c
 * @author         : Auto-generated by STM32CubeIDE
 * @brief          : Main program body
 ******************************************************************************
 * @attention
 *
 * Copyright (c) 2024 STMicroelectronics.
 * All rights reserved.
 *
 * This software is licensed under terms that can be found in the LICENSE file
 * in the root directory of this software component.
 * If no LICENSE file comes with this software, it is provided AS-IS.
 *
 ******************************************************************************
 */

#include <stdint.h>
#include "main.h"

/*    uint32_t *pClkCtrlReg =   (uint32_t*)0x40023830;
    uint32_t *pPortAModeReg = (uint32_t*)0x40020000;
    uint32_t *pPortAOutReg =  (uint32_t*)0x40020014;
*/

int main(void)
{
	RCC_AHB1ENR_t volatile *const pClkCtrlReg = (RCC_AHB1ENR_t*)0x40023830;
	GPIOx_MODE_t volatile *const pPortAModeReg = (RCC_AHB1ENR_t*)0x40020000;
	GPIOx_ODR_t volatile *const pPortAOutReg = (RCC_AHB1ENR_t*)0x40020014;

	pClkCtrlReg->gpioa_en = 1;

	pPortAModeReg->pin_5 = 1;

    while(1)
    {
    	pPortAOutReg->pin_5 = 1;

    	for(uint32_t i=0 ; i<100000 ; i++);

    	pPortAOutReg->pin_5 = 0;

    	for(uint32_t i=0 ; i<100000 ; i++);
    }
}
