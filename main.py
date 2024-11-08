import modules.Messages as Messages
import modules.Constructor as Constructor

def Main():

    def addItem():
        offerType = int(input(Messages.PROMPT_USER_OFFER_TYPE))
        
        if offerType == 1:
            offer = Constructor.typePC(offerType)
        elif offerType == 2:
            offer = Constructor.typePC(offerType)
        elif offerType == 3:
            offer = Constructor.typeMonitor()
        elif offerType == 4:
            offer = Constructor.typePrinter()
        elif offerType == 5:
            offer = Constructor.typeOther()

        return offer

Main()