import tkinter
from tkinter import *
import phonenumbers
from phonenumbers import carrier,geocoder,geodata,timezone
class Info:
    def get_carrier(number):
        phone_number=phonenumbers.parse(number,"FR")
        return str(carrier.name_for_number(phone_number,"FR"))+' '+str(phonenumbers.region_code_for_number(phone_number))
    def get_country(number):
        phone_number=phonenumbers.parse(number,"en")
        return str(geocoder.description_for_valid_number(phone_number,"en"))
    def get_time_zone(number):
        phone_number=phonenumbers.parse(number,"en")
        return str((timezone.time_zones_for_number(phone_number)[0]))
    def get_region_code(number):
        phone_number=phonenumbers.parse(number,"en")
        return str(phonenumbers.region_code_for_number(phone_number))
    def check_number(number):
        phone_number=phonenumbers.parse(number,"en")
        return str(phonenumbers.is_valid_number(phone_number))


