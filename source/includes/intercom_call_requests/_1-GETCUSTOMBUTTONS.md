## GET CUSTOM BUTTONS

The Intercom Proxy provides the ability to define two (2) custom buttons for each endpoint. These custom buttons will generate “on pressed” and “on released” events that can be used as programming triggers in Composer. This request is issued to obtain the custom button so that they can be displayed by the user interface. Detection of the “pressed” and “released” states of these buttons is the responsibility of the user interface displaying them, as well as the generation of the “pressed” and “released” notifications.


### Signature

`C4:GET_CUSTOM_BUTTONS ()`


| Parameter | Description |
| --- | --- |
| num | The Proxy Device ID of the intercom endpoint whose custom button information is to be returned. |


### Example

```
<GET_CUSTOM_BUTTONS>
   <idDevice>[22]</idDevice>
</GET_CUSTOM_BUTTONS>
```


### Response Parameters

| Parameter | Description |
| --- | --- |
| id | The proxy device id of the intercom endpoint to which this request’s response is sent. This value is used to insure that the response is processed by proper device driver (i.e. the "requestor"). It is a number that is greater than or equal to zero (0). |
| `custom_button` | An xml record describing a single custom button to be displayed on the active session view in the UI. |
| index | The serial index of the current custom button. (0 or 1) |
| state | The default state of the current custom button. (0=off or 1=on) |
| title | The display title (or label) of the current custom button. |

Response Prototype

```
<custom_buttons id=”[integer value]”>
  <custom_button>
   <index>[integer value]</index>
   <state>[integer value]</state>
   <title>[string value]</title>
  </custom_button>
  <custom_button>
   <index>[integer value]</index>
   <state>[integer value]</state>
   <title>[string value]</title>
  </custom_button>
</custom_buttons>
```
