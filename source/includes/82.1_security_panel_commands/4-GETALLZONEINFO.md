## GET\_ALL\_ZONE\_INFO\_

Request to return information about each zone on the panel. The information consists of its id, name, type_id, and  a list of partitions the zone is included in, a flag indicating if it can be bypassed, and a flag indicating if it is currently opened.


### Parameters

`None`


| Return | Description |
| --- | --- |
| int | Zone ID |
|str | Zone Name |
| int | Zone Type ID |
| table | Partitions the Zone is included in. |
| bool | True, False: True if Zone can be bypassed. |
| bool | True, False: True if Zone is currently Open. |
| str | State |