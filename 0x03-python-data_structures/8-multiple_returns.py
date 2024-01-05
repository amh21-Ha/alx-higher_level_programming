#!/usr/bin/python3

def multiple_returns(sentence):
    m_tuple = ()
    if len(sentence) == 0:
        m_tuple = 0, "None"
    else:
        m_tuple = len(sentence), sentence[0]
    return m_tuple
