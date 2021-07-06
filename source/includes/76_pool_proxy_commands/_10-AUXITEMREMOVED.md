## REMOVE AUX ITEM

Received from the proxy when aux item is removed by clicking on the - icon in Auxiliary Controls card. The command should be received only when **provides_aux_list** capability is set to **true**

### Sgnature

`AUX_ITEM_ADDED ()`

| Parameter | Description |
| --- | --- |
| `ID` | str: ID of the aux removed |

### Returns

`None`
