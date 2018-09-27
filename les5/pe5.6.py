#   Schrijf een for-loop die langs alle letters van een string loopt en de letter uitprint,
#  maar alleen als het een klinker is ('aeiou').
# Gebruik de volgende string:

s = "Guido van Rossum heeft programmeertaal Python bedacht."
klinkers = ''

for letters in s:
    if letters in 'aeoui':
        klinkers += letters

print(klinkers)


