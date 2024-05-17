## SAVE\_EQ\_TO\_CUSTOM\_PRESET

Navigator EQ command called to save the current EQ values to a custom preset with a name. The driver should notify proxy with the EQ\_NAMES\_CHANGED notification with the updated name.


### Signature

`SAVE_EQ_TO_CUSTOM_PRESET`


| Parameter | Description | Description                                                                                                                                                                                                                      |
| --------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| OUTPUT    | int         | Output Binding ID                                                                                                                                                                                                                |
| INDEX     | int         | Zero based custom preset index value used to save the custom preset.  The index range is from 0 to the number of custom presets defined in the `<eq_preset_nav_count>` capability, minus one due to the range being zero-based.  |
| NAME      | str         | Name for the new custom index.  Base64 encoded.                                                                                                                                                                                  |


### Returns

`None`



