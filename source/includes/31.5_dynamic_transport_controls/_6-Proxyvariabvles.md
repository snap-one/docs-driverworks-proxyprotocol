## Proxy Variables

The following Variables are used by Navigators. These Variables, with the exception of TRANSPORTS\_DEFINITION, are set by using the SendToProxy commands defined in the previous section. This causes the Proxy to set the Variable value. Navigators then read that Variable value which results in the correct transport elements being displayed on the Navigator interface. 

Note that It is not necessary for your driver to write Variable values.

**TRANSPORTS\_DEFINITION** 

Allows Navigators to get new button definitions without a Navigator refresh call. This cannot be updated by using SendToProxy. It is updated through the driver’s Capabilities at initialization or a driver update.

| Parameter | Description |
| --- | --- |
| XML | `<transports></transports>`  xml from the driver capabilities. Defaults to the full `<transports>..</transports>` from the driver’s capabilities. Must be updated when the driver is updated. |



**TRANSPORTS\_BUTTONS** 

| Parameter | Description |
| --- | --- |
| str | Comma separated list of button IDs referencing the buttons in the `<button_bar >`section of the capabilities. The UIs would show the buttons in the order specified here. For example: "GUIDE, MENU, CANCEL, INFO”. Defaults to the data set specified in `<default_buttons></default_buttons>` XML. |



**TRANSPORTS\_SUPPORTED**

| Parameter | Description |
| --- | --- |
| str | Comma separated list of transports. The UIs would show the buttons in the order specified here. Defaults to the data set specified in \<supported\>\</supported\> XML. This can be updated to include different sets on the fly such as hiding play and showing pause or vice versa when play/pause state changes. |



**TRANSPORTS\_DASHBOARD\_SMALL**

Dashboard to use on smaller devices.  The UIs would show the buttons in the order specified here.

| Parameter | Description |
| --- | --- |
| str | Comma separated list of IDs. IDs reference button definitions in the media\_dashboard capability. This should be 5 buttons or less. Defaults to the "default\_small" set of transports in the media\_dashboard: "SCAN\_REV, PLAY, PAUSE, SCAN\_FWD”. Defaults to the data set specified in `<default_small></default_small>` XML. |



**TRANSPORTS\_DASHBOARD\_LARGE**

Dashboard to use on larger devices.

| Parameter | Description |
| --- | --- |
| str | Comma separated list of IDs. The IDs reference button definitions in the media\_dashboard capability. This should be 7 buttons or less. Defaults to the "default\_large" set of transports in the media\_dashboard: "SKIP\_REV, SCAN\_REV, PLAY, PAUSE, SCAN\_FWD, SKIP\_FWD, RECORD”. Defaults to the data set specified in `<default_large></default_large>` XML. |