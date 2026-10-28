

## Stage 1 – Acquisition

### Reflection 1: Why is a silent `robots.txt` failure worse than a visible crash?

If the `robots.txt` check fails silently, the script keeps running as if
everything was fine. Nobody knows that the permission was never really checked.
If the script crashes with a visible error, we see the problem and we fix it.

Silence is dangerous because the check has only one job: respect the rules
before acting. If it fails without a warning, it has failed its only job, and
nobody can tell. Later, a reader of the report or the dashboard will believe the
data was collected within the site's rules, but we cannot be sure.

This breaks provenance: we can no longer say where the data comes from or
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
## Stage 3 – Data quality

### Reflection 4: Same skill, two spellings

I expected the model to write the same skill in different ways across separate
calls, mostly with different capital letters. I have to be honest: I had already
seen this in my first 3-posting test, so this is not a blind prediction.

Yes, I found instances in my own `extracted.json`:
- `Computer vision` (posting 1) and `computer vision` (posting 2)
- `Generative AI` and `generative AI`
- `Image technology` and `image technology`

Left unfixed, one real skill is split into two entries when we count, so the
top-skills ranking would be wrong. I also found other problems: 5 postings out of
15 have an empty skill list (possibly because the script only reads the first 1,500
characters), two postings seem to be duplicates, and some items are not really tools
(`Nuclear physics`, `Branding`).

<!--
FR :
Réflexion 4 : la même compétence écrite de deux façons

Je m'attendais à ce que le modèle écrive la même compétence de plusieurs façons
selon les appels, surtout avec des majuscules différentes. Je dois être honnête : je
l'avais déjà vu lors de mon premier test sur 3 offres, ce n'est donc pas une vraie
prédiction à l'aveugle.

Oui, j'ai trouvé des cas dans mon extracted.json :
- Computer vision (offre 1) et computer vision (offre 2)
- Generative AI et generative AI
- Image technology et image technology

Si on ne les corrige pas, une vraie compétence est coupée en deux entrées au
comptage, donc le classement des compétences serait faux. J'ai aussi trouvé d'autres
problèmes : 5 offres sur 15 ont une liste vide (peut-être parce que le script ne lit
que les 1 500 premiers caractères), deux offres semblent être des doublons, et
certains éléments ne sont pas vraiment des outils (Nuclear physics, Branding).
-->
