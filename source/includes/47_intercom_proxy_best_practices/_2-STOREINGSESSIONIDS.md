## Storing Session IDs


Many intercom API commands and requests require sessionId as an input parameter. The value for this parameter is provided by the intercom proxy in response to issuing a `START_CALL` command, and is included in the resulting `OUTGOING_CALL` and `INCOMING_CALL` notifications. The intercom proxy consumer is responsible for storing the sessionId returned with these notifications for use in subsequent commands and requests.