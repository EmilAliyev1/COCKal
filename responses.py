
def get_response(user_input: str, false=bool(False)) -> str:
    lowered: str = user_input.lower()
    lowered += ' '
    uzeyir_id = '<@1145248789276401724>'
    uzeyir_id2 = '<@&1250201529084936264>'
    bot_id = '<@1272284943665463409>'
    bot_id2 = '<@&1272287798648373271>'
    atilla_id = '<@858001658947567617>'
    atilla_id2 = '<@&1250201623859302400>'
    emil_id = '<@735410474643881994>'
    emil_id2 = '@735410474643881994'
    dorn_id = '<@962074754586665031>'
    dorn_id2 = '@962074754586665031'
    murad_id = '<@641656202920591380>'
    murad_id2 = '@641656202920591380'
    everyone = '<@everyone>'
    obzivatelstva = ['tupoy ', 'trapeziya ', 'trapeciya ', 'ebaniy ', 'ebanniy ', 'pidoras ', 'pos ', 'churdick ', 'chort ', 'nahuy ', 'soset ', 'huy ', 'xu y', 'psina ', 'churka ', 'tuporiliy ', 'eblan ', 'koncenniy ']

    if 'uzeyir ' in lowered:
        return 'konkretniy COCKal upomanut v soobsenii!'
    elif (bot_id in lowered or bot_id2 in lowered) and 'privedick ' in lowered and 'cock dela ' in lowered:
        return 'priveDICK, DICKo\nu teba COCK?'
    elif (bot_id in lowered or bot_id2 in lowered) and 'privedick ' in lowered:
        return 'priveDICK'
    elif 'privedik ' in lowered or 'privedic ' in lowered or 'privedikc' in lowered:
        return '*priveDICK\n' * 10
    elif (bot_id in lowered or bot_id2 in lowered) and 'cock dela ' in lowered:
        return 'DICKo, u teba COCK?'
    elif (bot_id in lowered or bot_id2 in lowered) and 'sps ' in lowered:
        return 'nzc'
    elif 'pon ' in lowered:
        return 'DICKo'
    elif 'dicko ' in lowered:
        return 'pon'
    elif 'ya cockal ' in lowered or (murad_id in lowered and 'cockal ' in lowered) or ((uzeyir_id in lowered or uzeyir_id2 in lowered) and 'cockal ' in lowered) or (dorn_id in lowered and 'cockal ' in lowered):
        return 'ya znayu'
    elif 'razmer ' in lowered and 'dicka ' in lowered and ('nadicka ' or 'nadick ') in lowered:
        return 'primerno s razmerom burj khalifa'
    elif 'osibdick ' in lowered or 'osibsa ' in lowered or 'soran ' in lowered:
        return 'nicego, COCK govoril Jason Statham, \"Esli ne upades to ne podnimessa\"'
    elif 'xocel ' in lowered:
        return 'no perexocel'
    elif (bot_id in lowered or bot_id2 in lowered) and ('cocklasen ' in lowered or 'soglasen ' in lowered or 'sogladick ' in lowered):
        return 'COCKnecno'
    elif 'donk xuyesos ' in lowered or ((bot_id in lowered or bot_id2 in lowered) and 'cockal ' in lowered):
        return 'po fakDICKam'
    elif (bot_id in lowered or bot_id2 in lowered) and ('donk ' in lowered or 'donka ' in lowered):
        return 'donk xuyesos'
    elif uzeyir_id == lowered or uzeyir_id2 == lowered:
        return 'konkretniy COCKal!'
    elif dorn_id == lowered:
        return 'DÖRNozavr'
    elif atilla_id == lowered or atilla_id2 == lowered or emil_id == lowered:
        return 'churkounictojitel!'
    elif murad_id == lowered:
        return 'ahuyevsaya psina'
    elif everyone == lowered:
        return 'COCKali'
    elif (bot_id in lowered or bot_id2 in lowered) and '? ' in lowered:
        return 'sprosi normalniye voprosi pOs'
    elif bot_id == lowered or bot_id2 == lowered:
        return 'da'
    
    if bot_id in lowered or bot_id2 in lowered:
        for i in range(len(obzivatelstva)):
            obzivatelstvo = obzivatelstva[i]
            if obzivatelstvo in lowered:
                return 'ides nahuy'