#!/usr/bin/env python

import rospy
import os
from gtts import gTTS
from playsound import playsound
from std_msgs.msg import String

class TextToSpeechNode:
    def __init__(self):
        rospy.init_node('text_to_speech_node', anonymous=True)
        
        self.subscriber = rospy.Subscriber('text_to_speech', String, self.callback)
        
        rospy.loginfo("Text-to-Speech Node initialized")
    
    def callback(self, msg):
        try:
            text = msg.data
            rospy.loginfo("Received text: %s" % text)
            
            tts = gTTS(text=text, lang='en')
            temp_file = "temp.mp3"
            tts.save(temp_file)
            
            playsound(temp_file)
            
            os.remove(temp_file)
            
            rospy.loginfo("Finished playing text")
        
        except Exception as e:
            rospy.logerr("Error processing text: %s" % str(e))

if __name__ == '__main__':
    try:
        node = TextToSpeechNode()
        rospy.spin()
    except rospy.ROSInterruptException:
        pass
