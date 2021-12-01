## AUTOBINDINGS in Receiver an TV DRIVERS

Usage Note on the use of Auto-Bindings in conjunction with the Receiver and TV Proxies:

If your Receiver and TV driver intends to use Auto-Binding feature in ComposerPro, the binding ID value for those connections must use an ID value of 7000. Any other value will result in the auto-binding connection not being created.

For example:

```xml
   <connection proxybindingid="5000">
      <id>7000</id>
      <facing>6</facing>
      <connectionname>Room Selection - Output</connectionname>
      <type>7</type>
      <consumer>False</consumer>
      <audiosource>True</audiosource>
      <videosource>True</videosource>
      <linelevel>True</linelevel>
      <classes>
        <class>
          <classname>AUDIO_SELECTION</classname>
        </class>
        <class>
          <classname>AUDIO_VOLUME</classname>
        </class>
        <class>
          <classname>VIDEO_SELECTION</classname>
        </class>
      </classes>
    </connection>
```
