## TOC

Issued when scanning the table of contents for a particular disc or cd.  Director will use this information to lookup and populate the database with the disc information if the lookup succeeds.  This command can also be used to indicate a slot now is empty and contains no disc.

### Name

`TOC ()`


### Parameter

| Parameter | Type | Description                     |
| --------- | ---- | ------------------------------- |
| int       | INT  | Index of the disc being scanned |
| str       | STR  | ‘cd’ for CD or ‘dvd’ for DVD    |
| data      | DATA | table of contents               |


### Returns

`None`