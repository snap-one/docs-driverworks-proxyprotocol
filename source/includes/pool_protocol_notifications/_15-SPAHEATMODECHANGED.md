## SPA HEATMODE CHANGED

Sent to the proxy to indicate that the spa heat mode has changed.


### Signature

`C4:SPA_HEATMODE_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `XML` | HEATMODE. |


### Returns

`None`


### Example

```
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
