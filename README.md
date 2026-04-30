# MAD 2.0
<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

**Authors:** Alison Moldovan-Mauer, Benedikt Mangold

This project is organized following the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) template. The structure is as follows:

```
├── notebooks  
├── src
├── env. 
├── README.md         
├── requirements.txt
```

The results in the paper have been obtained using the following models:
- Llama 3.1 with 405B parameters (equal to MAD 1.0)
- GPT-OSS with 120B parameters
- Mistral with 24B parameters

## Installation

1. Setup environment
```bash
pip install -r requirements.txt
``` 
2. In order to reproduce the results, you will need to connect to the available API endpoints for each model.
```bash
notebooks/run_eperiment.ipynb
```
2. Evaluate Results equal to MAD 1.0 
```bash
notebooks/eval_discussion_length*.ipynb
```
2. Evaluate the Winner of the Discussion
```bash
notebooks/eval_winner*.ipynb
```