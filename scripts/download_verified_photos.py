import urllib.request
import os
import time

DEST_DIR = 'frontend/public/assets/seasons'
os.makedirs(DEST_DIR, exist_ok=True)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
}

# Verified Wikimedia Commons photos for each month and festival
PHOTO_URLS = {
    # 1. Tagu: Blooming golden Padauk flowers
    'month-1-tagu': 'https://upload.wikimedia.org/wikipedia/commons/d/d2/Padauk_Flower.jpg',
    # Festival Thingyan: Traditional Thingyan Water Festival
    'fest-thingyan': 'https://upload.wikimedia.org/wikipedia/commons/1/13/Bagan_era_painting_of_Thingyan.jpg',
    # 2. Kason: Sacred Mahamuni Buddha / Bodhi tree veneration
    'month-2-kason': 'https://upload.wikimedia.org/wikipedia/commons/3/3d/Mahamuni_Image.JPG',
    'fest-kason-nyaung-yay': 'https://upload.wikimedia.org/wikipedia/commons/3/3d/Mahamuni_Image.JPG',
    # 3. Nayon: Traditional Novitiation ceremony (Shinbyu) & Buddhist exams
    'month-3-nayon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Myanmar_Traditional_novitiation_march.JPG/1280px-Myanmar_Traditional_novitiation_march.JPG',
    # 4. Waso: Buddhist monks & Waso robes / candles
    'month-4-waso': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Shwedagon_Pagoda_2017.jpg/1280px-Shwedagon_Pagoda_2017.jpg',
    'fest-waso-lent': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Lighting_Festival.jpg/1280px-Lighting_Festival.jpg',
    # 5. Wagaung: Lush monsoon landscape & Inle emerald waters
    'month-5-wagaung': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Inle_Lake_%28Myanmar%29.jpg/1280px-Inle_Lake_%28Myanmar%29.jpg',
    # 6. Tawthalin: Regatta & legendary leg-rowers on calm waters
    'month-6-tawthalin': 'https://upload.wikimedia.org/wikipedia/commons/thumb/d/d8/Inle_Lake_%28Myanmar%29.jpg/1280px-Inle_Lake_%28Myanmar%29.jpg',
    # 7. Thadingyut: Radiant Festival of Lights & evening illumination
    'month-7-thadingyut': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Lighting_Festival.jpg/1280px-Lighting_Festival.jpg',
    'fest-thadingyut-lights': 'https://upload.wikimedia.org/wikipedia/commons/thumb/7/7d/Lighting_Festival.jpg/1280px-Lighting_Festival.jpg',
    # 8. Tazaungmon: Taunggyi Hot Air Balloons & Tazaungdaing
    'month-8-tazaungmon': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Attaching_Fireworks_to_Balloon%2C_Taunggyi_2017.jpg/1280px-Attaching_Fireworks_to_Balloon%2C_Taunggyi_2017.jpg',
    'fest-tazaungdaing-balloons': 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ae/Attaching_Fireworks_to_Balloon%2C_Taunggyi_2017.jpg/1280px-Attaching_Fireworks_to_Balloon%2C_Taunggyi_2017.jpg',
    # 9. Nadaw: Serene Bagan temples in morning winter mist (Literary season)
    'month-9-nadaw': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Bagan%2C_Burma.jpg/1280px-Bagan%2C_Burma.jpg',
    # 10. Pyatho: Royal Mandalay Palace & traditional heritage
    'month-10-pyatho': 'https://upload.wikimedia.org/wikipedia/commons/thumb/6/61/Mandalay_Palace%2C_Myanmar.jpg/1280px-Mandalay_Palace%2C_Myanmar.jpg',
    # 11. Tabodwe: Traditional Htamane sticky rice making
    'month-11-tabodwe': 'https://upload.wikimedia.org/wikipedia/commons/6/60/Hta-Ma-Ne.jpg',
    'fest-tabodwe-htamane': 'https://upload.wikimedia.org/wikipedia/commons/6/60/Hta-Ma-Ne.jpg',
    # 12. Tabaung: Historic Pagoda Fair & glorious stupas
    'month-12-tabaung': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Shwedagon_Pagoda_2017.jpg/1280px-Shwedagon_Pagoda_2017.jpg',
    # Default Theme: Golden Shwedagon Pagoda
    'default-theme': 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c4/Shwedagon_Pagoda_2017.jpg/1280px-Shwedagon_Pagoda_2017.jpg',
}

print(f"Downloading {len(PHOTO_URLS)} verified photos from Wikimedia Commons...")

for key, url in PHOTO_URLS.items():
    dest_file = os.path.join(DEST_DIR, f"{key}.jpg")
    clean_url = url.split('?')[0]
    print(f"[{key}] Downloading from {clean_url}...")
    try:
        req = urllib.request.Request(clean_url, headers=HEADERS)
        with urllib.request.urlopen(req, timeout=20) as resp, open(dest_file, 'wb') as out_f:
            out_f.write(resp.read())
        sz = os.path.getsize(dest_file)
        print(f"  -> Saved {dest_file} ({sz:,} bytes)")
        time.sleep(1.0) # Respectful delay between requests
    except Exception as e:
        print(f"  -> Error downloading {key}: {e}")

print("Download process completed!")
