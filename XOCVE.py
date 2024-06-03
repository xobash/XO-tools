import platform
import requests

# Gather system information
system_info = {
    "OS": platform.system(),
    "Release": platform.release(),
    "Version": platform.version(),
    "Machine": platform.machine(),
    "Processor": platform.processor(),
}

print("System Information:")
for key, value in system_info.items():
    print(f"{key}: {value}")

# Search for CVE vulnerabilities
def search_cve_vulnerabilities():
    base_url = "https://cve.circl.lu/api/search"
    params = {"cpe": "cpe:/o:linux:linux_kernel"}
    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        cve_results = response.json()
        if cve_results:
            print("\nCVE Vulnerabilities:")
            for cve in cve_results:
                print(f"- {cve['id']}: {cve['summary']}")
        else:
            print("\nNo CVE vulnerabilities found.")
    else:
        print("Error:", response.status_code)

search_cve_vulnerabilities()