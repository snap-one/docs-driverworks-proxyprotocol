## Transport Controls and Driver XML

To designate which transport controls appear on Navigators, the driver’s capabilities XML needs to contain a new`<transports></transports>` section. Within the transports XML is a `<supported></supported` tag. The supported tag lists the default supported transports for the driver. Note that there is a fixed set of "transports" that can be included in the supported tag. These include:

1. PLAY
2. PAUSE
3. STOP
4. SCAN\_FWD
5. SCAN\_REV
6. SKIP\_FWD
7. SKIP\_REV
8. RECORD 
9. PG\_UP
10. PG\_DOWN
11. PRG\_BTNS
12. KEYPAD
13. CH\_UP\_DN
14. DPAD

The transport controls XML in the example to the right contains the full set of possible transports. A driver can support all of these or a subset of these transports. 


```xml
<capabilities>
    <transports>
        <supported>
            PLAY, PAUSE, STOP, SCAN_FWD, SCAN_REV, SKIP_FWD, SKIP_REV,
            RECORD, PG_UP, PG_DOWN, PRG_BTNS, KEYPAD, CH_UP_DN, DPAD
        </supported>
    </transports>
</capabilities>
```
