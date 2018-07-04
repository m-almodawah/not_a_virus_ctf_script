import binascii

hex_string = "6C6A7CBE6CF13D256C276DED33AF39423E4D7DB6"
# converts a hex string to a binary string
hex_to_binary = bin(int(hex_string, 16))[2:]
final_bin = ""
# This loop takes only the odd bits and stores them in final_bin
for i in range(0,len(hex_to_binary)):
    if (i % 2) == 1:
        final_bin = final_bin + list(hex_to_binary)[i]
# Converts final_bin to ASCII format
converter = int('0b'+final_bin, 2)
out = binascii.unhexlify('%x' % converter)
print(out)
