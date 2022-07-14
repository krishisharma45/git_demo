class TrainingDataset:  # Inherit from framework base, e.g. torch.utils.data.Dataset
    def __init__(self, data_path: str):
        """Initialize new training dataset."""
        self._split()
        # ...

    def __len__(self):
        """Return number of examples."""
        pass

    def __getitem__(self, idx):
        """Return an example from a particular index."""
        pass

    def _split(self):
        """Split training and validation data indexes."""
        pass
