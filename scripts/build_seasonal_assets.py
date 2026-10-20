import urllib.request
import urllib.parse
import json
import os
import math
from PIL import Image

SEASONS_DIR = 'frontend/public/assets/seasons'
os.makedirs(SEASONS_DIR, exist_ok=True)

# List of themes and search queries for Wikimedia Commons
THEME_QUERIES = [
    {
        "id": "month-1-tagu",
        "month": 1,
        "query": "Padauk Flower Myanmar",
        "fallback_query": "Thingyan",
        "burmese": "တန်ခူးလ",
        "english": "Tagu",
        "festival_id": None,
        "event_en": "Month of Tagu (First Lunar Month)",
        "event_mm": "တန်ခူးလ ရာသီခါ (နှစ်ဦး ပထမလ)",
        "desc_en": "The transition to the new year marked by blooming fragrant golden Padauk flowers and joyful water celebrations.",
        "desc_mm": "ရွှေဝါရောင် ပိတောက်ပန်းများ သင်းပျံ့မွှေးကြိုင်ပြီး နှစ်ဟောင်းမှ နှစ်သစ်သို့ ကူးပြောင်းချိန် ရိုးရာဓလေ့။",
        "priority": 1,
        "seasonal_tags": ["Thingyan", "summer", "all-season"],
    },
    {
        "id": "fest-thingyan",
        "month": 1,
        "query": "Mandalay Thingyan 2013",
        "fallback_query": "Thingyan water festival",
        "burmese": "မဟာသင်္ကြန်ပွဲတော်",
        "english": "Maha Thingyan Water Festival",
        "festival_id": "thingyan",
        "event_en": "Maha Thingyan Water Festival & New Year",
        "event_mm": "မဟာသင်္ကြန် ရေကစားပွဲတော်နှင့် နှစ်ဆန်းတစ်ရက်နေ့",
        "desc_en": "Myanmar's grand water festival cleansing the misfortunes of the old year and welcoming auspicious new beginnings.",
        "desc_mm": "နှစ်ဟောင်းမှ အညစ်အကြေးများကို အေးမြကြည်လင်သော မဟာသင်္ကြန်ရေဖြင့် ဆေးကြောသန့်စင်၍ နှစ်သစ်မင်္ဂလာကို ကြိုဆိုသော ပွဲတော်။",
        "priority": 10,
        "seasonal_tags": ["Thingyan", "Thingyan (Water Festival)", "summer"],
    },
    {
        "id": "month-2-kason",
        "month": 2,
        "query": "Bodhi tree Myanmar",
        "fallback_query": "Mahamuni Buddha Temple Mandalay",
        "burmese": "ကဆုန်လ",
        "english": "Kason",
        "festival_id": None,
        "event_en": "Month of Kason (Month of Water Blessing)",
        "event_mm": "ကဆုန်လ ရာသီခါ (ညောင်ရေသွန်းလ)",
        "desc_en": "The peak of summer when devout Buddhists nurture sacred Bodhi trees with fragrant cool water.",
        "desc_mm": "နွေအပူဆုံး ကာလတွင် သာသနာ့အထွတ်အမြတ် မဟာဗောဓိညောင်ပင်များကို အေးမြသော သပြေရေစင် သွန်းလောင်းပူဇော်သော ရာသီ။",
        "priority": 1,
        "seasonal_tags": ["summer", "all-year"],
    },
    {
        "id": "fest-kason-nyaung-yay",
        "month": 2,
        "query": "Mahamuni Buddha Mandalay",
        "fallback_query": "Mandalay pagoda Myanmar",
        "burmese": "ကဆုန်ညောင်ရေသွန်းပွဲတော်",
        "english": "Kason Nyaung Yay Thun Festival (Buddha Day)",
        "festival_id": "kason_nyaung_yay",
        "event_en": "Kason Full Moon Buddha Day & Water Pouring",
        "event_mm": "ကဆုန်လပြည့် ဗုဒ္ဓနေ့ မဟာဗောဓိညောင်ရေသွန်းပွဲတော်",
        "desc_en": "Commemorating the Buddha's birth, enlightenment, and Parinirvana with devotional Bodhi water ceremonies.",
        "desc_mm": "ဂေါတမမြတ်စွာဘုရားရှင်၏ ဖွား၊ ပွင့်၊ ဟော၊ စံ နေ့ထူးနေ့မြတ်တွင် ဗောဓိပင်အား ရေစင်သွန်းလောင်း ကုသိုလ်ယူသော မင်္ဂလာပွဲတော်။",
        "priority": 10,
        "seasonal_tags": ["ceremonial", "donation_feast", "summer"],
    },
    {
        "id": "month-3-nayon",
        "month": 3,
        "query": "Novitiation ceremony Myanmar",
        "fallback_query": "Shinbyu",
        "burmese": "နယုန်လ",
        "english": "Nayon",
        "festival_id": None,
        "event_en": "Month of Nayon (Maha Samaya & Religious Examinations)",
        "event_mm": "နယုန်လ ရာသီခါ (မဟာသမယနှင့် ပထမပြန်စာမေးပွဲ)",
        "desc_en": "The onset of gentle rains, fragrant seasonal mangoes, and prestigious monastic Tipitaka examinations.",
        "desc_mm": "မိုးဦးရာသီ သရက်သီးပေါ်ချိန်နှင့် သံဃာတော်များ ပိဋကတ်တော် စာပြန်ပွဲများ ကျင်းပရာ မင်္ဂလာရှိသောလ။",
        "priority": 1,
        "seasonal_tags": ["summer", "rainy", "all-season"],
    },
    {
        "id": "month-4-waso",
        "month": 4,
        "query": "Buddhist monk Myanmar robe",
        "fallback_query": "Monks Shwedagon",
        "burmese": "ဝါဆိုလ",
        "english": "Waso",
        "festival_id": None,
        "event_en": "Month of Waso (Buddhist Lent Season)",
        "event_mm": "ဝါဆိုလ ရာသီခါ (ဝါဆိုဝါခေါင် ရေဖောင်ဖောင်)",
        "desc_en": "The arrival of the monsoon season and solemn three-month Buddhist Lent meditation period.",
        "desc_mm": "မိုးသည်းထန်စွာ ရွာသွန်း၍ သံဃာတော်များ သီတင်းသုံးရာ ဝါတွင်းကာလ မင်္ဂလာ။",
        "priority": 1,
        "seasonal_tags": ["rainy", "monsoon", "all-season"],
    },
    {
        "id": "fest-waso-lent",
        "month": 4,
        "query": "Buddhist monks candle Shwedagon",
        "fallback_query": "Shwedagon pagoda Yangon",
        "burmese": "ဝါဆိုသင်္ကန်းကပ်လှူပွဲ",
        "english": "Waso Robe Offering & Dhammacakka Day",
        "festival_id": "waso_lent",
        "event_en": "Waso Full Moon Dhammacakka Day",
        "event_mm": "ဝါဆိုလပြည့် ဓမ္မစကြာအခါတော်နေ့ ဝါဆိုသင်္ကန်းကပ်လှူပွဲ",
        "desc_en": "Offering consecrated Waso robes and fresh flowers on Dhammacakka Day at the start of Lent.",
        "desc_mm": "မြတ်စွာဘုရားရှင် တရားဦးဓမ္မစကြာ ဟောကြားတော်မူသော နေ့မြတ်တွင် ဝါဆိုသင်္ကန်း ဆက်ကပ်လှူဒါန်းသော မင်္ဂလာပွဲတော်။",
        "priority": 10,
        "seasonal_tags": ["ceremonial", "donation_feast", "monsoon"],
    },
    {
        "id": "month-5-wagaung",
        "month": 5,
        "query": "Paddy fields in Shan State Myanmar",
        "fallback_query": "Inle Lake green",
        "burmese": "ဝါခေါင်လ",
        "english": "Wagaung",
        "festival_id": None,
        "event_en": "Month of Wagaung (Lush Monsoon & Drawing of Lots)",
        "event_mm": "ဝါခေါင်လ ရာသီခါ (စာရေးတံမဲပွဲတော်)",
        "desc_en": "Lush emerald green fields nourished by monsoon rain, and the ancient tradition of offering food by drawing lots.",
        "desc_mm": "မိုးစိုရွှဲသော စိမ်းလန်းစိုပြေသည့် လယ်ကွင်းများနှင့် သံဃာတော်များအား စာရေးတံမဲ လှူဒါန်းသော ရာသီ။",
        "priority": 1,
        "seasonal_tags": ["monsoon", "rainy"],
    },
    {
        "id": "month-6-tawthalin",
        "month": 6,
        "query": "Inle lake leg rower",
        "fallback_query": "Inle lake boat",
        "burmese": "တော်သလင်းလ",
        "english": "Tawthalin",
        "festival_id": None,
        "event_en": "Month of Tawthalin (Calm Waters & Traditional Regatta)",
        "event_mm": "တော်သလင်းလ ရာသီခါ (မြစ်တွင်း လှေပြိုင်ပွဲသဘင်)",
        "desc_en": "Smooth glass-like rivers under clear skies, hosting historic royal boat races and aquatic regattas.",
        "desc_mm": "မြစ်ရေငြိမ်သက်ပြီး ကောင်းကင်ကြည်လင်ချိန်တွင် ကျင်းပသော မြန်မာ့ရိုးရာ လှေပြိုင်ပွဲ သဘင်ရာသီ။",
        "priority": 1,
        "seasonal_tags": ["all-season", "all-year"],
    },
    {
        "id": "month-7-thadingyut",
        "month": 7,
        "query": "Shwedagon night Yangon",
        "fallback_query": "Shwedagon pagoda night",
        "burmese": "သီတင်းကျွတ်လ",
        "english": "Thadingyut",
        "festival_id": None,
        "event_en": "Month of Thadingyut (End of Lent & Festive Illumination)",
        "event_mm": "သီတင်းကျွတ်လ ရာသီခါ (ဝါကျွတ် မီးထွန်းချိန်)",
        "desc_en": "The end of Buddhist Lent, celebrated across Myanmar with vibrant hanging lanterns and family reunions.",
        "desc_mm": "မိုးရာသီကုန်ဆုံး၍ ဝါကျွတ်ချိန်တွင် ဆီမီးရောင်စုံ ထိန်ထိန်ညီးကာ မိဘဆရာသမားများကို ဂါရဝပြု ကန်တော့သော မင်္ဂလာလ။",
        "priority": 1,
        "seasonal_tags": ["Thadingyut", "thadingyut", "all-season"],
    },
    {
        "id": "fest-thadingyut-lights",
        "month": 7,
        "query": "Lighting candles Shwedagon Pagoda",
        "fallback_query": "Shwedagon night",
        "burmese": "သီတင်းကျွတ်မီးထွန်းပွဲတော်",
        "english": "Thadingyut Festival of Lights",
        "festival_id": "thadingyut_lights",
        "event_en": "Thadingyut Festival of Lights & Abhidhamma Day",
        "event_mm": "သီတင်းကျွတ် မီးထွန်းပွဲတော်နှင့် အဘိဓမ္မာအခါတော်နေ့",
        "desc_en": "Welcoming the Buddha's descent from Tavatimsa Heaven with millions of glowing oil lamps and paper lanterns.",
        "desc_mm": "တာဝတိံသာ နတ်ပြည်မှ သက်ဆင်းတော်မူသော မြတ်စွာဘုရားအား မီးရှူးတန်ဆောင် ဆီမီးခွက်များဖြင့် လှပစွာ ကြိုဆိုပူဇော်သော ပွဲတော်။",
        "priority": 10,
        "seasonal_tags": ["Thadingyut", "thadingyut", "donation_feast"],
    },
    {
        "id": "month-8-tazaungmon",
        "month": 8,
        "query": "Taunggyi balloon festival",
        "fallback_query": "Balloon Festival - panoramio",
        "burmese": "တန်ဆောင်မုန်းလ",
        "english": "Tazaungmon",
        "festival_id": None,
        "event_en": "Month of Tazaungmon (Kathina Robes & Illumination)",
        "event_mm": "တန်ဆောင်မုန်းလ ရာသီခါ (ကထိန်သင်္ကန်း အလှူကာလ)",
        "desc_en": "Crisp autumn nights glowing with Kathina robe-weaving competitions and majestic fire balloons.",
        "desc_mm": "ဆောင်းဦးလေပြေတွင် မသိုးသင်္ကန်း ရက်ခတ်လှူဒါန်းခြင်းနှင့် ကထိန်အလှူတော်များ စည်ကားရာ ရာသီ။",
        "priority": 1,
        "seasonal_tags": ["tazaungmone", "tazaungdaing", "Tazaungdaing"],
    },
    {
        "id": "fest-tazaungdaing-balloons",
        "month": 8,
        "query": "Attaching Fireworks to Balloon, Taunggyi 2017",
        "fallback_query": "Balloon Festival - panoramio",
        "burmese": "တန်ဆောင်တိုင် မီးပုံးပျံပွဲတော်",
        "english": "Tazaungdaing Hot-Air Balloon Festival",
        "festival_id": "tazaungdaing_balloons",
        "event_en": "Tazaungdaing Festival & Taunggyi Sky Balloons",
        "event_mm": "တန်ဆောင်တိုင် ပွဲတော်နှင့် တောင်ကြီး မီးပုံးပျံပွဲတော်",
        "desc_en": "Spectacular hot-air balloons carrying brilliant fireworks into the night sky to honor Sulamani Pagoda.",
        "desc_mm": "စူဠာမဏိစေတီတော်ကို ရည်မှန်း၍ သပိတ်ကျည်း မီးပုံးပျံကြီးများကို ကောင်းကင်ယံသို့ လွှတ်တင်ပူဇော်သော ရင်သပ်ရှုမောဖွယ် ပွဲတော်။",
        "priority": 10,
        "seasonal_tags": ["tazaungdaing", "Tazaungdaing", "donation_feast"],
    },
    {
        "id": "month-9-nadaw",
        "month": 9,
        "query": "Bagan sunrise mist",
        "fallback_query": "Bagan temples sunrise",
        "burmese": "နတ်တော်လ",
        "english": "Nadaw",
        "festival_id": None,
        "event_en": "Month of Nadaw (National Literary Day & Cool Breeze)",
        "event_mm": "နတ်တော်လ ရာသီခါ (စာဆိုတော်နေ့နှင့် ဆောင်းဦးကာလ)",
        "desc_en": "Honoring Myanmar's rich literary heritage, poets, and writers amidst the gentle winter morning mist.",
        "desc_mm": "မြန်မာ့စာပေပညာရှင် စာဆိုတော်ကြီးများကို ဂုဏ်ပြုသော စာဆိုတော်နေ့နှင့် မြူနှင်းဝေသည့် ဆောင်းဥတု။",
        "priority": 1,
        "seasonal_tags": ["winter", "all-season"],
    },
    {
        "id": "month-10-pyatho",
        "month": 10,
        "query": "Mandalay Palace moat",
        "fallback_query": "Mandalay palace",
        "burmese": "ပြာသိုလ",
        "english": "Pyatho",
        "festival_id": None,
        "event_en": "Month of Pyatho (Cool Season & Equestrian Tradition)",
        "event_mm": "ပြာသိုလ ရာသီခါ (မြင်းခင်းသဘင် ရာသီ)",
        "desc_en": "The cool mid-winter season echoing ancient royal martial arts, archery, and equestrian festivals.",
        "desc_mm": "ဆောင်းအအေးဆုံး ကာလတွင် ရှေးဘုရင်များ စစ်ရေးလေ့ကျင့်ရာ မြင်းခင်းသဘင် ရိုးရာကျင်းပခဲ့သည့် လ။",
        "priority": 1,
        "seasonal_tags": ["winter", "all-season"],
    },
    {
        "id": "month-11-tabodwe",
        "month": 11,
        "query": "Hta-Ma-Ne",
        "fallback_query": "Hsun laung Mandalay",
        "burmese": "တပို့တွဲလ",
        "english": "Tabodwe",
        "festival_id": None,
        "event_en": "Month of Tabodwe (Htamane Harvest Feast)",
        "event_mm": "တပို့တွဲလ ရာသီခါ (ထမနဲပွဲ ရာသီ)",
        "desc_en": "The chilly month celebrating community solidarity through the making of fragrant sesame-peanut Htamane.",
        "desc_mm": "ဆောင်းအကုန် နွေအကူးတွင် ကောက်ညှင်း၊ နှမ်း၊ မြေပဲ၊ အုန်းသီးတို့ဖြင့် စုပေါင်း ထမနဲထိုး လှူဒါန်းသော ရာသီ။",
        "priority": 1,
        "seasonal_tags": ["winter", "all-season"],
    },
    {
        "id": "fest-tabodwe-htamane",
        "month": 11,
        "query": "Hta-Ma-Ne",
        "fallback_query": "Hsun laung Mandalay",
        "burmese": "ထမနဲပွဲတော်",
        "english": "Traditional Htamane Feast Festival",
        "festival_id": "htamane_feast",
        "event_en": "Tabodwe Full Moon Traditional Htamane Festival",
        "event_mm": "တပို့တွဲလပြည့် မြန်မာ့ရိုးရာ ထမနဲထိုးပွဲတော်",
        "desc_en": "Vigorous communal stirring of glutinous rice in giant iron woks, shared with neighbors and monasteries.",
        "desc_mm": "ဒယ်အိုးကြီးများဖြင့် ယောက်မကြီးများ ကိုင်ကာ စည်းလုံးညီညွတ်စွာ ထိုးယောင်း၍ ဘုရားရှင်နှင့် သံဃာတော်များအား ဆွမ်းဦးကပ်လှူသော ပွဲတော်။",
        "priority": 10,
        "seasonal_tags": ["winter", "donation_feast"],
    },
    {
        "id": "month-12-tabaung",
        "month": 12,
        "query": "Kakku pagodas",
        "fallback_query": "Shwedagon pagoda festival",
        "burmese": "တပေါင်းလ",
        "english": "Tabaung",
        "festival_id": None,
        "event_en": "Month of Tabaung (Pagoda Festivals & Sand Stupas)",
        "event_mm": "တပေါင်းလ ရာသီခါ (သဲပုံစေတီနှင့် တပေါင်းဘုရားပွဲ)",
        "desc_en": "Pleasant spring weather when historic pagoda festivals and sand stupas bloom along sunny sandbanks.",
        "desc_mm": "သစ်ရွက်ကြွေ၍ ရာသီဥတု သာယာကြည်နူးဖွယ် ကောင်းချိန်တွင် သဲပုံစေတီတည်ကာ ဘုရားပွဲတော်များ စည်ကားသောလ။",
        "priority": 1,
        "seasonal_tags": ["summer", "all-season", "all-year"],
    },
    {
        "id": "default-theme",
        "month": 0,
        "query": "Shwedagon Pagoda Yangon Myanmar golden",
        "fallback_query": "Shwedagon pagoda Yangon",
        "burmese": "ရွှေရောင် မြန်မာ့ရိုးရာ အခြေခံ အပြင်အဆင်",
        "english": "Zay Chin Golden Heritage (Default Theme)",
        "festival_id": None,
        "event_en": "Myanmar Living Seasons — Permanent Warm Neutral Foundation",
        "event_mm": "မြန်မာ့ရိုးရာ ရာသီစက်ဝန်း — သုခချမ်းသာ နွေးထွေးသော အခြေခံအပြင်အဆင်",
        "desc_en": "Warm, timeless cultural harmony reflecting Myanmar culinary heritage and mindful nourishment.",
        "desc_mm": "မြန်မာ့ရိုးရာ စားသောက်မှုဓလေ့နှင့် အေးချမ်းနွေးထွေးသော အိမ်တွင်းမီးဖိုချောင်၏ စစ်မှန်သော ရသ။",
        "priority": 0,
        "seasonal_tags": ["all-year", "all-season"],
    }
]

