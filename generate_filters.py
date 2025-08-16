import json

categories = {
    "🎨 Filter Media": 109,
    "🤖 AI / Generatif": 107,
    "📷 Lens / Kamera": 107,
    "🔒 Konten / Keamanan": 107,
    "🧭 Navigasi / Marketplace": 107,
    "🛠️ Editing Lanjutan": 107
}

full_filters = {}

for cat, count in categories.items():
    full_filters[cat] = []
    for i in range(1, count + 1):
        full_filters[cat].append({
            "name": f"Filter {i}",
            "icon": cat[0],
            "subfilters": [f"Subfilter {i}.1", f"Subfilter {i}.2"]
        })

# Simpan JSON lengkap
with open('filters_644_full.json', 'w', encoding='utf-8') as f:
    json.dump(full_filters, f, ensure_ascii=False, indent=2)

print("File filters_644_full.json berhasil dibuat dengan 644 filter.")
