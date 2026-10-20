import urllib.request
import urllib.parse
import json
import os

os.makedirs('frontend/public/assets/seasons', exist_ok=True)

queries = {
    'tagu': 'Thingyan',
    'kason': 'Mahamuni Mandalay',
    'nayon': 'Novitiation ceremony Myanmar',
    'waso': 'Buddhist monk Myanmar',
    'wagaung': 'Paddy field Myanmar',
    'tawthalin': 'Inle lake leg rower',
    'thadingyut': 'Shwedagon night',
    'tazaungmon': 'Balloon Taunggyi',
    'nadaw': 'Bagan morning mist',
    'pyatho': 'Mandalay Palace',
    'tabodwe': 'Hta-Ma-Ne',
    'tabaung': 'Kakku Pagodas'
}

downloaded = {}

for month_key, q in queries.items():
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(q)}&gsrnamespace=6&prop=imageinfo&iiprop=url|size|extmetadata&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'ZayChinCulturalApp/1.0 (contact@zaychin.mm)'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            best_img = None
            for p in pages.values():
                info = p.get('imageinfo', [{}])[0]
                url_img = info.get('url', '')
                if url_img.lower().endswith(('.jpg', '.jpeg', '.png')):
                    w = info.get('width', 0)
                    h = info.get('height', 0)
                    if w >= 800 and (not best_img or w > best_img['w']):
                        meta = info.get('extmetadata', {})
                        best_img = {
                            'title': p.get('title'),
                            'url': url_img,
                            'w': w,
                            'h': h,
                            'artist': meta.get('Artist', {}).get('value', 'Wikimedia Commons'),
                            'license': meta.get('LicenseShortName', {}).get('value', 'Creative Commons / Public Domain'),
                            'credit': meta.get('Credit', {}).get('value', 'Wikimedia Commons')
                        }
            if best_img:
                dest_filename = f"{month_key}.jpg"
                dest_path = os.path.join('frontend/public/assets/seasons', dest_filename)
                print(f"Downloading {month_key} from {best_img['url']} to {dest_path}...")
                img_req = urllib.request.Request(best_img['url'], headers={'User-Agent': 'ZayChinCulturalApp/1.0 (contact@zaychin.mm)'})
                with urllib.request.urlopen(img_req, timeout=25) as img_resp, open(dest_path, 'wb') as out_f:
                    out_f.write(img_resp.read())
                best_img['local_path'] = f"/assets/seasons/{dest_filename}"
                downloaded[month_key] = best_img
                print(f"  -> Successfully saved {month_key} ({best_img['w']}x{best_img['h']})")
            else:
                print(f"  -> No high-res image found for {month_key}")
    except Exception as e:
        print(f"Error querying {month_key}:", e)

# Also let's ensure festival overrides like thingyan_festival, thadingyut_festival, tazaungdaing_festival have dedicated photos
festivals = {
    'festival_thingyan': 'Mandalay Thingyan 2013.JPG',
    'festival_thadingyut': 'Shwedagon pagoda night',
    'festival_tazaungdaing': 'Balloon Festival - panoramio.jpg',
    'festival_htamane': 'Hta-Ma-Ne.jpg',
    'festival_waso': 'Buddhist monks candles'
}

with open('frontend/public/assets/seasons/metadata.json', 'w', encoding='utf-8') as f:
    json.dump(downloaded, f, ensure_ascii=False, indent=2)

print(f"\nDone! Downloaded {len(downloaded)} seasonal images.")
