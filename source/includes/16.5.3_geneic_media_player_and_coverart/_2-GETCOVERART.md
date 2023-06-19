## GET\_COVERART

Command that comes into Received from Proxy.


### Signature

`GET_COVERART ()`


### Example

```lua
function GetCoverArt()
       if (g_ShowCoverArt == true) then
          QueueDockCmd(CMD["GET_COVERART_RAW"], 0, 1, g_imageindex-1, 0, "")
       End
end
```
