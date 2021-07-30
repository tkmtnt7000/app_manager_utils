import json
import os
import rospy

from rostwitter.msg import TweetGoal
from sound_play.msg import SoundRequestGoal


def speak(client, speech_text, lang=None):
    client.wait_for_server(timeout=rospy.Duration(1.0))
    sound_goal = SoundRequestGoal()
    sound_goal.sound_request.sound = -3
    sound_goal.sound_request.command = 1
    sound_goal.sound_request.volume = 1.0
    if lang is not None:
        sound_goal.sound_request.arg2 = lang
    sound_goal.sound_request.arg = speech_text
    client.send_goal(sound_goal)
    client.wait_for_result()
    return client.get_result()


def tweet(client, tweet_text, image=False, image_topic_name=None):
    client.wait_for_server(timeout=rospy.Duration(1.0))
    tweet_goal = TweetGoal()
    tweet_goal.text = tweet_text
    tweet_goal.image = image
    if image and image_topic_name:
        tweet_goal.image_topic_name = image_topic_name
    tweet_goal.speak = False
    tweet_goal.warning = False
    tweet_goal.warning_time = 0
    client.send_goal(tweet_goal)
    client.wait_for_result()
    return client.get_result()


def get_notification_json_paths():
    notification_json_path = rospy.get_param(
        '/service_notification_saver/json_path', None)
    smach_json_path = rospy.get_param(
        '/smach_notification_saver/json_path', None)
    if notification_json_path and smach_json_path:
        if notification_json_path == smach_json_path:
            json_paths = [notification_json_path]
        else:
            json_paths = [notification_json_path, smach_json_path]
    elif notification_json_path:
        json_paths = [notification_json_path]
    elif smach_json_path:
        json_paths = [smach_json_path]
    else:
        json_paths = ['/tmp/app_notification.json']
    return json_paths


def load_jsons(json_paths):
    notification = {}
    for json_path in json_paths:
        if not os.path.exists(json_path):
            continue
        with open(json_path, 'r') as f:
            n_data = json.load(f)
        for n_type in n_data.keys():
            if n_type in notification:
                notification[n_type].append(n_data[n_type])
            else:
                notification[n_type] = n_data[n_type]
    return notification
