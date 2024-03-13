## GET\_ALL\_PARTITION\_INFO

Request to return information to the panel proxy about each of its partitions.  The information consists of its id, if it’s enabled, its binding id, and its current state.

### Parameters

`None`


| Return       | Type | Description                                  |
| ------------ | ---- | -------------------------------------------- |
| Partition ID | INT  | Partition ID                                 |
|              | BOOL | True, False: True if this partition is Open. |
| Binding ID   | INT  | Binding ID                                   |
| State        | STR  | State                                        |
