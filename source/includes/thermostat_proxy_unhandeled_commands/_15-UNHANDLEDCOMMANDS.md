## Unhandled Commands

This section includes Commands supported by many protocol drivers but are not directly handled by the Thermostat proxy:


`DEC_SETPOINT_HUMIDIFY`
Used to Decrement the Setpoint by one step.

`DEC_SETPOINT_DEHUMIDIFY`
Used to Decrement the Setpoint by one step.

`INC_SETPOINT_DEHUMIDIFY`
Used to increment the Setpoint by one step.

`INC_SETPOINT_HUMIDIFY`
Used to increment the Setpoint by one step.

`SET_CALIBRATION`
Used to set the calibration value. 

`SET_EVENT`
Occurs when the scheduler determines it's time for a new event to be run for Preset Scheduling

`SET_EVENTS`
XML that is provided from the proxy in the case that a protocol driver wants to push the Preset Schedule to hardware

`SET_REMOTE_SENSOR`
Used to indicate if the remote sensor on the thermostat is in use.

`SET_SCALE`
Used to set the temperature scale the thermostat should use.

`SET_MODE_FAN`
Used to set the current fan mode of the thermostat.

`SET_MODE_HOLD`
Used to set the current hold mode of the thermostat.

`SET_MODE_HUMIDITY`
Used to set the humidification mode in a protocol driver.

`SET_MODE_HVAC`
Used to set the HVAC mode in a protocol driver.

`SET_OUTDOOR_TEMPERATURE`
Set the outdoor temperature which is used by some thermostats for the purpose of humidity balancing, fresh air venting, air quality venting, and other HVAC functionality.

`SET_PRESET`
Occurs when someone selects to run a preset OUTSIDE of its regular schedule. 

`SET_PRESETS`
XML that the Proxy sends down to a protocol driver that contains information about presets. If preset scheduling is a capability of the protocol driver.

`SET_SETPOINT_DEHUMIDIFY`
Used to set the dehumidify setpoint.

`SET_SETPOINT_COOL`
Used to set the cool setpoint. 

`SET_SETPOINT_HEAT`
Used to set the heat setpoint. 

`SET_SETPOINT_HUMIDIFY`
Used to set the humidify setpoint.

`SET_SETPOINT_SINGLE`
Used to set the single setpoint value.

`SET_VAC_SETPOINT_COOL`
Used to set the cool setpoint when it vacation mode

`SET_VAC_SETPOINT_HEAT`
Used to set the heat setpoint when it vacation mode

`SET_VACATION_MODE`
Used to indicate if the thermostat is in vacation mode or not

