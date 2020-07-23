from nltk import pos_tag
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import  word_setting

ps = PorterStemmer()


# process the job description.
def prepare_job_desc(desc):
    # tokenize description.
    tokens = word_tokenize(desc)

    # Parts of speech (POS) tag tokens.
    token_tag = pos_tag(tokens)

    # Only include some of the POS tags.
    include_tags = ['VBN', 'VBD', 'JJ', 'JJS', 'JJR', 'CD', 'NN', 'NNS', 'NNP', 'NNPS']
    filtered_tokens = [tok for tok, tag in token_tag if tag in include_tags]

    # stem words.
    stemmed_tokens = [ps.stem(tok).lower() for tok in filtered_tokens]
    return set(stemmed_tokens)

# process the keywords
tool_keywords1_set = set(
    [ps.stem(tok) for tok in word_setting.tool_keywords1])  # stem the keywords (since the job description is also stemmed.)
tool_keywords1_dict = {ps.stem(tok): tok for tok in
                       word_setting.tool_keywords1}  # use this dictionary to revert the stemmed words back to the original.

skill_keywords1_set = set([ps.stem(tok) for tok in word_setting.skill_keywords1])
skill_keywords1_dict = {ps.stem(tok): tok for tok in word_setting.skill_keywords1}

degree_keywords1_set = set([ps.stem(tok) for tok in word_setting.degree_dict.keys()])
degree_keywords1_dict = {ps.stem(tok): tok for tok in word_setting.degree_dict.keys()}

# print(degree_keywords1_dict)
#print(degree_keywords1_set)