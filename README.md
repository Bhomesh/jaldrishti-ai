# 💧 JalDrishti AI (जल दृष्टि)
### Urban Flood Sentinel, Heatwave Wet-Bulb Predictor & Water Fair-Share Logistics on AWS

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Hackathon](https://img.shields.io/badge/Bharat%20Builds%20Tour-WeMakeDevs%20x%20AWS-orange.svg)](https://www.wemakedevs.org/aws/env)
[![Track](https://img.shields.io/badge/Track-02%20Heat%20and%20Water-blue.svg)](https://www.wemakedevs.org/aws/env#tracks)
[![Lead Architect](https://img.shields.io/badge/Lead%20Architect-Bhomesh%20Razdan-purple.svg)](https://github.com/Bhomesh)

---

## Overview
**JalDrishti AI** is a resilient climate adaptation and hydrological defense platform built on AWS for the **Bharat Builds Tour: Environmental Hacks**.

It addresses India's urban hydrological challenges:
1. **Urban Underpass Submergence Engine:** Monitors stormwater depths using the Rational Hydrological Runoff Method ($Q = C \cdot I \cdot A / 360$).
2. **Physiological Heat Index & Wet-Bulb Engine:** Uses Stull's equation to predict dangerous thermal thresholds ($T_w > 32^\circ\text{C}$).
3. **Fair-Share Tanker Logistics:** Distributes municipal water tankers equitably based on groundwater depletion.
4. **AWS Cedar Zero-Trust Authorization:** Decouples permissions between citizens, ward engineers, and municipal hydrologists.

---

## Quickstart (Zero Dependencies)
```bash
git clone https://github.com/Bhomesh/jaldrishti-ai.git
cd jaldrishti-ai

# Run test suite
python3 -m unittest discover tests

# Launch web command center
python3 -m src.server 8081
```
Open **[http://localhost:8081](http://localhost:8081)**.

---

## Architecture & AWS Stack
* **AWS Open Source:** AWS Cedar (RBAC), AWS SAM CLI, LocalStack, AWS Finch.
* **AWS Cloud Services:** AWS Lambda, Amazon API Gateway, Amazon DynamoDB, Amazon EventBridge, Amazon SNS, Amazon Bedrock.

---

## Author
* **Lead Architect:** **Bhomesh Razdan** (`bhomeshrazdan@gmail.com`)
