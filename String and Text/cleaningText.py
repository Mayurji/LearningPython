import sys
import unicodedata

messedUpString = 'pýtĥöñ\fis\tawesome\r\n'
#creating a remapping
remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None
}
betterString = messedUpString.translate(remap)
print(f"Better String: {betterString}")

#Remove combining character (Check unicodeNormalization.py)
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode)
                        if unicodedata.combining(chr(c)))
normalizeChar = unicodedata.normalize('NFD', betterString)
print(f"Cleaned String: {normalizeChar.translate(cmb_chrs)}")

normalizeChar = unicodedata.normalize('NFD', betterString)
print(f"Clean String Using encode and decode: {normalizeChar.encode('ascii', 'ignore').decode('ascii')}")