from ingestion.src.catalog.competition import Competition

def test_create_competition():
    
    competition = Competition(
        competition_id=14,
        competition_name='1. Bundesliga',
        competition_international=False,
        competition_gender='male',
        competition_youth=False,
        country_name='Spain',
    )
    
    assert competition.competition_id == 10
    assert competition.competition_name == '1. Bundesliga'
    