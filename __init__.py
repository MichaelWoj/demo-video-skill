from mycroft import MycroftSkill, intent_file_handler


class DemoVideo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('video.demo.intent')
    def handle_video_demo(self, message):
        self.speak_dialog('video.demo')


def create_skill():
    return DemoVideo()

