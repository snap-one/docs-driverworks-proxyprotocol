## EQ\_FREQS\_CHANGED

Navigator EQ notification that the frequencies of a equalizer have been modified.


### Name

`EQFREQS_CHANGED`


| Parameter       | Type | Description                           |
| --------------- | ---- | ------------------------------------- |
| OutputBindingID | INT  | OutputBindingID                       |
|                 |      | Table of comma delimited frequencies. |


### Returns

`None`


### Example

```lua
-- Notify Gains and Frequencies for EQ Bands for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "EQGAINS_CHANGED", { OUTPUT = "4002", VALUES = "7.5,3.8,5.4,4.59,7.8,7.4" }, "NOTIFY")_

C4:SendToProxy(5001, "EQFREQS_CHANGED", { OUTPUT = "4002", VALUES = "33,125,750,3000,8000,16000" }, "NOTIFY")
```

