import modules.Messages as Messages
import modules.Constructor as Constructor

def Main():

    offerType = int(input(Messages.PROMPT_USER_OFFER_TYPE))
    
    if offerType == 1:
        print(Constructor.typePC(offerType))
    elif offerType == 2:
        print(Constructor.typePC(offerType))
    elif offerType == 3:
        Constructor.typeMonitor()
    elif offerType == 4:
        Constructor.typePrinter()
    elif offerType == 5:
        Constructor.typePrinter()

Main()