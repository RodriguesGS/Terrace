from ingestion.src.catalog.season import Season


def test_create_season():
    
    season = Season(
        season_id=24,
        season_name='2023/2024'
    )
    
    assert season.season_id == 24
    assert season.season_name == '2023/2024'
