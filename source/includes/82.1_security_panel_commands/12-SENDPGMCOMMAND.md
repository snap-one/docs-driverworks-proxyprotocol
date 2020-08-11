## SEND_PGM_COMMAND

Send a command to a PGM on the panel.


| Parameter | Description |
| --- | --- |
| int | PGM ID:  The id of the targeted PGM. |
| bool | ENABLED: ‘True’ if this partition should now be enabled, False if not. |
| str | COMMAND: Possible commands are: ‘open’, ‘close’, ‘toggle’, and ‘trigger’. |