N = int(input())
odp = []
odp_cz = ''



for i in range(N):
    pierwszy_sygnal = list(input())
    drugi_sygnal = list(input())

    for znak1s in pierwszy_sygnal:
        for znak2s in drugi_sygnal:

            if znak1s == znak2s:
                odp_cz += znak2s
                drugi_sygnal.remove(znak2s)


    odp.append(odp_cz)
    odp_cz = ''


for j in range(N):
    print(odp[j])
