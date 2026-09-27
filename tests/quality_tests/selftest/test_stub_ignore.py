"""Guard rails for the `stubs-ignore` conditions used in test metadata and snippets."""

import pytest
import test_snippets
import typecheck


def _all_conditions():
    """Yield every `<name>:<condition>` condition used in PORTBOARD_FEATURES."""
    for key, features in test_snippets.PORTBOARD_FEATURES.items():
        if ":" in key:
            yield key, key.split(":", 1)[1]
        for feature in features:
            if ":" in feature:
                yield feature, feature.split(":", 1)[1]


@pytest.mark.parametrize("source, condition", list(_all_conditions()), ids=lambda v: str(v))
def test_portboard_conditions_are_valid(source, condition):
    """Every condition in PORTBOARD_FEATURES must evaluate to a bool without errors."""
    assert isinstance(
        typecheck.stub_ignore(condition, "1.24.0", "rp2", "rpi_pico", linter="pytest", is_source=False, strict=True),
        bool,
    ), source


@pytest.mark.parametrize(
    "condition",
    [
        "version=<1.24.0",  # `=<` is not a python operator
        "version",  # truncated condition, evaluates to a Version instance
        "port ==",  # incomplete expression
    ],
)
def test_malformed_condition_raises_in_strict_mode(condition):
    with pytest.raises(ValueError):
        typecheck.stub_ignore(condition, "1.24.0", "rp2", "rpi_pico", linter="pytest", is_source=False, strict=True)


def test_malformed_condition_is_tolerated_without_strict(caplog):
    assert not typecheck.stub_ignore("version=<1.24.0", "1.24.0", "rp2", "rpi_pico", linter="pytest", is_source=False)
