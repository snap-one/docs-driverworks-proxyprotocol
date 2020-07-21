## Storing Session IDs


Many intercom API commands and requests require sessionId as an input parameter. The value for this parameter is provided by the intercom proxy in response to issuing a [`START_CALL`][1] command, and is included in the resulting [`OUTGOING_CALL`][2] and [`INCOMING_CALL`][3] notifications. The intercom proxy consumer is responsible for storing the sessionId returned with these notifications for use in subsequent commands and requests.

[1]:	https://control4.github.io/docs-driverworks-proxyprotocol/#start-call
[2]:	https://control4.github.io/docs-driverworks-proxyprotocol/#outgoing-call
[3]:	https://control4.github.io/docs-driverworks-proxyprotocol/#incoming-call