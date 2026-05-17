# ssot-pack-event-behavioral-telemetry

Installable SSOT governance pack for event envelopes, behavioral telemetry vocabularies, interaction events, and normalized event schemas.

This repository is an installable SSOT Registry governance pack. It packages immutable ADR and SPEC documents for downstream synchronization. It intentionally does not cross-link to other governance packs.

## Pack Metadata

- Pack ID: `pack:event-behavioral-telemetry`
- Priority: `P0.4`
- PyPI package: `ssot-pack-event-behavioral-telemetry`
- Import package: `ssot_pack_event_behavioral_telemetry`
- GitHub repository: `groupsum/event-behavioral-telemetry-governance-pack`
- Reservation owner: `extension-pack:ssot-pack-event-behavioral-telemetry`

## Domain Focus

Event Tracking And Behavioral Telemetry

## Authority Sources

- CloudEvents core, HTTP binding, and JSON event format
- OpenTelemetry specification, logs data model, and semantic conventions
- WHATWG DOM Events
- W3C UI Events, Pointer Events, and Input Events
- W3C Activity Streams and Activity Vocabulary
- Experience API / xAPI
- IMS Caliper Analytics
- Elastic Common Schema
- Open Cybersecurity Schema Framework
- Splunk Common Information Model
- IBM QRadar LEEF
- ArcSight Common Event Format

## Included ADRs

- `adr:event-envelope-authority-policy` - Event Envelope Authority Policy
- `adr:event-transport-and-serialization-policy` - Event Transport And Serialization Policy
- `adr:behavioral-event-taxonomy-policy` - Behavioral Event Taxonomy Policy
- `adr:web-interaction-event-policy` - Web Interaction Event Policy
- `adr:activity-stream-model-policy` - Activity Stream Model Policy
- `adr:learning-activity-telemetry-policy` - Learning Activity Telemetry Policy
- `adr:normalized-event-schema-policy` - Normalized Event Schema Policy
- `adr:event-identity-and-correlation-policy` - Event Identity And Correlation Policy

## Included SPECs

- `spc:cloudevents-envelope-contract` - CloudEvents Envelope Contract
- `spc:opentelemetry-event-contract` - OpenTelemetry Event Contract
- `spc:dom-ui-pointer-input-event-contract` - DOM UI Pointer Input Event Contract
- `spc:activity-streams-xapi-caliper-contract` - Activity Streams xAPI Caliper Contract

## Install With uv

```bash
uv add ssot-pack-event-behavioral-telemetry
uv add ssot-registry ssot-pack-event-behavioral-telemetry
```

## Use With The SSOT Registry CLI

```bash
uvx --from ssot-registry ssot pack install ssot-pack-event-behavioral-telemetry
uvx --from ssot-registry ssot pack sync . ssot-pack-event-behavioral-telemetry
uv run ssot adr list .
uv run ssot spec list .
```

## Programmatic Usage

```python
from ssot_pack_event_behavioral_telemetry import load_document_manifest

adr_manifest = load_document_manifest("adr")
spec_manifest = load_document_manifest("spec")
```

## Resources

- GitHub repository: https://github.com/groupsum/event-behavioral-telemetry-governance-pack
- PyPI package: https://pypi.org/project/ssot-pack-event-behavioral-telemetry/
- SSOT Registry: https://pypi.org/project/ssot-registry/
