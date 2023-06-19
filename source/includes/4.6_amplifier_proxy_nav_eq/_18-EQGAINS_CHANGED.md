## EQ \_  GAINS \_  CHANGED

Navigator EQ notification that the gains of an equalizer have been modified.


### Signature

`EQGAINS_CHANGED`


| Parameter | Description |
| --- | --- |
| int | OUTPUT: OutputBindingID |
| num | VALUES: Comma delimited list of current equalizer values. |


### Returns

`None`


### Example

```lua
-- Notify Gains and Frequencies for EQ Bands for Output 3 (Binding ID 4002)
C4:SendToProxy(5001, "EQGAINS_CHANGED", { OUTPUT = "4002", VALUES = "7.5,3.8,5.4,4.59,7.8,7.4" }, "NOTIFY")_

C4:SendToProxy(5001, "EQFREQS_CHANGED", { OUTPUT = "4002", VALUES = "33,125,750,3000,8000,16000" }, "NOTIFY")
```

