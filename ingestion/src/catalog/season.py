from dataclasses import dataclass


@dataclass(frozen=True)
class Season:
    
    season_id: int
    season_name: str
    