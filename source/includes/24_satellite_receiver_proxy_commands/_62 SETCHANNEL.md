## SET CHANNEL

Tune device to the specified channel.


### Signature

`SET_CHANNEL ()`


| Parameter | Description |
| --- | --- |
| str | Channel value in string format. |


### Returns

`None`


### Example

The examples to the right detail the table of information that is received from the proxy when a channel is selected:

```
FM:
ReceivedFromProxy:	SET_CHANNEL
BindingID           5002
CHANNEL             96.3
INPUT               3028
OUTPUT              0

AM:
ReceivedFromProxy: SET_CHANNEL
INPUT              3027
BindingID          5002
CHANNEL            1100
INPUT              3027
OUTPUT             0
```

In the FM example, channel 96.3 has been selected in the tuner protocol. The 96.3 value is passed into the data table as a string.

It is important to note that if the bandwidth type (AM, FM) is not provided (and the proxy in question is not TV) a manner in which to identify the bandwidth type will need to be developed. An example of this code follows:

```lua

if tParams['BANDTYPE'] == nil then
       if (string.find(tParams['CHANNEL'],"%p") ~= nil) then
        tParams['BANDTYPE'] = 'FM'
        local ChannelLen = string.len(tParams['CHANNEL'] )
        local ChannelFix = string.sub(tParams['CHANNEL'],1,ChannelLen-2) .. '.' .. string.sub(tParams['CHANNEL'],ChannelLen-1,ChannelLen-1)
        tParams ['CHANNEL'] = ChannelFix
       else
        tParams['BANDTYPE'] = 'AM'
      end
    end 
```
