def study_schedule(permanence_period, target_time):
    """Faça o código aqui."""
    count = 0
    if target_time:
        for period in permanence_period:
            if all(isinstance(period, int) for period in period):
                if period[0] <= target_time <= period[1]:
                    count += 1
            else:
                return
        return count