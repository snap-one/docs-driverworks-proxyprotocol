## Media Dashboard and Driver XML

The ability to define what transport controls display on the Media Dashboard is supported. The Media Dashboard is shown when Navigators are displaying a single line "dashboard" view of transport controls. This requires the addition of a `<dashboard></dashboard>`tag to the transports XML section. Note that Media Dashboard buttons are always shown using an icon. _See below for more information._


```xml
<capabilities>
    <transports>
        <dashboard>
            <buttons>
                <button>
                    <id>PLAY</id>
                    <icon>http://sampleiconURL.com</icon>
                    <name>Play</name>
                    <command>PLAY</command>
                    <type>PROXY</type>
                </button>
                ...
            </buttons>
            <default_large>SCAN_REV, PLAY, PAUSE, SSCAN_FWD</default_large>
            <default_small>SCAN_REV, PLAY, PAUSE, SCAN_FWD</default_small>
        </dashboard>
        ...
    </transports>
    ...
</capabilities>
```


Note the use of the default\_large and default\_small XML tags in the example to the right:

`<default_large>` - A comma separated list of ID values which match those defined in the button XML section. A maximum of 7 IDs are allowed. default\_large is meant for large user interfaces such as tablets.

`<default_small>` - A comma separated list of ID values which match those defined in the button XML section. A maximum of 5 IDs are allowed. default\_small is meant for smaller user interfaces such as phones.


**Referencing Built In Icons for the Media Dashboard**

Media Dashboard button icons are typically accessed using the `<icon></icon>` tag containing a URL. In addition to this, a small set of built in icons can be referenced by using the following “ID”s and omitting the "icon" tag from the definition:

| Icon ID | Icon |
| --- | --- |
| PLAY | <img src="images/31.5_5_01.png"/> |
| PAUSE | <img src="images/31.5_5_02.png"/> |
| STOP | <img src="images/31.5_5_03.png"/> | 
| CH\_UP | <img src="images/31.5_5_04.png"/> | 
| CH\_DOWN | <img src="images/31.5_5_05.png"/> |
| SCAN\_FWD | <img src="images/31.5_5_06.png"/>  | 
| SCAN\_REV | <img src="images/31.5_5_07.png"/> | 
| SKIP\_REV | <img src="images/31.5_5_08.png"/> |
| SKIP\_FWD | <img src="images/31.5_5_09.png"/> | 
| RECORD | <img src="images/31.5_5_10.png"/> | 

For example, to use the built in icon for PLAY, see the example to the right.


```xml
<buttons>                
  <button>
     <id>PLAY</id>
     <name>Play</name>
     <command>PLAY</command>
     <type>PROXY</type>
  </button>
 ...
</buttons>
```


_Example image of the Icons in the Media Dashboard:_

<img src="images/31.5_5_11.png"/> 