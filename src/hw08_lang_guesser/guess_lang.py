from hw08_lang_guesser.model_bigram_lang import LangBigramModeler
from nltk.corpus import udhr


languages = ['English', 'German_Deutsch', 'French_Francais']

# udhr corpus contains the Universal Declaration of Human Rights in over 300 languages
language_base = dict((language, udhr.words(language + '-Latin1')) for language in languages)

# build the language models
langModeler = LangBigramModeler(languages, language_base)
language_model_cfd = langModeler.build_language_models()


# print the models for visual inspection (you always should have a look at the data :)
for language in languages:
    for key in list(language_model_cfd[language].keys())[:10]:
        print(language, key, "->", language_model_cfd[language].freq(key))

text1 = "Peter had been to the office before they arrived."
text2 = "Si tu finis tes devoirs, je te donnerai des bonbons."
text3 = "Das ist ein schon recht langes deutsches Beispiel."

# guess the language by comparing the frequency distributions
print("\n")
print(text1+" -> "+langModeler.guess_language(language_model_cfd, text1)+"\n") # English 2.88

print(text2+" -> "+langModeler.guess_language(language_model_cfd, text2)+"\n") # French_Francais 2.74

print(text3+" -> "+langModeler.guess_language(language_model_cfd, text3)+"\n") # German_Deutsch 3.03
