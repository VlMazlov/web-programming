__author__ = 'vlmazlov'

LEFT_SYMBOLS_NUM=35

def truncate(string ):
    return (string[:LEFT_SYMBOLS_NUM] + '..') if len(string) > LEFT_SYMBOLS_NUM else string