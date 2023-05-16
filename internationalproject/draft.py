def est_de(l: str) -> bool:
    result = any(
        [
            "et" in str.lower(l),
            "de" in str.lower(l),
            "ru" in str.lower(l),
            "en" in str.lower(l),
        ]
    )
    return result


from django.conf.global_settings import LANGUAGES

langs = LANGUAGES

for l in langs:
    if est_de(l[0]):
        print(l)
