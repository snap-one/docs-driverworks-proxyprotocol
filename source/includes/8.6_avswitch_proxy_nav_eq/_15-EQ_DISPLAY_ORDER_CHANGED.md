## EQ\_DISPLAY\_ORDER\_CHANGED

Navigator EQ notification of the order that the names from EQ\_NAMES\_CHANGED should be presented to the user.


### Name

`EQ_DISPLAY_ORDER_CHANGED`


| Parameter | Type             | Description                                                                                                                                                                                                                                            |
| --------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| OUTPUT    | INT              | OutputBindingID                                                                                                                                                                                                                                        |
| INDEX     | Table of indexes | Table of indexes that represents display order of the names.  Note that any programming for selecting a preset will be INDEX based, not name based.  Hence the names can be changed but the programming will be tied to the index at time of creation. |


### Returns

`None`


### Example

```lua
C4:SendToProxy(5001, "EQ_DISPLAY_ORDER_CHANGED", {​​​​​​​ [1] = 1, [2] = 2, [3] = 3, [4] = 4, [5] = 5, OUTPUT = "4002" }​​​​​​​, "NOTIFY")

C4:SendToProxy(5001, "EQ_DISPLAY_ORDER_CHANGED", {​​​​​​​ 1, 2, 3, 4, 5, OUTPUT = "4002" }​​​​​​​, "NOTIFY")
```


