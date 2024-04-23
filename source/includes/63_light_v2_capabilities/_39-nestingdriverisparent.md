## nesting\_driver\_is\_parent

This capability is applicable to drivers where supporting drivers are required for the one device. This capability makes it easier to understand what drivers are associated with each other. This specific capability indicates whether or not this driver is dependent on other drivers. When used correctly, it will setup the dependent driver(s) to be nested under the primary (parent) driver in Composer Pro.

###### Available from 3.4.2.

### Signature

`<nesting_driver_is_parent></nesting_driver_is_parent>`


### Type

Boolean: Defaults to false.


### Dynamic Capability

No

### Usage Note

The following variable must be added and configured to use this capability:

VAR\_C4\_NESTING\_PARENTS\_CHILD\_DEVICES - Set this variable to a comma delimited list of ID values for the secondary device(s) required by the parent driver. This list represents the drivers that will be nested under the parent driver in Composer Pro. This is the associated driver(s) with the nested\_driver\_is\_child capability set to true.

### Example

```xml
<capabilities>
  <nesting_driver_is_parent>false</nesting_driver_is_parent>
</capabilities>
```
