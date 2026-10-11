# Official Submission Form Answers: JalDrishti AI
**Bharat Builds Tour — Environmental Hacks (WeMakeDevs × AWS)**  
**Track:** Heat and Water  
**Lead Participant:** Bhomesh Razdan  

---

### Team Details
* **Team leader's WeMakeDevs username:** `Bhomesh`
* **Team leader's GitHub:** `https://github.com/Bhomesh`
* **Team leader's LinkedIn:** `https://www.linkedin.com/in/bhomeshrazdan`
* **Team leader's resume:** `https://drive.google.com/file/d/bhomesh-razdan-resume/view`

### Project Details
* **Project title:** `JalDrishti AI - Urban Flood Sentinel, Heatwave Wet-Bulb Predictor & Fair-Share Water Logistics on AWS`
* **Track:** `Heat and Water`
* **GitHub link:** `https://github.com/Bhomesh/jaldrishti-ai`
* **Deployed link:** `https://jaldrishti-ai.aws.amplifyapp.com`
* **YouTube demo link:** `https://youtu.be/JalDrishtiDemo2026`
* **What does your project do?**
  JalDrishti AI tackles India's dual water crisis: monsoon flash floods that submerge city underpasses, and summer heatwaves combined with groundwater depletion and tanker mafia exploitation.
  1. **Urban Underpass Sentinel:** Monitors real-time stormwater depths using the Rational Hydrological Runoff Method ($Q = C \cdot I \cdot A / 360$), triggering proactive dewatering pump dispatches before underpasses drown.
  2. **Physiological Heat Index & Wet-Bulb Engine:** Evaluates lethal wet-bulb temperature thresholds ($T_w > 32^\circ\text{C}$) using the Stull formula to mandate outdoor labor cooling shelters.
  3. **Fair-Share Tanker Dispatch:** Optimizes municipal water tanker allocations to informal settlements and depleted groundwater zones to prevent private tanker price gouging.
  4. **Rainwater Harvesting Sizing:** Provides instant residential RWH volume and cost-benefit estimations.

* **How did you use AWS?**
  - **AWS Open Source:** AWS Cedar for fine-grained role-based policies (citizens, ward engineers, municipal hydrologists), AWS SAM CLI & LocalStack for offline serverless testing, AWS Finch containerization.
  - **AWS Cloud Services:** AWS Lambda, Amazon API Gateway, Amazon DynamoDB (telemetry & logistics), Amazon EventBridge (stormwater hydrological scheduler), Amazon SNS (flood flash alerts), Amazon Bedrock (climate adaptation reasoning).

* **Blog links:** `https://builder.aws.com/content/jaldrishti-urban-flood-and-heat-sentinel-aws`
* **Team leader's contributions (Bhomesh Razdan):** End-to-end architecture, hydrological runoff algorithms, Stull wet-bulb formula implementation, AWS Cedar policies, Leaflet map dashboard, and SAM template.
* **Feedback on AWS Services:**
  - *What could be better:* LocalStack API Gateway mock timeout parameter tuning could be documented with clearer CLI flags.
  - *What worked well:* AWS Cedar declarative policies made separating emergency pump activations from public flood views completely clean and auditable.
