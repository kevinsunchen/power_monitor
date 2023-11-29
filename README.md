# **Carbon Monitor**

***In-progress project building off of power_monitor***

This repository is forked and modified from [carbon tracker](https://github.com/lfwa/carbontracker)

The power and carbon monitoring software is used for our SC'23 papers 

``Toward Sustainable HPC: Carbon Footprint Estimation and Environmental Implications of HPC Systems``. Link to repository: https://github.com/boringlee24/sc23-sustainability.

``Clover: Toward Sustainable AI with Carbon-Aware Machine Learning Inference Service``. Link to repository: https://github.com/boringlee24/sc23-clover

## Dependencies

Please use the same dependency from the original repository [carbon tracker](https://github.com/lfwa/carbontracker)

## Importing

Simply clone/download this repository and put it in a path that is accessible by python. For instance, [here](https://github.com/boringlee24/transformers/blob/main/examples/pytorch/question-answering/run_qa_no_trainer.py#L58) is an example of how to import the carbontracker module.

## Usage
The ``example.py`` shows how to use the carbon monitor

```
python example.py
```
The summary will be available in ``test.json``
