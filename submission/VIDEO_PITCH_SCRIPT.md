# 3-Minute Video Pitch Script: JalDrishti AI
**Speaker:** Bhomesh Razdan (Lead Architect)  
**Track:** 02 Heat and Water | Bharat Builds Tour (WeMakeDevs x AWS)  

### [0:00 - 0:35] The Problem
"Hello judges! I am Bhomesh Razdan. In Indian cities, our relationship with water is broken in two directions: when we need it most during 45°C summer heatwaves, the taps run dry and citizens are at the mercy of the tanker mafia. When it finally rains, city underpasses like Minto Bridge drown buses and paralyze millions of commuters. We built **JalDrishti AI** to solve both."

### [0:35 - 1:30] Solution & Live Walkthrough
"JalDrishti monitors urban stormwater using the Rational Runoff formula ($Q = C \cdot I \cdot A / 360$). In our live dashboard, sensor nodes track depth across key Delhi underpasses, calculating inflow rates and alerting crews before water reaches hazardous thresholds.

Next, our heat engine uses Stull's empirical equation for Wet-Bulb Temperature ($T_w$). When wet-bulb breaches 32°C—where human sweat can no longer evaporate—our system automatically triggers labor cooling advisories and misting shelters.

Finally, for water scarcity, our Fair-Share Tanker Algorithm prioritizes groundwater-depleted settlements, ensuring minimum drinking water allocations and preventing cartel hoarding."

### [1:30 - 2:30] AWS Architecture
"We built JalDrishti on AWS Serverless:
- AWS Lambda and API Gateway serve real-time sensor streams.
- Amazon DynamoDB stores high-velocity underpass depth telemetry.
- AWS Cedar enforces zero-trust policies: citizens can report waterlogging, but only verified ward engineers can trigger municipal dewatering pumps.
- We packaged with AWS Finch and tested locally using AWS SAM CLI and LocalStack."

### [2:30 - 3:00] Conclusion
"With 8 automated unit tests and a zero-dependency server, JalDrishti provides a resilient water defense platform for India's cities. Thank you!"
