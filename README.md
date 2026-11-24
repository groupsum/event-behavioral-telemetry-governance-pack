# event-behavioral-telemetry-governance-pack

<!-- readme-standards:begin branding -->
<p align="center"><a href="https://github.com/groupsum/readme-standards"><img src="https://raw.githubusercontent.com/groupsum/readme-standards/master/docs/assets/readme-standards.svg" alt="Groupsum README Standards" width="300"></a></p>
<p align="center"><strong>event-behavioral-telemetry-governance-pack</strong></p>
<p align="center">Installable SSOT governance pack for event envelopes, behavioral telemetry vocabularies, interaction events, and normalized event schemas.</p>
<p align="center">
<a href="https://pypi.org/project/event-behavioral-telemetry-governance-pack/"><img alt="pypi: event-behavioral-telemetry-governance-pack" src="https://img.shields.io/pypi/v/event-behavioral-telemetry-governance-pack?labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/pyproject.toml"><img alt="Source version: 0.2.0.dev1" src="https://img.shields.io/static/v1?label=Source%20version&amp;message=0.2.0.dev1&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/pyproject.toml"><img alt="Python: &gt;=3.10,&lt;3.15" src="https://img.shields.io/static/v1?label=Python&amp;message=%3E%3D3.10%2C%3C3.15&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/pyproject.toml"><img alt="Layer: governance" src="https://img.shields.io/static/v1?label=Layer&amp;message=governance&amp;labelColor=1E293B&amp;color=6D28D9"></a>
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/README.md#lifecycle-and-migration"><img alt="Lifecycle: active" src="https://img.shields.io/static/v1?label=Lifecycle&amp;message=active&amp;labelColor=1E293B&amp;color=166534"></a>
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/LICENSE"><img alt="License: Apache-2.0" src="https://img.shields.io/static/v1?label=License&amp;message=Apache-2.0&amp;labelColor=1E293B&amp;color=86198F"></a>
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/README.md#notices"><img alt="Notice: not required" src="https://img.shields.io/static/v1?label=Notice&amp;message=not%20required&amp;labelColor=1E293B&amp;color=475569"></a>
</p>
<p align="center">
<a href="https://pypi.org/project/event-behavioral-telemetry-governance-pack/"><img alt="Monthly PyPI downloads: event-behavioral-telemetry-governance-pack" src="https://img.shields.io/pypi/dm/event-behavioral-telemetry-governance-pack?labelColor=1E293B&amp;color=0E7490"></a>
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/README.md"><img alt="README hits: event-behavioral-telemetry-governance-pack" src="https://hits.sh/github.com/groupsum/event-behavioral-telemetry-governance-pack/README.md.svg?label=README%20hits&amp;labelColor=1E293B&amp;color=0E7490"></a>
</p>
<p align="center">
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/actions/workflows/readme-standards.yml"><img alt="README standards: CI gate" src="https://img.shields.io/static/v1?label=README%20standards&amp;message=CI%20gate&amp;labelColor=1E293B&amp;color=1D4ED8"></a>
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/actions/workflows/readme-standards.yml"><img alt="Tests: package and example checks" src="https://img.shields.io/static/v1?label=Tests&amp;message=package%20and%20example%20checks&amp;labelColor=1E293B&amp;color=0F766E"></a>
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/README.md#certification-status"><img alt="Certification: not certified" src="https://img.shields.io/static/v1?label=Certification&amp;message=not%20certified&amp;labelColor=1E293B&amp;color=92400E"></a>
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/docs/governance/pack-authoring-guide.md"><img alt="Governance: pack governance" src="https://img.shields.io/static/v1?label=Governance&amp;message=pack%20governance&amp;labelColor=1E293B&amp;color=4338CA"></a>
<a href="https://github.com/groupsum/event-behavioral-telemetry-governance-pack/actions/workflows/readme-standards.yml"><img alt="Evidence: README and wheel checks" src="https://img.shields.io/static/v1?label=Evidence&amp;message=README%20and%20wheel%20checks&amp;labelColor=1E293B&amp;color=6D28D9"></a>
</p>
<p align="center"><a href="#overview">Overview</a> · <a href="#installation">Installation</a> · <a href="#quick-start">Quick Start</a> · <a href="#usage">Usage</a> · <a href="#public-api-and-import-surfaces">API</a> · <a href="#contributing">Contributing</a> · <a href="#governance">Governance</a> · <a href="#license">License</a></p>
<!-- readme-standards:end branding -->

---

## Overview

### Summary

