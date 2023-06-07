elapsed_time = current_time - start_time
        remaining_time = max(0, countdown - elapsed_time)
        seconds = remaining_time // 1000
        minutes = seconds // 60
        seconds %= 60