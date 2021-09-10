## AUX NAMES CHANGED

This notification provides a way to dinamically add auxiliaries from the driver.
The \<type\> should be one of the \<aux\_types\> defined in the driver's \<capabilities\>


### Signature

`AUX_NAMES_CHANGED ()`


| Parameter | Description |
| --- | --- |
| `AUXNAMES` | XML (see example)|
| `UPDATE_LIST` | (optional) True/False (default). When set to True, finds an existing item and changes its name only. Otherwise creates a new list based on the XML.|

### Returns

`None`


### Example

```xml

<items>
    <item>
        <id>1</id>
        <item_text>Pool Cleaner</item_text>
        <type>Toggle</type>
    </item>
    <item>
        <id>2</id>
        <item_text>Low Speed Pump</item_text>
        <type>Toggle</type>
    </item>
    <item>
        <id>3</id>
        <item_text>Spa Spillover</item_text>
        <type>Toggle</type>
    </item>
</items>
```
