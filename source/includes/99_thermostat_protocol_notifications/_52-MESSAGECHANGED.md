## MESSAGE\_CHANGED

Update the text message displayed in the UI.  Multiple lines can be specified by using \n to separate lines, although UI's will display each line in its own way. Could be a paragraph, ticker scrolling, cycling, etc. To UI comes through as `message`.


### Name

`MESSAGE_CHANGED ()` 


| Parameter | Type | Description                                                                                                                                                                                                                                                                                      |
| --------- | ---- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| MESSAGE   | STR  | Text string, max length of the string is not set, though driver developers need to keep in mind that this information shows up in Navigators in a ticker or similar scrolling text display and should not be cluttered but kept to key things like HVAC system errors, and CRITICAL information. |

 

### Returns

`None`


### Usage Note

This string may or may not have multiple message segments. If it does, the message segments are delimited by a \n (newlines). Some protocol drivers such as the c4-therm support up to 4 lines of messages. Most UI's scroll these \n delimited messages right to left in a marquee style.
