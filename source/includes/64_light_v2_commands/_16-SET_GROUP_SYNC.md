## SET GROUP SYNC

Received when Keep loads in sync property is changed. In case of checking the Keep loads in sync, `GROUP_SET_LEVEL` will be sent right before `SET_GROUP_SYNC`.

### Signature

| Parameter | Description |
| --- | --- |
| String | GROUP\_ID Driver ID of the Load Group driver |
| String | KEEP\_SYNC 0 for False and 1 for True |

### Received

`None`
