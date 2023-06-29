## OVERVIEW

**Overview**
The Intercom Proxy interface is defined in terms of Commands, Requests and Notifications, each of which are described in this section of the proxy and Protocol Guide.

[Intercom Proxy Commands][1] are issued by a proxy consumer and may or may not result in an asynchronous notification in response.  Commands typically change state of the Intercom Proxy, or other components of the intercom architecture.

Intercom Proxy Requests are issued from a proxy consumer with the expectation of getting a response from the protocol.  Requests do not change state of the intercom proxy or any other component of the architecture.  [Notifications][2] are sent from the intercom proxy to the intercom consumer asynchronously, and indicate a state change in the intercom proxy or one of its related architecture components.

All communication through the proxy interface is asynchronous.  Even request responses, such as getting a list of known intercom devices, are returned asynchronously with respect to the request for that data.

[1]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-commands
[2]:	https://snap-one.github.io/docs-driverworks-proxyprotocol/#intercom-call-notifications