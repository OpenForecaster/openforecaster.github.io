---
layout: default
title: "OpenForecaster"
description: "OpenForecaster projects on language model forecasting, evaluation, and simulation."
nav: landing
---

<section class="landing-hero">
  <div class="container">
    <h1>Forecasting world events with language models</h1>
  </div>
</section>

<section class="landing-section" id="projects">
  <div class="container">
    <div class="project-grid">
      <a class="project-card" href="{{ '/scaling-data/' | relative_url }}">
        <figure class="project-media">
          <img src="{{ '/assets/images/fig1.png' | relative_url }}" alt="OpenForecaster question generation and training overview.">
        </figure>
        <div class="project-body">
          <h3>Scaling Open-Ended Reasoning to Predict the Future</h3>
          <p class="project-summary">Training OpenForecaster on OpenForesight improves open-ended forecasting accuracy, calibration, and consistency.</p>
          <p class="project-authors">Nikhil Chandak, Shashwat Goel, Ameya Prabhu, Moritz Hardt, Jonas Geiping</p>
        </div>
      </a>

      <a class="project-card" href="{{ '/futuresim/' | relative_url }}">
        <figure class="project-media project-media--contain">
          <img src="{{ '/futuresim/figures/main_fig/futuresim-env2-colored.png' | relative_url }}" alt="FutureSim environment diagram.">
        </figure>
        <div class="project-body">
          <h3>FutureSim</h3>
          <p class="project-summary">Evaluates how forecasting agents adapt their beliefs as new information arrives over real-world time.</p>
          <p class="project-authors">Shashwat Goel, Nikhil Chandak, Arvindh Arun, Ameya Prabhu, Steffen Staab, Moritz Hardt, Maksym Andriushchenko, Jonas Geiping</p>
        </div>
      </a>

      <a class="project-card" href="https://spylab.ai/blog/forecasting-pitfalls/" target="_blank" rel="noreferrer">
        <figure class="project-media">
          <img src="{{ '/assets/images/pitfalls-jan6.webp' | relative_url }}" alt="Search bias example from the forecasting pitfalls post.">
        </figure>
        <div class="project-body">
          <h3>LLM Forecasting Evaluations Need Fixing</h3>
          <p class="project-summary">Shows how leakage, retrieval bias, unreliable cutoffs, and benchmark incentives can break LLM forecasting evaluations.</p>
          <p class="project-authors">Daniel Paleka, Shashwat Goel, Jonas Geiping, Florian Tramèr</p>
        </div>
      </a>
    </div>
  </div>
</section>

<section class="landing-section landing-why" id="motivation">
  <div class="container">
    <h2>Why we care about language model forecasting</h2>
    <p>Every day, we make decisions under uncertainty. Under the hood, such decisions often involve a forecasting problem. What gift will my friend like the most? How will this policy intervention impact the economy? Which experiment will lead to the most informative results for a research goal?</p>

    <p>At the outset, forecasting might seem subjective. Multiple options may be backed by reasonable arguments. By design, experts get it wrong all the time--it is impossible to always be correct. There's probably a ceiling to predictability and we don't know where it is.</p>

    <p>Crucially though, in forecasting we eventually learn the correct outcome. This provides the "verifiable" signal needed for evaluations and improvement. This is why forecasting has been a particularly successful application of ML--whether it be predicting prices, or the weather.</p>

    <p>Yet, traditional statistical and time-series models lack the expressivity to predict the kinds of questions we deal with in our day to day, which are expressible only in natural language, also called <strong>judgemental forecasting</strong>. Language models can change this.</p>

    <p>However, forecasting requires different capabilities than solving a fully specified math or code problem-- such as seeking new information, aggregating unreliable sources, updating beliefs coherently, and reporting appropriately hedged predictions.</p>

    <p>One could call it building a <em>world model</em> of events in society.</p>
  </div>
</section>
