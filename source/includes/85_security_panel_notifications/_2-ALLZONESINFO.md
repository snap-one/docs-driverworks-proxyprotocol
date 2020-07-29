## ALL\_ZONES\_INFO

Sends and XML string of all zones and respective zone information.


| Parameter | Description |
| --- | --- |
| xml | XML data. See example. | |


### Example

```xml
<zones>
		<zone>
			<id>1</id>
			<name>Back Door</name>
			<type_id>2</type_id>
			<partitions></partitions>
			<can_bypass>false</can_bypass>
			<is_open>false</is_open>
		</zone>
		<zone>
			<id>2</id>
			<name>Front Door</name>
			<type_id>2</type_id>
			<partitions></partitions>
			<can_bypass>false</can_bypass>
			<is_open>false</is_open>
		</zone>
		<zone>
			<id>3</id>
			<name>Back Window</name>
			<type_id>3</type_id>
			<partitions></partitions>
			<can_bypass>true</can_bypass>
			<is_open>true</is_open>
		</zone>
		<zone>
			<id>4</id>
			<name>Zone 4</name>
			<type_id>5</type_id>
			<partitions></partitions>
			<can_bypass>true</can_bypass>
			<is_open>false</is_open>
		</zone>
</zones>
```
