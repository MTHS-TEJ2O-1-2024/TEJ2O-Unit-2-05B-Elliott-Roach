/* Copyright (c) 2020 MTHS All rights reserved
 *
 * Created by: elliott
 * Created on: Sep 2024
 * This program takes temperature and converts to Kelven
*/

let temperature: number

basic.clearScreen()
basic.pause(1000)

input.onButtonPressed(Button.A, function () {
    temperature = input.temperature()
    temperature = temperature + 273.15
    temperature = Math.round(temperature)
    basic.showString('the temperature is:')
    basic.showNumber(temperature)
    basic.showString('K.')
    basic.showIcon(IconNames.Happy)
})
