## ADD\_AUX\_ITEM

Received from the proxy when an auxiliary item is added by clicking on the + icon in Auxiliary Controls card. The command should be received only when [provides\_aux\_list ][1]capability is set to true.


### Name

`AUX_ITEM_ADDED ()`


| Parameter | Type | Description         |
| --------- | ---- | ------------------- |
| `AUX_ID`  | STR  | ID of the aux added |


### Returns

`None`

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#pool-capabilities