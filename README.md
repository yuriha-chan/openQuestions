# openQuestions dataset
This is a small experimental dataset of open-ended, non-factual questions designed for evaluating the qualitative reasoning capacity of large language model (LLM) chatbots. Unlike conventional QA benchmarks, it does not aim to test factual precision/recall or problem-solving accuracy. Instead, it probes the ability of a model to handle complex, interdisciplinary prompts that require synthesis, judgment, and rhetorical adaptability.

## Motivation

Most widely used QA benchmarks optimize for correctness under well-defined ground truths. While useful for measuring factual accuracy, such benchmarks often fail to capture whether a model is usable in contexts where the answer space is indeterminate, ambiguous, or heavily context-dependent. This dataset was conceived as a way to highlight the gap between "best-performing on metrics" models and models that behave usefully in real-world conversations, especially in human-AI collaboration settings.

## Key properties:

Non-factual: No ground-truth answers are provided or even possible in many cases.

Non-task-oriented: Prompts resist reduction to step-by-step problem-solving.

Interpretive: Questions require models to show reasoning, creativity, and academic precision.


## Data Generation

Questions were generated using Gemini Pro 2.5.

Prompts were varied to elicit diverse syntactic structures and thematic domains.

Selection was manual, prioritizing questions with rhetorical complexity, cross-domain analogies, or demands for critical reflection.

The current version includes 80 questions.

## Example Questions

- "Explain the standard process of Reinforcement Learning from Human Feedback (RLHF) used to align large language models. Then, critique the usability of this process for optimizing a model where factual accuracy and avoidance of hallucination are paramount, such as a medical information chatbot. Propose a set of principles for designing a reward model and feedback collection process that would specifically penalize plausible-sounding falsehoods and reward evidence-based, cautious responses.Explain the standard process of Reinforcement Learning from Human Feedback (RLHF) used to align large language models. Then, critique the usability of this process for optimizing a model where factual accuracy and avoidance of hallucination are paramount, such as a medical information chatbot. Propose a set of principles for designing a reward model and feedback collection process that would specifically penalize plausible-sounding falsehoods and reward evidence-based, cautious responses."
- "My partner and I have the same arguments over and over, and we always get stuck on disagreements about who said what or what was previously agreed upon. It's made me think about the philosophical concept of epistemic humility—the idea of acknowledging the limits and fallibility of our own knowledge and memory. I want to find a way to apply this concept practically to our conversations. What would a communication strategy look like that is built on this principle? I'm trying to figure out how we can shift our arguments away from a 'battle of memories' and towards a method for problem-solving that accepts that both of our recollections might be flawed."
- "I'm exploring how methodologies from tech product management could be applied to public health challenges. Tech companies are obsessed with user onboarding—the carefully designed initial experience that helps users adopt a new product. What if we treated a public health initiative, like an adult vaccination campaign, not as a broadcasted message but as a 'product' that citizens need to be 'onboarded' onto? What would the process look like if a product manager, instead of an epidemiologist, was in charge of designing the end-to-end citizen experience for something like scheduling a preventative screening? I'm interested in what this shift in perspective from public information to user engagement might reveal about improving health outcomes."

## Intended Use

This dataset is not suitable for accuracy scoring. Instead, it supports:

- Qualitative model comparison: Observe stylistic, rhetorical, and reasoning differences across LLMs.
- Stress-testing: Identify failure modes such as hallucination, verbosity, overconfidence, or evasion.
- Rehearsal learning: Use the open-ended prompts as generative scaffolds for training or fine-tuning models to exhibit more reflective and interdisciplinary reasoning styles.

## Limitations

Small scale: Only 80 questions; best understood as a pilot corpus.
No ground truth: Cannot be used for metric-driven benchmarking.
