from ingestion.src.catalog.competition import Competition


def test_create_competition():
    
    competition = Competition(
        competition_id=14,
        competition_name='1. Bundesliga',
        country_name='Spain',
        competition_gender='male',
        competition_youth=False,
        competition_international=False,
    )
    
    assert competition.competition_id == 10
    assert competition.competition_name == '1. Bundesliga'
    