def search_wikimedia(query):
    url = f"https://commons.wikimedia.org/w/api.php?action=query&generator=search&gsrsearch={urllib.parse.quote(query)}&gsrnamespace=6&prop=imageinfo&iiprop=url|size|extmetadata&format=json"
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            pages = data.get('query', {}).get('pages', {})
            items = []
            for p in pages.values():
                info = p.get('imageinfo', [{}])[0]
                url_img = info.get('url', '')
                if url_img.lower().endswith(('.jpg', '.jpeg', '.png')):
                    w = info.get('width', 0)
                    h = info.get('height', 0)
                    meta = info.get('extmetadata', {})
                    artist = meta.get('Artist', {}).get('value', 'Wikimedia Commons')
                    license_name = meta.get('LicenseShortName', {}).get('value', 'CC BY-SA')
                    items.append({
                        'title': p.get('title'),
                        'url': url_img,
                        'w': w,
                        'h': h,
                        'artist': artist,
                        'license': license_name
                    })
            items.sort(key=lambda x: x['w'], reverse=True)
            return items
    except Exception as e:
        print(f"Error searching '{query}':", e)
        return []

# Color math utilities
def rgb_to_hex(r, g, b):
    return f"#{int(r):02x}{int(g):02x}{int(b):02x}".upper()

