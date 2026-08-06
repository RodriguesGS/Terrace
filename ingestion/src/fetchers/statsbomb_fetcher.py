import pandas as pd

from statsbombpy import sb


class StatsBombFetcher:
    
    def fetch_competitions(self) -> pd.DataFrame:
        return sb.competitions()
        