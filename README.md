# retina-sdk.py - A Python Client for the Cortical.io Retina API

Pure Python wrapper library for [Cortical.io's Retina API](http://api.cortical.io/). Register for a 
[free API key](http://www.cortical.io/resources_apikey.html) and include retina-sdk.py to add language intelligence to 
your application.

## Introduction

Cortical.io's Retina API allows the user to perform semantic operations on text. One can for example:

* measure the semantic similarity between two written entities
* create a semantic classifier based on positive and negative example texts
* extract keywords from a text
* divide a text into sub-sections corresponding to semantic changes
* extract terms from a text based on part of speech tags

The meaning of terms and texts is stored in a sparse binary representation that allows the user to apply logical 
operators to refine the semantic representation of a concept.

You can read more about the technology at the [documentation page](http://documentation.cortical.io/intro.html).

To access the API, you will need to register for an [API key](http://www.cortical.io/resources_apikey.html).


## Installation

The client is available on [PyPI](https://pypi.python.org/pypi) and can be installed via 
[pip](https://pip.pypa.io/en/stable/) by running the following command in your terminal:

`pip install retinasdk`

This will pull in the [`requests`](http://docs.python-requests.org/en/latest/) library as well. 

The client has been tested with Python versions 2.6, 2.7 and 3.4. It is compatible with 2.x.x versions of 
[cortical.io's api](http://api.cortical.io)</a>.


## Usage

**retina-sdk.py** offers two abstractions of the Cortical.io Retina API, a lightweight module that offers simplified 
access to the most common and useful API functions available and a full version module that gives the user complete 
control over various parameter settings and complete access to all API endpoints.
 
### LiteClient Module

The LiteClient module is sufficient for most applications and offers the ability to quickly and easily 
compute keywords for a text, semantically compare two texts, retrieve similar terms, create category filters for 
semantic filtering and generate semantic fingerprints of a given text. To get started, create an instance of the 
lightweight client by passing your API key as follows:  

```python
import retinasdk
liteClient = retinasdk.LiteClient("your_api_key")
```

The `LiteClient` object has 5 methods for accessing the API. You can:

* Convert text into a semantic fingerprint, which is a list of integers (here shortened):
```python
>>> liteClient.getFingerprint("Python is a widely used general-purpose, high-level programming language.")
[1, 3, 7, 8, 33, 35, 65, 66, 68, 69, 70, 71, 72, 77, 79, 89, 117, ..., 16380, 16381, 16382]
```


* Retrieve similar terms for a text (or a fingerprint):
```python
>>> liteClient.getSimilarTerms("python")
['python', 'perl', 'implementations', 'compiler', 'javascript', 'programmers', 'runtime', 'unix', 'php', 'api', 'gui', 'java', 'object-oriented', 'executable', 'functionality', 'compilers', 'scripting', 'programmer', 'plugins', 'interface']
```

* Get the keywords of a text:
```python
>>> liteClient.getKeywords("Vienna is the capital and largest city of Austria, and one of the nine states of Austria")
['austria', 'vienna']
```

* Compute the similarity (in the range [0;1]) between two texts (here just terms to keep the example short), or 
any combination of texts and fingerprints:
```python
>>> liteClient.compare("apple", "microsoft")
0.4024390243902438
>>> liteClient.compare(liteClient.getFingerprint("apple"), liteClient.getFingerprint("microsoft"))
0.4024390243902438
>>> liteClient.compare(liteClient.getFingerprint("apple"), "microsoft")
0.4024390243902438
```

* Construct a composite Fingerprint from a list of texts (here just terms to keep the example short), and use
 the filter to compare and classify new texts:
```python
neurologyFilter = liteClient.createCategoryFilter(["neuron", "synapse", "neocortex"])
>>> liteClient.compare(neurologyFilter, "cortical column")
0.35455851788907006 # high semantic similarity -> poitive classification
>>> liteClient.compare(neurologyFilter, "skylab")
0.056544622895956895 # low semantic similarity -> negative classification
```

### FullClient Module

Using this client, you will have access to the full functionality of 
[Cortical.io's Retina API](http://api.cortical.io/). 

As with the LiteClient, the FullClient must be instantiated with a valid Cortical.io API key, but you can also change 
the default host address (in case you have your own 
[AWS](https://aws.amazon.com/marketplace/seller-profile?id=c88ca878-a648-464c-b29b-38ba057bd2f5) or 
[Azure](https://azure.microsoft.com/en-us/marketplace/partners/cortical-io/cortical-io-retinaservice-eng-gen/) instance),
as well as which retina to use.

```python
import retinasdk
fullClient = retinasdk.FullClient("your_api_key", apiServer="http://api.cortical.io/rest", retinaName="en_associative")
```

On the full client, you get responses back in accordance with the response objects delivered from the 
[REST api](http://api.cortical.io/). For 
example calling `getTerms` will return a list of `Term` objects, and `compare` will return a `Metric` object:

```python
>>> fullClient.getTerms(term="python")
[Term(df=0.00025051038056906765, term='python', score=0.0, pos_types=['NOUN'], fingerprint=Fingerprint(positions=[]))]

>>> import json
>>> fullClient.compare(json.dumps([{"term": "synapse"}, {"term": "skylab"}]))
Metric(cosineSimilarity=0.032885723350542136, overlappingLeftRight=0.02631578947368421, jaccardDistance=0.9836956521739131, weightedScoring=0.6719223186964691, sizeRight=146, sizeLeft=228, overlappingAll=6, overlappingRightLeft=0.0410958904109589, euclideanDistance=0.9679144385026738)
```

All return types are defined in modules in the source folder `retinasdk/model/`. Please visit the 
[REST api](http://api.cortical.io/) for more details about return types, or consult the documentation of the methods
of the `FullClient`.







#### Semantic Expressions

The semantic fingerprint is the basic unit within the Retina API. A text or a term can be resolved into a fingerprint
 using the API. Fingerprints can also be combined in *expressions*, and a number of methods
 expect input in our expression language. This is explained in more detail [here](http://documentation.cortical.io/the_power_of_expressions.html). 

Expressions are essentially `json` strings with reserved keys: `term`, `text`, and `positions`.
In the previous example, we note that the `compare` function takes as argument a list of two such expressions. 
In Python we can create a list of two dictionaries with (in this case) `term` elements and use 
the `json` module to convert it to a valid `json` string (`json.dumps()`). You can however also create the string yourself:

```python
>>> fullClient.compare('[{"term": "synapse"}, {"term": "skylab"}]')
Metric(cosineSimilarity=0.032885723350542136, overlappingLeftRight=0.02631578947368421, jaccardDistance=0.9836956521739131, weightedScoring=0.6719223186964691, sizeRight=146, sizeLeft=228, overlappingAll=6, overlappingRightLeft=0.0410958904109589, euclideanDistance=0.9679144385026738)
```


#### FullClient Example Usage



```python
import json

# Retrieve a list of all available Retinas
fullClient.getRetinas()

# Retrieve information about a specific term
fullClient.getTerms(term="python")

# Get contexts for a given term
fullClient.getContextsForTerm("python", maxResults=3)

# Get similar terms and their Fingerprints for a given term
fullClient.getSimilarTermsForTerm("python", getFingerprint=True)

# Encode a text into a Semantic Fingerprint
fullClient.getFingerprintForText("Python is a widely used general-purpose, high-level programming language.")

# Return keywords from a text
fullClient.getKeywordsForText("Python is a widely used general-purpose, high-level programming language.")

# Returns tokens from an input text
fullClient.getTokensForText("Python is a widely used general-purpose, high-level programming language.", POStags="NN,NNP")

# Slice the input text according to semantic changes (works best on larger texts of at least several sentences)
fullClient.getSlicesForText("longer text with several sentences...")

# Return Semantic Fingerprints for numerous texts in a single call
fullClient.getFingerprintsForTexts(["first text", "second text"])

# Detect the language for an input text
fullClient.getLanguageForText("Dieser Text ist auf Deutsch")

# Return the Fingerprint for an input expression
fullClient.getFingerprintForExpression(json.dumps({"text": "Python is a widely used general-purpose, high-level programming language."}))

# Return contexts for an input expression
fullClient.getContextsForExpression(json.dumps({"text": "Python is a widely used general-purpose, high-level programming language."}))

# Return similar terms for an input expression
fullClient.getSimilarTermsForExpression(json.dumps({"text": "Python is a widely used general-purpose, high-level programming language."}))

# Return Fingerprints for multiple semantic expressions
fullClient.getFingerprintsForExpressions(json.dumps([{"text": "first text"}, {"text": "second text"}]))

# Return contexts for multiple semantic expressions
fullClient.getContextsForExpressions(json.dumps([{"text": "first text"}, {"text": "second text"}]))

# Return similar terms for multiple semantic expressions
fullClient.getSimilarTermsForExpressions(json.dumps([{"text": "first text"}, {"text": "second text"}]))

# Compute the semantic similarity of two input expressions
fullClient.compare(json.dumps([{"term": "synapse"}, {"term": "skylab"}]))

# Make multiple comparisons in a single call
comparison1 = [{"term": "synapse"}, {"term": "skylab"}]
comparison2 = [{"term": "mir"}, {"text": "skylab was a space station"}]
fullClient.compareBulk(json.dumps([comparison1, comparison2]))

# Create an image from an expression
imageData = fullClient.getImage(json.dumps({"term": "python"}), plotShape="square")

# Create multiple images from multiple expressions in a single call
fullClient.getImages(json.dumps([{"text": "first text"}, {"text": "second text"}]))

# Create a composite image showing the visual overlap between two expressions
fullClient.compareImage(json.dumps([{"text": "first text"}, {"text": "second text"}]))

# Create a filter Fingerprint from positive (related) and negative (unrelated) example texts.
fullClient.createCategoryFilter("test", ["Python is a widely used general-purpose, high-level programming language."], negativeExamples=["Monty Python (sometimes known as The Pythons) were a British surreal comedy group."])
```




## Support

For further documentation about the Retina-API and information on cortical.io's 'Retina' technology please see our 
[Knowledge Base](http://www.cortical.io/resources_tutorials.html). Also the `tests` folder contains more examples of how to use the 
clients. 

If you have any questions or problems please visit our [forum](http://www.cortical.io/resources_forum.html).

## Change Log
**v 1.0.0**

* Initial release.
* Refactoring and migrating project from previous GitHub repo.

