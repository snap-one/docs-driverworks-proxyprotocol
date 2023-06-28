## MAX\_ON

Used to inform the proxy that the hardware maximum On level has changed.  This is useful for hardware such as Control4’s Gen3 lighting where the hardware supports remapping where 100% brightness is at for the actual hardware.  This does not change the available brightness percent range from 0-100%.

### Signature

`MAX_ON ()`



| Parameter | Description |
| --- | --- |
| int | BRIGHTNESS: Percent from 1-100 for the Max On brightness to be remapped to. |


### Returns

`None`