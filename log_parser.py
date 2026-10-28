# IT Log Parser - Real World Project
# Purpose: Read a simulated Windows Event Log and extract only the Error/Critical entries.

def parse_logs(log_file_path):
    print(f"--- Starting Log Parse for: {log_file_path} ---")
    
    error_count = 0
    
    try:
        # Open the log file in read mode
        with open(log_file_path, 'r') as file:
            for line in file:
                # Logic: If the line contains "ERROR" or "CRITICAL", we want to extract it
                if "ERROR" in line or "CRITICAL" in line:
                    print(f"ALERT FOUND: {line.strip()}")
                    error_count += 1
                    
        print(f"--- Scan Complete. Total Errors Found: {error_count} ---")
        
    except FileNotFoundError:
        print(f"Error: The file {log_file_path} was not found.")

# This is where the script starts running
if __name__ == "__main__":
    # We will create a fake log file to test this later
    parse_logs("system_logs.txt")
