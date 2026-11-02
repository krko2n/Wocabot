# Wocabot – úplný návod pro Windows

Toto je hotová přenositelná aplikace pro Windows. Nemusíš programovat ani znát GitHub. Stačí jednou stáhnout správnou kompletní verzi, vyplnit svoje přihlašovací údaje a spustit ovládání.

> Používej jen svůj vlastní účet a jen způsobem, který ti škola a WocaBee dovolují. Wocabot není oficiální produkt WocaBee.

## Než začneš

Potřebuješ:

- Windows 10 nebo 11;
- stabilní internet při stahování;
- alespoň **3 GB** volného místa na disku;
- svůj účet WocaBee;
- asi 10–20 minut na první nastavení.

## Důležité: nestahuj obyčejný ZIP

V repozitáři je přibalený velký Chromium prohlížeč. Dva jeho soubory používají Git LFS, takže tlačítko **Code → Download ZIP** na GitHubu nemusí stáhnout funkční kompletní aplikaci.

Použij jednu z následujících metod. Pro začátečníky je doporučená metoda A.

## A. Doporučeno: GitHub Desktop

### 1. Nainstaluj GitHub Desktop

1. Otevři [desktop.github.com](https://desktop.github.com/).
2. Klikni na **Download for Windows** a spusť stažený instalátor.
3. Po instalaci otevři GitHub Desktop. Přihlášení do GitHub účtu je doporučené, ale pro stažení veřejného repozitáře není nutné.

### 2. Nainstaluj Git LFS

1. Otevři [stránku poslední verze Git LFS](https://github.com/git-lfs/git-lfs/releases/latest).
2. V části Assets stáhni `git-lfs-windows-amd64.exe` pro běžný 64bitový Windows.
3. Spusť instalátor a dokonči instalaci.
4. Zavři a znovu otevři GitHub Desktop.

Git LFS je nutný jen proto, aby se stáhly dva velké soubory prohlížeče. Bez něj aplikace nemusí spustit Chromium.

### 3. Stáhni Wocabot

1. V GitHub Desktop klikni nahoře na **File → Clone repository…**.
2. Otevři záložku **URL**.
3. Do **Repository URL** vlož:

   ```text
   https://github.com/krko2n/Wocabot.git
   ```

4. Do **Local path** vyber jednoduché umístění, například `C:\Wocabot`. Nepoužívej složku, kterou automaticky synchronizuje OneDrive.
5. Klikni na **Clone** a počkej na dokončení.
6. V GitHub Desktop zvol **Repository → Open in Command Prompt**.
7. Do otevřeného černého okna vlož tento příkaz a potvrď Enterem:

   ```bat
   git lfs pull
   ```

8. Počkej, až se stáhnou velké soubory. Okno nezavírej, dokud příkaz neskončí bez chyby.

## B. Alternativa: příkazy ke zkopírování

Pokud máš nainstalovaný Git pro Windows a Git LFS, otevři **Příkazový řádek** a vlož postupně tyto příkazy:

```bat
git lfs install
cd /d C:\
git clone https://github.com/krko2n/Wocabot.git
cd Wocabot
git lfs pull
```

Git pro Windows je dostupný na [git-scm.com/download/win](https://git-scm.com/download/win). Instalaci nech na výchozích hodnotách.

## Nastavení přihlašovacích údajů

Po úspěšném stažení otevři složku `C:\Wocabot` (nebo složku, kterou sis vybral). Najdi soubor `config.toml`.

1. Klikni na něj pravým tlačítkem → **Otevřít v programu → Poznámkový blok**.
2. Najdi tyto dva řádky:

   ```toml
   username = "GENERIC_USERNAME"
   password = "GENERIC_PASSWORD"
   ```

3. Nahraď pouze text mezi uvozovkami svým uživatelským jménem a heslem.
4. Uvozovky ponech. Výsledek má mít tento tvar:

   ```toml
   username = "tvoje_jmeno"
   password = "tvoje_heslo"
   ```

5. V Poznámkovém bloku klikni na **Soubor → Uložit** a okno zavři.

Nikomu neposílej svůj upravený `config.toml`, screenshot jeho obsahu ani ho necommituj do GitHubu. Veřejná verze obsahuje pouze generické údaje.

## Spuštění

1. Ve složce projektu dvakrát klikni na `Start-WocaBee-Control.cmd`.
2. Otevře se `WocaBee-Control.exe`.
3. Zkontroluj nastavení v ovládacím okně a spusť jen to, čemu rozumíš.
4. Během práce prohlížeč nezavírej a nespouštěj druhou kopii aplikace současně.

Pokud Windows zobrazí bezpečnostní varování, nejprve se ujisti, že jsi aplikaci skutečně stáhl z tohoto repozitáře. EXE soubory nejsou digitálně podepsané.

## Co znamenají hlavní soubory

| Soubor/složka | K čemu je |
| --- | --- |
| `Start-WocaBee-Control.cmd` | Běžný start aplikace. |
| `WocaBee-Control.exe` | Grafické ovládání. |
| `WocaBee-Runner.exe` | Spouštěč vybraného plánu. Nespouštěj jej samostatně, pokud nevíš, co bude dělat. |
| `WocaBee-Solver.exe` | Vlastní řešič. |
| `config.toml` | Tvoje nastavení a přihlašovací údaje. |
| `ms-playwright` | Přibalený Chromium potřebný pro chod aplikace. |
| `diagnostics` | Starší diagnostické výstupy z portable sestavy. |
| `wordlist.json`, `picturelist.json` | Přibalené mapy používané aplikací. |

## Běžná nastavení v `config.toml`

| Název | Význam |
| --- | --- |
| `class_index`, `package_index` | Výběr třídy a balíčku. Číslování začíná od nuly. |
| `headless = false` | Prohlížeč zůstane viditelný; doporučené pro kontrolu, co aplikace dělá. |
| `action_delay_ms` | Zpoždění mezi kroky. Nezmenšuj bezdůvodně. |
| `addon_points`, `milestone_reminder` | Bodové cíle a připomínky. |
| `ntfy_*` | Volitelné notifikace; výchozí hodnoty jsou prázdné. |

Když si nejsi jistý, nech výchozí hodnoty a změň jen uživatelské jméno a heslo.

## Aktualizace aplikace

1. Ukonči Wocabot.
2. Otevři GitHub Desktop a vyber repozitář Wocabot.
3. Klikni na **Fetch origin** a potom na **Pull origin**.
4. Zvol **Repository → Open in Command Prompt**.
5. Spusť:

   ```bat
   git lfs pull
   ```

Před aktualizací si pro jistotu zkopíruj svůj `config.toml` někam mimo složku projektu. Po aktualizaci ověř, že v něm zůstaly tvoje údaje.

## Problémy a řešení

### V prohlížeči se neotevře Chromium / chybí soubor

1. Zavři aplikaci.
2. Otevři příkazový řádek ve složce Wocabot.
3. Spusť `git lfs pull`.
4. Pokud to nepomůže, spusť `Setup-Browser.cmd`. Ten vyžaduje Python 3 a internet.

### Otevřel jsem soubor prohlížeče a vidím jen pár řádků textu

Git LFS se nestáhl. Nejde o funkční prohlížeč, ale o LFS ukazatel. Nainstaluj Git LFS a spusť `git lfs pull` ve složce projektu.

### Přihlášení nefunguje

- Zkontroluj překlepy v `username` a `password` v `config.toml`.
- Uvozovky musí zůstat.
- Ulož soubor před spuštěním aplikace.
- Nezkoušej heslo posílat do GitHub issues, Discordu ani screenshotů.

### Windows blokuje spuštění

EXE soubory nejsou digitálně podepsané. Ověř, že repozitář a poslední commit odpovídají [krko2n/Wocabot](https://github.com/krko2n/Wocabot), a rozhodni se až potom, zda souboru důvěřuješ.

### Po aktualizaci zmizela moje konfigurace

Vrať svoji zálohu `config.toml`. Protože tento soubor obsahuje heslo, nedávej ho do veřejného GitHubu.

## Obsah a licence

Repozitář obsahuje kompletní portable sestavu včetně browser runtime, diagnostiky, historických záloh EXE a přibalených map. Zdrojový strom této konkrétní portable sestavy nebyl na původním médiu k dispozici.

Licence a oznámení třetích stran jsou v [LICENSE](LICENSE) a [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md). Git LFS ukládá velké soubory přes ukazatele v Gitu a data stáhne při klonování s LFS. [Vysvětlení GitHubu](https://docs.github.com/en/repositories/working-with-files/managing-large-files/about-git-large-file-storage)
