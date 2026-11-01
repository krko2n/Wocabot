# Wocabot – WocaBee Control Portable

Přenosná Windows aplikace pro ovládání automatizace WocaBee. Distribuce obsahuje hotové spustitelné soubory; zdrojový strom této konkrétní portable sestavy nebyl součástí původního média.

Používejte jen se svým účtem, v souladu s pravidly školy a služby. Aplikace není oficiálním produktem WocaBee.

## Co umí

- grafické ovládání přes `WocaBee-Control.exe`;
- spuštění vybraných tříd a balíčků přes `WocaBee-Runner.exe`;
- řešení podporovaných slovních a obrázkových typů cvičení přes `WocaBee-Solver.exe`;
- nastavení cílové třídy/balíčku, zpoždění, bodových milníků a režimu viditelného prohlížeče;
- místní diagnostiku a průběžně vytvořené slovní či obrázkové mapy.

## Rychlý start ve Windows

1. Stáhněte ZIP repozitáře a rozbalte jej do vlastní složky s dostatkem místa na disku.
2. Dvakrát klikněte na `Setup-Browser.cmd`. Jednou nainstaluje kompatibilní Playwright runtime do této složky. Vyžaduje Python 3 a internetové připojení; stáhne několik stovek MB.
3. Otevřete `config.toml`, doplňte vlastní přihlašovací údaje a uložte jej. Tento soubor je záměrně ignorovaný Gitem.
4. Spusťte `Start-WocaBee-Control.cmd` a pokračujte z ovládacího okna.

Pokud Python ve Windows nemáte, instalační skript zobrazí odkaz na jeho oficiální instalaci. Po instalaci skript spusťte znovu.

## Konfigurace a soukromí

`config.example.toml` je veřejná šablona. Při prvním nastavení se zkopíruje jako místní `config.toml`. Do repozitáře nepatří:

- přihlašovací údaje, tokeny a nastavení oznámení;
- adresář `runtime/` s místně naučenými slovními a obrázkovými mapami;
- `diagnostics/` a screenshoty;
- `ms-playwright/` se staženým browser runtime;
- zálohy spustitelných souborů a soubory `*.bak`.

Pokud chcete začít znovu s prázdnými mapami, zavřete aplikaci a smažte pouze složku `runtime` ve své lokální kopii. Nikdy nemažte `config.toml`, pokud si jej nejdříve nezálohujete.

## Nastavení

| Nastavení | Význam |
| --- | --- |
| `class_index`, `package_index` | Výběr třídy a balíčku od nuly. |
| `headless` | `false` ponechá prohlížeč viditelný. |
| `action_delay_ms`, `post_action_settle_ms` | Časování jednotlivých kroků. |
| `addon_points`, `milestone_reminder` | Bodové cíle a připomínky. |
| `ntfy_*` | Volitelné oznámení; výchozí stav je vypnutý. |

Změny v `config.toml` se týkají jen vaší lokální kopie.

## Struktura

```text
Wocabot/
├── WocaBee-Control.exe      # grafické ovládání
├── WocaBee-Runner.exe       # spuštění zvoleného plánu
├── WocaBee-Solver.exe       # řešič cvičení
├── Setup-Browser.cmd        # jednorázové stažení browser runtime
├── Start-WocaBee-Control.cmd
├── config.example.toml       # bezpečná šablona
├── defaults/                 # prázdné šablony místních map
└── runtime/                  # vytvoří se lokálně, není ve verzování
```

## Řešení problémů

- **Chybí Chromium / prohlížeč se nespustí:** spusťte znovu `Setup-Browser.cmd`; ověřte volné místo a internetové připojení.
- **Python nebyl nalezen:** nainstalujte Python 3 z [python.org](https://www.python.org/downloads/) a zopakujte setup.
- **Přihlášení nefunguje:** zkontrolujte vlastní hodnoty v `config.toml`; žádné skutečné údaje nevkládejte do issues ani commitů.
- **Aplikace nenajde data:** nechte `wordlist_file` a `picture_file` na výchozích cestách `runtime/...` a spusťte setup.
- **Chování služby se změnilo:** neprodlužujte bezmyšlenkovitě časování; nejprve ověřte aktuální webové rozhraní a ponechte diagnostiku pouze lokálně.

## Omezení vydání

Spustitelné soubory nejsou digitálně podepsané. Před spuštěním používejte pouze vydání z tohoto repozitáře a podle potřeby ověřte jejich kontrolní součty. Přenosná aplikace byla ověřena základní kontrolou nápovědy řešiče; tento repozitář neobsahuje původní zdrojový strom ani automatizované testy sestavení.

Licence a poděkování jsou v [LICENSE](LICENSE) a [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
