#  a = abbaa
#  b = aacdabz
#  a2 = cdb
#  b2 = dab
def set_to_dict(m_set, m_str):
    m_dict = {}
    for c in m_set:
        m_dict[c]=m_str.count(c)
    return m_dict

def compare_dict(m_dict1, m_dict2):
    compare_sum = 0

    for key,value in m_dict1.items():
        if key in m_dict2:
            compare_sum += abs(value - m_dict2[key])
            del(m_dict2[key])
        else:
            compare_sum += value
    return compare_sum

def number_needed(a, b):
    set_a, set_b = set(a), set(b)
    dict_a = set_to_dict(set_a, a)
    dict_b = set_to_dict(set_b, b)
    #print(dict_a, dict_b)

    m_sum = compare_dict(dict_b, dict_a)
    m_sum += compare_dict(dict_a, dict_b)
    return m_sum

a = input().strip()
b = input().strip()

print(number_needed(a, b))
