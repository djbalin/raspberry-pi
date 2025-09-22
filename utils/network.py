import requests

from .logging import LOG

API_ENDPOINT = "https://air-quality-backend-production.up.railway.app/readings"

def send_sensor_data(tvoc_ppb, eco2_ppm, temp_c, aqi, pressure_hPa, humidity_pct):
    """Send sensor reading to the API endpoint"""
    
    # Create the data dictionary
    reading_data = {
        "tvoc_ppb": tvoc_ppb,
        "eco2_ppm": eco2_ppm,
        "temp_c": temp_c,
        "aqi": aqi,
        "pressure_hPa": pressure_hPa,
        "humidity_pct": humidity_pct
    }
    
    try:
        response = requests.post(
            API_ENDPOINT,
            json=reading_data,
            headers={"Content-Type": "application/json"},
            timeout=10
        )
        
        if response.status_code == 201:
            LOG(f"✓ Data sent successfully: {response.json()}")
            return True
        else:
            LOG(f"✗ Failed to send data. Status: {response.status_code}, Response: {response.text}")
            return False
            
    except requests.exceptions.Timeout:
        LOG("✗ Request timed out")
        return False
    except requests.exceptions.ConnectionError:
        LOG("✗ Connection error - check internet connection")
        return False
    except requests.exceptions.RequestException as e:
        LOG(f"✗ Request failed: {e}")
        return False
