#!/usr/bin/env python3


#Code written by Mario Shebib and taken from https://pimylifeup.com/raspberry-pi-rfid-rc522/
import sys

class no_RC522:
    def __init__(self):
        # Get account id and data from file
        try:
            with open("nfc_id_address.txt", "r") as idfile:
                self.account_id = idfile.read().strip()
            with open("nfc_data.txt", "r") as datafile:
                self.data = datafile.read().strip()
        except FileNotFoundError as e:
            print("Could not open testcase files.")
            exit(1)

    #method returns id from file
    def read_card(self):     
        return self.account_id
    #method returns data from file
    def read_card_data(self,adr):
        return self.data

