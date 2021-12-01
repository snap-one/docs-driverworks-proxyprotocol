

`<navigator_display_options></navigator_display_options>` 

This capability adds the ability to display device state icons for the button. As of this release, icon resolution for non-Media Server Proxy based drivers is:

- 300x300px
- 90x90px 
- 70x70px

### Example

```xml
<capabilities>
    <navigator_display_option proxybindingid="5001">
        <display_icons>
            <!-- Default Icon -->
            <Icon width="300" height="300">controller://driver/shortcutTest/icons/msp_ico_settings/msp_ico_settings_300.png</Icon>
            <!-- On State -->
            <state id="Settings-on">
            <Icon width="300" height="300">controller://driver/shortcutTest/icons/msp_ico_settings_a/msp_ico_settings_a_300.png</Icon>
            </state>
              <!-- Off State -->
              <state id="Settings-off">
              <Icon width="300" height="300">controller://driver/shortcutTest/icons/msp_ico_settings/msp_ico_settings_a_300.png</Icon>
            </state>     
        </display_icons>
    </navigator_display_option>
</capabilities>
```

Note, the example to the right does not include all icon sizes for brevity.





`<web_view_url></web_view_url>`
Optional Capability which, when added contains the default URL that is associated with the shortcut.

### Example

```xml
<capabilities>
   <web_view_url proxybindingid="5000">http://youtube.com</web_view_url>
</capabilities>
```





### web\_view\_url

`<web_view_url></web_view_url>`

An optional capability which points to the c4z-delivered web application. The controller://driver/driver\_name construct (i.e., the Controller URL Scheme) connects at the driver's www directory as the root of the path. 

Note that the driver name **MUST** be the same as the driver's filename. 

### Example

```xml
<capabilities>
   <web_view_url proxybindingid="5001">controller://driver/JavascriptAPIDemo/contents/index.html</web_view_url>
</capabilities>
```





### mobile\_web\_view\_enabled

`<mobile_web_view_enabled></mobile_web_view_enabled>`

An optional boolean capability that indicates that the driver can be shown in mobile clients when the `web_view_url` capability is also present. Applicable to O.S. 3.0.0 and later.
