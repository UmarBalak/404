from huggingface_hub import HfApi
from itertools import islice

# Create an instance of HfApi
hf_api = HfApi()

# Search for Models
models = hf_api.list_models(search="r1" ,task=["object-detection"], library=["transformers", "pytorch"], tags=[], model_name="", sort="downloads")

for model in islice(models, 10):
    print(f"Model id: {model.modelId}")
    print(f"Link: https://huggingface.co/{model.modelId}")
    print(f"Created at: {model.created_at}")
    print(f"Last modified: {model.last_modified}")
    print(f"Downloads: {model.downloads}")
    print(f"Likes: {model.likes}")
    print(f"Library name: {model.library_name}")
    print(f"Tags: {model.tags}\n")

"""
filter ([`ModelFilter`] or `str` or `Iterable`, *optional*):
    A string or [`ModelFilter`] which can be used to identify models
    on the Hub.
library (`str` or `List`, *optional*):
    A string or list of strings of foundational libraries models were
    originally trained from, such as pytorch, tensorflow, or allennlp.
model_name (`str`, *optional*):
    A string that contain complete or partial names for models on the
    Hub, such as "bert" or "bert-base-cased"
task (`str` or `List`, *optional*):
    A string or list of strings of tasks models were designed for, such
    as: "fill-mask" or "automatic-speech-recognition"
tags (`str` or `List`, *optional*):
    A string tag or a list of tags to filter models on the Hub by, such
    as `text-generation` or `spacy`.
search (`str`, *optional*):
    A string that will be contained in the returned model ids.
sort (`Literal["last_modified"]` or `str`, *optional*):
    The key with which to sort the resulting models. Possible values
    are the properties of the [`huggingface_hub.hf_api.ModelInfo`] class.
"""
    
################################################

# Search for Datasets
datasets = hf_api.list_datasets(search="object-detection", filter="", sort="downloads")
for dataset in islice(datasets, 10):
    print(f"Dataset id: {dataset.id}")
    print(f"Link: https://huggingface.co/datasets/{dataset.id}")
    print(f"Created at: {dataset.created_at}")
    print(f"Last modified: {dataset.last_modified}")
    print(f"Downloads: {dataset.downloads}")
    print(f"Likes: {dataset.likes}")
    print(f"Task Categories: {dataset.tags[0].split(':')[1]}")
    print(f"Tags: {dataset.tags}\n")
    try:
        dataset_info = hf_api.dataset_info(dataset.id)
    except Exception as e:
        pass
    
"""
filter ([`DatasetFilter`] or `str` or `Iterable`, *optional*):
    A string or [`DatasetFilter`] which can be used to identify
    datasets on the hub.
search (`str`, *optional*):
    A string that will be contained in the returned datasets.
sort (`Literal["last_modified"]` or `str`, *optional*):
    The key with which to sort the resulting datasets. Possible
    values are the properties of the [`huggingface_hub.hf_api.DatasetInfo`] class.
"""

#####################################################



