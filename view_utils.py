def parse_ta_data(data):
    speaker_map = {
        'English speaker': 1,
        'non-English speaker': 2,
        '1': 'English speaker',
        '2': 'non-English speaker'
    }
    semester_map = {
        'Summer': 1,
        'Regular': 2,
        '1': 'Summer',
        '2': 'Regular'
    }
    score_map = {
        'Low': 1,
        'Medium': 2,
        'High': 3,
        '1': 'Low',
        '2': 'Medium',
        '3': 'High'
    }

    for key, value in data.items():
        if key == 'native_english_speaker':
            data[key] = speaker_map[str(value)]
        elif key == 'semester':
            data[key] = semester_map[str(value)]
        elif key == 'performance_score':
            data[key] = score_map[str(value)]

    return data
