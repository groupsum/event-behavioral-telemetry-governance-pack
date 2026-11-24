"""Find a specification and its downstream path in the installed manifest."""

from ssot_pack_event_behavioral_telemetry import load_document_manifest

specification = next(
    row for row in load_document_manifest("spec")
    if row["id"] == "spc:cloudevents-core-envelope-requirements"
)
assert specification["target_path"] == ".ssot/specs/SPEC-2001-cloudevents-core-envelope-requirements.yaml"
