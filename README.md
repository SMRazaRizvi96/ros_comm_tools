# ros_comm_tools

This ROS package provides a set of communication tools that allow for advanced topic interactions, such as triggering republishing of messages upon specific events.

## Features

- **Triggered Republishing**: Subscribe to a topic and republish its content to another topic upon a user-defined trigger, such as pressing a button.

## Prerequisites

- ROS Noetic (though it might work with other ROS versions, it's only been tested on Noetic)
- `sensor_msgs` package for handling `Image` messages.

## Installation

1. Clone this package into your catkin workspace's `src` directory.
   
   ```bash
   cd ~/your_catkin_workspace/src
   git clone https://github.com/SMRazaRizvi96/ros_comm_tools.git
   ```

2. Compile your catkin workspace.
   
   ```bash
    cd ~/your_catkin_workspace
    catkin_make
    ```

3. Source your workspace's setup.bash:

    ```bash
    source devel/setup.bash
    ```

## Usage

1. Start the ROS core:

    ```bash
    roscore
    ```

2. Run the triggered publisher node:

    ```bash
    rosrun ros_comm_tools triggered_publisher.py
    ```

3. Follow the prompts to trigger republishing of messages.

## Parameters
The triggered publisher node supports the following ROS parameters:


- `~input_topic` : Name of the topic to subscribe to. Default: `/camera/image_raw`
- `~output_topic` : Name of the topic to publish messages to. Default: `/camera/image_raw`

Parameters can be set via the command line using rosparam or through a ROS launch file.

## Contributing
Feel free to open issues or pull requests if you want to improve the package or add new functionalities.