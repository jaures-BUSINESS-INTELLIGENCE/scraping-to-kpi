import json, os, time
from collections import Counter

# Le KPI est une CONSTRUCTION : on choisit la compétence qu'on mesure.
TARGET_SKILL = "docker"

def load_extracted(path="data/extracted.json"):
    # On lit le fichier produit par extract_skills.py
    with open(path, encoding="utf-8") as f:
        return json.load(f)["postings"]

def clean_skills(skills):
    # Nettoyage : on ignore les majuscules et on garde chaque compétence UNE seule
    seen = {}
    for s in skills:
        s = s.strip()
        key = s.lower()
        if key and key not in seen:
            seen[key] = s  # on garde la première écriture rencontrée
    return list(seen.values())

def compute_kpi(postings, target_skill=TARGET_SKILL):
    n = len(postings)
    cleaned = [clean_skills(p.get("required_skills", [])) for p in postings]

    # Offres qui mentionnent la compétence cible 
    matching = [
        skills for skills in cleaned
        if any(target_skill.lower() in s.lower() for s in skills)
    ]

    # Classement : combien d'offres mentionnent chaque compétence
    counts = Counter()
    display = {}
    for skills in cleaned:
        for s in skills:
            counts[s.lower()] += 1
            display.setdefault(s.lower(), s)

    return {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "kpi_label": f"% of postings mentioning '{target_skill}'",
        "kpi_value": round(len(matching) / n, 3) if n else 0.0,
        "n_postings_analyzed": n,
        "n_matching": len(matching),
        "top_skills": [{"skill": display[k], "count": c} for k, c in counts.most_common(10)],
        "avg_skills_per_posting": round(sum(len(s) for s in cleaned) / n, 2) if n else 0.0,
    }

def main():
    postings = load_extracted()
    kpi = compute_kpi(postings)
    print(json.dumps(kpi, indent=2, ensure_ascii=False))
    os.makedirs("docs/data", exist_ok=True)  # crée le dossier s'il n'existe pas
    with open("docs/data/kpi.json", "w", encoding="utf-8") as f:
        json.dump(kpi, f, indent=2, ensure_ascii=False)
    print("\nWrote docs/data/kpi.json")

if __name__ == "__main__":
    main()
