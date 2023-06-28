## POOL\_HEATMODE\_CHANGED

Sent to the proxy to indicate that the pool heat mode has changed.


### Signature

`POOL_HEATMODE_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `XML` | HEATMODE. |


### Returns

`None`


### Example

```xml

<pool_heatstate>
   <item>
        <id>set_pool_heater</id>
        <mode>ON</mode>
   </item>
   <item>
        <id>set_solar_heater</id>
        <mode>OFF</mode>
   </item>
</pool_heatstate>`
```
