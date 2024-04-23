## nested\_driver\_is\_child

This capability is applicable to light drivers where multiple light drivers are added for one light device. These capabilities make it easier to understand what drivers are associated with each other. This specific capability indicates whether or not this driver is a dependent driver required by primary light driver for use.  When used correctly, it will setup the dependent driver(s) to be nested under the primary driver in Composer Pro.

###### Available from 3.4.2.  

### Signature

`<nested_driver_is_child></nested_driver_is_child>`


### Type

Boolean: Defaults to false.


### Dynamic Capability

No

### Usage Note

The following variable must be added and configured to use this capability:

VAR\_C4\_NESTED\_CHILDS\_PARENT\_DEVICE - Set the variable to the ID of primary driver requiring its use. This is the associated driver with the nesting\_driver\_is\_parent capability set to true.


### Example

```xml
<capabilities>
  <nested_driver_is_child>false</nested_driver_is_child>
</capabilities>
```
