from dataclasses import dataclass

@dataclass
class Competition:
    
    competition_id: int
    competition_name: str
    competition_international: bool
    competition_gender: str
    competition_youth: bool
    country_name: str