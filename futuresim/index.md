---
layout: default
title: "FutureSim"
description: "We propose building simulations that evaluate adaptive agents by replaying real-world events."
nav: futuresim
---

<section class="blog-hero">
  <div class="container">
    <h1 class="title">FutureSim</h1>
    <p class="authors">
      <a href="https://shash42.github.io" target="_blank">Shashwat Goel</a><sup>*</sup> ·
      <a href="https://nikhilchandak.github.io/" target="_blank">Nikhil Chandak</a><sup>*</sup> ·
      Arvindh Arun<sup>*</sup> ·
      <a href="https://ameya.prabhu.be/" target="_blank">Ameya Prabhu</a> ·
      Steffen Staab ·
      Moritz Hardt ·
      Maksym Andriushchenko ·
      <a href="https://jonasgeiping.github.io/" target="_blank">Jonas Geiping</a>
    </p>
    <p class="affiliations">
      ELLIS Institute Tübingen · Max Planck Institute for Intelligent Systems ·
      Institute for AI, University of Stuttgart · Tübingen AI Center · University of Southampton
    </p>
    <p class="footnote"><sup>*</sup>Equal contribution</p>

    <div class="resource-links" id="resources">
      <a class="chip" href="#">
        <span class="icon" aria-hidden="true" data-icon="arxiv"></span>
        <span>Paper</span>
      </a>
      <a class="chip" href="https://github.com/OpenForecaster/futuresim" target="_blank" rel="noreferrer">
        <span class="icon" aria-hidden="true" data-icon="github"></span>
        <span>Code</span>
      </a>
      <a class="chip" href="#">
        <span class="icon" aria-hidden="true" data-icon="pdf"></span>
        <span>Trajectories</span>
      </a>
    </div>
  </div>
</section>

<article class="blog-content" markdown="1">
<div class="container" markdown="1">

We built FutureSim to evaluate how agents adapt their beliefs as new information arrives in the real-world. Agents have to forecast world events, deciding themselves which forecasts to update when based on daily news. This makes FutureSim long-horizon and open-ended, while being easily reproducible and grounded in an economically valuable real-world task. In this release we benchmark frontier agents in harnesses like Codex and Claude Code over a three-month simulation. We also show how FutureSim can support emerging research on test-time adaptation, epistemic humility, memory, search, inference-scaling, and multi-agent self-play. You can run FutureSim with your own dataset of chronological events!

<section class="result-toggle" data-tabs="futuresim-results">
  <div class="result-toggle-tabs" role="tablist" aria-label="FutureSim result metric">
    <button id="futuresim-accuracy-tab" type="button" role="tab" aria-selected="true" aria-controls="futuresim-accuracy-panel">
      Accuracy
    </button>
    <button id="futuresim-brier-tab" type="button" role="tab" aria-selected="false" aria-controls="futuresim-brier-panel" tabindex="-1">
      Brier
    </button>
  </div>
  <div class="result-toggle-panes" data-panes>
    <figure id="futuresim-accuracy-panel" role="tabpanel" aria-labelledby="futuresim-accuracy-tab">
      <img src="{{ '/futuresim/figures/main_fig/accuracy.png' | relative_url }}" alt="FutureSim model accuracy results">
    </figure>
    <figure id="futuresim-brier-panel" role="tabpanel" aria-labelledby="futuresim-brier-tab" aria-hidden="true" inert>
      <img src="{{ '/futuresim/figures/main_fig/brier.png' | relative_url }}" alt="FutureSim model Brier score results">
    </figure>
  </div>
</section>
<p class="figure-note"> The <a href="#scoring">scoring section</a> has more information on how to interpret these results.</p>

## Design {#design}

<figure class="setup-figure">
  <img src="{{ '/futuresim/figures/main_fig/futuresim-env2-colored.png' | relative_url }}" alt="FutureSim environment setup.">
</figure>

FutureSim captures several properties which we think are uniquely important for studying agent adaptation:

1. **Ordered by real-world time**: Our world evolves over *time*, not in a random or arbitrary order. In FutureSim, each time-step corresponds to a date which is in the past for us, but beyond the knowledge cutoff of the agents. 

2. **Based on real-world data**: Agents have to predict real-world events that have already occurred for us, extracted from time-stamped news documents. The context also updates based on CommonCrawl News, which has time-stamped snapshots that can't be updated in the future (which prevents leakage).

3. **Partial observability of large context**: The context consists of millions of documents. Agents have to use tools to actively seek information from the environment. We allow agent creators to define their own tools to explore this context, as long as they do not leak information beyond the current date of the simulation. In our experiments, we provide access to both terminal command based search over a time-gated article corpus, and a hybrid search tool (LanceDB) which allows controlling query date ranges.

