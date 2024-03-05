## SET\_BASS\_LEVEL

Navigator EQ command called to set the bass level for tone control. The driver should notify proxy with the  BASS\_LEVEL\_CHANGED notification of the new value.


### Name

`SET_BASS_LEVEL`


| Parameter       | Type | Description                           |
| --------------- | ---- | ------------------------------------- |
| OutputBindingID | INT  | Output Binding ID                     |
| Level           | INT  | LEVEL: Bass level. range is -12 to 12 |

### Returns

`None`