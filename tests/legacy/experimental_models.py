from __future__ import annotations

from dataclasses import dataclass

from authority_composition_experiment.models import EvidenceState


@dataclass(frozen=True)
class AuthorityGrantEvidence:
    """
    Legacy experimental authority-grant evidence.

    Preserved for pre-v0.1 experimental lineage only.
    """

    grant_id: str
    issuer: str
    covered_capability_ids: tuple[str, ...]
    covered_composition_ids: tuple[str, ...] = ()
    covered_resulting_capabilities: tuple[str, ...] = ()


@dataclass(frozen=True)
class ComponentAuthorityFinding:
    """
    Legacy experimental component-authority finding.

    Not part of the frozen v0.1 inspector contract.
    """

    capability_id: str
    state: EvidenceState
    grant_ids: tuple[str, ...]


@dataclass(frozen=True)
class CompositionAuthorityFinding:
    """
    Legacy experimental composition-authority finding.

    Superseded by independent AuthorityBasisFinding,
    AuthorityCompetenceFinding, and AuthorityScopeFinding.
    """

    composition_id: str
    state: EvidenceState
    grant_ids: tuple[str, ...]
