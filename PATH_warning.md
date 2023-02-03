Pokud se při instalaci pipenv vyskytly chyby s proměnnou PATH jako následující:
```
WARNING: The script virtualenv-clone.exe is installed in 'C:\Users\matus\AppData\Roaming\Python\Python311\Scripts' which is not on PATH.
````
Je potřebné přidat **cestu** v apostrofech do systémové proměněné PATH.
## Úprava proměnné PATH
1. Klikněte pravým tlačítkem myši na tlačítko Start.
2. Z kontextové nabídky vyberte „Systém“.
3. Klikněte na „Upřesnit nastavení systému“.
4. Přejděte na kartu „Upřesnit“.
5. Klikněte na „Proměnné prostředí…“.
6. Klikněte na proměnnou s názvem „Path“ v systémových proměnných a klikněte na „Upravit…“.
7. Klikněte na „Nový“.
8. Zadejte cestu z Warning-u. (Ve vzorovém případě `C:\Users\matus\AppData\Roaming\Python\Python311\Scripts`)
Po úpravě je nutný reset počítače.

