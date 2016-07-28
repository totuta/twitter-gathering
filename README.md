# twitter-gathering #

### What is this repository for? ###

* Quick summary

	* gather and store tweets by Twitter Search API
 
* Version

	* v0.1 : basic extraction of triples(ROOT, relation, WORD) from the huge wackypedia_en data
	* v0.2 : rules added
		* ignore punctuation
		* ignore stop-words
		* ignore be-verbs
		* ignore have-verb
		* include any verbs with child(ren)
		* use lemma for verbs
		* output format : quadruples(ROOT or V, lemma(of ROOT or V), relation, WORD)
	* v0.3 : context extraction
		* make context database
			* format: word relation (word1 count word2 count word3 count..)
			* TO-BE-FILLED
	* v0.4 : add preposition info to context

		

### How do I get set up? ###

* Summary of set up
	* Just git clone and python wacky_extract.py
* Configuration
	* NO configuration needed
* Dependencies
	* NLTK : stopwords
* Database configuration
	* TBD
* How to run tests
	* python wacky_extract.py --small True
		* This will process 20,000 lines sample from Wackypedia

### Example ###

* command

> python twitter-gathering.py


* original data


* output


### Who do I talk to? ###

* Repo owner or admin
	* totuta