Installable SSOT governance pack for event envelopes, behavioral telemetry vocabularies, interaction events, and normalized event schemas.

### Why This Package

Use this package when a downstream repository needs to answer: which standards, specifications, or compliance targets govern event tracking and behavioral telemetry, which ADRs should capture the target policy choices, and which SPECs should define implementation-ready conformance requirements.

### When to Use

Use this pack when a downstream SSOT Registry needs reusable decisions and requirements for Event Tracking And Behavioral Telemetry.

### Features

**Included ADRs**

- [`adr:event-envelope-authority-policy`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/adr/ADR-1001-event-envelope-authority-policy.yaml) — Event Envelope Authority Policy
- [`adr:event-transport-and-serialization-policy`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/adr/ADR-1002-event-transport-and-serialization-policy.yaml) — Event Transport And Serialization Policy
- [`adr:behavioral-event-taxonomy-policy`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/adr/ADR-1003-behavioral-event-taxonomy-policy.yaml) — Behavioral Event Taxonomy Policy
- [`adr:web-interaction-event-policy`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/adr/ADR-1004-web-interaction-event-policy.yaml) — Web Interaction Event Policy
- [`adr:activity-stream-model-policy`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/adr/ADR-1005-activity-stream-model-policy.yaml) — Activity Stream Model Policy
- [`adr:learning-activity-telemetry-policy`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/adr/ADR-1006-learning-activity-telemetry-policy.yaml) — Learning Activity Telemetry Policy
- [`adr:normalized-event-schema-policy`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/adr/ADR-1007-normalized-event-schema-policy.yaml) — Normalized Event Schema Policy
- [`adr:event-identity-and-correlation-policy`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/adr/ADR-1008-event-identity-and-correlation-policy.yaml) — Event Identity And Correlation Policy
- [`adr:cloudevents-envelope-and-binding-are-owned-here`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/adr/ADR-1009-cloudevents-envelope-and-binding-are-owned-here.yaml) — Cloudevents Envelope And Binding Are Owned Here

**Included SPECs**

