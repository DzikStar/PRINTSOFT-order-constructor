import Messages
import Constructor

def Main():

    offerType = int(input(Messages.ASK_USER_OFFER_TYPE))
    
    if offerType == 1:
        Constructor.typePC(offerType)
    elif offerType == 2:
        Constructor.typePC(offerType)
    elif offerType == 3:
        Constructor.typeMonitor()
    elif offerType == 4:
        Constructor.typePrinter()
    elif offerType == 5:
        Constructor.typePrinter()

Main()