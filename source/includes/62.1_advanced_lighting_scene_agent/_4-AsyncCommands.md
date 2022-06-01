
## Asynchronous Commands

This section lists the Commands (Bound Call, aka SendToDevice in Lua) that the Proxy supports.  These are for use by Navigators, Composer Programming and other services like Voice Control.  The thing to remember with Proxies is that many of the commands are passed on to the Protocol and it is the Protocol drivers responsibility to ripple the commands result back up to the Proxy using a 'Notify' command. This allows the Protocol to optionally make slight adjustments to commands for its unique driver or hardware and then inform the Proxy of the change.