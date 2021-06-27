# Bootstrapped Confidence Intervals (bsci)

[![License](https://img.shields.io/badge/license-MIT-brightgreen)](https://opensource.org/licenses/MIT)
[![codecov](https://codecov.io/gh/famura/bsci/branch/master/graph/badge.svg?token=ESUTNFwtYY)](https://codecov.io/gh/famura/blm)
[![codestyle](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A frequentist approach to construct confidence intervals by sampling with replacement. 

The statistical boostrap method was first introduced by 
B. Efron, "Bootstrap methods: another look at the jackknife", Annals of Statistics, 1979, [link to pdf](http://jeti.uni-freiburg.de/studenten_seminar/stud_sem_SS_09/EfronBootstrap.pdf).  
[These lecture notes](https://ocw.mit.edu/courses/mathematics/18-05-introduction-to-probability-and-statistics-spring-2014/readings/MIT18_05S14_Reading24.pdf) provide a nice entry-level introduction. More references are given in the code.

## Citing

If you use code or ideas from this repository for your projects or research, please cite it.
```
@misc{Muratore_bsci,
  author = {Fabio Muratore},
  title = {bsci - Constructing frequentist confidence intervals using the statistical bootstrap},
  year = {2021},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/famura/bsci}}
}
```

## Installation

To install the core part of the package run
```
pip install bsci
```

For (local) development install the dependencies with
```
pip install -e .[dev]
```

## Getting Started

Play around with the model's parameters in the `demo.py` script
```
cd examples
python demo.py
```
