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

Toto vydání obsahuje kompletní portable runtime včetně Chromiumu. Dva jeho velké soubory jsou uložené přes Git LFS, proto nepoužívejte obyčejný GitHub ZIP — nemusí obsahovat LFS data.

1. Nainstalujte [Git LFS](https://git-lfs.com/) a v terminálu spusťte `git lfs install`.
2. Stáhněte celý projekt: `git clone https://github.com/krko2n/Wocabot.git`.
3. V jeho složce spusťte `git lfs pull` a počkejte na stažení všech souborů.
4. Otevřete `config.toml`, nahraďte `GENERIC_USERNAME` a `GENERIC_PASSWORD` vlastními údaji a soubor uložte.
5. Spusťte `Start-WocaBee-Control.cmd`.

`Setup-Browser.cmd` zůstává jako záložní varianta pro lokální obnovení browser runtime, pokud jste jej přes Git LFS nestáhli.

## Konfigurace a soukromí

`config.toml` je veřejná výchozí konfigurace. Jediné nahrazené hodnoty jsou `username` a `password`, které obsahují generické zástupné řetězce; notifikační hodnoty jsou prázdné.

Distribuce záměrně obsahuje kompletní portable obsah média včetně diagnostiky, naučených map, browser runtime a historických záložních EXE. Po doplnění vlastních údajů proto `config.toml` nikdy znovu necommitujte ani nesdílejte.

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
├── ms-playwright/           # přibalený Chromium runtime (část je v Git LFS)
├── Start-WocaBee-Control.cmd
├── config.toml               # veřejná konfigurace s generickými údaji
├── diagnostics/              # přibalená diagnostika z portable média
├── wordlist.json             # přibalená mapa slov
└── picturelist.json          # přibalená mapa obrázků
```

## Řešení problémů

- **Chybí Chromium / prohlížeč se nespustí:** proveďte `git lfs pull`; případně spusťte `Setup-Browser.cmd` a ověřte volné místo i internetové připojení.
- **Python nebyl nalezen:** nainstalujte Python 3 z [python.org](https://www.python.org/downloads/) a zopakujte setup.
- **Přihlášení nefunguje:** zkontrolujte vlastní hodnoty v `config.toml`; žádné skutečné údaje nevkládejte do issues ani commitů.
- **Aplikace nenajde data:** ponechte `wordlist_file` a `picture_file` na výchozích cestách z `config.toml`.
- **Chování služby se změnilo:** neprodlužujte bezmyšlenkovitě časování; nejprve ověřte aktuální webové rozhraní a ponechte diagnostiku pouze lokálně.

## Omezení vydání

Spustitelné soubory nejsou digitálně podepsané. Před spuštěním používejte pouze vydání z tohoto repozitáře a podle potřeby ověřte jejich kontrolní součty. Přenosná aplikace byla ověřena základní kontrolou nápovědy řešiče; tento repozitář neobsahuje původní zdrojový strom ani automatizované testy sestavení.

Licence a poděkování jsou v [LICENSE](LICENSE) a [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
