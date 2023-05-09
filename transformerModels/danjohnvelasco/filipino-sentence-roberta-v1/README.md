---
language: tl
tags:
- roberta
- tagalog
- filipino
- sentence-transformers
datasets: newsph_nli
license: cc-by-sa-4.0
---

# Filipino Sentence RoBERTa
We finetuned [RoBERTa Tagalog Base (finetuned on COHFIE)](https://huggingface.co/danjohnvelasco/roberta-tagalog-base-cohfie-v1) on [NewsPH-NLI](https://huggingface.co/datasets/newsph_nli) to learn to encode filipino/tagalog sentences to sentence embeddings. We used [sentence-transformers](https://www.SBERT.net) to finetune the model. All model details, training setups, and corpus details can be found in this paper: [Automatic WordNet Construction using Word Sense Induction through Sentence Embeddings](https://arxiv.org/abs/2204.03251).

## Intended uses & limitations
The intended use of this model is to extract sentence embeddings which will be used for clustering. This model may not be safe for use in production since we did not examine it for biases. Please use it with caution.

## How to use
Using this model is easier when you have [sentence-transformers](https://www.SBERT.net) installed:
```
pip install -U sentence-transformers
```

Here is how to use this model to encode sentences to sentence embeddings using `SentenceTransformer`:
```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("danjohnvelasco/filipino-sentence-roberta-v1")
sentence_list = ["sentence 1", "sentence 2", "sentence 3"]
sentence_embeddings = model.encode(sentence_list)
print(sentence_embeddings)
```

## BibTeX entry and citation info
If you use this model, please cite our work:

```
@misc{https://doi.org/10.48550/arxiv.2204.03251,
  doi = {10.48550/ARXIV.2204.03251},
  url = {https://arxiv.org/abs/2204.03251},
  author = {Velasco, Dan John and Alba, Axel and Pelagio, Trisha Gail and Ramirez, Bryce Anthony and Cruz, Jan Christian Blaise and Cheng, Charibeth},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Automatic WordNet Construction using Word Sense Induction through Sentence Embeddings},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}
}
```