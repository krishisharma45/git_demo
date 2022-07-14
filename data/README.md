# Data Directory
Data organization philosophy from [cookiecutter data science](https://github.com/drivendata/cookiecutter-data-science)

```
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
```

Note: this directory will often be backed up with a blob store (e.g. S3) or a shared mounted drive (e.g. EFS).
