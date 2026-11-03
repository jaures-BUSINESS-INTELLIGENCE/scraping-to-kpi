# Scraping to KPI

From raw job postings to one defensible number: a small pipeline that uses a local
LLM to extract skills from job postings, checks the result, computes KPIs and
publishes only the totals as a web page.

**Live dashboard:** https://jaures-business-intelligence.github.io/scraping-to-kpi/

## The pipeline

1. **Acquisition** – 15 job postings from a private CSV (never published). A small
   demo (`scrape_demo.py`) also shows how to check `robots.txt` before reading a web
   page.
2. **Structuring** – `extract_skills.py` asks a local LLM (Ollama, `qwen3:8b`) to list
   the concrete tools and skills in each posting.
3. **Data quality** – I checked the output by hand (spelling variants, empty lists,
   duplicates). See `REFLECTIONS.md`.
4. **KPI** – `compute_kpi.py` computes two KPIs: the share of postings mentioning
   `docker`, and the share mentioning any cloud provider.
5. **Publishing** – only `docs/data/kpi.json` (totals and skill counts) is published.
6. **Visualization** – `docs/index.html` shows the KPIs and a skills chart (Chart.js).

## What is published and what is not

| File | Published? | Why |
|---|---|---|
| `docs/data/kpi.json` | Yes | Only totals, no posting can be identified |
| `data/jobs_sample.csv` | No (in `.gitignore`) | Postings come from sites that forbid redistribution |
| `data/extracted.json` | No (in `.gitignore`) | Contains job titles and company names |

## How to run (locally)

1. Install Python, then `pip install requests beautifulsoup4`.
2. Install [Ollama](https://ollama.com) and run `ollama pull qwen3:8b`.
3. Put your postings in `data/jobs_sample.csv` (columns `title`, `company`,
   `description`).
4. Run:
   python scripts/extract_skills.py 15
   python scripts/compute_kpi.py


5. Commit and push only `docs/data/kpi.json`.

## Limits

- Only 15 postings, taken from the first rows of a file (not a random sample), and
  one posting appears twice.
- The model can miss skills or add items that are not tools, and it can spell one
  skill in several ways.
- Both KPIs rest on 2 postings out of 15: they show a direction, not a conclusion.

<!--
FR :
Scraping to KPI : des offres d'emploi brutes à un chiffre défendable. Un petit
pipeline qui utilise une IA locale pour extraire les compétences des offres,
vérifie le résultat, calcule des KPI et ne publie que les totaux sur une page web.
Seul docs/data/kpi.json est publié : les offres et le fichier extrait restent sur mon
ordinateur (.gitignore). Limites : 15 offres seulement, échantillon non aléatoire,
un doublon, erreurs possibles du modèle, KPI reposant sur 2 offres sur 15.
-->
