## THERMOSTAT PROXY VARIABLES

Thermostats that use this proxy have the following registered variables that can be manipulated:
Note: Temperature Units are stored and processed in the proxy as Current Units, `Kelvin * 10`, or `Celsius * 10` depending on V1, V2 and programming.


`CALIBRATION` (ID=1129) - int - Set to the value given with the Notify `CALIBRATION_CHANGED`


`CoolSetPoint_C` (ID=1135) - Read only - Double representing the cool setpoint. Replaces CoolSetpoint


`CoolSetPoint_F` (ID=1134) - Read only - Double representing the cool setpoint. Replaces CoolSetpoint


`PRESET` (ID=1144) - Read Only - Name of the currently Active Preset in Preset Scheduling.


`DEHUMIDIFY_SETPOINT` (ID=1143) - Read Only - Percent 0-100. (Note: The range and resolutions are set via capabilities)


`FAN_MODE` (ID=1105) - string - Current Fan Mode


`HEATCOOL_SETPOINTS_DEADBAND_C` (ID=1147) - Read Only - string - Setpoint different between heat and cool


`HEATCOOL_SETPOINTS_DEADBAND_F` (ID=1146) - Read Only - string - Setpoint different between heat and cool


`HeatSetPoint_F` (ID=1132) - Read only - Double representing the heat setpoint. Replaces HeatSetpoint


`HeatSetPoint_C` (ID=1133) - Read only - Double representing the heat setpoint. Replaces HeatSetpoint


`HEATPUMP` (ID=1124) - bool - Whether or not a heat pump exists.


`HOLD_MODE `(ID=1106) - string - Current Hold Mode


`HOLD_MODES_LIST` (ID=1122) - string - comma separated list of hold modes that can be selected for the thermostat.


`HEATCOOL_SETPOINTS_DEADBAND_C` (ID=1147) - Read Only - string - Setpoint different between heat and cool


`HUMIDITY_STATE` (ID=1141) - Read Only - Currently state. Typically Humidify, Humidify Auto or Dehumidify.


`HVAC_MODES_LIST` (ID=1120) - string - comma separated list of hvac modes that can be selected for the thermostat.


`HVAC STATE` (ID=1107) - string - Current HVAC State (Could be Heat, Heating, Cool, Cooling, 1st Stage Heat, or any other phrase passed in by the protocol driver for the` HVAC_STATE` notify.


`HVAC_MODE` (ID=1104) - string - Current HVAC Mode


`IS_CONNECTED` (ID=1112) - bool - Indicator if the hardware is online/available.  This will be set to 'true' on startup UNLESS a protocol driver has the `has_connection_status` capability set to true.  If this value is false, UI's will display "–" for temperature when the device is offline.


`MESSAGE` (ID=1145) - Read Only - Status message that a protocol driver can send to the UI


`REVERSING_VALVE` (ID=1128) - string - Name of reversing valve.


`SINGLE_SETPOINT_F` (ID=1149) - Read only - Double representing the single setpoint.


`SINGLE_SETPOINT_F` (ID=1149) - Read only - Double representing the single setpoint.


`OUTDOOR_TEMPERATURE_C` (ID=1137) - Can be read and written. Read is for providing info to UI/Navigator or other thermostats and write is for allowing programming and other devices to set this value, which can be read by some devices (Including the C4 AAT Thermostat) so they do not have to be hard wired to outside to perform some calculations.


`OUTDOOR_TEMPERATURE_F` (ID=1136) - Can be read and written. Read is for providing info to UI/Navigator or other thermostats and write is for allowing programming and other devices to set this value, which can be read by some devices (Including the C4 AAT Thermostat) so they do not have to be hard wired to outside to perform some calculations.


`SCALE` (ID=1100) - String - the current scale that was passed in on the `SCALE_CHANGED` notify.


`SCHEDULE` (ID=1113) - string - XML of the entire schedule


`TEMPERATURE_C` (ID=1131) - Read only - Double representing the temperature. Replaces TEMPERATURE


`TEMPERATURE_F` (ID=1130) - Read only - Double representing the temperature. Replaces TEMPERATURE


`VACATION_MODE` (ID=1109) - bool - Will be set to the value passed in for the `VACATION_MODE's` `ON_VACATION` parameter.
This variable will be deprecated when the traditional scheduling model is deprecated. No date has been set at this time for this deprecation.