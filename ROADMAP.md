# Roadmap: from biophysics to NeuroAI

This is a dependency map, not a promise to finish every topic soon. An arrow means “learn enough of the left before relying on the right.”

```text
scientific Python + calculus + linear algebra + probability
                         │
                         ▼
membrane voltage → differential equations → neuron models
                         │                         │
                         │                         ▼
                         │                  spike trains
                         │                         │
                         ▼                         ▼
synapses, excitation/inhibition ─────→ neural coding
                                             │
                    statistics + information theory + decoding
                                             │
                                             ▼
population representations → dynamics / recurrence / oscillations
                                             │
                                             ▼
plasticity, adaptation, memory, reinforcement learning
                                             │
                                             ▼
real neural data: behavior + spikes/LFP/imaging + inference
                                             │
                                             ▼
NeuroAI: test—not assume—whether biological principles transfer
```

## 1. Neuron biology

Learn membrane potential, ionic gradients, ion channels, action potentials, synapses, excitation, inhibition, and refractory periods. The question is not “what is a neuron shaped like?” but “what physical variables change and what constraints do they impose on signaling?”

Prerequisites: basic electricity, derivatives, units. First model: leaky integrate-and-fire. Later: conductance-based/Hodgkin–Huxley models.

## 2. Mathematical foundations

- **Calculus and differential equations:** describe continuous-time change such as membrane charging.
- **Linear algebra:** represents populations, covariance, linear decoders, and dimensionality reduction.
- **Probability and statistics:** distinguish noise, variability, estimation uncertainty, and evidence.
- **Dynamical systems:** asks how states evolve, stabilize, oscillate, or transition.
- **Information theory:** quantifies uncertainty and stimulus-response dependence; it does not automatically reveal meaning or mechanism.

## 3. Computational neuron models

Start with integrate-and-fire, then leaky integrate-and-fire. Learn what each term omits. Hodgkin–Huxley comes only after conductances, reversal potentials, and numerical integration are intelligible. Izhikevich-type models are later convenience/phenomenology models, not replacements for biophysics.

## 4. Neural coding

Move from “did a neuron spike?” to “which properties of a stimulus can be inferred from spike trains?” Topics: spike trains, firing rate, inter-spike intervals, timing, tuning curves, population coding, entropy, mutual information, encoding, and decoding. A decoder can recover information without proving that a biological system uses the same algorithm.

## 5. Networks and representations

Learn excitation/inhibition, recurrence, attractors, synchrony, oscillations, and population trajectories. The central object changes from one voltage trace to a high-dimensional population state. Dimensionality reduction is descriptive unless paired with a clear generative or behavioral hypothesis.

## 6. Learning, plasticity, and adaptation

Learn Hebbian rules, spike-timing-dependent plasticity, homeostasis, reinforcement learning, memory, and continual adaptation. Separate a proposed synaptic mechanism from a behavioral observation. “The brain learns” does not imply one universal rule or an immediate AI algorithm.

## 7. Neural data analysis

Learn experimental design, spike sorting provenance, peri-stimulus representations, tuning estimation, decoding, statistical inference, and cross-session/animal stability. Reuse the EEG project’s lessons about data leakage, nested observations, and reproducibility—while recognizing that spikes, LFP, imaging, and behavior have different measurement models.

## 8. Real datasets

Only after simulation literacy: work with a small documented slice of Allen, DANDI, or IBL data. Public availability is not a substitute for understanding acquisition, preprocessing, behavior, trial structure, and observation units. No large dataset is downloaded during Milestone 1.

## 9. NeuroAI

Potential topics include continual learning, sparse/event-driven representations, adaptive computation, recurrent dynamics, efficient coding, and neuromorphic systems. Each proposal must say:

1. the biological observation;
2. the mathematical abstraction;
3. the artificial-system prediction;
4. the comparison baseline; and
5. the result that would falsify transfer.

The right conclusion can be “this biological feature did not help this artificial task.”

## Current stop line

Milestone 1 covers only the first bridge: membrane voltage → LIF dynamics → spikes. Do not treat completion as understanding neural coding or biological learning.
