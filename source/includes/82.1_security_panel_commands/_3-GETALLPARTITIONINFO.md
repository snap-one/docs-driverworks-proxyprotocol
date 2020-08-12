## GET\_ALL\_PARTITION\_INFO

Request to return information to the panel proxy about each of its partitions.  The information consists of its id, if it’s enabled, its binding id, and its current state.

### Parameters

`None`


| Return | Description |
| --- | --- |
| int | Partition ID |
| bool | True, False: True if this partition is Open. |
| int | Binding ID |
| str | State |