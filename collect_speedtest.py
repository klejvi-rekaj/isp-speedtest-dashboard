import speedtest
import pandas as pd
from datetime import datetime
import os
import time

def run_speedtest():
    s = speedtest.Speedtest()
    s.get_best_server()
    download = s.download() / 1_000_000  
    upload = s.upload() / 1_000_000
    ping = s.results.ping
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return {"timestamp": timestamp, "download_speed_mbps": round(download, 2), "upload_speed_mbps": round(upload, 2), "ping_ms": round(ping, 2)}

def save_result(result, filename="speedtest_data.csv"):
    df = pd.DataFrame([result])
    if os.path.exists(filename):
        df.to_csv(filename, mode='a', header=False, index=False)
    else:
        df.to_csv(filename, mode='w', header=True, index=False)

if __name__ == "__main__":
    num_tests = 20  
    wait_seconds = 3  

    print(f"Running {num_tests} speed tests, one every {wait_seconds} seconds...")

    for i in range(num_tests):
        print(f"Test {i+1} of {num_tests}...")
        result = run_speedtest()
        save_result(result)
        print(f"Saved: {result}")
        if i < num_tests - 1:
            time.sleep(wait_seconds)

    print("Done! All speed tests saved to speedtest_data.csv")

