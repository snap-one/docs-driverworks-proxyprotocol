## GET\_ALL\_ZONE\_INFO

Request to return information about each zone on the panel. The information consists of its id, name, type\_id, and  a list of partitions the zone is included in, a flag indicating if it can be bypassed, and a flag indicating if it is currently opened.


### Parameters

`None`


| Return    | Type  | Description                                  |
| --------- | ----- | -------------------------------------------- |
| ZONE ID   | INT   | Zone ID                                      |
| ZONE NAME | STR   | Zone Name                                    |
| ZONE TYPE | INT   | Zone Type ID                                 |
|           | TABLE | Partitions the Zone is included in.          |
|           | BOOL  | True, False: True if Zone can be bypassed.   |
|           | TBOOL | True, False: True if Zone is currently Open. |
| State     | STR   | State                                        |
