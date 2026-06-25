# Final Forecasting Summary

## Overall Performance
- Total Questions: 331
- Accuracy: 15.7%
- Brier Skill Score: -0.018
- Time-Weighted Score: -1537.52

## Key Lessons Learned

### 1. Specific name/location questions are extremely difficult
- Many questions asked for specific people, cities, towns that were impossible to predict without direct evidence
- Examples: Ben White, Menashe Zalka, Qom, Jezzine, Meknes, Beit Awwa
- Spread probability broadly when guessing specific answers

### 2. Never go above 55% without absolute certainty
- High confidence on wrong answers was the biggest TW-score killer
- Ali Khamenei at 60% (truth: Larijani), Aston Martin at 50% (truth: McLaren)
- ADNOC at 55% (truth: Emirates Global Aluminium)

### 3. Surprising answers are common - expect the unexpected
- Pope Leo: Expected for Jerusalem worship, but it was Macron
- Latvia drone: Expected Russia, was Ukraine
- Abu Dhabi company: Expected ADNOC, was Emirates Global Aluminium
- Paris app: Expected Telegram, was Snapchat
- Armed group: Called them "Ansar Allah" instead of "Houthis" (same group, different naming)

### 4. Direct article search >> mcp__forecast__search_news
- The search tool returned "No articles found" for most queries
- Bash/Python searching of articles/*.jsonl was far more reliable

### 5. Time-weighted scoring penalizes wrong early predictions heavily
- Making predictions early earns more days of weight
- But wrong early predictions cost more too
- Best strategy: predict early with moderate confidence, update as evidence comes in

### 6. Iran-US-Israel war dominated the question set
- Many questions about the "Twelve Day War" (June 2025) and second conflict (Feb-March 2026)
- Gulf states (UAE, Bahrain, Kuwait, Saudi) all targeted by Iran
- Hezbollah, Houthis, Iraqi militias all active

### 7. Name matching matters
- "Ansar Allah" vs "Houthis" caused a loss (same group)
- "Turkiye" vs "Turkey" was accepted
- Always use the most commonly used English name

## Best Predictions
- Australia visitor ban: Iran (correct, +49.74)
- Iran school accusation (+63.85)
- Trump Middle East (+42.87)
- Kosovo playoff: Turkey (correct, +28.71)
- Kuwait power plant (correct, +15.72)

## Worst Predictions  
- Meknes/Eritrea hosting (-36.94)
- Senegal AFCON appeal (-28.74)
- Latvia drone/Russia (-23.79)
- Germany Hormuz (-22.38)
- Chuck Norris Hawaii (-21.54)
