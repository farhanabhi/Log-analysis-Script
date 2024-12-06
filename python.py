import csv
from collections import defaultdict, Counter
LOG_FILE = "sample.log"
CSV_OUTPUT_FILE = "log_analysis_results.csv"
FAILED_LOGIN_THRESHOLD = 10

def parse_log_file(log_file):
    log_entries = []
    with open(log_file, 'r') as file:
        for line in file:
            parts = line.split()
            if len(parts) > 6:
                ip = parts[0]
                endpoint = parts[6]
                status_code = parts[8]
                log_entries.append((ip, endpoint, status_code, line))
    return log_entries

def count_requests_per_ip(log_entries):
    ip_counts = Counter(entry[0] for entry in log_entries)
    return ip_counts.most_common()

def find_most_frequent_endpoint(log_entries)
    endpoint_counts = Counter(entry[1] for entry in log_entries)
    return endpoint_counts.most_common(1)[0]

def detect_suspicious_activity(log_entries)
    failed_logins = defaultdict(int)
    for ip, _, status_code, line in log_entries:
        if status_code == '401' or "Invalid credentials" in line:
            failed_logins[ip] += 1
    return [(ip, count) for ip, count in failed_logins.items() if count > FAILED_LOGIN_THRESHOLD]

def save_results_to_csv(ip_counts, frequent_endpoint, suspicious_ips):
    with open(CSV_OUTPUT_FILE, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        writer.writerow(["Requests per IP"])
        writer.writerow(["IP Address", "Request Count"])
        writer.writerows(ip_counts)

        writer.writerow([])
        writer.writerow(["Most Accessed Endpoint"])
        writer.writerow(["Endpoint", "Access Count"])
        writer.writerow(frequent_endpoint)

        writer.writerow([])
        writer.writerow(["Suspicious Activity"])
        writer.writerow(["IP Address", "Failed Login Count"])
        writer.writerows(suspicious_ips)

def display_results(ip_counts, frequent_endpoint, suspicious_ips):
    print("IP Address           Request Count")
    for ip, count in ip_counts:
        print(f"{ip:<20}{count}")
    
    print("\nMost Frequently Accessed Endpoint:")
    print(f"{frequent_endpoint[0]} (Accessed {frequent_endpoint[1]} times)")
    
    print("\nSuspicious Activity Detected:")
    print("IP Address           Failed Login Attempts")
    for ip, count in suspicious_ips:
        print(f"{ip:<20}{count}")

def main():
    log_entries = parse_log_file(LOG_FILE)

    ip_counts = count_requests_per_ip(log_entries)
    frequent_endpoint = find_most_frequent_endpoint(log_entries)
    suspicious_ips = detect_suspicious_activity(log_entries)

    display_results(ip_counts, frequent_endpoint, suspicious_ips)
    save_results_to_csv(ip_counts, frequent_endpoint, suspicious_ips)
    print(f"\nResults saved to {CSV_OUTPUT_FILE}")

if __name__ == "__main__":
    main()
