import Messages

def typePC(desktopType):

    if desktopType == 1:
        offerSpecs = {
            "producent": input(f"{Messages.SPEC_PRODUCENT}: "),
            "processor": input(f"{Messages.SPEC_PROCESSOR}: "),
            "ram": input(f"{Messages.SPEC_RAM}: "),
            "disk": input(f"{Messages.SPEC_DISK}: "),
            "os": input(f"{Messages.SPEC_OS}: "),
            "warranty": input(f"{Messages.SPEC_WARRANTY}: "),
            "retailPrice": input(f"{Messages.SPEC_RETAIL_PRICE}") 
        }
    elif desktopType == 2:
        offerSpecs = {
            "producent": input(f"{Messages.SPEC_PRODUCENT}: "),
            "processor": input(f"{Messages.SPEC_PROCESSOR}: "),
            "ram": input(f"{Messages.SPEC_RAM}: "),
            "disk": input(f"{Messages.SPEC_DISK}: "),
            "os": input(f"{Messages.SPEC_OS}: "),
            "warranty": input(f"{Messages.SPEC_WARRANTY}: "),
            "monitorSize": input(f"{Messages.SPEC_MONITOR_SIZE}: "),
            "retailPrice": input(f"{Messages.SPEC_RETAIL_PRICE}") 
        }

    return offerSpecs

def typeMonitor():
    
    return

def typePrinter():
    
    return

def typePC():
    
    return