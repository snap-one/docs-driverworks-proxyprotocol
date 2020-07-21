## can switch separately

Device specific capability that must be set to True to in order for a device’s Composer Pro interface reflecting independent audio and video signal switching.


### Signature
`<can_switch_separately></can_switch_separately>`


| Parameter | Description |
| --- | --- |
| bool | True/False |


### Usage Note

This capability is not related with the requires separate switching capability.  A setting of True or False will have no impact on requires separate switching.


### Example

```xml
<capabilities>
   <can_switch_separately>true</can_switch_separately>
</capabilities>
```




