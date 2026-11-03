

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

I did the critique pass myself on posting 15. I compared the model's
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

J'ai fait la passe de critique moi-même  sur l'offre 15. J'ai
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
### Reflection 6 (part 2): Which number would I trust?

With the default skill, `python`, the KPI is 60% (9 postings out of 15). With my
own choice, `docker`, it is 13.3% (2 postings out of 15). Only the tracked skill
changed, so the KPI really depends on what I chose to measure .

I would not use either number alone to tell the committee "students should learn
X". The Python number is more stable (it rests on 9 postings), but it does not help
the committee decide, because Python is probably already taught. The Docker number
is the useful one for a decision, but it rests on only 2 postings: one posting more
or less changes it by about 7 points.

There are other problems: my 15 postings are simply the first lines of the file,
not a random sample, one posting is counted twice, and the model can miss a skill
that is only mentioned briefly. To support a real decision I would need many more
postings, picked at random, without duplicates, and a human check of a part of
the extracted skills.

<!--
FR :
Réflexion 6 (partie 2) : à quel chiffre faire confiance ?

Avec la compétence par défaut, python, le KPI est de 60 % (9 offres sur 15). Avec
mon propre choix, docker, il est de 13,3 % (2 offres sur 15). Seule la compétence
suivie a changé, donc le KPI dépend vraiment de ce que j'ai choisi de mesurer .

Je n'utiliserais aucun des deux chiffres seul pour dire au comité « les étudiants
devraient apprendre X ». Le chiffre de Python est plus stable (il repose sur 9
offres), mais il n'aide pas le comité à décider, car Python est probablement déjà
enseigné. Le chiffre de Docker est celui qui est utile pour une décision, mais il
repose sur seulement 2 offres : une offre de plus ou de moins le change d'environ 7
points.

Il y a d'autres problèmes : mes 15 offres sont simplement les premières lignes du
fichier, pas un échantillon aléatoire, une offre est comptée deux fois, et le modèle
peut manquer une compétence mentionnée seulement brièvement. Pour appuyer une vraie
décision, il me faudrait beaucoup plus d'offres, tirées au hasard, sans doublons,
et une vérification humaine d'une partie des compétences extraites.
-->
## Stage 5 – Storage and what is safe to publish

### Reflection 7: Can someone rebuild my postings from `kpi.json`?

No, a classmate could not find which postings I used, or which company they come
from. `kpi.json` only contains totals: the KPI value, the number of postings
analyzed, the number of matching postings, the average number of skills, and a
top-10 list of skill names with their counts. It has no job titles, no company
names, no links, no descriptions and no emails.

To guarantee this, I had to leave out of the KPI every field that identifies a
posting: `title`, `company` and the text itself. This was a deliberate design
choice and not luck: `compute_kpi()` builds a new dictionary with only totals, and it
only reads the skills lists, so it never copies a title or a company. Also, the
`.gitignore` keeps `jobs_sample.csv` and `extracted.json` (which has titles and
companies) on my computer only. I have to be honest that this design came with the
TD, but I now understand why each choice matters.

One small risk remains: with only 15 postings, a rare skill with a count of 2 (for
example `Diffusion architectures`) could point to one specific job ad. With more
postings, or by showing only skills that appear in several postings, this risk
would be lower.

<!--
FR :
Réflexion 7 : peut-on reconstituer mes offres à partir de kpi.json ?

Non, un camarade ne pourrait pas retrouver quelles offres j'ai utilisées, ni de
quelle entreprise elles viennent. kpi.json ne contient que des totaux : la valeur du
KPI, le nombre d'offres analysées, le nombre d'offres qui correspondent, la moyenne
de compétences, et un top 10 de noms de compétences avec leurs comptes. Il n'y a
aucun titre d'offre, aucun nom d'entreprise, aucun lien, aucune description et aucun
email.

Pour le garantir, j'ai dû laisser de côté dans le KPI tous les champs qui identifient
une offre : title, company et le texte lui-même. C'était un choix de conception
volontaire et pas de la chance : compute_kpi() construit un nouveau dictionnaire avec
seulement des totaux, et il ne lit que les listes de compétences, donc il ne copie
jamais un titre ou une entreprise. De plus, le .gitignore garde jobs_sample.csv et
extracted.json (qui contient titres et entreprises) uniquement sur mon ordinateur.
Je dois être honnête : cette conception venait du TD, mais je comprends maintenant
pourquoi chaque choix compte.

Un petit risque demeure : avec seulement 15 offres, une compétence rare avec un
compte de 2 (par exemple Diffusion architectures) pourrait désigner une annonce
précise. Avec plus d'offres, ou en n'affichant que les compétences présentes dans
plusieurs offres, ce risque serait plus faible.
-->
## Stage 6 – Visualization

### Reflection 8: Who is this dashboard really for?

As first built, the dashboard was for me: the title "Scraping to
KPI lab" and the sentence about LLM extraction and `compute_kpi.py` describe the
method, not the result. A curriculum committee would not know what the number means,
and nothing on the page warned that it rests on only 15 postings, taken from the
first rows of a file and not chosen at random.

So the framing did not match the audience I chose in Stage 4. I changed the title to
a question the committee cares about ("What skills do job postings ask for?") and I
replaced the one-line description with this sentence: it says who the page is for,
what the number measures, and that it is a small, non-random sample showing a
direction, not a final conclusion.

<!--
FR :
Réflexion 8 : à qui s'adresse vraiment ce tableau de bord ?

Tel que je l'avais construit, le tableau de bord s'adressait à moi  : le titre « Scraping to KPI lab » et la phrase sur l'extraction par LLM
et compute_kpi.py décrivent la méthode, pas le résultat. Un comité pédagogique ne
saurait pas ce que le chiffre veut dire, et rien sur la page ne prévenait qu'il
repose sur seulement 15 offres, prises dans les premières lignes d'un fichier et non
choisies au hasard.

Le cadrage ne correspondait donc pas au public que j'avais choisi à l'étape 4. J'ai
changé le titre en une question qui intéresse le comité (« Quelles compétences les
offres d'emploi demandent-elles ? ») et j'ai remplacé la description d'une ligne par
cette phrase : elle dit à qui s'adresse la page, ce que mesure le chiffre, et qu'il
s'agit d'un petit échantillon non aléatoire qui montre une tendance, pas une
conclusion définitive.
-->
