import modules.Messages as Messages
import modules.Constructor as Constructor
import modules.Utils as Utils

def Main():

    def addItem(offerId):
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

        return [{
            "offerId": offerId,
            "offerContent": f"{offer}"
        }]
    
    def manageItems(offerId):
        Utils.terminalClear

        clientChoice = int(input(Messages.PROMPT_USER_ITEMS_MANAGER))
        itemsAmount = int(input(Messages.PROMPT_USER_AMOUNT))

        if clientChoice == 1:
            Utils.terminalClear()
            offer = addItem(offerId)
        elif clientChoice == 2:
            Utils.terminalClear()
            print("TODO")
        elif clientChoice == 3:
            Utils.terminalClear()
            print("TODO")
        
        return offer

    offers = []
    currentOfferId = 0

    while True:
        Utils.terminalClear()

        currentOfferId += 1
        offers += manageItems(currentOfferId)

Main()