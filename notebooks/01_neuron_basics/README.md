# Module 01 — From stimulus to spike

## Question

How can an input current change a simplified neuron’s membrane voltage until the model emits discrete spikes?

## What this module is—and is not

A leaky integrate-and-fire (LIF) model treats the membrane as a leaky electrical compartment. It is useful because one can trace each term in its equation and predict the output. It is not a complete neuron: it omits voltage-gated ion channels, dendrites, synaptic conductances, morphology, neurotransmitters, adaptation currents, and realistic action-potential shape.

The model is:

\[
\tau_m\frac{dV(t)}{dt}=-(V(t)-E_L)+R_mI(t).
\]

| Symbol | Meaning | Units here |
| --- | --- | --- |
| \(V(t)\) | membrane voltage | mV |
| \(E_L\) | leak/reversal or resting voltage in this model | mV |
| \(\tau_m\) | membrane time constant; how quickly voltage changes | ms |
| \(R_m\) | membrane resistance | MΩ |
| \(I(t)\) | injected input current | nA |

`MΩ × nA = mV`, so the right-hand terms have voltage units. The negative leak term pulls voltage back toward \(E_L\). With a constant current, the subthreshold equilibrium is \(V_\infty=E_L+R_mI\). The model adds a rule: when voltage reaches threshold, record a spike, reset to \(V_{reset}\), and hold it there for a refractory period.

The implementation uses forward Euler integration:

\[
V_{t+\Delta t}=V_t+\frac{\Delta t}{\tau_m}
[-(V_t-E_L)+R_mI_t].
\]

Smaller \(\Delta t\) usually reduces numerical discretization error but costs more computation. This module uses 0.1 ms as a transparent teaching choice; it is not a claim about biological sampling precision.

## Before running the notebook

Predict, then write down your prediction in `LEARNING_LOG.md`:

1. With \(I=0\), where does voltage go and why?
2. If constant current makes \(V_\infty\) remain below threshold, will the neuron spike?
3. If input current increases, which changes first: equilibrium voltage, time to first spike, firing rate, or all three?
4. What information is discarded when a continuous voltage trace is converted to threshold events?

## Exercises

Do these by modifying notebook parameters deliberately; do not search for a “best” plot.

1. Calculate by hand the equilibrium voltage for `I = 0.10 nA` and `I = 0.30 nA` using the default values. Predict whether either crosses −50 mV.
2. Double \(\tau_m\). Does a positive current change the final equilibrium? Does it change how fast the model approaches it?
3. Change only the reset voltage from −65 mV to −70 mV. Predict the effect on firing rate for a strong constant current.
4. Set a 50-ms pulse of current followed by zero current. Explain the voltage after the pulse using the leak term.
5. Reduce `dt_ms` from 0.1 to 0.05. Which reported quantity should be checked for numerical stability before believing a precise firing-rate claim?

## Stop condition

You are ready for the next module only if you can derive the Euler update, explain each parameter and its units, predict subthreshold versus repetitive firing, and state at least three things this model leaves out.
