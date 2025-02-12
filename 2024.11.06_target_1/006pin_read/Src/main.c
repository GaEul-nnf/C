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

#include<stdint.h>

int main(void)
{
    uint32_t volatile *const pClkCtrlReg =   (uint32_t*)0x40023830;
    uint32_t volatile *const pPortAModeReg = (uint32_t*)0x40020000;
    uint32_t volatile *const pPortAOutReg =  (uint32_t*)0x40020014;

	uint32_t  const volatile *const pPortAInReg = (uint32_t*)0x40020010;

    *pClkCtrlReg |= (1<<0);

    *pPortAModeReg &= ~(3<<4);
    *pPortAModeReg |= (1<<10);

	*pPortAModeReg &= ~(3 << 0);

	while(1)
	{
		uint8_t  pinStatus = (uint8_t)(*pPortAInReg & 0x1);

		if(pinStatus){
			*pPortAOutReg |= (1<<5);
		}else{
			*pPortAOutReg &= ~(1<<5);
		}
	}

}
