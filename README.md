# NeuroAI Foundations

This is a long-term computational-neuroscience learning and research notebook. Its central question is:

> How do biological neural systems encode, process, learn, and represent information—and which computational principles, if any, can inform artificial systems?

It is not a product, startup, generic AI demo, or model leaderboard. The work proceeds through small, falsifiable experiments whose mathematics and biological assumptions are visible.

The prior project, **EEG Motor Imagery**, remains separate as Research Project #1: a reproducible offline EEGMMIDB replication and methodology study. It is prior preparation, not a dependency or a source of copied analyses.

## Milestone 1 — From stimulus to spike

The current milestone is intentionally narrow: understand a leaky integrate-and-fire (LIF) neuron as a simplified dynamical model, simulate it with NumPy, and interpret the relationship between input current, membrane voltage, and spikes.

Start here:

1. [Roadmap](ROADMAP.md)
2. [First module](notebooks/01_neuron_basics/README.md)
3. [LIF notebook](notebooks/01_neuron_basics/01_leaky_integrate_and_fire.ipynb)
4. [Questions](QUESTIONS.md) and [learning log](LEARNING_LOG.md)

## Reproduce the first notebook

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e '.[dev,notebooks]'
pytest
jupyter nbconvert --to notebook --execute --inplace \
  notebooks/01_neuron_basics/01_leaky_integrate_and_fire.ipynb
```

The notebook uses only NumPy, Matplotlib, and the small reusable implementation in `src/`. No specialized simulator is used in Milestone 1.

## Boundaries

- A LIF neuron is a useful abstraction, not a full biological neuron and not an artificial-network activation unit.
- A successful numerical simulation validates the stated equations/code path, not a biological mechanism.
- The repository will not advance automatically to Hodgkin–Huxley, neural coding, plasticity, real neural data, or machine learning until this module is understood.

## Local research context

The [Farfán research map](farfan/FARFAN_RESEARCH_MAP.md) documents a local bridge between tactile neural coding, electrophysiology, biomimetics, and neuroprosthetics. It distinguishes verified historical work from currently listed work and makes no claim that a particular course or laboratory position is available.
