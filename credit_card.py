# ----------------------------------------------------------------------
# Card                | Prefix                                 | Length
# ----------------------------------------------------------------------
# American Express    | 34, 37                                 | 15
# Diners Club         | 36, 38                                 | 14, 15
# Visa                | 4                                      | 16
# Visa Electron       | 4026, 417500, 4508, 4844, 4913, 4917   | 16

def get_issuer(card_number):
    prefixes = {
        'Visa': ['4'],
        'Visa Electron': ['4026', '417500', '4508', '4844', '4913', '4917'],
        'American Express': ['34', '37'],
        'Diners Club': ['36', '38']
    }
    
    lengths = {
        14: ['Diners Club'],
        15: ['American Express', 'Diners Club'],
        16: ['Visa Electron', 'Visa']
    }
    
    # # for each possible card type from lengths map
    # // for each prefix of each possible card Type
    # // if card number strats with the prefix then return
    
    card_length = len(card_number)
    
    if card_length in lengths:
        cards = lengths[card_length]
        
        for card in cards:
            for prefix in prefixes[card]:
                if card_number.startswith(prefix):
                    return card

    return 'Unknown'
    
#     prefix = int(card_number[:2])
    
#     card_number_dict ={34: 'American Express', 
#                          37: 'American Express', 
#                          36: 'Diners Club', 
#                          38: 'Diners Club',
#                         }
#     print(prefix)
    
#     if len(card_number) == 15 or len(card_number) == 14:
#         if prefix in card_number_dict:
#             return card_number_dict[prefix]
        
#     return 'Unknown'

import pytest

def test_issuer():
    assert get_issuer('4026000000000000') == 'Visa Electron'
    assert get_issuer('4000000000000000') == 'Visa'
    assert get_issuer('342600000000000') == 'American Express'
    # assert get_issuer('

pytest.main()