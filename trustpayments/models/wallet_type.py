# coding: utf-8
from enum import Enum, unique


@unique
class WalletType(Enum):
    
    APPLE_PAY = "APPLE_PAY"
    CLICK_TO_PAY = "CLICK_TO_PAY"
    NONE = "NONE"

