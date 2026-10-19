import requests

urls = [
    ('/', ['Zay Chin', 'ဈေးခြင်း']),
    ('/recipes', ['Recipe Explorer', 'ဟင်းချက်နည်း', 'Zay Chin']),
    ('/recipes/R0001', ['Butter Rice', 'ထောပတ်', 'Zay Chin', 'ဈေးခြင်း']),
    ('/planner', ['Planner', 'အစားအစာ', 'Zay Chin']),
    ('/grocery-list', ['Grocery', 'ဈေးဝယ်', 'Zay Chin']),
    ('/markets', ['Market', 'ဈေး', 'Zay Chin'])
]

print("=" * 65)
print("VERIFYING LIVE NEXT.JS FRONTEND (http://127.0.0.1:3001):")
print("=" * 65)

frontend_ok = True
for path, expected_list in urls:
    url = f"http://127.0.0.1:3001{path}"
    try:
        r = requests.get(url, timeout=10)
        status = r.status_code
        has_text = any(exp in r.text for exp in expected_list)
        print(f"  GET {path:20} -> Status: {status} | Matches {expected_list}: {has_text}")
        if status != 200 or not has_text:
            frontend_ok = False
    except Exception as e:
        print(f"  GET {path:20} -> FAILED: {e}")
        frontend_ok = False

print("\n" + "=" * 65)
print("VERIFYING LIVE FASTAPI BACKEND (http://127.0.0.1:8001):")
print("=" * 65)

api_tests = [
    ("/health", "healthy"),
    ("/api/v1/recipes?page=1&page_size=2", "R0001"),
    ("/api/v1/recipes/R0001", "Butter Rice"),
    ("/api/v1/recipes/categories", "Rice dishes"),
    ("/api/v1/markets", "MKT_YGN_CSO")
]

backend_ok = True
for path, expected in api_tests:
    url = f"http://127.0.0.1:8001{path}"
    try:
        r = requests.get(url, timeout=10)
        status = r.status_code
        has_text = expected in r.text
        print(f"  GET {path:35} -> Status: {status} | Matches '{expected}': {has_text}")
        if status != 200 or not has_text:
            backend_ok = False
    except Exception as e:
        print(f"  GET {path:35} -> FAILED: {e}")
        backend_ok = False

print("\n" + "=" * 65)
if frontend_ok and backend_ok:
    print("ALL INTEGRATION VERIFICATION CHECKS PASSED WITH 100% SUCCESS!")
else:
    print("WARNING: Some endpoints did not return 200 OK.")
print("=" * 65)
