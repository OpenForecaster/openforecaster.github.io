# FINAL SIMULATION RESULTS - All 330 Questions Resolved

## Date: 2026-03-28 (Simulation Complete)

## Final Scores
- **Total Predictions**: 330 (all resolved)
- **Accuracy**: 13.0%
- **Brier Skill Score**: 0.008
- **Time-Weighted Score**: -2984.23

## Final Batch Results (March 27-28)

### March 27 (4 questions):
1. **177801 (Armed group southern Israel)**: Truth=Houthis | My prob: 0.05 | Brier +0.05 | ✅ ON-MARKET
2. **320138 (Paris bank recruitment app)**: Truth=Snapchat | My prob: 0.03 | Brier +0.02 | ✅ ON-MARKET (tiny)
3. **560679 (Abu Dhabi site damage company)**: Truth=Emirates Global Aluminium | My prob: 0.03 | Brier -0.01 | ✅ ON-MARKET (tiny)
4. **795856 (Lebanese town journalists killed)**: Truth=Jezzine | OFF-MARKET | Brier -0.02 | ❌

### March 28 (3 questions):
5. **144312 (Jerusalem worship guarantee)**: Truth=Emmanuel Macron | My prob: 0.06 | Brier +0.05 | ✅ ON-MARKET
6. **26340 (Iran raid kills plant worker)**: Truth=Kuwait | My prob: 0.05 | Brier +0.02 | ✅ ON-MARKET
7. **267975 (Sudan state aid disruption)**: Truth=White Nile State | OFF-MARKET | Brier -0.04 | ❌

**Final batch: 5/7 on-market (71%) — massive improvement over ~20% historical rate!**

## Key Patterns & Lessons Learned

### Overall Pattern
- Off-market rate was approximately 80% across all 330 questions
- Questions asking for specific persons, small towns, or unique identifiers almost always went off-market
- Context-dependent questions (war-related, geographically bounded) had higher hit rates

### What Worked
1. **Evidence-based adjustments**: Mid-day searches for new evidence led to hits (Iranian Red Crescent, Naini, Old City)
2. **Geographic reasoning**: Using conflict zone knowledge helped narrow options
3. **Conservative probabilities**: Summing to 0.35-0.55 per question, reserving probability for off-market
4. **War context**: Understanding the US-Iran-Israel war dynamics helped with many Gulf/Middle East questions

### What Didn't Work
1. **Overconfidence on strong evidence**: Rajasthan Royals (0.40) based on HT article was wrong - RCB won
2. **Missing question framing**: "Trump 10-day pause requester" was Iran itself, not a mediator
3. **Insufficient off-market reserve**: Probabilities still too concentrated on listed outcomes
4. **Specific location questions**: Jezzine, White Nile State, Qom, Menashe Zalka - consistently unpredictable

### Best Hits (Brier > +0.20)
- Australia visa ban: Iran (0.57)
- Jerusalem explosion: Old City (0.30)
- IRGC spokesman funeral: Ali Mohammad Naini (0.31)
- Toddler rescue org: Iranian Red Crescent (0.36)
- Several others in 0.15-0.30 range

### Worst Misses (Brier < -0.10)
- Rajasthan Royals IPL (0.40 → RCB, -0.17)
- Multiple off-market questions at -0.05 to -0.08

## Key Context for This Simulation
- **US-Iran-Israel War (Operation Epic Fury)**: Feb 28 - ongoing, Khamenei killed March 1
- **Lebanon front**: Hezbollah joined March 2, 1000+ killed
- **Gulf attacks**: Iran struck desalination plants, oil facilities across UAE, Bahrain, Kuwait, Qatar, Saudi Arabia
- **Sudan civil war**: SAF vs RSF continuing, East Darfur hospital attack
- **UEFA World Cup 2026 playoffs**: Italy, Kosovo paths through March
- **Pope Leo XIV**: First US Pope, very vocal on Middle East peace

## Final TW-Score: -2984.23
This represents the sum of time-weighted Brier scores across all 330 questions. The maximum possible would have been +33000 (100 × 330 with perfect predictions from day 1). The minimum would be -33000.
