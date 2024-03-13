## SEND\_PGM\_COMMAND

Send a command to a PGM on the panel.


| Parameter | Type | Description                                                      |
| --------- | ---- | ---------------------------------------------------------------- |
| PGM ID    | INT  | The id of the targeted PGM.                                      |
| ENABLED   | BOOL | ‘True’ if this partition should now be enabled, False if not.    |
| COMMAND   | STR  | Possible commands are: ‘open’, ‘close’, ‘toggle’, and ‘trigger’. |
