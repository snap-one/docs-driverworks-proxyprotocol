## HOLD MODE CHANGED

Notification that should be sent to the proxy when hold mode has changed. Changes the variables `HOLD_MODE`, `ANA_HOLDMODE`. Fires event `HOLD_MODE_CHANGED`.


### Signature

`C4:HOLD_MODE_CHANGED ()` 


| Parameter | Description |
| --- | --- |
| str | MODE: One of the supported hold modes for example: Off, 2 Hours, Permanent. Required parameter options if Hold Mode is "Hold Until" : YEAR - integer 2000+,  MONTH - integer 0-11,  DAY - integer 0-31,  HOUR - integer 0-23, MINUTE - integer 0-60. |



### Returns

`None`

