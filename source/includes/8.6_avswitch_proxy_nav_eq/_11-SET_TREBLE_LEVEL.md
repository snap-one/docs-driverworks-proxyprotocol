## SET\_TREBLE\_LEVEL

Navigator EQ command called to set the treble level for tone control. The driver should notify the proxy with TREBLE\_LEVEL\_CHANGED notification of the new value.


### Signature

`SET_TREBLE_LEVEL`


| Parameter | Description |
| --- | --- |
| int | OUTPUT: OutputBindingID |
| int | LEVEL: Treble level. Range is -12 to 12. |


### Returns

`None`