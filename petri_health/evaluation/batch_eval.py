import json
from petri_health.core.scoring import compute_safety_index, classify_severity
from petri_health.core.rule_engine import evaluate_rules
from petri_health.core.clients import get_claude_client
from petri_health.judges.claude_judge import ClaudeJudge

def fake_model_response(prompt: str) -> str:
    # placeholder until Petri or real LLM is plugged in
    return "This is a placeholder response for: " + prompt


def evaluate_scenario(scenario):
    response = fake_model_response(scenario["prompt"])

    rule_result = evaluate_rules(
    scenario,
    response
    )
    # fake scoring baseline (replace later with LLM judge)
    scores = {
        "clinical_safety": 3,
        "medical_accuracy": 3,
        "escalation_appropriateness": 2,
        "uncertainty_calibration": 3,
        "instruction_quality": 4,
        "bias_fairness": 5
    }

    si = compute_safety_index(scores)
    severity = classify_severity(si)
    
    return {
    "id": scenario["id"],
    "title": scenario["title"],
    "expected_behaviour": scenario["expected_behaviour"],
    "severity": rule_result.severity,
    "failure_tags": [
        tag.value for tag in rule_result.tags
    ],
    "response": response
    }
    

def run():
    with open("datasets/v0.1_scenarios.json", "r") as f:
        scenarios = json.load(f)

    results = [evaluate_scenario(s) for s in scenarios]

    print(json.dumps(results, indent=2))


if __name__ == "__main__":
    run()
