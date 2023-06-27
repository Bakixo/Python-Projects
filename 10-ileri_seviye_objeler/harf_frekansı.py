string = "ProgramlamaÖdeviİleriSeviyeVeriYapilariveObjeleripynb"

def harf_frekansi():
    for harf in string:
        frekans = string.count(harf)
        print("{} harfden {} tane var".format(harf,frekans))

harf_frekansi()




"""
string = "ProgramlamaÖdeviİleriSeviyeVeriYapilariveObjeleripynb"
kaç_tane = {}

def harf_frekansi():
    for harf in string:
        if harf in kaç_tane:
            kaç_tane[harf] += 1
        else:
            kaç_tane[harf] = 1
    for harf, frekans in kaç_tane.items():
        print("{} harfden {} tane var".format(harf,frekans))

harf_frekansi()

"""