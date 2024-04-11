## INPUT\_CHANGED

Notification indicating that the TV's input source has changed.


### Name

`INPUT_CHANGED ()`


| Parameter | Type | Description   |
| --------- | ---- | ------------- |
| INPUT     | INT  | Changed Input |


### Returns

`None`


### Usage Note

If the BANDTYPE is not supplied, as in older drivers, the INPUT binding # will be used to determine which band the tuner is on. All DriverWorks drivers need to use the BANDTYPE parameter if they want the band to propagate up to Navigator to display the channel properly. If the DriverWorks driver does not know the current channel and the “has\_feedback” capability is not set to “True”, none of this matters and everything will keep working as it previously has.
A CHANNEL\_CHANGED must be issued immediately after the INPUT\_CHANGED in order for the UI to update. See the example to the right.

```xml
C4:SendToproxy(5002,'INPUT_CHANGED',
{INPUT=3009,BANDTYPE='FMBand',MINCHANNEL=8750,
MAXCHANNEL=10790,CHANNELSPACING=20})
C4:SendToProxy(5002,'CHANNEL_CHANGED',{CHANNEL=10290})
```

Note that in the example, 5002 is the ProxyBindingID for the Tuner. INPUT 3009 is the ID for the FM Antenna on the 5002 Tuner. Navigator determines AM/FM/XM with the following rule:

- ID 3000 and 3001 are AM
- ID 3002 and 3003 are FM