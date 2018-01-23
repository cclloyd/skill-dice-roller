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

        d20_intent = IntentBuilder('D20Intent') \
            .require('D20Keyword') \
            .build()
        self.register_intent(d20_intent, self.handle_d20_intent)

        #single_intent = IntentBuilder('SingleDieIntent') \
        #    .require('SingleRollKeyword') \
        #    .require('step') \
        #    .build()
        #self.register_intent(single_intent, self.handle_dice_single_roll_intent)

        intent = IntentBuilder('DiceRollerIntent') \
            .require('DiceRollerKeyword') \
            .require('amount') \
            .require('DiceDKeyword') \
            .require('step') \
            .build()
        self.register_intent(intent, self.handle_dice_roll_intent)

    def handle_dice_roll_intent(self, message):
        # self.process = play_mp3(join(dirname(__file__), "mp3", "coin-flip.mp3"))
        # self.speak('Please provide the second number.',  expect_response=True)

        total = 0
        amount = int(message.data.get("amount"))
        step = int(message.data.get("step"))
        math = ""
        if not isinstance(amount, int):
            amount = 1
        if not isinstance(step, int):
            step = 20

        self.speak("amount, step: {}, {}, die".format(amount, step))

        for i in range(0, amount):
            val = randint(1, step)
            total += val
            if i != amount:
                math += "{} + ".format(val)
            else :
                math += "{}".format(val)

        self.speak("dice roll: {}".format(total))
        if amount > 1:
            self.speak("{}".format(math))

    def handle_d20_intent(self, message):

        total = randint(1, 20)

        self.speak(format("d20: {}".format(total)))
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
