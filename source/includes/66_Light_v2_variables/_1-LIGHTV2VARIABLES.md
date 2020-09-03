


| Parameter | Description |
| --- | --- |
| str | PASSCODE |



| **Variable Name** | **ID** | **Description** |
| --- | --- |
| Light State | 1000 | Boolean indicating if the light Brightness is not at the Off preset. If you set this variable to true on a dimmer, it will go to the On preset. On a switch, only the first variable exists. |
| Light Brightness Percent | 1001 | An integer indicating the current brightness for a dimmer. The value should be between 0-100. | Click Rate Up | 1002 | An integer indicating the number of milliseconds. (Used in "On" Preset) |
| Click Rate Down | 1003 | An integer indicating the number of milliseconds. (Used in "Off" Preset) |
| Hold Rate Up | 1004 | An integer indicating the number of milliseconds. (Used in "Slow On" Preset) |
| Default On Preset Brightness | 1006 | An integer indicating what the preset "On" brightness is and thus what a light Brightness would go to if the top wall keypad button is clicked, regardless what the light level is at and including even if the current brightness is higher. (Used in "On" Preset) |
| Max Brightness | 1007 | An integer indicating how high the light will go with a click. To go passed the max (still capped at 100%), you need to press and hold. |
| Min Brightness | 1008 | An integer on how low the light will go before skipping values between this number and 0/completely off. |
| Cold Start Brightness | 1009 | An integer of what level to go to when first turning on before attempting to do a ramp. | 
| Cold Start Time | 1010 An integer indicating the amount of time in milliseconds to stay at the cold start level before starting a ramp. |