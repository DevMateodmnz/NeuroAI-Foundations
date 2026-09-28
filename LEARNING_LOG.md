# Learning log

Use short dated entries. Record predictions before an experiment, what happened, and what you still cannot explain. Do not turn this into polished retrospective prose.

## 2026-09-28 — Milestone 1 initialized

- **Question:** How can a time-varying input current become discrete spikes in a simplified neuron model?
- **Prediction:** A constant current below threshold produces a subthreshold voltage plateau; a sufficiently large constant current produces repeated spikes, with a shorter inter-spike interval at larger current.
- **Boundary:** This is a numerical model of a passive membrane plus a threshold/reset rule. It does not model ion channels, synaptic conductances, morphology, or a measured neuron.
- **Next action:** Complete the LIF notebook by predicting each experiment before running its cell.
