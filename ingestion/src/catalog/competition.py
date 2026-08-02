from dataclasses import dataclass


@dataclass(frozen=True)
class Competition:
    
    competition_id: int
    competition_name: str
    country_name: str
    competition_gender: str
    competition_youth: bool
    competition_international: bool
