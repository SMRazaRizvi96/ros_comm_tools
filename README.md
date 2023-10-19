# ros_comm_tools

This ROS stack provides a collection of communication tools that allow for advanced topic interactions and other functionalities within the ROS ecosystem. 

## Current Structure

The `ros_comm_tools` stack currently comprises the following package(s):

- **add_topic_tools**: 
  - **Nodes**:
    - **Triggered Publisher**: Subscribe to a topic and republish its content to another topic upon a user-defined trigger, such as pressing a button.

More packages and nodes will be added to this stack in the future to further enhance its capabilities.

## Features

- **Triggered Republishing**: As part of the `add_topic_tools` package, you can use the `Triggered Publisher` node to subscribe to a `sensor_msgs/Image` topic and republish its content based on manual keyboard triggers.

## Prerequisites

- ROS Noetic (though it might work with other ROS versions, it's only been tested on Noetic)

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

2. Run the `Triggered Publisher` node from the `add_topic_tools` package:

    ```bash
    rosrun add_topic_tools triggered_publisher.py
    ```

3. Follow the prompts to trigger republishing of messages.

## Parameters
The `Triggered Publisher` node from the `add_topic_tools` package supports the following ROS parameters:


- `~input_topic` : Name of the topic to subscribe to. Default: `/camera/image_raw`
- `~output_topic` : Name of the topic to publish messages to. Default: `/camera/image_raw`

Parameters can be set via the command line using rosparam, through a ROS launch file, or as command line parameters when running the node through `rosrun`.

## Contributing
Feel free to open issues or pull requests if you want to improve the package or add new functionalities.