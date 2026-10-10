"""MiniCPM-Math: a proof swarm harness for MiniCPM5-2B-Math."""

__version__ = "0.1.2"

from .client import Backend, Generation
from .swarm import PROFILES, AnswerResult, Candidate, ProofResult, Swarm, SwarmConfig, config_for

__all__ = [
    "AnswerResult", "Backend", "Candidate", "Generation", "PROFILES", "ProofResult", "Swarm", "SwarmConfig",
    "config_for", "__version__",
]
