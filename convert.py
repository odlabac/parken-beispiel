import json


with open('fines_with_locations.csv', newline="\n") as f:
    lines = f.readlines()
    fields = lines[0][:-1].split(";")
    fields[0] = "ID"
    doc = []
    for l in lines[1:20]:
        l = l[:-1]
        rec = {}
        p = l.split(";")
        for idx, f in enumerate(fields):
            if f in ("lat", "lon"):
                rec[f] = float(p[idx])
            else:
                rec[f] = p[idx]

        doc.append(
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [rec['lon'],rec['lat']]
                },
                'properties': {
                    'title': 'Tat!',
                    'description': 'Böse Dinge geschahen hier!'
                }
            },
        )

result = {
    'type': 'FeatureCollection',
    'features' : doc
}

print(json.dumps(result))
