# pyqt-slideshow
PyQt widget for slide show

## Requirements
* PyQt5 >= 5.8

## Setup
`python -m pip install pyqt-slideshow`

## Included Packages
* <a href="https://github.com/yjg30737/pyqt-single-image-graphics-view.git">pyqt-single-image-graphics-view</a> - main image view
* <a href="https://github.com/yjg30737/pyqt-svg-button.git">pyqt-svg-button</a> - for navigation button on left and right sides
* <a href="https://github.com/yjg30737/pyqt-ani-radiobutton.git">pyqt-ani-radiobutton</a> - for navigation button at the bottom

## Detailed Description

![image](https://user-images.githubusercontent.com/55078043/170638847-1816f292-f731-49bc-bbb3-d7180e7ec779.png)

This widget mainly consists of three child widget.

* View
* Navigation widget - buttons on the both sides of the view
* Bottom widget - buttons at the bottom

## Method Overview
* `setFilenames(filenames: list)` - give the image files. You have to call this one time only so far.
* `setInterval(milliseconds: int)` - set the image change interval
* `setNavigationButtonVisible(f: bool)` - set the navigation button's visibility(which also decides that you use it or not)
* `setBottomButtonVisible(f: bool)` - set the bottom button's visibility(which also decides that you use it or not)

## Example
Code Sample
```python
from PyQt5.QtWidgets import QApplication
from pyqt_slideshow import SlideShow


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    s = SlideShow()
    s.setFilenames(['bioshock.jpg', 'dragon_age.jpg', 'ride_to_hell_retribution.jpg'])
    s.show()
    app.exec_()
```

Result

https://user-images.githubusercontent.com/55078043/170615616-932fb93d-3311-4f97-8ad7-10943e0d2308.mp4

I'm still working on SvgButton's style. You can see the <, > buttons in the picture. Those things are SvgButton. 

It is kinda ugly looking and could be hard to see depending on the photo. So i will definitely change the style.

Note: Don't play the last game on the list.
