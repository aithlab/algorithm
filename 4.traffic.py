def solution(lines):
    data, intervals, init_t = [],[], -1
    for line in lines:
        _, end_t, elapsed_t = line.split(' ')
        h,m,s = map(float, end_t.split(':'))
        end_t = h*60*60+m*60+s
        elapsed_t = float(elapsed_t.split('s')[0])
        start_t = end_t - elapsed_t + 0.001
        
        data.append([start_t, end_t])
        intervals.append([start_t, start_t+1, 0])
        intervals.append([end_t, end_t+1, 0])

    max_tps = 0
    for start_t, end_t, cnt in intervals:
        for log in data:
            log_s_t, log_e_t = log
            if start_t<= log_s_t < end_t or \
                start_t<= log_e_t < end_t or \
                 log_s_t < start_t and log_e_t > end_t:
                cnt += 1
        if cnt > max_tps:
            max_tps = cnt 

    return max_tps