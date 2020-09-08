def calculate_frequencies(file_contents):
    """Frequency count dict for generating wordcloud."""
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    frequencies = {}
    for line in file_contents:
        line = line.split()
        for word in line:
            for char in word:
                if word not in uninteresting_words and char.isalpha():
                    if word not in frequencies:
                        frequencies[word] = 1
                    else:
                        frequencies[word] += 1




    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()
