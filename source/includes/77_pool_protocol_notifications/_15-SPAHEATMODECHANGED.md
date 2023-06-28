## SPA\_HEATMODE\_CHANGED

Sent to the proxy to indicate that the spa heat mode has changed.


### Signature

`SPA_HEATMODE_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `XML` | HEATMODE. |


### Returns

`None`


### Example

```xml
XML:
id: from <command>
mode: OFF | ON | ENABLED
 
<spa_heatstate>
    <item>
        <id>set_spa_heater</id>
        <mode>OFF</mode>
    </item>
</spa_heatstate>
```
