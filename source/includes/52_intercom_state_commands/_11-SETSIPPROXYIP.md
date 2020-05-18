## SET SIP PROXY IP

This command established the IP Address of the SIP Proxy.


### Signature

`C4: SET_SIP_PROXY_IP ()`


| Parameter | Description |
| --- | --- |
| str | A string representing the IP address of the SIP server, such as “192.168.1.13” (without the quotes) |


### Returns

`None`


### Example

```lua
<SET_SIP_PROXY_IP>
   <sipproxyip>[192.168.1.13]</sipproxyip>
</SET_SIP_PROXY_IP>
```
