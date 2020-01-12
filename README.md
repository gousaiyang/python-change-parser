# python-change-parser

This tool parses Python documentation and searches for new features and changed features of Python. It can generate HTML reports, and you can also extract JSON data for further analysis. The result can be used to generate rules for the [`vermin`](https://github.com/netromdk/vermin) project.

You can find the already generated reports under the [`output`](https://github.com/gousaiyang/python-change-parser/tree/master/output) directory.

If you want to run the code by yourself, please download the HTML version of Python documentation from [here](https://docs.python.org/3/download.html) and extract it into the `data` directory.

Known drawbacks and issues:

- Some changes may be undocumented (especially the major differences between Python 2 and Python 3).
- Some changes are expressed vaguely in the documentation. Different kinds of wording should be identified. String matching is error prone, so manual inspection of the result is needed.
- A single `versionmodified` indicator may be associated with multiple objects (e.g. [`operator.matmul` and `operator.__matmul__` are both new in 3.5](https://docs.python.org/3/library/operator.html#operator.matmul)). Such entries are now marked as `multi` and highlighted in HTML output.
