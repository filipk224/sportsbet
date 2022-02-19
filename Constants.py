year_for_link=2022
legal_days_away=7

allowedSport=(
            'Australian Rules', 
            'Rugby League',
            'Basketball - Aus/Other',
            'Basketball - US',
            'Athletics',  # See what other it does outside Olympics
            'Canoeing', # If they do 4person outside of olympics
            'Gymnastics',
            'Rowing', # Might 4 person
            'Sport Climbing', # See if just climbing?
            'Badminton', # Watching if always non-team
            'Rugby Union',
            'Volleyball',
            'Handball',
            'Cricket',
            'American Football',
            'Netball',
            )

disallowedSport=({
            'Boxing': 'Not-team',
            'Chess': 'Non-team',
            'Cycling': 'Non-team',
            'Darts': 'Non-team',
            'Golf': 'Non-team',
            'Motor Racing': 'Non-team',
            'Politics': 'Non-team',
            'Snooker': 'Non-team',
            'Surfing': 'Non-team',
            'Table Tennis': 'Non-team',
            'Tennis': 'Non-team',
            'UFC - MMA': 'Non-team',
            'Archery': 'Non-team',
            'Fencing': 'Non-team',
            'Judo': 'Non-team',
            'Karate': 'Non-team',
            'Shooting': 'Non-team',
            'Sailing': 'Non-team',
            'Skateboarding': 'Non-team',
            'Soccer': 'Low Scoring',
            'Swimming': 'Non-team',
            'Taekwondo': 'Non-team',
            'Weightlifting': 'Non-team',
            'Wrestling': 'Non-team',
            'Diving': 'Non-team',
            'Artistic Swimming': 'Non-team',
            'Bowls': 'Non-team',
            'Equestrian': 'Non-team',
            'Modern Pentathlon': 'Non-team',
            'Novelties and Entertainment': 'Non-team',
            'Olympic Games': 'Too Competitive',
            'Triathlon': 'Non-team',
            'Sports Novelties': 'Not Sport',
            'Ice Hockey - US': 'Low Scoring',
            'Baseball': 'Low Scoring',
            'Cross Country': 'Non-team',
            'Ice Hockey - Other': 'Low Scoring',
            'Ski Jumping': 'Non-team',
            'Snowboarding': 'Non-team',
            'Curling': 'Non-team',
            })

disallowed_leagues = ({
            'International Friendly Men': 'Basketball - Aus/Other',  # Unreliable league
            'State of Origin': 'Rugby League',  # 2 Teams always
            'State of Origin - Man of the Match': 'Rugby League',  # Not a league
            "Men's Olympics 2020": 'Basketball - Aus/Other',  # Unreliable league
            "Men's Olympics 3x3 2020": 'Basketball - Aus/Other',  # Unreliable league
            "Women's Olympics 2020": 'Baskebtall - Aus/Other',  # Unreliable league
            "Women's Olympics 3x3 2020": 'Basketball - Aus/Other',  # Unreliable league
            'Rugby League Extra Markets': 'Rugby League',  # Extra's Market
            'NBA Draft Markets': 'Basketball - US',  # Not a league
            'The Basketball Tournament': 'Basketball - US',  # Not a league
            'AFL Team Futures Multis': 'Australian Rules',  # Not a league # Only standing can find needs selenium
            'Australian Big V Women': 'Basketball - Aus/Other',
            'NRL Team Futures Multis': 'Rugby League',  # Not a league
            'Euro Championship for Small Countries': 'Basketball - Aus/Other',  # Not a league
            'FIBA Asia Cup Qualifying': 'Basketball - Aus/Other',  # Not a league
            'European Championship Women': "Vollyball",  # Not a league
            'NORCECA Championship Men': 'Vollyball',  # Not a league
            'Italian Supercup': "Basketball - Aus/Other",  # Not a league
            'FIBA Champions League': "Basketball - Aus/Other",  # Not a league
            'FIBA Europe Cup': "Basketball - Aus/Other",  # Not a league
            'Lithuanian Cup': "Basketball - Aus/Other",  # Not a league
            'New Zealand NPC': "Rugby Union", # Found some teams play less through the league, not accurate
            'Slovenian Cup': "Basketball", # Not a league
            'Champions League Women': "Volleyball", # Not a league
            'Polish Cup Men': "Volleyball", # Not a league
            'Russian Cup': "Basketball", # Not a league
            'Turkish Federation Cup': "Basketball", # Not a league
            'Croatian Cup': "Basketball", # Not a league
            'Italian Cup Basketball': "Basketball", # Not a league
            'French Cup Basketball': "Basketball", # Not a league
        })