- [`spc:cloudevents-core-envelope-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2001-cloudevents-core-envelope-requirements.yaml) — CloudEvents Core Envelope Requirements
- [`spc:cloudevents-http-binding-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2002-cloudevents-http-binding-requirements.yaml) — CloudEvents HTTP Binding Requirements
- [`spc:cloudevents-json-format-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2003-cloudevents-json-format-requirements.yaml) — CloudEvents JSON Format Requirements
- [`spc:opentelemetry-event-data-model-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2004-opentelemetry-event-data-model-requirements.yaml) — OpenTelemetry Event Data Model Requirements
- [`spc:opentelemetry-browser-event-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2005-opentelemetry-browser-event-requirements.yaml) — OpenTelemetry Browser Event Requirements
- [`spc:dom-event-model-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2006-dom-event-model-requirements.yaml) — DOM Event Model Requirements
- [`spc:ui-event-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2007-ui-event-requirements.yaml) — UI Event Requirements
- [`spc:pointer-event-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2008-pointer-event-requirements.yaml) — Pointer Event Requirements
- [`spc:input-event-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2009-input-event-requirements.yaml) — Input Event Requirements
- [`spc:activity-streams-core-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2010-activity-streams-core-requirements.yaml) — Activity Streams Core Requirements
- [`spc:activity-vocabulary-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2011-activity-vocabulary-requirements.yaml) — Activity Vocabulary Requirements
- [`spc:xapi-statement-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2012-xapi-statement-requirements.yaml) — xAPI Statement Requirements
- [`spc:ims-caliper-event-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2013-ims-caliper-event-requirements.yaml) — IMS Caliper Event Requirements
- [`spc:elastic-common-schema-event-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2014-elastic-common-schema-event-requirements.yaml) — Elastic Common Schema Event Requirements
- [`spc:ocsf-event-schema-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2015-ocsf-event-schema-requirements.yaml) — OCSF Event Schema Requirements
- [`spc:splunk-cim-event-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2016-splunk-cim-event-requirements.yaml) — Splunk CIM Event Requirements
- [`spc:qradar-leef-event-format-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2017-qradar-leef-event-format-requirements.yaml) — QRadar LEEF Event Format Requirements
- [`spc:arcsight-cef-event-format-requirements`](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates/specs/SPEC-2018-arcsight-cef-event-format-requirements.yaml) — ArcSight CEF Event Format Requirements

### Non-Goals

The pack supplies governance records. A downstream application implements the controls and collects its own conformance evidence.

---

## Getting Started

### Prerequisites

Use Python `>=3.10,<3.15`. Downstream synchronization also requires SSOT Registry and permission to write the target registry.

### Installation

If the desired PyPI release is a prerelease, use its exact version in the installer command.

#### uv

<!-- readme-standards:begin installation.uv -->
```bash
uv add event-behavioral-telemetry-governance-pack
```
<!-- readme-standards:end installation.uv -->

#### pip

<!-- readme-standards:begin installation.pip -->
```bash
python -m pip install event-behavioral-telemetry-governance-pack
```
<!-- readme-standards:end installation.pip -->

#### Poetry

<!-- readme-standards:begin installation.poetry -->
```bash
poetry add event-behavioral-telemetry-governance-pack
```
<!-- readme-standards:end installation.poetry -->

### Quick Start

#### Example

<!-- readme-standards:begin example.quick-start -->
Source: [examples/quick_start.py](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/examples/quick_start.py).

```python
"""Inspect the installed pack identity."""

from ssot_pack_event_behavioral_telemetry import load_pack_metadata

metadata = load_pack_metadata()
assert metadata["origin"]["id"] == "pack:event-behavioral-telemetry"
print(metadata["origin"]["id"])
```
<!-- readme-standards:end example.quick-start -->

#### Expected Result

The script prints `pack:event-behavioral-telemetry` from the installed pack metadata.

---

## Usage

### Common Workflows

<!-- readme-standards:begin example.usage -->
Source: [examples/usage.py](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/examples/usage.py).

```python
"""Resolve and read a packaged specification without synchronizing it."""

from ssot_pack_event_behavioral_telemetry import load_document_manifest, read_packaged_document_text

spec = next(row for row in load_document_manifest("spec") if row["id"] == "spc:cloudevents-core-envelope-requirements")
document = read_packaged_document_text("spec", spec["filename"])
assert spec["id"] in document
```
<!-- readme-standards:end example.usage -->

Use the downstream environment that has both SSOT Registry and `event-behavioral-telemetry-governance-pack` installed. Inspect the pack and preflight the target registry before approving synchronization.

```bash
uv run ssot pack inspect ssot_pack_event_behavioral_telemetry
uv run ssot pack preflight . ssot_pack_event_behavioral_telemetry --all
uv run ssot pack sync . ssot_pack_event_behavioral_telemetry --all --trust --yes
uv run ssot validate .
```

### Configuration

Select the installed import package `ssot_pack_event_behavioral_telemetry` in SSOT Registry. Review reservation owner `extension-pack:event-behavioral-telemetry-governance-pack` and the target's trust policy before syncing.

### Error Handling

If preflight reports a schema, trust, or document-number conflict, resolve it in the target registry and repeat preflight before synchronization.

### Best Practices

Pin the pack version in downstream projects. Reference document IDs in local governance and inspect the change set before granting trust.

---

## Package Boundary

### What It Owns

Declared canonical CloudEvents ownership relative to catalog lineage.

### Public API and Import Surfaces

Import `load_pack_metadata`, `load_document_manifest`, and `read_packaged_document_text` from `ssot_pack_event_behavioral_telemetry` to inspect packaged records.

### Entry Points

<!-- readme-standards:begin entry-points -->
This package declares no command-line, GUI, or plugin entry points in its manifest.
<!-- readme-standards:end entry-points -->

### Injected Dependencies

The package binds its metadata and document loaders through `ssot-pack-contracts`. The caller supplies the target registry to SSOT Registry when synchronizing.

### Protocol Consumers

SSOT Registry uses the pack metadata, document manifests, and bundled templates during inspect, preflight, and sync.

### Extensions

Define downstream policies as local records and reference the pack's document IDs. Send proposed changes to the canonical pack through repository review.

---

## Operations and Readiness

### Operational Requirements

Local inspection reads installed package resources. Synchronization requires an initialized downstream registry and explicit operator approval.

### Health and Observability

Review the preflight and sync output, then use `ssot validate` to check the resulting registry.

### Security and Resource Limits

Implicit trust is disabled. Review the exact distribution, version, records, and reserved IDs before enabling trust in a target registry.

### Compatibility

- Python `>=3.10,<3.15`
- SSOT Registry schema `>=0.4.0`
- SSOT pack contracts `>=0.2.17,<0.3.0`

---

## Verification

### Tests

Run `python -m unittest discover -s tests -v` with the pack installed. The [README workflow](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/actions/workflows/readme-standards.yml) checks the source README and runs both examples against an installed wheel.

### Certification Status

The pack has no external certification. Downstream adoption requires evidence for the controls an application implements.

### Evidence

See the [README workflow](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/actions/workflows/readme-standards.yml) for package and documentation verification and the [packaged records](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/templates) for document-level sources.

---

## FAQ

### Why

**Why do document IDs matter?** Downstream records use them to trace an adopted decision or requirement to the pack that owns it.

### How

**How do I preview changes?** Use the registry's pack preflight before approving a sync.

### When

**When should I upgrade?** Read the changelog and preflight the new version against the target registry before applying it.

---

## Documentation and Related Packages

### More Documentation

See the [Pack guide](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/docs/pack-guide.md), [changelog](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/CHANGELOG.md), and [pack metadata](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/src/ssot_pack_event_behavioral_telemetry/metadata.json).

### Related Packages

[SSOT Registry](https://pypi.org/project/ssot-registry/) manages downstream registries. [SSOT Pack Contracts](https://pypi.org/project/ssot-pack-contracts/) provides the shared pack interface.

### Project Links

<!-- readme-standards:begin project-links -->
- [Homepage](https://github.com/groupsum/event-behavioral-telemetry-governance-pack)
- [Issues](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/issues)
- [Repository](https://github.com/groupsum/event-behavioral-telemetry-governance-pack)
- [pypi: event-behavioral-telemetry-governance-pack](https://pypi.org/project/event-behavioral-telemetry-governance-pack/)
<!-- readme-standards:end project-links -->

---

## Contributing

### How to Contribute

Open an [issue](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/issues) or pull request describing the affected records, their authority, and the expected downstream effect.

### Development Setup

Install the checkout with `python -m pip install -e .`, then run `python -m unittest discover -s tests -v`. On Python 3.11 or newer, run `uvx --from readme-standards==0.1.3 readme-standards check`.

### Notes for Maintainers

Keep source links, document identifiers, and committed manifest hashes aligned. Run `uvx --from readme-standards==0.1.3 readme-standards render --write` after changing generated README inputs.

---

## Governance

### Ownership and Decision Making

Groupsum maintains `pack:event-behavioral-telemetry`. The pack's reservation owner is `extension-pack:event-behavioral-telemetry-governance-pack`. Downstream registry operators approve synchronization.

### Standards and Policies

**Authority Sources**

- [CloudEvents core](https://github.com/cloudevents/spec/blob/main/cloudevents/spec.md), [HTTP binding](https://github.com/cloudevents/spec/blob/main/cloudevents/bindings/http-protocol-binding.md), and [JSON event format](https://github.com/cloudevents/spec/blob/main/cloudevents/formats/json-format.md)
- [OpenTelemetry specification](https://opentelemetry.io/docs/specs/), [logs data model](https://opentelemetry.io/docs/specs/otel/logs/data-model/), and [semantic conventions](https://opentelemetry.io/docs/specs/semconv/)
- [WHATWG DOM Events](https://dom.spec.whatwg.org/#events)
- [W3C UI Events](https://www.w3.org/TR/uievents/), [Pointer Events](https://www.w3.org/TR/pointerevents/), and [Input Events](https://w3c.github.io/input-events/)
- [W3C Activity Streams](https://www.w3.org/TR/activitystreams-core/) and [Activity Vocabulary](https://www.w3.org/TR/activitystreams-vocabulary/)
- [Experience API / xAPI](https://xapi.com/specification/)
- [IMS Caliper Analytics](https://www.imsglobal.org/spec/caliper/v1p2/)
- [Elastic Common Schema](https://www.elastic.co/docs/reference/ecs/)
- [Open Cybersecurity Schema Framework](https://ocsf.io/)
- [Splunk Common Information Model](https://help.splunk.com/en/splunk-enterprise-security-8/common-information-model/8.5/introduction/overview-of-the-splunk-common-information-model)
- [IBM QRadar LEEF](https://www.ibm.com/docs/en/qsip/7.5?topic=leef-overview)
- [ArcSight Common Event Format](https://docs.delinea.com/online-help/cloud-suite/siem-integrations/arcsight-cef/arcsight-cef-format.htm)

### Lifecycle and Migration

Review [release changes](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/CHANGELOG.md) and preflight the chosen version against each downstream registry.

---

## License and Attribution

### License

<!-- readme-standards:begin license -->
Licensed under `Apache-2.0`. See [LICENSE](https://github.com/groupsum/event-behavioral-telemetry-governance-pack/blob/master/LICENSE).
<!-- readme-standards:end license -->

### Notices

<!-- readme-standards:begin notices -->
No separate NOTICE file is declared. Review the license and bundled third-party attributions.
<!-- readme-standards:end notices -->
