# **Log Analysis Script**

## **Hello there! 👋**

Welcome to my **Log Analysis Script** project! This script helps you make sense of those endless lines of server log files by pulling out the useful bits.

Here’s what it does:

* *   Counts how many requests came from each IP address.
* *   Finds the most visited endpoint.
* *   Spots any suspicious activity (like a ton of requests from the same IP in a short time).

* * *

## **Why You’ll Love It ❤️**

* *   **Save Time:** No more manually going through logs.
* *   **Actionable Insights:** See the most active IPs and endpoints instantly.
* *   **Suspicious?** It flags odd behavior to help you take action.

* * *

## **What You’ll Need**

All you need is:

* *   **Python 3.6 or later** installed on your system.
* *   Some libraries like `csv` and `collections` (don’t worry; they’re standard in Python).

If you’re adding more features later, just run this to grab all dependencies:

bash

Copy code

`pip install -r requirements.txt`

* * *

## **How to Use It**

### **Step 1: Clone This Repository**

First, grab the code:

bash

Copy code

`git clone https://github.com/username/repository_name.git cd repository_name`

### **Step 2: Add Your Log File**

Put your web server log file in the same folder, or note the path if it’s somewhere else.

### **Step 3: Run the Script**

Run the script and pass the log file as input:

bash

Copy code

`python log_analysis.py your_log_file.txt`

### **Step 4: Check the Output**

* *   **Terminal Output:** A quick summary of your log analysis.
* *   **CSV File:** A neatly organized file (`analysis_results.csv`) with all the details.

* * *

## **Example in Action**

### **Input Log File** (`sample_log.txt`):

sql

Copy code

`192.168.0.1 - - [01/Dec/2024:10:00:00 +0000] "GET /home HTTP/1.1" 200 1234 192.168.0.2 - - [01/Dec/2024:10:00:01 +0000] "POST /login HTTP/1.1" 200 567 192.168.0.1 - - [01/Dec/2024:10:00:02 +0000] "GET /about HTTP/1.1" 200 432`

### **Output in Terminal:**

yaml

Copy code

`Top 5 IPs by Request Count: 1. 192.168.0.1: 2 requests 2. 192.168.0.2: 1 request  Most Accessed Endpoint: /home  Suspicious IPs: None detected`

### **Output in CSV File:**

IP Address

Request Count

Most Accessed Endpoint

Suspicious Activity

192.168.0.1

2

/home

No

192.168.0.2

1

/login

No

* * *

## **What’s Inside This Project?**

Here’s the file structure so you know where everything lives:

bash

Copy code

`project/ │ ├── log_analysis.py       # The brain of the operation ├── sample_log.txt        # Example log file to get you started ├── requirements.txt      # If you need extra Python packages ├── analysis_results.csv  # Where the script saves its output └── README.md             # The file you’re reading now!`

* * *

## **How Can You Help?** 🤝

Found a bug? Have a cool idea? I’d love to hear from you!

Here’s how you can contribute:

1. 1.  Fork this repository.
1. 2.  Create a new branch with your feature or fix.
1. 3.  Submit a pull request, and let’s make this script even better!

* * *

## **Questions or Feedback?**

Feel free to reach out:

* *   **Author:** Farhan M Hameed
* *   **Email:** farhanmhameed@gmail.com
* *   **GitHub:** [farhanabhi](https://github.com/farhanabhi)

Let’s analyze some logs! 🚀

Paste your rich text content here. You can paste directly from Word or other rich text sources.
