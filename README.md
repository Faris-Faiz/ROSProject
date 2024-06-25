# ROS Project
**!!IMPORTANT!!
 in [chatgpt_node.py](https://github.com/Faris-Faiz/ROSProject/blob/main/scripts/chatgpt_node.py "chatgpt_node.py") under the scripts folder, please adjust the OpenAI Key as usual.**

This is the ROS Project for the Autonomous Robots assignment by our group.

Run these codes to test out the entire

    rosrun chatgpt_ros chatgpt_node.py
    rosrun chatgpt_ros tts_node.py

Run the code below to test out the ChatGPT Component

    rostopic pub /chatgpt_input std_msgs/String "Hello, ChatGPT!"




