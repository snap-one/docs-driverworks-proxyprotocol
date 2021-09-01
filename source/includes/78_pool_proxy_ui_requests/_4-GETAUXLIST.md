## GET AUX LIST

Obtains the aux list that will appear in Choose Auxiliary window in Composer Pro.

Choose Auxiliary window pops up when + icon is clicked in Auxiliary Contreol card.

UI request will be received when user clicks on the + icon in Auxiliary Contreol card.

Drivers should response with a xml that contains aux id, aux name in Control4 Customer Interface and

aux type defined in driver xml file.

Aux Circuits will be sorted in the Choose Auxiliary window by id asigned in the xml sent by driver.

### Example

```xml
	<aux_list>
		<items>
	            <item>
	                <id>1</id>
	                <item_text>Auxiliary Control 1</item_text>
	                <type>Toggle</type>
	            </item>
	            <item>
	                <id>2</id>
	                <item_text>Auxiliary Control 2</item_text>
	                <type>Toggle</type>
	            </item>
	            <item>
	                <id>3</id>
	                <item_text>Auxiliary Control 3</item_text>
	                <type>Toggle</type>
	            </item>
	            <item>
	                <id>4</id>
	                <item_text>Auxiliary Control 4</item_text>
	                <type>Toggle</type>
	            </item>
	            <item>
	                <id>5</id>
	                <item_text>Jandy Color Aux 5</item_text>
	                <type>Light Dimmer Jandy Colors</type>
	            </item>
	            <item>
	                <id>6</id>
	                <item_text>Dimmer Aux 6</item_text>
	                <type>Dimmer</type>
	            </item>
	            <item>
	                <id>7</id>
	                <item_text>Auxiliary Control 7</item_text>
	                <type>Toggle</type>
	            </item>
	            <item>
	                <id>8</id>
	                <item_text>Auxiliary Control 8</item_text>
	                <type>Toggle</type>
		    </item>
		</items>
	</aux_list>
```
