def get_feedback(mark):
    result = "Excellent"
    if mark <= 1:
        result = "very bad"
    elif 3 >= mark >= 2:
        result = "unsatisfactory"
    elif mark == 4:
        result = "satisfactory"
    elif 6 >= mark >= 5:
        result = "you could better"
    elif 8 >= mark >= 7:
        result = "good"
    return result

