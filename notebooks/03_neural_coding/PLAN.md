# Planned module: from stimulus to spike train to decoder

This is a design document only. Do not implement it until the LIF module and its prerequisites are understood.

## Future question

Which properties of a stimulus can be recovered from a simulated spike train, and does the answer depend on whether the representation uses rate, timing, or a population?

## Candidate simulation chain

```text
stimulus intensity or temporal waveform
  → LIF neuron or small heterogeneous population
  → spike train(s)
  → rate / inter-spike interval / timing features
  → explicitly defined decoder
  → estimated reconstruction or classification performance
```

## Planned comparisons

1. **Rate representation:** count spikes in a fixed window.
2. **Temporal representation:** use first-spike latency or selected spike times.
3. **Population representation:** compare several neurons with different thresholds or gains against one neuron.
4. **Noise:** inject controlled input noise and quantify uncertainty rather than showing only attractive raster plots.

Potential measures are firing rate, inter-spike intervals, timing dispersion, entropy, mutual information, and held-out decoding accuracy. Each needs an explicit estimator, bias/finite-sample discussion, and observation unit before use.

## Connection to tactile neural coding

Farfán, Albarracín, and Felice studied rat vibrissal afferent recordings during tactile texture discrimination. Their 2013 work evaluated event-based codes using Shannon mutual information, including cumulative event count and median inter-event time. That makes it a valuable later bridge between simple simulated rate/timing representations and empirical sensory recordings—not a reason to claim that a LIF simulation reproduces the vibrissal system. See [the verified reading list](../../farfan/READING_LIST.md).

## Pre-implementation requirements

- Explain entropy and mutual information with a discrete toy example.
- Distinguish encoding (stimulus → response model) from decoding (response → stimulus estimate).
- State why a successful decoder does not by itself identify the biological code.
- Define a train/test boundary and a finite-sample baseline.
