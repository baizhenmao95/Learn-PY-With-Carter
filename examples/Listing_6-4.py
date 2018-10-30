# Listing_6-4.py
# Copyright Warren & Carter Sande, 2013
# Released under MIT license   http://www.opensource.org/licenses/mit-license.php
# Version: $version: be6c6824f35f $  ----------------------------

# EasyGui - Default choices in an EnterBox

import easygui
flavor = easygui.enterbox("What is your favorite ice cream flavor?",
                           default = 'Vanilla')              #Here's the default
easygui.msgbox ("You entered " + flavor)


