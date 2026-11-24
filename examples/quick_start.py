"""Inspect the installed pack identity."""

from ssot_pack_event_behavioral_telemetry import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:event-behavioral-telemetry"
print(metadata["origin"]["id"])
