# Vocabot

Jednoduchý pomocník pro [WocaBee](https://wocabee.app/). Python + Playwright; vlastní okno Chromium, přihlášení, výběr třídy/balíčku a původní automatický řešič. **Žádné osobní údaje ani hesla v repozitáři.**

> **Stav:** Experimentální verze. Opraven výběr balíčků s podporou obou známých selektorů `pTableRow` a `packageTableRow`. Dosud neotestováno na aktuální přihlášené aplikaci; změny rozhraní mohou způsobit selhání.

## Windows: 4 kroky

1. Nainstaluj [Python 3.9+](https://www.python.org/downloads/) (zaškrtni *Add Python to PATH*).
2. Stáhni tento repozitář jako **Code → Download ZIP** a rozbal ho.
3. Dvojklik na **`install.bat`** (závislosti + prohlížeč).
4. Dvojklik na **`start.bat`**. Zadej přihlašovací jméno, heslo, pořadové číslo třídy a balíčku (od 1) a požadovaný počet bodů.

## Linux / macOS

```sh
python3 -m pip install -r requirements.txt
python3 -m playwright install chromium
python3 bot.py
```

Některé distribuce Linuxu vyžadují také systémové knihovny pro Chromium – viz [dokumentace Playwright](https://playwright.dev/python/docs/browsers).

## Struktura

- `bot.py` — průvodce, bezpečné zadání hesla bez zápisu na disk.
- `startup.py` — otevření prohlížeče, přihlášení, výběr třídy a balíčku.
- `solver.py` — původní řešič, přizpůsobený privátním lokálním datům.
- `data/` — automaticky vytvořená složka pro naučené překlady a obrázky; ignorována Gitem.
- `config.example.toml` — čistý příklad pokročilého nastavení (pro běžné spuštění není potřeba).
- `tests/` a GitHub Actions — kontrola základních bezpečnostních pravidel a syntaxe.

První neznámé překlady může bot vyžadovat ručně. Původní řešič vznikl zejména pro slovenštinu/angličtinu, takže čeština vyžaduje ověření.

## Soukromí

- V repozitáři nejsou žádné účty, hesla, tokeny, cookies, osobní cesty ani seznamy školních slovíček.
- Přihlašovací údaje se načítají za běhu a předávají jen lokálnímu podprocesu přes proměnné prostředí; po dobu běhu k nim proces přístup má.
- `.gitignore` vylučuje `data/`, `config.toml`, `.env`, logy a screenshoty. **Nesdílej tyto soubory ani celé debug logy.**
- Chromium používá lokální debugging `127.0.0.1:9222`. Tento port nevystavuj veřejně.
- Pokud by se tajný údaj dostal do Git historie, změň jej ihned. Pouhé smazání souboru z nové verze nestačí.

## Kontrola bez přihlašování

```sh
python -m unittest discover -s tests -v
python -m compileall -q bot.py startup.py solver.py
```

## Omezení a licence

Nástroj není oficiálním produktem WocaBee a může být v rozporu s podmínkami služby nebo školy. Automatizace může přestat fungovat při změně webu. Původní zdroj: [toomcis/WocaFuckOff](https://github.com/toomcis/WocaFuckOff). Soubory `startup.py` a `solver.py` jsou odvozeným dílem. Původní autor a znění licence MIT jsou zachovány v [LICENSE](LICENSE).
