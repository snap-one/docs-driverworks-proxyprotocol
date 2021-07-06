## UPDATE AUX ITEM

Received from the proxy when the auxiliary id is changed in Auxiliary Controls card. The command should be received only when **provides\_aux\_list** capability is set to **true**


### Signature

`AUX_ITEM_UPDATED ()`


| Parameter | Description |
| --- | --- |
| `ID` | str: Current aux ID |
| `NEW_ID` | str: New aux ID |


### Returns

`None`
