from os.path import dirname, join
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
import requests
from os.path import dirname, join
from mycroft.util.log import getLogger
from mycroft.util import play_mp3
import random

# Logger: used for debug lines, like "LOGGER.debug(xyz)". These
# statements will show up in the command line when running Mycroft.
LOGGER = getLogger(__name__)

class DiceRollerSkill(MycroftSkill):

    # The constructor of the skill, which calls MycroftSkill's constructor
    def __init__(self):
        super(DiceRollerSkill, self).__init__(name="DiceRollerSkill")

    # This method loads the files needed for the skill's functioning, and
    # creates and registers each intent that the skill uses
    def initialize(self):
        self.load_data_files(dirname(__file__))

        coin_flip_intent = IntentBuilder("DiceRollerIntent").\
            require("DiceRollerKeyword").build()
        self.register_intent(coin_flip_intent, self.handle_coin_flip_intent)

    # The "handle_xxxx_intent" functions define Mycroft's behavior when
    # each of the skill's intents is triggered: in this case, he simply
    # speaks a response. Note that the "speak_dialog" method doesn't
    # actually speak the text it's passed--instead, that text is the filename
    # of a file in the dialog folder, and Mycroft speaks its contents when
    # the method is called.
    def handle_coin_flip_intent(self, message):
        #self.speak_dialog("flip.coin")
        #self.process = play_mp3(join(dirname(__file__), "mp3", "coin-flip.mp3"))

        dialog_options = 4
        total = 0
        amount = 1
        step = 4
        for i in range(0, amount):
            total += random.randint(1,step)

        self.speak(format("it's %d", total))


'''
        self.speak(format("it's %d.", total))
        if bool(random.getrandbits(1)):
            #self.process.wait()
            #choice = randint(1, dialogOptions);
            #self.speak_dialog(format("heads_%d", choice))
        else:
            #self.process.wait()
            self.speak_dialog("tails")
'''
    # The "stop" method defines what Mycroft does when told to stop during
    # the skill's execution. In this case, since the skill's functionality
    # is extremely simple, the method just contains the keyword "pass", which
    # does nothing.
    def stop(self):
        pass

# The "create_skill()" method is used to create an instance of the skill.
# Note that it's outside the class itself.
def create_skill():
    return DiceRollerSkill()