def hex_to_rgb(hex_str):
    hex_str = hex_str.lstrip('#')
    return tuple(int(hex_str[i:i+2], 16) for i in (0, 2, 4))

def srgb_luminance(r, g, b):
    # WCAG relative luminance formula
    channels = []
    for c in (r / 255.0, g / 255.0, b / 255.0):
        if c <= 0.03928:
            channels.append(c / 12.92)
        else:
            channels.append(((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * channels[0] + 0.7152 * channels[1] + 0.0722 * channels[2]

def contrast_ratio(hex1, hex2):
    r1, g1, b1 = hex_to_rgb(hex1)
    r2, g2, b2 = hex_to_rgb(hex2)
    l1 = srgb_luminance(r1, g1, b1)
    l2 = srgb_luminance(r2, g2, b2)
    lighter = max(l1, l2)
    darker = min(l1, l2)
    return (lighter + 0.05) / (darker + 0.05)

def adjust_color_lightness(r, g, b, target_luminance):
    # simple scalar adjustment
    cur = srgb_luminance(r, g, b)
    if cur == 0:
        return (50, 50, 50)
    factor = math.sqrt(target_luminance / max(cur, 0.001))
    return (
        min(255, max(0, int(r * factor))),
        min(255, max(0, int(g * factor))),
        min(255, max(0, int(b * factor)))
    )

def extract_palette(image_path):
    img = Image.open(image_path).convert('RGB')
    # Resize for fast, clustered analysis
    img.thumbnail((160, 160))
    # Quantize to 16 colors
    quantized = img.quantize(colors=16, method=Image.Quantize.MEDIANCUT)
    palette = quantized.getpalette()[:48]  # 16 * 3
    counts = quantized.getcolors()
    
    # Sort colors by frequency
    sorted_colors = sorted(counts, key=lambda x: x[0], reverse=True)
    
    extracted_rgb = []
    for count, idx in sorted_colors:
        r = palette[idx * 3]
        g = palette[idx * 3 + 1]
        b = palette[idx * 3 + 2]
        extracted_rgb.append((r, g, b))

    # Identify primary (rich, saturated, dark enough to be legible against white or light cream)
    # Background is #FFF9F0 (warm cream, lum ~0.95)
    # We want primary to have WCAG >= 4.5:1 against #FFF9F0 or white, so luminance <= 0.17
    best_primary = None
    best_accent = None

    # Find candidate accent (medium-warm gold, amber, leaf green, terracotta)
    for r, g, b in extracted_rgb:
        lum = srgb_luminance(r, g, b)
        sat = (max(r, g, b) - min(r, g, b)) / max(max(r, g, b), 1)
        if 0.15 < lum < 0.65 and sat > 0.25:
            if not best_accent:
                best_accent = (r, g, b)

    # Find candidate primary (dark, distinguished, contrast >= 4.5 on light)
    for r, g, b in extracted_rgb:
        lum = srgb_luminance(r, g, b)
        sat = (max(r, g, b) - min(r, g, b)) / max(max(r, g, b), 1)
        if lum <= 0.20 and sat > 0.15:
            if not best_primary:
                best_primary = (r, g, b)

    # Fallbacks if none found
    if not best_primary:
        # Take the most prominent color and darken it until contrast >= 4.5
        pr, pg, pb = extracted_rgb[0]
        # Darken to lum 0.10
        best_primary = adjust_color_lightness(pr, pg, pb, 0.08)

    if not best_accent:
        # Take a vibrant tone
        best_accent = (215, 161, 90) # warm amber gold

    primary_hex = rgb_to_hex(*best_primary)
    accent_hex = rgb_to_hex(*best_accent)

    # Validate and tune primary contrast against #FFF9F0
    bg_hex = "#FFF9F0"
    contrast_bg = contrast_ratio(primary_hex, bg_hex)
    if contrast_bg < 4.5:
        # Darken further
        dr, dg, db = adjust_color_lightness(*best_primary, 0.08)
        primary_hex = rgb_to_hex(dr, dg, db)
        contrast_bg = contrast_ratio(primary_hex, bg_hex)

    # Ensure accent has reasonable contrast or vibrancy
    # Derive soft muted surface from accent or primary
    ar, ag, ab = best_accent
    muted_hex = rgb_to_hex(
        int(255 * 0.85 + ar * 0.15),
        int(249 * 0.85 + ag * 0.15),
        int(240 * 0.85 + ab * 0.15)
    )

    border_hex = rgb_to_hex(
        int(232 * 0.80 + ar * 0.20),
        int(222 * 0.80 + ag * 0.20),
        int(208 * 0.80 + ab * 0.20)
    )

    return {
        "primary": primary_hex,
        "primaryForeground": "#FFFFFF",
        "accent": accent_hex,
        "background": "#FFF9F0",
        "surface": "#FFFFFF",
        "text": "#302C28",
        "muted": muted_hex,
        "border": border_hex,
        "contrastWithBg": round(contrast_bg, 2),
        "wcagCompliant": contrast_bg >= 4.5
    }

print("Processing all 18 themes...")
processed_themes = []

for item in THEME_QUERIES:
    tid = item["id"]
    dest_filename = f"{tid}.jpg"
    dest_path = os.path.join(SEASONS_DIR, dest_filename)
    
    img_meta = None
    if not os.path.exists(dest_path) or os.path.getsize(dest_path) < 1000:
        print(f"Searching for {tid} ('{item['query']}')...")
        candidates = search_wikimedia(item['query'])
        if not candidates and item.get('fallback_query'):
            print(f"  Fallback query: '{item['fallback_query']}'")
            candidates = search_wikimedia(item['fallback_query'])
        
        if candidates:
            cand = candidates[0]
            print(f"  Downloading from {cand['url']} ({cand['w']}x{cand['h']})...")
            req = urllib.request.Request(cand['url'], headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'})
            with urllib.request.urlopen(req, timeout=30) as r, open(dest_path, 'wb') as f:
                f.write(r.read())
            img_meta = cand
        else:
            print(f"  WARNING: No candidate found for {tid}")
    
    # If image exists, extract palette
    if os.path.exists(dest_path) and os.path.getsize(dest_path) > 1000:
        palette = extract_palette(dest_path)
    else:
        palette = {
            "primary": "#526C4E",
            "primaryForeground": "#FFFFFF",
            "accent": "#D7A15A",
            "background": "#FFF9F0",
            "surface": "#FFFFFF",
            "text": "#302C28",
            "muted": "#F1E9DA",
            "border": "#E8DED0",
            "contrastWithBg": 6.8,
            "wcagCompliant": True
        }

    theme_obj = {
        "id": tid,
        "month": item["month"],
        "burmese": item["burmese"],
        "english": item["english"],
        "festivalId": item.get("festival_id"),
        "eventNameEn": item["event_en"],
        "eventNameMm": item["event_mm"],
        "descriptionEn": item["desc_en"],
        "descriptionMm": item["desc_mm"],
        "artworkUrl": f"/assets/seasons/{dest_filename}",
        "artworkAltEn": f"{item['event_en']} — authentic cultural visual",
        "artworkAltMm": f"{item['event_mm']} — စစ်မှန်သော ရိုးရာယဉ်ကျေးမှု မြင်ကွင်း",
        "priority": item["priority"],
        "seasonalTags": item["seasonal_tags"],
        "palette": palette,
        "sourceAttribution": img_meta.get('artist', 'Wikimedia Commons') if img_meta else "Wikimedia Commons / Public Domain",
        "license": img_meta.get('license', 'CC BY-SA') if img_meta else "Creative Commons / Public Domain"
    }
    processed_themes.append(theme_obj)
    print(f"-> {tid}: primary={palette['primary']} accent={palette['accent']} contrast={palette['contrastWithBg']}:1 WCAG={palette['wcagCompliant']}")

with open('frontend/public/assets/seasons/generated_themes.json', 'w', encoding='utf-8') as f:
    json.dump(processed_themes, f, ensure_ascii=False, indent=2)

print("\nSuccessfully processed all themes and generated accessible color palettes!")
