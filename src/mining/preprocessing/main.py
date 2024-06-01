from src.mining.preprocessing.normalization import Normalization

def preprocess(df, columna):
    normalization = Normalization()
    df[columna] = df[columna].apply(normalization.normalize)

    ## Tokenization
    # tokens = custom_tokenize(inc, keep_alnum=False, keep_stop=False) # tokenize
    #CONSULTAR SI UTILIZAR SNOWBALLSTEMMER O PorterStemmr
    #stemmer = SnowballStemmer("spanish") # define stemmer
    #stemmer = PorterStemmer()
    #stem = stem_tokens(tokens, stemmer) # stem tokens