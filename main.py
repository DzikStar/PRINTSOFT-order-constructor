import modules.Messages as Messages
import modules.Constructor as Constructor
import modules.Utils as Utils

def Main():

    def addItem():
        Utils.terminalClear()
        offerType = int(input(Messages.PROMPT_USER_OFFER_TYPE))
        Utils.terminalClear()

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

        offerItem = [{
            "offerId": "TODO",
            "offerContent": f"{offer}"
        }]

        return offerItem
    
    def manageItems():
        Utils.terminalClear

        clientChoice = int(input(Messages.PROMPT_USER_ITEMS_MANAGER))

        if clientChoice == 1:
            Utils.terminalClear()
            offer = addItem()
        elif clientChoice == 2:
            Utils.terminalClear()
            print("TODO")
        elif clientChoice == 3:
            Utils.terminalClear()
            print("TODO")
        
        return offer

    offers = []

    Utils.terminalClear()

    while True:
        offers += manageItems()

Main()