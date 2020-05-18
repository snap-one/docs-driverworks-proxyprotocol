## CUSTOM SETTINGS

Sent in response to the command `REQUEST_CUSTOM_SETTINGS`.


### Signature

`C4:CUSTOM_SETTINGS ()`


### Parameter

`None`

### Returns

`None`


### Example

```lua
<lock_custom_settings>
	<custom_setting>
		<name>name STRING</name>
		<type>STRING,LIST,RANGED_INTEGER,RANGED_FLOAT,BOOLEAN</type>
		<mode> alpha|alpha-numeric|password</mode>
		<items>
			<item>item</item>
			<item>item</item>
		</items>
		<minimum>min</minimum>
		<maximum>max</maximum>
		<value>value</value>
</custom_setting>
</lock_custom_settings>
```
