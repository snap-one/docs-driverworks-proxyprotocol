## POOL HEATMODE CHANGED

Sent to the proxy to indicate that the pool heat mode has changed.


### Signature

`C4:POOL_HEATMODE_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `XML` | HEATMODE. |


### Returns

`None`


### Example

```
`XML:`
`id: from <command>`
`mode: OFF | ON | ENABLED`
` `
`<pool_heatstate>`
`    <item>`
`        <id>set_pool_heater</id>`
`        <mode>ON</mode>`
`    </item>`
`    <item>`
`        <id>set_solar_heater</id>`
`        <mode>OFF</mode>`
`    </item>`
`</pool_heatstate>`
```
