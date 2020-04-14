## SET PANEL TIME DATE

Command sent directly to the various partition proxies that passes the ID of the panel proxy. This allows the partitions to send their panel commands and queries to the correct panel.


### Signature

`C4:SET_PANEL_TIME_DATE ()`


| Parameter | Description |
| --- | --- |
| int | YEAR - integer current year e.g. 2020 |
| int | MONTH: 1-12 1=Jan, 2=Feb, etc. |
| int | DAY: 1-31 |
| int | HOUR: 0-23 |
| int | MINUTE: 0-59 |
| int | SECOND: 0-59 |
| int | INTERFACE ID: Unique string that identifies this instance of the UI |


### Returns

`None
`
