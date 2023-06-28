
## What’s New in 3.2.0

### Proxies that were Modified\*\* 

**Security Proxy**
The [REQUEST\_DEFAULT\_USER\_CODE][1] partition notification was added as a mechanism for the protocol driver
to initiate the communication to get that default user code upon driver update.

The following Security Protocol Notifications were deprecated from the SDK: ALARM, ALARM\_CLEAR, AWAY, DISARM, HOME, TROUBLE. Please see the [Security Panel Notification][2] and [Security Partition Notification][3] areas for the latest list of Notifies.


[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#security-partition-notifications-request_default_user_code_
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#security-panel-notifications
[3]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#security-partition-notifications