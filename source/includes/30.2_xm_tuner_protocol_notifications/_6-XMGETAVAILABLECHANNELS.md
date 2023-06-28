## XM\_GET\_AVAILABLE\_CHANNELS

Displays available XM channels.


### Signature

`XM_GET_AVAILABLE_CHANNELS ()`


| Parameter | Description |
| --- | --- |
| num | MAP HALF: 1 is used for channels 0-127. 0 is used for channels 128 - 255. |


### Returns

`None`


### Example

```
00000000000000000000000000000001 indicates that channel 0 (or 128) is the only channel available.
00000000000000000000000000000002 indicates that channel 1 (or 129) is the only channel available.
00000000000000000000000000000003 indicates that channels 0 & 1 (or 128 & 129) are the only channels available.
00000000000000000000000000000004 indicates that channel 2 (or 130) is the only channel available.
00000000000000000000000000000005 indicates that channels 0 & 2 (or 128 & 130) are the only channels available.
00000000000000000000000000000006 indicates that channels 1 & 2 (or 129 & 130) are the only channels available.
00000000000000000000000000000007 indicates that channels 0, 1 & 2 (or 128, 129 & 130) are the only channels available.
00000000000000000000000000000008 indicates that channel 3 (or 131) is the only channel available.
00000000000000000000000000000009 indicates that channels 0 & 3 (or 128 & 131) are the only channels available.
0000000000000000000000000000000A indicates that channels 1 & 3 (or 129 & 131) are the only channels available.
0000000000000000000000000000000B indicates that channels 0, 1 & 3 (or 128, 129 & 131) are the only channels available.
0000000000000000000000000000000C indicates that channels 2 & 3 (or 130 & 131) are the only channels available.
0000000000000000000000000000000D indicates that channels 0, 2 & 3 (or 128, 130 & 131) are the only channels available.
0000000000000000000000000000000E indicates that channels 1, 2 & 3 (or 129, 130 & 131) are the only channels available.
0000000000000000000000000000000F indicates that channels 0, 1, 2 & 3 (or 128, 129, 130 & 131) are the only channels available.
```

