## SET BASS LEVEL

Navigator EQ command called to set the bass level for tone control. The driver should notify proxy with the  BASS\_LEVEL\_CHANGED notification of the new value.


### Signature

`SET_BASS_LEVEL`


| Parameter | Description |
| --- | --- |
| int | OUTPUT: OutputBindingID |
| int | LEVEL: Bass level. range is -12 to 12 |

### Returns

`None`