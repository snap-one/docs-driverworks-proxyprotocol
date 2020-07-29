
## What’s New in 3.2.0

### Proxies that were Modified\*\* 

**Security Proxy**
The REQUEST\_DEFAULT\_USER\_CODE partition notification was added as a mechanism for the protocol driver
to initiate the communication to get that default user code upon driver update.

The following Security Protocol Notifications were deprecated from the SDK: ALARM, ALARM_CLEAR, AWAY, DISARM, HOME, TROUBLE. Please see the [Security Panel Notification][1] and [Security Partition Notification][2] areas for the latest list of Notifies.


[1]:	https://control4.github.io/docs-driverworks-proxyprotocol/#security-panel-notifications
[2]:	https://control4.github.io/docs-driverworks-proxyprotocol/#security-partition-notifications