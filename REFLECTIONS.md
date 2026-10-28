

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
### Reflection 5: The human check on `extracted.json`

I did the critique pass myself (no classmate) on posting 15. I compared the model's
output with the source text and found a real error: with the first setting
(`MAX_CHARS = 1500`) the model only saw the company presentation and returned an
empty list, while the real skills (RTL, SerDes, LVDS...) were in the part that was
cut. After I raised the limit to 5000, the list was correct.

This is human-in-the-loop because a person reads the model's raw output next to the
original text and decides if it is right. The model cannot check itself: it does not
know what it did not see.

It has to be done on `extracted.json` and not on `kpi.json` because `extracted.json`
keeps the detail of each posting, so I can compare each list with its source. In
`kpi.json` everything is already averaged into counts, so an error like an empty
list or a hallucinated skill is hidden inside a percentage and cannot be traced back.

<!--
FR :
Réflexion 5 : la vérification humaine sur extracted.json

J'ai fait la passe de critique moi-même (pas de camarade) sur l'offre 15. J'ai
comparé la sortie du modèle avec le texte d'origine et j'ai trouvé une vraie erreur :
avec le premier réglage (MAX_CHARS = 1500), le modèle ne voyait que la présentation
de l'entreprise et renvoyait une liste vide, alors que les vraies compétences (RTL,
SerDes, LVDS...) étaient dans la partie coupée. Après avoir monté la limite à 5000,
la liste était correcte.

C'est du human-in-the-loop car une personne lit la sortie brute du modèle à côté du
texte d'origine et décide si elle est juste. Le modèle ne peut pas se vérifier
lui-même : il ne sait pas ce qu'il n'a pas vu.

Cela doit se faire sur extracted.json et non sur kpi.json car extracted.json garde
le détail de chaque offre, donc je peux comparer chaque liste à sa source. Dans
kpi.json tout est déjà agrégé en comptages : une erreur comme une liste vide ou une
compétence inventée est cachée dans un pourcentage et on ne peut plus remonter à
la source.
-->
## Stage 4 – KPI definition

### Reflection 6 (part 1): The skill I would track first

If I built this dashboard for the ENSIM curriculum committee, I would track
**Docker** first. Python is probably already taught everywhere, so a KPI on Python
would not help the committee decide anything. Docker appears in DevOps and data
engineering jobs, and it is a skill students can learn in a short module, so the
committee can act on the result: teach more of it, or not.

Honest note: I had already seen in my extraction results that Python appears in many
of my postings, so I did not choose my skill completely blind. I chose Docker
because of the decision it supports, not because of a number.

<!--
FR :
Réflexion 6 (partie 1) : la compétence que je suivrais en premier

Si je construisais ce tableau de bord pour le comité pédagogique de l'ENSIM, je
suivrais **Docker** en premier. Python est probablement déjà enseigné partout, donc
un KPI sur Python n'aiderait pas le comité à décider quoi que ce soit. Docker
apparaît dans les métiers DevOps et data engineering, et c'est une compétence que
les étudiants peuvent apprendre dans un court module : le comité peut donc agir sur
le résultat (en enseigner plus, ou non).

Note honnête : j'avais déjà vu dans mes résultats d'extraction que Python apparaît
dans beaucoup de mes offres, donc je n'ai pas choisi ma compétence complètement à
l'aveugle. J'ai choisi Docker pour la décision qu'il permet, pas à cause d'un chiffre.
-->
