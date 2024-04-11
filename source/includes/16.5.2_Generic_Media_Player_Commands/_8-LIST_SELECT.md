## LIST\_SELECT

Command to select an item from a list of media on the GenericMediaPlayer. If the item has a child list, that list is sent to the UI. If the item is playable, playback should be started.


### Name

`LIST_SELECT ()`


| Parameter | Type | Description                        |
| --------- | ---- | ---------------------------------- |
| ITEM      | INT  | The id of the item selected        |
| TITLE     | STR  | The name of the item.              |
| TYPE      | INT  | he item type returned in the list. |


### SendToProxy

`<list>`
