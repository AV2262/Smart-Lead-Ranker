def score_lead(title, size):
    title = title.lower()
    score = 0
    if any(t in title for t in ['ceo', 'founder', 'chief']):
        score += 5
    elif any(t in title for t in ['director', 'vp']):
        score += 4
    elif any(t in title for t in ['manager']):
        score += 3
    else:
        score += 1

    if size == 'Large':
        score += 3
    elif size == 'Medium':
        score += 2
    else:
        score += 1

    return score