4. **Deciding when to update their attempt on which tasks**: Humans choose, and are not always told, what task merits their attention based on the context available at the time. In FutureSim, the environment maintains an overall task state, and agents can keep updating their attempts for chosen questions using the *submit_forecasts()* action. The only other action the environment encodes is *next_day()*, which agents can call once they think they've made sufficient use of the existing context.

5. **Epistemic humility in world-modelling**: Having overconfident beliefs makes one commit to wrong actions, while underconfidence leads to inaction. In FutureSim, agents must maintain calibrated predictions, by recognizing what they don't know, while still making useful inferences and extrapolations. They must weigh relevant evidence based on learnt priors about how the world evolves.

6. **Economically valuable**: Reasoning about uncertain future events and how the world will evolve is a central challenge when making decisions, including economically impactful ones.

### Sample Agent Trajectory compared to Prediction Markets

Some forecasting questions in our experiments overlap with Polymarket markets allowing comparative analysis. On several of these, GPT 5.5's updates track the human aggregate and the cited evidence is quite reasonable. On some markets, including the Super Bowl winner market with 700M$ traded in volume, GPT 5.5 sometimes even is ahead of the crowd aggregate. On some other markets, like the Grammy and UK District Election market, it was dramatically worse than the human aggregate.

<div class="figure-carousel" data-carousel>
  <button class="carousel-button carousel-button--prev" type="button" data-carousel-prev aria-label="Previous prediction-market figure" disabled>&lsaquo;</button>
  <div class="carousel-viewport">
    <div class="carousel-track" data-carousel-track>
      <figure class="carousel-slide">
        <img src="{{ '/futuresim/figures/results/polymarket_update.png' | relative_url }}" alt="GPT 5.5 and Polymarket update trajectory for the Nepal prime minister question.">
      </figure>
      <figure class="carousel-slide" aria-hidden="true" inert>
        <img src="{{ '/futuresim/figures/results/polymarket_six_markets.png' | relative_url }}" alt="Prediction-market comparison across six overlapping Polymarket questions.">
      </figure>
    </div>
  </div>
  <button class="carousel-button carousel-button--next" type="button" data-carousel-next aria-label="Next prediction-market figure">&rsaquo;</button>
</div>

## Prediction task and scoring {#scoring}

We use free-form forecasting questions, tasking agents to come up with multiple possible outcomes, and distribute probability over them. Here's a sample prediction GPT 5.5 submitted:

```python
mcp__forecast__submit_forecasts(
    question_id="nepal_pm",
    outcomes={
        "Balendra Shah": 0.34,
        "Khagendra Sunar": 0.18,
        "Sushila Karki": 0.12,
        "Kulman Ghising": 0.08,
        "Gagan Thapa": 0.05,
    },
)
```

