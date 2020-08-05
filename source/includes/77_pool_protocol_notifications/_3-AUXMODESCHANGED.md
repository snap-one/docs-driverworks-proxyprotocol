## AUX MODE CHANGED

Notification sent to the proxy to indicate whether Aux Buttons on the right side of the UI are On or Off.  ID corresponds to the button name ID in the BUTTONNAMES notify. Mode Y is On, N is Off.


### Signature

`AUX_MODE_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `ID` | ID of auxiliary |
| `MODE` | ON/OFF |
| `SELECTED` | For type LIST from `<aux_types> <items>` item selected if is provided by the device.m |


### Returns

`None`


### Example

```xml

<aux_state>
    <item>
        <id>1</id>
        <mode>ON</mode>
    </item>
    <item>
        <id>6</id>
        <mode>ON</mode>
        <selected>50%</selected>
    </item>
</aux_state>
```

