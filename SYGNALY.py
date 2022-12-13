
N = int(input())
odp_cz = ''
odp = []


for i in range(N):
    pierwszy_sygnal = input()
    drugi_sygnal = input()

    for znak in pierwszy_sygnal:
        if znak in drugi_sygnal:
            ile_razy = min(pierwszy_sygnal.count(znak), drugi_sygnal.count(znak))
            znak_zastepczy = znak
            pierwszy_sygnal = pierwszy_sygnal.replace(znak, '')
            drugi_sygnal = drugi_sygnal.replace(znak, '')
            odp_cz += (ile_razy * znak_zastepczy)


    odp.append(odp_cz)
    odp_cz = ''

for j in range(N):
    print(odp[j])