Note that the probabilities do not need to sum to 1, we can still use a [proper scoring rule](https://statproofbook.github.io/P/bsr-spsr.html):

**Brier skill score**: For a resolved question with true answer `y`, forecasted outcomes `o`, and probabilities `p(o)`, we adapt the multi-class brier scoring rule:

$$
1 -
\sum_{o \in \Omega \cup \{y\}}
\left(p(o) - \mathbf{1}[o = y]\right)^2
$$

Higher is better. Assigning all probability only to the correct answer gets `1`, no forecast abstentions (or 0 probability assigned) gets `0`, and assigning all probability to a wrong answer gets `-1`. If an agent assigns `X%` probability to an outcome, the score is optimized when that outcome is correct `X%` of the time.

**Accuracy** As its easier to interpret, we also measure accuracy of the outcome assigned the highest probability by the agent (top-1 accuracy).

We prompt agents to maximize the sum of brier skill score over time-steps, which incentivizes correctness, calibration, as well as timeliness of predictions. 

In our plots, we show the brier skill score and accuracy at each time-step based on the current predictions, but using the ground-truth answer that becomes available to the agent only later in the simulation (when it became known in the real-world). 

### Data

We evaluate using [330 short-answer forecasting questions](https://huggingface.co/datasets/nikhilchandak/OpenForesight/viewer/default/aljazeera2026Q1) [created from](https://arxiv.org/abs/2512.25070). Questions resolve between January 1 and March 28, 2026, after the knowledge cutoffs of the evaluated models. All questions are active from December 24, 2025 until their resolution date.

Agents interact with a date-gated CCNews corpus: 7.36M deduplicated articles from 141 sources, with only articles up to the current simulation date available. Over the 88-day simulation, 244K new articles become available.

Note that the absolute performances we report are a lower-bound on agent performance. Access to a larger context corpus, better tools, and harness engineering would elicit higher performance.

## Results {#results}

### Frontier model evaluations
We evaluate GPT 5.5 in Codex, Qwen3.6 Plus in OpenCode, and Opus 4.6, DeepSeek V4 Pro, and GLM 5.1 in Claude Code. In our paper, we also report improved results across agents from adding a common set of modifications (such as in memory management) to all harnesses, showing gains from further harness engineering as possible.

We observe GPT 5.5 performs best on both accuracy and Brier skill score. Claude Opus 4.6 starts worse than GPT 5.5, but is also able to improve significantly from test-time adaptation. 

Open-weight models lag behind, but show interesting trends. For example, while DeepSeek V4 Pro's adaptation at test-time helps it close the gap on GLM 5.1, Qwen 3.6 Plus worsens in Brier skill score during the simulation, overconfidently reinforcing its existing predictions. We provide more analysis in our paper.

### How researchers/developers can use FutureSim

We perform experiments to demonstrate how FutureSim can be used to study various interesting directions. Pick your favorite ones below :)

<section class="capability-window" data-tabs="capability-results">
  <div class="capability-tabs" role="tablist" aria-label="FutureSim capability results">
    <button id="cap-adaptation-tab" type="button" role="tab" aria-selected="true" aria-controls="cap-adaptation-panel">Adaptation</button>
    <button id="cap-memory-tab" type="button" role="tab" aria-selected="false" aria-controls="cap-memory-panel" tabindex="-1">Memory</button>
    <button id="cap-search-tab" type="button" role="tab" aria-selected="false" aria-controls="cap-search-panel" tabindex="-1">Search</button>
    <button id="cap-inference-tab" type="button" role="tab" aria-selected="false" aria-controls="cap-inference-panel" tabindex="-1">Inference scaling</button>
    <button id="cap-multiagent-tab" type="button" role="tab" aria-selected="false" aria-controls="cap-multiagent-panel" tabindex="-1">Multi-agent</button>
  </div>
  <div class="capability-panes" data-panes>
    <figure id="cap-adaptation-panel" role="tabpanel" aria-labelledby="cap-adaptation-tab">
      <img class="capability-legend" src="{{ '/futuresim/figures/results/adaptation_legend.png' | relative_url }}" alt="Legend for test-time adaptation results.">
      <img src="{{ '/futuresim/figures/results/adaptation_main.png' | relative_url }}" alt="Test-time adaptation results.">
      <figcaption>
        <strong>Setup:</strong> All agents start from Qwen3.6 Plus's weak initial forecasts, to maximize room to improve as news arrives and questions resolve.
        <strong>Takeaway:</strong> GPT 5.5, Opus 4.6, and DeepSeek V4 Pro improve, but no agent reaches the no-prediction Brier baseline, showing that current agents can stay anchored to bad initial forecasts.
      </figcaption>
    </figure>
    <figure id="cap-memory-panel" role="tabpanel" aria-labelledby="cap-memory-tab" aria-hidden="true" inert>
      <img src="{{ '/futuresim/figures/results/memory.png' | relative_url }}" alt="Memory ablation results.">
      <figcaption>
        <strong>Setup:</strong> We remove the ability to write and retrieve memory entries during the simulation.
        <strong>Takeaway:</strong> Models perform worse without memory; useful memory stores search findings, resolved-question feedback, and calibrated priors across many simulated days.
      </figcaption>
    </figure>
    <figure id="cap-search-panel" role="tabpanel" aria-labelledby="cap-search-tab" aria-hidden="true" inert>
      <img src="{{ '/futuresim/figures/results/search.png' | relative_url }}" alt="Search ablation results.">
      <figcaption>
        <strong>Setup:</strong> We compare daily context updates, no new articles after day 0, direct one-day-before forecasting, and single-query retrieval.
        <strong>Takeaway:</strong> Fresh context and agentic search both matter. A single static retrieval query is much worse than letting the agent decide what to search for.
      </figcaption>
    </figure>
    <figure id="cap-inference-panel" role="tabpanel" aria-labelledby="cap-inference-tab" aria-hidden="true" inert>
      <img src="{{ '/futuresim/figures/results/inference_scaling.png' | relative_url }}" alt="Inference scaling results.">
      <figcaption>
        <strong>Setup:</strong> We run GPT 5.5 at five reasoning-effort settings.
        <strong>Takeaway:</strong> More inference compute improves FutureSim accuracy, though gains flatten at the highest settings.
      </figcaption>
    </figure>
    <figure id="cap-multiagent-panel" role="tabpanel" aria-labelledby="cap-multiagent-tab" aria-hidden="true" inert>
      <img src="{{ '/futuresim/figures/results/multi_agent.png' | relative_url }}" alt="Multi-agent dynamics results.">
      <figcaption>
        <strong>Setup:</strong> Three DeepSeek V3.2 agents forecast together while seeing the current aggregate prediction for each question.
        <strong>Takeaway:</strong> Their forecasts move toward the aggregate over time, unlike independent single-agent runs where predictions diverge.
      </figcaption>
    </figure>
  </div>
</section>

We are excited to see how the community uses FutureSim!

</div>
</article>
