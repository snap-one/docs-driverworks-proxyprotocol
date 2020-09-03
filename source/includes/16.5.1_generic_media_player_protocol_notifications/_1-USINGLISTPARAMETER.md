## Using the List Parameter

There are two ways to handle sending a list of media information. The first involves the protocol driver manually creating the .xml for the list and then passing that list to the proxy. The format of the list can be seen to the right. 

```xml
<list>
       <clear>true</clear>
       <top>false</top>
       <alpha>true</alpha>
       <title>Smashing Pumpkins</title>
       <total_items>80</total_items>
       <num_items>21</num_items>
       <first>0</first>
       <items>
               <item>
                       <id>1</id>
                       <text>Siamese Dream</text>
                       <type>1</type>
               </item>
               <item>
                       <id>2</id>
                       <text>Greatest Hits</text>
                       <type>1</type>
               </item>                
       </items>
</list>

```


The second method involves adding new list data to an existing list and passing the updated list along. This prevents the protocol driver from having to recreate a list every time new data is passed. The commands below need to reside inside the protocol driver’s Lua code:


**NEW LIST**

Creates a new media data list.

### Signature

`NEW_LIST ()`


| Parameter | Description |
| --- | --- |
| title | text string of the list title. |
| total\_items | Numerical value of the total number of items in the list. |
| num\_items | Numerical value of the new items added to the list. |
| first | First item in the return list. |
| clear | True or False. Indicates whether or not the cache for the previously returned items should be cleared, or not. |



**ADD LIST ITEM**

Adds an item to a media data list.

### Signature

`ADD_LIST_ITEM ()`


| Parameter | Description |
| --- | --- |
| id | Id of the item being added to the list. |
| type |  Type of items being added to the list; playable, selectable. |
| text |  Display text for the new item. |
| last | True or False. This parameter is passed last and triggers the list to be sent to the UI (if True) |

When the protocol is ready to send a new list it should send a NEW\_LIST command followed by ADD\_LIST\_ITEM for each item to be added to the list.



**ADD MENU ITEM**

Adds an item to a media data menu.

### Signature

`ADD_MENU_ITEM ()`

| Parameter | Description |
| --- | --- |
| id |  Id of the item being added to the menu. |
| type | Type of items being added to the list; playable, selectable |
| text |  Display text for the new menu item. |
| last |  True or False. This parameter is passed last and triggers the menu to be sent to the UI (if True). |



**NEW\_MENU**

Creates a new menu of media data.

### Signature

`NEW_MENU ()`

| Parameter | Description |
| --- | --- |
| title | Text string of the menu title. |
| num\_items | Numerical value of the new items added to the list. |\_


When the protocol is ready to send a new menu it should send a NEW\_MENU command followed by ADD\_MENU\_ITEM for each item to be added to the menu. See the example to the right.\_

```xml
-- MENU_LIST

<menu_list>
       <title>Main Menu</title>
       <total_items>4</total_items>
       <num_items>4</num_items>
       <first>0</first>
       <items>
               <item>
                       <id>0</id>
                       <type>4</type>
                       <text>Playlists</text>
               </item>
               <item>
                       <id>1</id>
                       <type>4</type>
                       <text>Artists</text>
               </item>
               <item>
                       <id>2</id>
                       <type>4</type>
                       <text>Albums</text>
               </item>
               <item>
                       <id>4</id>
                       <type>4</type>
                       <text>Songs</text>
               </item>
       </items>
</menu_list>


```
