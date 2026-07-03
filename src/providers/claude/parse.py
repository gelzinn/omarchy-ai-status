import json

def parse(raw_output):
    if raw_output == "NO_TOKEN":
        return {"provider": "Claude", "metrics": []}
    
    if raw_output == "OFFLINE" or not raw_output.startswith("{"):
        return {"provider": "Claude", "metrics": [{"type": "generic", "percentage": 0, "detail": "API unreachable"}]}
    
    try:
        data = json.loads(raw_output)
        fraction = float(data.get("remainingFraction", 1))
        pct = round((1 - fraction) * 100)
        reset = data.get("resetTime", "Unknown")
        
        return {
            "provider": "Claude",
            "metrics": [{
                "type": "generic",
                "percentage": pct,
                "detail": f"Resets at {reset}"
            }]
        }
    except Exception:
        return {"provider": "Claude", "metrics": []}
