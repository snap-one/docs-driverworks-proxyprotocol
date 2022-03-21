## num\_buttons

Keypad capability that indicates the number of buttons the driver supports.  The value can be one of the following options: 

- 0 = None This disables the field in Composer Programming Commands box.
- 1 = Top
- 2 = Top and Bottom
- 3 = Top, Bottom, and Toggle

Defaults to 0.


### Signature

`<num_buttons></num_buttons>`


### Type

Integer


### Dynamic Capability

No


### Example

```xml
<capabilities>
    <num_buttons>0</num_buttons>
</capabilities>
```
