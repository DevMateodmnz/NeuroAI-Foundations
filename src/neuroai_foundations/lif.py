"""A deliberately small leaky integrate-and-fire simulation.

This module implements a teaching model, not a conductance-based biological neuron.
All voltages are millivolts (mV), currents nanoamperes (nA), resistances megaohms
(MΩ), and times milliseconds (ms).  MΩ × nA = mV, which keeps the LIF equation
dimensionally consistent without hidden conversion factors.
"""

from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class LIFParameters:
    """Parameters for a current-driven leaky integrate-and-fire neuron.

    The subthreshold equation is

        tau_m * dV/dt = -(V - E_leak) + R_m * I(t).

    A threshold crossing records a spike, resets the voltage, and starts an
    absolute refractory period. The threshold/reset event is a model rule, not
    a numerical solution of an action-potential ion-channel mechanism.
    """

    tau_m_ms: float = 20.0
    resistance_mohm: float = 100.0
    resting_potential_mv: float = -65.0
    threshold_mv: float = -50.0
    reset_potential_mv: float = -65.0
    refractory_period_ms: float = 2.0

    def validate(self) -> None:
        """Reject values that make the model or its units nonsensical."""
        if self.tau_m_ms <= 0:
            raise ValueError("tau_m_ms must be positive.")
        if self.resistance_mohm <= 0:
            raise ValueError("resistance_mohm must be positive.")
        if self.refractory_period_ms < 0:
            raise ValueError("refractory_period_ms cannot be negative.")
        if self.reset_potential_mv >= self.threshold_mv:
            raise ValueError("reset_potential_mv must be below threshold_mv.")


@dataclass(frozen=True)
class LIFSimulation:
    """Outputs aligned on discrete simulation time samples."""

    time_ms: np.ndarray
    voltage_mv: np.ndarray
    input_current_na: np.ndarray
    spikes: np.ndarray

    @property
    def spike_times_ms(self) -> np.ndarray:
        """Return the sampled times at which the threshold rule emitted spikes."""
        return self.time_ms[self.spikes]


def _coerce_current(input_current_na: float | np.ndarray, n_steps: int) -> np.ndarray:
    """Make a scalar current constant in time or validate a current vector."""
    current = np.asarray(input_current_na, dtype=float)
    if current.ndim == 0:
        if not np.isfinite(current):
            raise ValueError("input_current_na must contain only finite values.")
        return np.full(n_steps, float(current), dtype=float)
    if current.ndim != 1 or current.size != n_steps:
        raise ValueError("input_current_na must be scalar or have one value per time step.")
    if not np.isfinite(current).all():
        raise ValueError("input_current_na must contain only finite values.")
    return current.copy()


def simulate_lif(
    input_current_na: float | np.ndarray,
    duration_ms: float,
    dt_ms: float,
    parameters: LIFParameters = LIFParameters(),
) -> LIFSimulation:
    """Simulate one LIF neuron with forward Euler integration.

    `duration_ms / dt_ms` must be an integer so every input element has one
    unambiguous sample. At each non-refractory step, forward Euler applies

        V[t + dt] = V[t] + dt/tau_m * (-(V[t] - E_leak) + R_m I[t]).

    A crossing is recorded at the next sampled time and reset immediately for
    the next update. This explicitly favors readability over a more exact
    threshold-crossing interpolation scheme.
    """
    parameters.validate()
    if duration_ms <= 0 or dt_ms <= 0:
        raise ValueError("duration_ms and dt_ms must be positive.")
    raw_steps = duration_ms / dt_ms
    n_steps = int(round(raw_steps))
    if not np.isclose(raw_steps, n_steps):
        raise ValueError("duration_ms must be an integer multiple of dt_ms.")

    current = _coerce_current(input_current_na, n_steps)
    time_ms = np.arange(n_steps, dtype=float) * dt_ms
    voltage = np.empty(n_steps, dtype=float)
    spikes = np.zeros(n_steps, dtype=bool)
    voltage[0] = parameters.resting_potential_mv
    refractory_steps = int(round(parameters.refractory_period_ms / dt_ms))
    refractory_remaining = 0

    for index in range(n_steps - 1):
        if refractory_remaining > 0:
            voltage[index + 1] = parameters.reset_potential_mv
            refractory_remaining -= 1
            continue

        dv_mv = (dt_ms / parameters.tau_m_ms) * (
            -(voltage[index] - parameters.resting_potential_mv)
            + parameters.resistance_mohm * current[index]
        )
        candidate_mv = voltage[index] + dv_mv
        if candidate_mv >= parameters.threshold_mv:
            spikes[index + 1] = True
            voltage[index + 1] = parameters.reset_potential_mv
            refractory_remaining = refractory_steps
        else:
            voltage[index + 1] = candidate_mv

    return LIFSimulation(time_ms, voltage, current, spikes)
