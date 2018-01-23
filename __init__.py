from os.path import dirname, join
from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
import requests
from os.path import dirname, join
from mycroft.util.log import getLogger
from mycroft.util import play_mp3
from random import randint

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
        self.load_regex_files(join(dirname(__file__), 'regex', 'en-us'))

        # dice_roll_intent = IntentBuilder("DiceRollerIntent").\
        #    require("DiceRollerKeyword").build()

        intent = IntentBuilder('DiceRollerIntent') \
            .require('DiceRollerKeyword') \
            .require('amount') \
            .require('DKeyword') \
            .require('step') \
            .build()
        self.register_intent(intent, self.handle_dice_roll_intent)

        d20_intent = IntentBuilder('DiceRollerIntent') \
            .require('D20Keyword') \
            .build()
        self.register_intent(d20_intent, self.handle_d20_intent)

    def handle_dice_roll_intent(self, message):
        # self.speak_dialog("flip.coin")
        # self.process = play_mp3(join(dirname(__file__), "mp3", "coin-flip.mp3"))
        # self.speak('Please provide the second number.',  expect_response=True)



        dialog_options = 4
        total = 0
        #amount = 1
        step = 6


        amount = message.data.get("amount")
        step = message.data.get("step")
        if (not isinstance(amount, int)):
            amount = 1



        for i in range(0, amount):
            total += randint(1,step)

        self.speak_dialog("it's %d".format(total))

    def handle_d20_intent(self, message):

        total = 0

        total += randint(1,20)

        self.speak_dialog(format("it's %d".format(total)))
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