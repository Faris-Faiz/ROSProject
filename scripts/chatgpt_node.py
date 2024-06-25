#!/usr/bin/env python2.7

import rospy
from std_msgs.msg import String
import requests
import json

# Set your OpenAI API key here
API_KEY = "Your OpenAI API Key"
API_URL = "https://api.openai.com/v1/chat/completions"

def get_chatgpt_response(prompt):
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer {}'.format(API_KEY)
    }
    data = {
        'model': 'gpt-3.5-turbo',  # Ensure the model name is correct
        'messages': [{'role': 'user', 'content': prompt}],
        'temperature': 0.7
    }
    try:
        response = requests.post(API_URL, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content'].strip()
    except requests.exceptions.RequestException as e:
        rospy.logerr("Error getting response from OpenAI: {}".format(e))
        if response:
            rospy.logerr("Response status code: {}".format(response.status_code))
            rospy.logerr("Response content: {}".format(response.content))
        return "Error"

def callback(data):
    rospy.loginfo("Received: {}".format(data.data))
    response = get_chatgpt_response(data.data)
    rospy.loginfo("Response: {}".format(response))
    text_to_speak = response
    rospy.loginfo("Text to speak: {}".format(text_to_speak))
    pub.publish(text_to_speak)

if __name__ == '__main__':
    rospy.init_node('chatgpt_node', anonymous=True)
    pub = rospy.Publisher('text_to_speech', String, queue_size=10)
    rospy.Subscriber("chatgpt_input", String, callback)
    rospy.loginfo("ChatGPT Node Started")
    rospy.spin()
