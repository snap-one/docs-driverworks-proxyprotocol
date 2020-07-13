## requires separate switching

Device specific capability that when set to True notifies Director of the existence of individual audio and video paths. This capability has no impact on Composer Pro user interface. For that reason, when set to True it is recommended that the capability can switch separately be set to True as well.


### Signature

`<requires_separate_switching></requires_separate_switching>`


| Parameter | Description |
| --- | --- |
| bool | True/False |


### Example

```xml
<capabilities>
   <requires_separate_switching>true</requires_separate_switching>
</capabilities>
```
