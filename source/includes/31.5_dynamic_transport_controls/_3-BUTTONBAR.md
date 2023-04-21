## Button Bar and Driver XML

To designate which transport control buttons appear on the Button Bar, the transports capabilities XML needs to include a  `<button_bar></button_bar` tag. 

Within the button bar XML is a `<buttons></buttons>` tag. This tag contains the buttons that will display in the button bar. Each button is defined further in the XML with a `<button></button>` tag that includes an id, name, command, type. 

| Element | Description |
| --- | --- |
| id | Identification used for the button. For example: PLAY. This id value is important as it used by a corresponding Proxy Variable to identify this button. |
| name | Name used for the button. For example: Play. This text will be displayed in the button if no alternative icon is defined. |
| command | The command that is sent to the Room or Proxy. For example: PLAY. |
| type | Whether the command is sent to the Room or the Proxy. Values include ROOM or PROXY. |


```xml
<capabilities>
    <transports>
        <button_bar>
            <buttons>
                <button>
                    <id>PLAY</id>
                    <name>Play</name>
                    <command>PLAY</command>
                    <type>PROXY</type>
                </button>
                ...
            </buttons>
            <default_buttons>GUIDE, MENU, CANCEL, INFO</default_buttons>
        <button_bar>
        ...
    </transports>
    ...
</capabilities>
```


Note the `<default_buttons></default_buttons>` XML in the example to the right. This tag can contain up to eight default buttons in a comma separated list.

_Example image of the Controls in the Button Bar:_

<img src="images/31.5_3_01.png"/> 

