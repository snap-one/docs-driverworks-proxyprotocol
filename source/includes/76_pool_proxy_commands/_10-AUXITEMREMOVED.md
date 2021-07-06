## REMOVE AUX ITEM

Received from the proxy when an auxiliary item is removed by clicking on the - icon in Auxiliary Controls card. The command should be received only when [provides\_aux\_list][1] capability is set to true.


### Signature

`AUX_ITEM_ADDED ()`


| Parameter | Description |
| --- | --- |
| `ID` | str: ID of the aux removed |


### Returns

`None`

[1]:	https://control4.github.io/docs-driverworks-proxyprotocol/#pool-capabilities