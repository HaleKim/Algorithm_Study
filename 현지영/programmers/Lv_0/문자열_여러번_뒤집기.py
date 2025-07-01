def solution(my_string, queries):
    m_list = list(my_string)
    for s,e in queries :
        m_list[s:e+1] = list(reversed(m_list[s:e+1]))
    return ''.join(m_list)