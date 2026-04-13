# MAD 2.0
<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>

**Authors:** Alison Moldovan-Mauer, Benedikt Mangold

The results in the paper have been obtained using the Llama 3.1 model with 405B parameters.


This project is organized following the [Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/) template. The structure is as follows:

```
├── notebooks  
├── src
├── env. 
├── README.md         
├── requirements.txt
```

## Installation

1. Setup environment
```bash
pip install -r requirements.txt
``` 
2. To reproduce the results you need to connect to available API endpoints for every model. 
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