## AUX ITEM ADDED

Received from the proxy when an auxiliary item is added by clicking on the + icon in Auxiliary Controls card. The command should be received only when [provides\_aux\_list ][1]capability is set to true.


### Signature

`AUX_ITEM_ADDED ()`


| Parameter | Description |
| --- | --- |
| `AUX_ID` | str: ID of the auxiliary added |
| `ID` | str: ID that the auxiliary will have in the 'Auxiliary Controls' card |
| `TYPE` | str: auxiliary type as defined in the driver's [\<aux\_types\> ][1] |
| `ITEM_TEXT` | str: name of the auxiliary |


### Returns

`None`

[1]:	https://control4.github.io/docs-driverworks-proxyprotocol/#pool-capabilities
