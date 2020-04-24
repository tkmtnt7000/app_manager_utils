# app_manager_utils
[![](https://travis-ci.com/knorth55/app_manager_utils.svg?branch=master)](https://travis-ci.com/github/knorth55/app_manager_utils)

## Build 

```
mkdir ~/catkin_ws/src -p
cd ~/catkin_ws/src
wstool init
wstool merge  https://raw.githubusercontent.com/knorth55/app_manager_utils/master/fc.rosinstall
wstool up
rosdep install --ignore-src --from-path . -y -r
cd ~/catkin_ws
catkin build
```

## app_scheduler

Scheduler for `app_manager`

For detailed information, please read [app_scheduler](app_scheduler/README.md).

## app_manager_plugin

Plugin for app_manager

**Caution**

app_manager_plugin depends on [knorth55/app_manager@add-app-manager-plugin](https://github.com/knorth55/app_manager/tree/add-app-manager-plugin)  branch.


## test_app_manger

Simple test package for app_manager
