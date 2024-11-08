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
            f"{Messages.SPEC_RETAIL_PRICE}: {input(f"{Messages.SPEC_RETAIL_PRICE}: ")} {Messages.CURRENCY_PLN}"
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
            f"{Messages.SPEC_RETAIL_PRICE}: {input(f"{Messages.SPEC_RETAIL_PRICE}: ")} {Messages.CURRENCY_PLN}"
            ])
    return offerSpecs

def typeMonitor():
    return "\n".join([
        f"{Messages.SPEC_PRODUCENT}: {input(f"{Messages.SPEC_PRODUCENT}: ")}",
        f"{Messages.SPEC_MONITOR_SIZE}: {input(f"{Messages.SPEC_MONITOR_SIZE}: ")}",
        f"{Messages.SPEC_RESOLUTION}: {input(f"{Messages.SPEC_RESOLUTION}: ")}",
        f"{Messages.SPEC_DISPLAY_TYPE}: {input(f"{Messages.SPEC_DISPLAY_TYPE}: ")}",
        f"{Messages.SPEC_DISPLAY_HZ}: {input(f"{Messages.SPEC_DISPLAY_HZ}: ")}",
        f"{Messages.SPEC_WARRANTY}: {input(f"{Messages.SPEC_WARRANTY}: ")}",
        f"{Messages.SPEC_RETAIL_PRICE}: {input(f"{Messages.SPEC_RETAIL_PRICE}: ")} {Messages.CURRENCY_PLN}"
    ])

def typePrinter():
    return "\n".join([
        f"{Messages.SPEC_PRODUCENT}: {input(f"{Messages.SPEC_PRODUCENT}: ")}",
        f"{Messages.SPEC_PRINT_TYPE}: {input(f"{Messages.SPEC_PRINT_TYPE}: ")}",
        f"{Messages.SPEC_DUPLEX}: {input(f"{Messages.SPEC_DUPLEX}: ")}",
        f"{Messages.SPEC_PRINT_COLOR}: {input(f"{Messages.SPEC_PRINT_COLOR}: ")}",
        f"{Messages.SPEC_WARRANTY}: {input(f"{Messages.SPEC_WARRANTY}: ")}",
        f"{Messages.SPEC_COMMUNICATION}: {input(f"{Messages.SPEC_COMMUNICATION}: ")}",
        f"{Messages.SPEC_SCANNER}: {input(f"{Messages.SPEC_SCANNER}: ")}",
        f"{Messages.SPEC_RETAIL_PRICE}: {input(f"{Messages.SPEC_RETAIL_PRICE}: ")} {Messages.CURRENCY_PLN}",
    ])

def typeOther():
    return "\n".join([
        # TODO: Adding items implementation
        f"{Messages.SPEC_RETAIL_PRICE}: {input(f"{Messages.SPEC_RETAIL_PRICE}: ")} {Messages.CURRENCY_PLN}",
    ])