# ant-crawl-python

An object-oriented solution for the ant crawling problem, written in Python.

A UI for all showcases is to be included, using PyQt.

## Compile .ui file and .qrc resource file

Use `pyuic5` and `pyrcc5` to generate resource files before compiling.

```shell
pyuic5 -x -o ./resources/antcrawl_ui.py ./resources/antcrawl.ui
pyrcc5 -o ./resources/res_rc.py ./resources/resources.qrc
```
