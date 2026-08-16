from __future__ import annotations

from dataclasses import dataclass
from enum import Enum


class EvidenceState(str, Enum):
    PASS = "PASS"
    HOLD = "HOLD"
    NOT_ESTABLISHED = "NOT_ESTABLISHED"


class AuthorityDeltaState(str, Enum):
    EXPLAINED = "EXPLAINED"
    NO_MATERIAL_DELTA = "NO_MATERIAL_DELTA"
    HOLD = "HOLD"


class AuthorityDeltaDiagnostic(str, Enum):
    UNEXPLAINED_AUTHORITY_DELTA = "UNEXPLAINED_AUTHORITY_DELTA"


@dataclass(frozen=True)
class CapabilityIdentity:
    capability_id: str
    action: str
    resource: str


@dataclass(frozen=True)
class AuthorityGrantEvidence:
    grant_id: str
    issuer: str
    covered_capability_ids: tuple[str, ...]
    covered_composition_ids: tuple[str, ...] = ()
    covered_resulting_capabilities: tuple[str, ...] = ()


@dataclass(frozen=True)
class CompositionEvidence:
    composition_id: str
    component_capability_ids: tuple[str, ...]
    resulting_capability_id: str


@dataclass(frozen=True)
class MaterialDeltaEvidence:
    present: bool
    dimensions: tuple[str, ...]


@dataclass(frozen=True)
class CapabilityFinding:
    capability_id: str
    state: EvidenceState


@dataclass(frozen=True)
class ComponentAuthorityFinding:
    capability_id: str
    state: EvidenceState
    grant_ids: tuple[str, ...]


@dataclass(frozen=True)
class CompositionFinding:
    composition_id: str
    state: EvidenceState
    resulting_capability_id: str


@dataclass(frozen=True)
class MaterialDeltaFinding:
    composition_id: str
    state: EvidenceState
    dimensions: tuple[str, ...]


@dataclass(frozen=True)
class CompositionAuthorityFinding:
    composition_id: str
    state: EvidenceState
    grant_ids: tuple[str, ...]


@dataclass(frozen=True)
class AuthorityBasisFinding:
    authority_basis_id: str
    composition_id: str
    resulting_capability_id: str
    state: EvidenceState


@dataclass(frozen=True)
class AuthorityCompetenceFinding:
    authority_basis_id: str
    state: EvidenceState


@dataclass(frozen=True)
class AuthorityScopeFinding:
    authority_basis_id: str
    composition_id: str
    resulting_capability_id: str
    state: EvidenceState


@dataclass(frozen=True)
class AuthorityDeltaFinding:
    composition_id: str
    state: AuthorityDeltaState
    diagnostics: tuple[AuthorityDeltaDiagnostic, ...]
    explanation_authority_basis_ids: tuple[str, ...]
