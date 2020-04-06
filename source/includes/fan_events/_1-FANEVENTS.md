## Fan Events

The following Events are supported by the Fan Proxy. The events fired by the proxy have to deal with changes in the fan itself. They include:

`turned_on` - Fired when the power goes from off to on.

`turned_off` - Fired when the power goes from on to off.

`speed_changed` - Fired when the speed number changes. Since turning on or off also involves a change of speed this would also fire when the fan turns on or off.

`direction_changed` - Fired when the fan spin direction changes. This would only be available if the `can_reverse` capability is set to true in the driver file.