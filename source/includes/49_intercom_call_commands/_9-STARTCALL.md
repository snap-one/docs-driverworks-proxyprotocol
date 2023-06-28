## START \_CALL

Used by Programming or ComposerPro. Start Call is issued by a third party to the device. Start Call is not used when call are initiated through Navigator.


### Signature

`START_CALL ()`


| Parameter | Description |
| --- | --- |
| num | `DEVICE_ID` - The proxy ID of the caller |
| num | `REMOTE_DEVICE_ID` - The proxy ID of the callee |
| num | AUDIO - The requested audio cap for the call. |
| num | VIDEO - The requested video cap for the call. |
| num | RING - This parameter has been deprecated. |

### Returns

`None`
