## movement

Integer enumeration of a movement function for the blind.  If set in the driver, the pull-down to select this value will be disabled in the proxy. For louvers and other slate type objects, the movement observed is that of the forward/leading (aka nearest to the person viewing the movement) edge of the louver or slate.  

An example for a general louver would be where the primary closed position for the leading edge is Down, so Up (Middle) would be Open, and an optional Secondary Closed would be where the front edge is furthest up.


### Signature

`<movememt></movement>`


| Parameter | Description |
| --- | --- |
| 0 | Open/Close (Open/Close) |
| 1 | Up to Down (Up is open, Down is closed) |
| 2 | Down to Up (Down is open, Up is Closed) |
| 3 | Out to In (Out is Open, In is Closed) |
| 4 | Left to Right (Left is Open, Right is Closed) |
| 5 | Right to Left (Right is Open, Left is Closed) |


### Example

```xml
<capabilities>
    <movememt>4</movememt>
</capabilities>
```


