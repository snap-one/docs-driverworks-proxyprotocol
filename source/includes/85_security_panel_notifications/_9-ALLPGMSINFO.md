## ALL_PGMS_INFO

Sends and XML string of all PGMs (relays) and respective PGM information.


### Signature

`ALL_PGMS_INFO ()`


| Parameter | Description |
| --- | --- |
| xml | XML data. See example. | |


### Returns

`None`


### Example

```xml
<pgms>
		<pgm>
			<id>1</id>
			<is_open>true</is_open>
		</pgm>
		<pgm>
			<id>2</id>
			<is_open>false</is_open>
		</pgm>
		<pgm>
			<id>3</id>
			<is_open>false</is_open>
		</pgm>
</pgms>
```
