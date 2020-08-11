

The following Capabilities are supported by the Security Proxy:


**`button_list`**

Defines buttons to be displayed on UI panel along with IDs for Keypad. locCode defines button's column (A...Z) and row (1...9). For example, A3 indicates column 1 row 3. Width defines button width (in columns).

| Parameter | 
| --- | --- |
| True/False |



**`display_type`**

Define GUI display location and width.

| Parameter | Description |
| --- | --- |
| locCode | location code |
| width |


### Example

`<location>locCode</location>`
`<width>nWidth</width>`





**`has_alrm_cleared_event`**

Alarm capable of generating an event when alarm is cleared.

| Parameter | 
| --- | --- |
| True/False |





**`has_alrm_event`**

Alarm capable of generating an event when activated

| Parameter | 
| --- | --- |
| True/False |





**`has_trouble_event`**

Alarm capable of generating an event when alarm trouble is detected.

| Parameter | 
| --- | --- |
| True/False |