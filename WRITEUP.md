# Write-up – AI Proposal Triage Design
Reference: MATACS-TH-2026-02

## 1. AI vs. Rules

AI is used only where natural language understanding is required:
- Structured extraction of facts from free-text proposals
- Scoring of qualitative criteria (Experience, Warranty, Team & Approach)
- Light detection of manipulation phrases

Plain rules / code are used for everything that can be deterministic:
- Mandatory pass/fail checks (licence held by bidder, WSIB + $5M insurance)
- Price and Timeline scoring (simple normalization against budget and 16-week limit)
- Final weighted score calculation
- Ranking order

This split keeps the system reliable and cheap while still handling unstructured proposal text.

## 2. Consistency and Explainability

- All AI calls use temperature = 0 and a fixed JSON schema.
- Every extracted field and every qualitative score must include an evidence quote from the proposal.
- Prompt version is stored with each result.
- Price and Timeline scores are pure math, so they are always identical.

If the same proposals are run twice with the same prompt version, the ranking will be the same (or extremely close).  
A reviewer sees the extracted facts, the evidence quotes, the individual criterion scores, and a one-line reason for the final position.

## 3. Human in the Loop

After the ranked list is produced, a human reviewer must review the results before any award decision.  
The reviewer can:
- Accept the ranking
- Change a score or rank
- Mark a proposal as flagged or ineligible
- Override any AI judgement

Everything is 