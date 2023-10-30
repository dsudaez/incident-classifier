from src.mining.preprocessing.normalization import Normalization

def preprocess(incidencia):
    normalization = Normalization()
    incidencia = normalization.normalize(incidencia);

    return incidencia

    ## Tokenization
    # tokens = custom_tokenize(inc, keep_alnum=False, keep_stop=False) # tokenize
    #CONSULTAR SI UTILIZAR SNOWBALLSTEMMER O PorterStemmr
    #stemmer = SnowballStemmer("spanish") # define stemmer
    #stemmer = PorterStemmer()
    #stem = stem_tokens(tokens, stemmer) # stem tokens