from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill, intent_handler
from mycroft.util.log import LOG

__author__ = 'ipokay'
LOGGER = LOG.create_logger( __name__ )

class MyFirstSkill( MycroftSkill ):

    def __init__( self ):
        super( MyFirstSkill, self ).__init__( name="SchlattCoinSkill" )
        LOGGER.info( "__init__" )

    @intent_handler( IntentBuilder( "" ).require( "SchlattCoin" ) )
    def handle_lyric_intent( self, message ):
        LOGGER.info( "schlattcoin" )
        self.speak_dialog( "ImInterested", data={} )

def create_skill():
    return SchlattCoinSkill()