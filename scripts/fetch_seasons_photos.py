import urllib.request
import urllib.parse
import json
import os

os.makedirs('frontend/public/assets/seasons', exist_ok=True)

queries = {
    'tagu': 'Thingyan water festival Myanmar',
    'kason': 'Mahamuni Buddha temple Mandalay',
    'nayon': 'Novitiation ceremony Myanmar OR Shinbyu',
    'waso': 'Buddhist monks Myanmar robes candlelight',
    'wagaung': 'Monsoon paddy field Myanmar OR green Shan hills',
    'tawthalin': 'Inle lake leg rower boat racing Myanmar',
    'thadingyut': 'Shwedagon pagoda night lighting candles oil lamps',
    'tazaungmon': 'Taunggyi hot air balloon festival Myanmar',
    'nadaw': 'Bagan sunset temples mist morning',
    'pyatho': 'Mandalay royal palace moat sunset',
    'tabodwe': 'Hta-Ma-Ne OR Htamane Myanmar',
    'tabaung': 'Kakku pagodas Shan State Myanmar'
}

print("Searching Wikimedia Commons for authentic cultural photography...")
results = {}
for key, q in queries.items():
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&prop=imageinfo&iiprop=url|size|extmetadata&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'ZayChinCulturalApp/1.0 (contact@zaychin.mm)'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            items = []
            for p in pages.values():
                info = p.get('imageinfo', [{}])[0]
                url_img = info.get('url', '')
                ext_meta = info.get('extmetadata', {})
                artist = ext_meta.get('Artist', {}).get('value', 'Wikimedia Commons')
                license_name = ext_meta.get('LicenseShortName', {}).get('value', 'CC BY-SA / Public Domain')
                if url_img.lower().endswith(('.jpg', '.jpeg', '.png')) and info.get('width', 0) >= 800:
                    items.append({
                        'title': p.get('title'),
                        'url': url_img,
                        'w': info.get('width'),
                        'h': info.get('height'),
                        'artist': artist,
                        'license': license_name
                    })
            results[key] = items
            print(f"[{key}] Found {len(items)} matching candidates for '{q}'")
    except Exception as e:
        print(f"[{key}] Error:", e)
        results[key] = []

with open('seasonal_photo_candidates.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
print("Saved candidates to seasonal_photo_candidates.json")
