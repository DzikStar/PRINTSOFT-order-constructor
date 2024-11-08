import modules.Messages as Messages
import modules.Constructor as Constructor

def Main():

    offerType = int(input(Messages.PROMPT_USER_OFFER_TYPE))
    
    if offerType == 1:
        x = Constructor.typePC(offerType)
    elif offerType == 2:
        x = Constructor.typePC(offerType)
    elif offerType == 3:
        x = Constructor.typeMonitor()
    elif offerType == 4:
        x = Constructor.typePrinter()
    elif offerType == 5:
        x = Constructor.typeOther()

Main()