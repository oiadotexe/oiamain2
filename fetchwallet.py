import requests
import time

TOKEN_MINT_ADDRESS = "OIAAIOEXE_MINT_ADDRESS"
SOLSCAN_API_URL = "https://api.solscan.io/account/tokenholders"
HEADERS = {
    "Accept": "application/json",
    "User-Agent": "OIADOTEXE-Explorer/0.1"
}

def fetch_token_holders(mint_address):
    print(f"[INFO] Fetching holders for token mint address: {mint_address}")
    params = {"mint": mint_address, "limit": 100}
    try:
        response = requests.get(SOLSCAN_API_URL, headers=HEADERS, params=params)
        if response.status_code == 200:
            return response.json().get("data", [])
        else:
            print(f"[ERROR] Failed to fetch data: {response.status_code} - {response.text}")
            return []
    except Exception as e:
        print(f"[ERROR] Exception occurred: {e}")
        return []

def parse_wallets(token_holders):
    print("[INFO] Parsing wallet addresses...")
    wallets = []
    for holder in token_holders:
        wallet_address = holder.get("owner")
        balance = holder.get("amount")
        if wallet_address and balance:
            wallets.append({"wallet": wallet_address, "balance": balance})
    return wallets

def generate_project_hint(wallets):
    print("[INFO] Generating project hint...")
    selected_wallets = wallets[:3]
    return "||".join([wallet["wallet"][:10] for wallet in selected_wallets])

if __name__ == "__main__":
    print("=== OIADOTEXE Holder Fetcher ===")
    time.sleep(1)
    token_holders = fetch_token_holders(TOKEN_MINT_ADDRESS)
    
    if token_holders:
        wallets = parse_wallets(token_holders)
        print(f"[SUCCESS] Found {len(wallets)} holders!")
        
        hint = generate_project_hint(wallets)
        print(f"[HINT] Next project clue: {hint}")
    else:
        print("[INFO] No holders found or API returned an error.")
