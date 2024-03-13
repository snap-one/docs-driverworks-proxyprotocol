## SET\_GROUP\_SYNC

Received when Keep loads in sync property is changed. In case of checking the Keep loads in sync, `GROUP_SET_LEVEL` will be sent right before `SET_GROUP_SYNC`.

### Name

| Parameter | Type | Description                        |
| --------- | ---- | ---------------------------------- |
| GROUP ID  | STR  | Driver ID of the Load Group driver |
| KEEP SYNC | STR  | 0 for False and 1 for True         |

### Received

`None`
