## GET_ALL_PARTITION_INFO_

Request to return information to the panel proxy about each of its partitions.  The information consists of its id, if it’s enabled, its binding id, and its current state.

### Parameters

`None`


| Return | Description |
| --- | --- |
| int | PGM ID |
| bool | True, False: True if PGM is Open. |
| int | Binding ID |
| str | State |