import datasets
import pandas as pd
from datasets import DownloadManager

_CITATION = """
Nothing to say yet.
"""


class KinopoiskReviewConfig(datasets.BuilderConfig):
    def __init__(self, features, **kwargs):
        super(KinopoiskReviewConfig, self).__init__(version=datasets.Version("1.0.0", ""), **kwargs)
        self.features = features


class Kinopoisk(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        KinopoiskReviewConfig(
            name="simple",
            description="Simple config",
            features=["content", 'title', 'grade3', 'movie_name', 'part', 'review_id', 'author', 'date']
        )
    ]


    def _info(self):
        return datasets.DatasetInfo(
            description='Kinopoisk movie reviews dataset',
            features=datasets.Features(
                {
                    "content": datasets.Value("string"),
                    "title": datasets.Value("string"),
                    "grade3": datasets.Value("string"),
                    "movie_name": datasets.Value("string"),
                    "part": datasets.Value("string"),
                    "review_id": datasets.Value("string"),
                    "author": datasets.Value("string"),
                    "date": datasets.Value("string"),
                    "grade10": datasets.Value("string"),
                    "Idx": datasets.Value("int32"),
                }
            ),
            supervised_keys=None,
            homepage='',
            citation=_CITATION
        )

    def _split_generators(self, dl_manager: datasets.DownloadManager):
        urls_to_download = {
            "train" : "kinopoisk.jsonl",
            "dev" : "kinopoisk.json",
        }
        downloaded_files = dl_manager.download_and_extract(urls_to_download)

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": downloaded_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": downloaded_files["dev"]}),
        ]

    def _generate_examples(self, filepath):
        df = pd.read_json(filepath, lines=True)
        rows = df.to_dict(orient="records")

        for n, row in enumerate(rows):
            example = row
            example["Idx"] = n

            yield example["Idx"], example
