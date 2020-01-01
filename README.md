# python-change-parser

This tool parses Python documentation and searches for new features and changed features of Python. It can generate HTML reports, and you can also extract JSON data for further analysis. The result can be used to generate rules for the [`vermin`](https://github.com/netromdk/vermin) project.

You can find the already generated reports under the [`output`](https://github.com/gousaiyang/python-change-parser/tree/master/output) directory.

If you want to run the code by yourself, please download the HTML version of Python documentation from [here](https://docs.python.org/3/download.html) and extract it into the `data` directory.

**NOTE: This tool is based on string matching and is thus imperfect. Manual inspection of the result is recommended.**
