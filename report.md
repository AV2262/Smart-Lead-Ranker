# Smart Leads Tool — Strategy Report

## Objective
To enhance lead generation by validating contact information and prioritizing leads based on high-impact signals such as job title and company size.

## Feature Focus
We focused on a **Quality First** approach:
- **Email Verification**: Basic regex validation to ensure syntactic correctness.
- **Lead Scoring Engine**: Prioritizes decision-makers and large organizations.

## Tools & Tech Stack
- **Flask** for the web interface
- **Pandas** for CSV data processing
- **Bootstrap CSS** for UI polish

## Sample Logic Used
- CEOs/Founders get a higher score (5), followed by Directors/VPs (4), Managers (3), and Others (1)
- Large companies get 3 bonus points, medium 2, small 1

## Real-World Alignment
B2B sales teams want to target:
- Decision-makers (CEO, VP)
- Companies with higher budgets (Large/Medium businesses)

This tool quickly ranks uploaded CSV files to identify top opportunities.

## Time Utilized: ~4.5 hours
- Web UI + file upload: 1.5 hrs
- Scoring logic + validation: 1 hr
- Integration + output export: 1.5 hrs
- Styling & testing: 0.5 hrs

## Future Enhancements (if more time allowed)
- Use SMTP or API-based email verification
- Integrate LinkedIn scraping or enrichment
- Export to CRM APIs (HubSpot, Salesforce)

---

**Submitted by:** Anjali Verma
**Repository:** https://github.com/AV2262
