# See also examples/example_track/example_meta.py for a longer, commented example
track = dict(
    author_username='alexisbcook',
    course_name='Advanced SQL',
    course_url='https://www.kaggle.com/learn/advanced-sql'
)

lessons = [ {'topic': topic_name} for topic_name in
                    ['JOINs and UNIONs',
                     'Analytic Functions',
                     'Nested and Repeated Data',
                     'Writing Efficient Queries'
                     ]
            ]

notebooks = [
    dict(
        filename='tut1.ipynb',
        lesson_idx=0,
        type='tutorial',
        dataset_sources = ["hacker-news/hacker-news"],
        ),
    dict(
        filename='ex1.ipynb',
        lesson_idx=0,
        type='exercise',
        dataset_sources = ["stackoverflow/stackoverflow"],
        scriptid=17990556
        ),
    dict(
        filename='tut2.ipynb',
        lesson_idx=1,
        type='tutorial',
        dataset_sources = ["datasf/san-francisco"],
        ),
    dict(
        filename='ex2.ipynb',
        lesson_idx=1,
        type='exercise',
        dataset_sources = ["chicago/chicago-taxi-trips-bq"],
        scriptid=17990574
        ),
    dict(
        filename='tut3.ipynb',
        lesson_idx=2,
        type='tutorial',
        dataset_sources = ["bigquery/google-analytics-sample"],
        ),
    dict(
        filename='ex3.ipynb',
        lesson_idx=2,
        type='exercise',
        dataset_sources = ["github/github-repos"],
        scriptid=17990570
        ),
    dict(
        filename='tut4.ipynb',
        lesson_idx=3,
        type='tutorial',
        dataset_sources = ["github/github-repos", "datasf/san-francisco"],
        ),
    dict(
        filename='ex4.ipynb',
        lesson_idx=3,
        type='exercise',
        dataset_sources = [],
        scriptid=17990566
        ),
]
