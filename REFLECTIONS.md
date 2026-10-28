## Stage 1 – Acquisition

### Reflection 1: Why is a silent `robots.txt` failure worse than a visible crash?

If the `robots.txt` check fails silently, the script keeps running as if
everything was fine. Nobody knows that the permission was never really checked.
If the script crashes with a visible error, we see the problem and we fix it.

Silence is dangerous because the check has only one job: respect the rules
before acting. If it fails without a warning, it has failed its only job, and
nobody can tell. Later, a reader of the report or the dashboard will believe the
data was collected within the site's rules, but we cannot be sure.

This breaks provenance : we can no longer say where the data comes from or
how it was obtained. That is why my script uses `raise_for_status()` and
`raise SystemExit(...)`: when something goes wrong, it must stop loudly.

<!--
FR :
Réflexion 1 : pourquoi un échec silencieux de robots.txt est-il pire qu'un plantage visible ?

Si la vérification de robots.txt échoue en silence, le script continue comme si
tout allait bien. Personne ne sait que la permission n'a jamais vraiment été
vérifiée. Si le script plante avec une erreur visible, on voit le problème et on
le corrige.

Le silence est dangereux car cette vérification n'a qu'une seule mission :
respecter les règles avant d'agir. Si elle échoue sans avertissement, elle a
échoué dans sa seule mission, et personne ne peut le savoir. Plus tard, un lecteur
du rapport ou du tableau de bord croira que les données ont été collectées dans
le respect des règles du site, mais on ne peut pas en être sûr.

Cela casse la provenance  : on ne peut plus dire d'où viennent les données ni
comment elles ont été obtenues. C'est pour cela que mon script utilise
raise_for_status() et raise SystemExit(...) : quand quelque chose ne va pas, il
doit s'arrêter bruyamment.
-->
