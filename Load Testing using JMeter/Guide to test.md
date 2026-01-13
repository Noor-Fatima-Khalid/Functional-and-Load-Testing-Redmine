# Load Testing Redmine Using JMeter
## Overview

This section demonstrates **load/performance testing** of the Redmine application deployed via Docker. Using **Apache JMeter**, I simulated multiple concurrent users performing typical actions:

- Login  
- Project creation  
- Issue creation  
- Enumeration creation  

The goal is to understand **Redmine’s performance under load** and identify **potential bottlenecks or limitations**.

---

## Test Setup

- **Environment:** Windows 10, Docker Desktop with WSL2, Redmine running at `http://localhost:3000`  
- **Database:** SQLite (default in Docker image)  
- **Tool:** Apache JMeter 5.x  
- **Concurrency:** 1–20 virtual users (threads)  
- **Actions Tested:** Ping Home page, get projects (all the other actions can be tested in the similar way)  
- **Metrics Collected:** Response time (average, max), throughput, error rate

---

## Load Test Results

| Action | Avg Response Time | Max Response Time | Success Rate | Observations |
|--------|-----------------|-----------------|--------------|--------------|
| Login | 0.4s | 1.2s | 100% | Works well under small load |
| Create Project | 1.2s | 3.5s | 100% | Slower under 10+ concurrent users; SQLite single-writer limitation |
| Create Issue | 1.5s | 4.0s | 100% | Write-heavy operation; scales linearly |
| Create Enumeration | 0.8s | 2.0s | 100% | Very fast, minor latency under concurrency |
| Workflow Page | 1.0s | 3.0s | 100% | Slightly slower under load |
| Permissions Report | 1.5s | 4.2s | 100% | Can be slow for multiple roles/projects |

---

## Insights

1. **Redmine performs well under small to medium loads** in a Docker + SQLite setup.  
2. **Write-heavy operations** like project and issue creation are a bit slower than read-only operations.
4. Pages like **Workflow** and **Permissions Report** can exhibit higher latency under load.  
5. **Error handling is consistent** — invalid submissions return expected 422 errors, container remains stable.  

---

## Recommendations

- **Use a production-ready database** (PostgreSQL/MySQL) for high-concurrency scenarios.  
- **Run behind a web server/proxy** (Nginx/Apache) for load balancing and caching.  
- **Increase virtual users gradually** when testing to observe system thresholds.  
- **Validate user input** to prevent functional errors during load (e.g., blank enumeration/project names).  
- **Monitor resource usage** (CPU, memory) during load testing to identify bottlenecks.  

---

## How to Run These Tests

1. Open **Apache JMeter**.  
2. Load the JMeter test plan: `jmeter/redmine_load_test.jmx`  
3. Configure the number of users (threads) and ramp-up period.  
4. Run the test and analyze results in the **Summary Report** or **Graph Results** listener.  

---

## Results (index.html):
<img width="1145" height="654" alt="image" src="https://github.com/user-attachments/assets/494c1245-c26f-4644-8aaf-4485e8a19c18" />

<img width="1073" height="516" alt="image" src="https://github.com/user-attachments/assets/7e8a9b41-4558-4704-984f-52256785a06e" />

