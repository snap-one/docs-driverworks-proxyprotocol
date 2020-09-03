## TOGGLE

Used to toggle the light.  If it is a dimmer and it is off, toggling will activate the "On" preset. Should only be used in Composer Programming when the current brightness of the light does not matter nor does the brightness level it will go to matter as delays of brightness reporting to the proxy or network issues will result in unreliable final brightness.  If final brightness is important, then the On or Off presets should be specifically referenced in the SET\_BRIGHTNESS\_TARGET command.


### Signature

`TOGGLE ()`


### Parameter

`None`


### Returns

`None`