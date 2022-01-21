"""
option vendor-encapsulated-options 01:11:68:74:74:70:3A:2F:2F:61:63:73:2E:6D:65:2E:63:6F:6D;

In any case you have to remember the 3 fields: option_code, value_length and value.
In this example we use http://acs.me.com as ACS URL, so our option will contain 0x01 (CWMP option for ACS URL), 0x11 (hex of decimal 17 = length of the URL) then the other 17 bytes forming the URL.

"""
url_to_convert = input('Give me a url: ')

encoded = '01:' + ('%x:' % (len(url_to_convert))).rjust(3,'0') + ''.join([('%x:'%(ord(i))).rjust(2,'0') for i in url_to_convert])[:-1]

print('Result: '+encoded.upper())
