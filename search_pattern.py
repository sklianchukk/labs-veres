def search_pattern(text, pattern):
    m, n = len(pattern), len(text)
    indices = []
    comparisons = 0

    for i in range(n - m + 1):
        j = 0
        while j < m and text[i + j] == pattern[j]:
            comparisons += 1
            j += 1

        if j < m:
            comparisons += 1

        if j == m:
            indices.append(i)

    if indices:
        return f"Last pattern was found at {indices[-1]} and were done {comparisons} comparisons"
    else:
        return "Pattern not found"