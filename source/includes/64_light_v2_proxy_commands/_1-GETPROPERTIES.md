## GET PROPERTIES

Used to get all the information about the proxy. Note that even if certain functionality doesn't exist on the device, it will still be included in the return data. See usage note below.


### Signature

`GET_PROPERTIES ()`


### Parameters

`None`


### Returns

`None`

### Usage Note
Return Data:

```lua
<State>
    <HOLD_RATE_UP>x</HOLD_RATE_UP>
    <HOLD_RATE_DOWN>x</HOLD_RATE_DOWN>
    <CLICK_RATE_UP>x</CLICK_RATE_UP>
    <CLICK_RATE_DOWN>x</CLICK_RATE_DOWN>
    <PRESET_LEVEL>x</PRESET_LEVEL>
    <MIN_ON_LEVEL>x</MIN_ON_LEVEL>
    <MIN_OFF_LEVEL>x</MIN_OFF_LEVEL>
    <COLD_START_TIME>x</COLD_START_TIME>
    <COLD_START_LEVEL>x</COLD_START_LEVEL>
    <NUMBER_BUTTONS>x</NUMBER_BUTTONS>
    <BUTTON_LIST_INFO>
        <BUTTON_INFO>
            <NAME>foo</NAME>
            <BUTTON_ID>x</BUTTON_ID>
            <ON_COLOR>000000</ON_COLOR>
            <OFF_COLOR>0b0b0b</OFF_COLOR>
        </BUTTON_INFO>
        <BUTTON_INFO>
            <NAME>bar</NAME>
            <BUTTON_ID>y</BUTTON_ID>
            <ON_COLOR>000000</ON_COLOR>
            <OFF_COLOR>0b0b0b</OFF_COLOR>
        </BUTTON_INFO>
    </BUTTON_LIST_INFO>
    <SceneMap>
        <SceneMapEntry>
            <SceneID>x</SceneID>
            <Level>y</Level>
            <Time>z</Time>
        </SceneMapEntry>
    </SceneMap>
</State>
```

