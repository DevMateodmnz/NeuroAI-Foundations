import numpy as np
import pytest

from neuroai_foundations.lif import LIFParameters, simulate_lif


def test_zero_current_stays_at_rest_and_never_spikes() -> None:
    simulation = simulate_lif(0.0, duration_ms=100.0, dt_ms=0.1)
    assert not simulation.spikes.any()
    np.testing.assert_allclose(simulation.voltage_mv, -65.0)


def test_suprathreshold_current_emits_spikes() -> None:
    simulation = simulate_lif(0.3, duration_ms=200.0, dt_ms=0.1)
    assert simulation.spikes.sum() > 1
    assert np.all(simulation.voltage_mv[simulation.spikes] == -65.0)


def test_stronger_current_increases_spike_count() -> None:
    weak = simulate_lif(0.2, duration_ms=300.0, dt_ms=0.1)
    strong = simulate_lif(0.5, duration_ms=300.0, dt_ms=0.1)
    assert strong.spikes.sum() > weak.spikes.sum()


def test_vector_current_has_one_value_per_time_step() -> None:
    current = np.zeros(1000)
    current[300:] = 0.3
    simulation = simulate_lif(current, duration_ms=100.0, dt_ms=0.1)
    assert simulation.input_current_na.shape == (1000,)
    assert simulation.spikes.sum() > 0


@pytest.mark.parametrize(
    ("duration_ms", "dt_ms"), [(10.0, 0.3), (-1.0, 0.1), (10.0, 0.0)]
)
def test_invalid_time_grid_is_rejected(duration_ms: float, dt_ms: float) -> None:
    with pytest.raises(ValueError):
        simulate_lif(0.1, duration_ms=duration_ms, dt_ms=dt_ms)


def test_reset_must_be_below_threshold() -> None:
    invalid = LIFParameters(reset_potential_mv=-50.0)
    with pytest.raises(ValueError):
        simulate_lif(0.1, duration_ms=10.0, dt_ms=0.1, parameters=invalid)


@pytest.mark.parametrize("current", [np.nan, np.inf, -np.inf])
def test_nonfinite_scalar_current_is_rejected(current: float) -> None:
    with pytest.raises(ValueError, match="finite"):
        simulate_lif(current, duration_ms=10.0, dt_ms=0.1)
