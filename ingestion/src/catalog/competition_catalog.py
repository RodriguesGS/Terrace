import sys
from pathlib import Path

sys.path.append(r"C:\Users\User\Documents\Codes\Terrace")

from ingestion.src.fetchers.statsbomb_fetcher import StatsBombFetcher
from ingestion.src.catalog.competition import Competition


class CompetitionCatalog:
    
    def __init__(self, fetcher: StatsBombFetcher):
        
        self.fetcher = fetcher
    
    def list_competitions(self) -> list[Competition]: 
        
        data = self.fetcher.fetch_competitions()
        
        print(data.columns)
        print(data.to_dict('records')[0])
        

fetcher = StatsBombFetcher()
catalog = CompetitionCatalog(fetcher)

catalog.list_competitions()