## Using the RemoteAor Property

When the “remoteAor” parameter is used in a notification or command, the value is always the address of record of the other intercom device participating in an intercom call. 

For example, consider that intercom device A has address of record of “sip-user-A@192.168.1.123” and intercom device B has an address of record of “sip-user-B@192.168.1.123”. 

Intercom device A initiates a call with intercom device B, which results in an [`INCOMING_CALL`][1] notification on intercom device B. When intercom device B issues the [`ACCEPT_CALL`][2] command, which takes remoteAor as a parameter, intercom device B should use “sip-user-A@192.168.1.123” (the address of record of intercom device A, or the initiator) as the value of this parameter. 

Likewise, when intercom device A sends the [`CALL_ACCEPTED`][3] notification, it will contain a remoteAor property that has the value of the address of record of intercom device B, or “sip-user-B@192.168.1.123”.

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications-incoming_call
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-commands-accept_call
[3]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications-call_accepted