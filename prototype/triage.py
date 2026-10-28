"""
Simple demonstration of the AI Proposal Triage design.
Extra credit prototype – no external API calls.
"""

from ranking_logic import get_ranking_summary

def main():
    print("=== AI Proposal Triage – Demo ===\n")
    print("This script demonstrates the designed process:")
    print("1. Structured extraction (AI)")
    print("2. Mandatory rule checks")
    print("3. Manipulation detection")
    print("4. Hybrid scoring (AI + rules)")
    print("5. Final ranking + human review checkpoint\n")

    print("Final ranking of sample proposals A–E:\n")
    
    results = get_ranking_summary()
    
    for item in results:
        status = item["status"].upper()
        rank = item["rank"] if item["rank"] is not None else "-"
        score = item["score"] if item["score"] is not None else "-"
        print(f"Proposal {item['proposal']}:  Rank {rank}  |  {status}  |  Score: {score}")
        print(f"   → {item['reason']}\n")

    print("Note: Full proposal texts are intentionally not included")
    print("in this repository (per assessment rules).")
    print("In a real system the texts would be passed to the prompts")
    print("defined in ../PROMPTS.md")

if __name__ == "__main__":
    main()