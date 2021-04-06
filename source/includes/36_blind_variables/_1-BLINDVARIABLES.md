
Registered Variables included in post 2.9.0 releases include:

`Open` (ID=1000) - A boolean indicating if the control is open.  Will be true when level is at `level_open`.

`Fully Closed` (ID=1001) - A boolean indicating if the control is fully closed.  Will be true when level is at `level_closed`.

`Stopped` (ID=1002) - A boolean indicating if the blind is stopped.  On drivers that support stop and extended functionality, drivers must send stopped = false when the hardware starts to move and stopped = true once it has finished moving.

`Fully Open` (ID=1003) - A boolean indicating if the control is fully open.

`Level` (ID=1004) - An integer indicating the blind level (level range is potentially unique per driver.

`Target Level` (ID=1005) - An integer indicating the target blind level when the hardware is to stop.  This is used to know if a driver is currently going up or down.

`Type` (ID=1006) - A string representation of the enumeration for the type.

`Movement` (ID=1007) - A string representation of the enumeration for the movement.

`Opening` (ID= 1008) - A boolean indicating if the control is in the process of opening.

`Closing` (ID= 1009) - A boolean indicating if the control is in the process of closing.

