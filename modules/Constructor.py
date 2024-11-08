import modules.Messages as Messages

def typePC(deviceType):

    if deviceType == 1:
        offerSpecs = "\n".join([
            f"{Messages.SPEC_PRODUCENT}: {input(f"{Messages.SPEC_PRODUCENT}: ")}",
            f"{Messages.SPEC_PROCESSOR}: {input(f"{Messages.SPEC_PROCESSOR}: ")}",
            f"{Messages.SPEC_RAM}: {input(f"{Messages.SPEC_RAM}: ")}",
            f"{Messages.SPEC_DISK}: {input(f"{Messages.SPEC_DISK}: ")}",
            f"{Messages.SPEC_OS}: {input(f"{Messages.SPEC_OS}: ")}",
            f"{Messages.SPEC_WARRANTY}: {input(f"{Messages.SPEC_WARRANTY}: ")}",
            f"{Messages.SPEC_RETAIL_PRICE}: {input(f"{Messages.SPEC_RETAIL_PRICE}: ")}"
            ])
    elif deviceType == 2:
        offerSpecs = "\n".join([
            f"{Messages.SPEC_PRODUCENT}: {input(f"{Messages.SPEC_PRODUCENT}: ")}",
            f"{Messages.SPEC_PROCESSOR}: {input(f"{Messages.SPEC_PROCESSOR}: ")}",
            f"{Messages.SPEC_RAM}: {input(f"{Messages.SPEC_RAM}: ")}",
            f"{Messages.SPEC_DISK}: {input(f"{Messages.SPEC_DISK}: ")}",
            f"{Messages.SPEC_OS}: {input(f"{Messages.SPEC_OS}: ")}",
            f"{Messages.SPEC_WARRANTY}: {input(f"{Messages.SPEC_WARRANTY}: ")}",
            f"{Messages.SPEC_MONITOR_SIZE}: {input(f"{Messages.SPEC_MONITOR_SIZE}: ")}",
            f"{Messages.SPEC_RETAIL_PRICE}: {input(f"{Messages.SPEC_RETAIL_PRICE}: ")}"
            ])
    return offerSpecs

def typeMonitor():
    return

def typePrinter():
    return

def typeOther():
    return