## new CoverArt

SendDataToUI(newCoverArt)


### Signature

`NEW_COVERART ()`


| Parameter | Description |
| --- | --- |
| width | Image width |
| height | Image height |
| path |  Location of image |

### Example

```lua
AutoNode newCoverArt(C4XML::CreateXmlNode("NEW_COVER_ART"));
newCoverArt->AddChild("image_path", m_ImagePath);
newCoverArt->AddChild("width", m_ImageWidth);
newCoverArt->AddChild("height", m_ImageHeight);
SendDataToUI( *newCoverArt );
```
