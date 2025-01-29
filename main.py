function 调用机械臂初始化 (_90: game.LedSprite) {
	
}
let _83: game.LedSprite = null
makerbit.connectIrReceiver(DigitalPin.P0, IrProtocol.Keyestudio)
let speed5 = 1
let STOP = 0
pins.digitalWritePin(DigitalPin.P0, 0)
pins.servoWritePin(AnalogPin.P3, 90)
pins.servoWritePin(AnalogPin.P4, 90)
basic.showIcon(IconNames.Heart)
调用机械臂初始化(_83)
