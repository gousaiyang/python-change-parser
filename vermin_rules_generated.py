modules_rules = {
    "DocXMLRPCServer": ((2, 3), None),  # TODO
    "HTMLParser": ((2, 2), None),  # TODO
    "SimpleXMLRPCServer": ((2, 2), None),  # TODO
    "_ast": ((2, 5), None),  # TODO
    "_winreg": ((2, 0), None),  # TODO
    "abc": ((2, 6), None),  # TODO
    "argparse": ((2, 7), (3, 2)),
    "ast": ((2, 6), None),  # TODO
    "bisect": ((2, 1), None),  # TODO
    "bz2": ((2, 3), None),  # TODO
    "cProfile": ((2, 5), None),  # TODO
    "cgitb": ((2, 2), None),  # TODO
    "collections": ((2, 4), None),  # TODO
    "collections.abc": (None, (3, 3)),
    "concurrent.futures": (None, (3, 2)),
    "contextlib": ((2, 5), None),  # TODO
    "contextvars": (None, (3, 7)),
    "cookielib": ((2, 4), None),  # TODO
    "csv": ((2, 3), None),  # TODO
    "ctypes": ((2, 5), None),  # TODO
    "curses": ((2, 0), None),  # TODO
    "curses.ascii": ((2, 0), None),  # TODO
    "curses.textpad": ((2, 0), None),  # TODO
    "dataclasses": (None, (3, 7)),
    "datetime": ((2, 3), None),  # TODO
    "decimal": ((2, 4), None),  # TODO
    "difflib": ((2, 1), None),  # TODO
    "email": ((2, 2), None),  # TODO
    "email.charset": ((2, 2), None),  # TODO
    "email.contentmanager": (None, (3, 6)),
    "email.header": ((2, 2), None),  # TODO
    "email.headerregistry": (None, (3, 6)),
    "email.message": (None, (3, 6)),
    "email.policy": (None, (3, 3)),
    "encodings.idna": ((2, 3), None),  # TODO
    "encodings.utf_8_sig": ((2, 5), None),  # TODO
    "ensurepip": ((2, 7), (3, 4)),
    "enum": (None, (3, 4)),
    "faulthandler": (None, (3, 3)),
    "fractions": ((2, 6), None),  # TODO
    "functools": ((2, 5), None),  # TODO
    "future_builtins": ((2, 6), None),  # TODO
    "hashlib": ((2, 5), None),  # TODO
    "heapq": ((2, 3), None),  # TODO
    "hmac": ((2, 2), None),  # TODO
    "hotshot": ((2, 2), None),  # TODO
    "hotshot.stats": ((2, 2), None),  # TODO
    "importlib": ((2, 7), (3, 1)),
    "importlib.resources": (None, (3, 7)),
    "inspect": ((2, 1), None),  # TODO
    "io": ((2, 6), None),  # TODO
    "ipaddress": (None, (3, 3)),
    "itertools": ((2, 3), None),  # TODO
    "json": ((2, 6), None),  # TODO
    "logging": ((2, 3), None),  # TODO
    "lzma": (None, (3, 3)),
    "modulefinder": ((2, 3), None),  # TODO
    "msilib": ((2, 5), None),  # TODO
    "multiprocessing": ((2, 6), None),  # TODO
    "multiprocessing.shared_memory": (None, (3, 8)),
    "netrc": ((2, 0), None),  # TODO
    "numbers": ((2, 6), None),  # TODO
    "optparse": ((2, 3), None),  # TODO
    "ossaudiodev": ((2, 3), None),  # TODO
    "pathlib": (None, (3, 4)),
    "pickletools": ((2, 3), None),  # TODO
    "pkgutil": ((2, 3), None),  # TODO
    "platform": ((2, 3), None),  # TODO
    "pydoc": ((2, 1), None),  # TODO
    "runpy": ((2, 5), None),  # TODO
    "secrets": (None, (3, 6)),
    "selectors": (None, (3, 4)),
    "sets": ((2, 3), None),  # TODO
    "shlex": ((2, 0), None),  # TODO
    "site": ((2, 6), None),  # TODO
    "spwd": ((2, 5), None),  # TODO
    "sqlite3": ((2, 5), None),  # TODO
    "ssl": ((2, 6), None),  # TODO
    "statistics": (None, (3, 4)),
    "stringprep": ((2, 3), None),  # TODO
    "subprocess": ((2, 4), None),  # TODO
    "sysconfig": ((2, 7), (3, 2)),
    "tarfile": ((2, 3), None),  # TODO
    "textwrap": ((2, 3), None),  # TODO
    "timeit": ((2, 3), None),  # TODO
    "tracemalloc": (None, (3, 4)),
    "typing": (None, (3, 5)),
    "unittest": ((2, 1), None),  # TODO
    "unittest.mock": (None, (3, 3)),
    "uuid": ((2, 5), None),  # TODO
    "venv": (None, (3, 3)),
    "warnings": ((2, 1), None),  # TODO
    "weakref": ((2, 1), None),  # TODO
    "winsound": ((2, 0), None),  # TODO
    "wsgiref": ((2, 5), None),  # TODO
    "xml.dom": ((2, 0), None),  # TODO
    "xml.dom.minidom": ((2, 0), None),  # TODO
    "xml.dom.pulldom": ((2, 0), None),  # TODO
    "xml.etree.ElementTree": ((2, 5), None),  # TODO
    "xml.parsers.expat": ((2, 0), None),  # TODO
    "xml.sax": ((2, 0), None),  # TODO
    "xml.sax.handler": ((2, 0), None),  # TODO
    "xml.sax.saxutils": ((2, 0), None),  # TODO
    "xml.sax.xmlreader": ((2, 0), None),  # TODO
    "xmlrpclib": ((2, 2), None),  # TODO
    "zipapp": (None, (3, 5)),
    "zipfile": ((2, 0), None),  # TODO
    "zipimport": ((2, 3), None),  # TODO
}

classes_rules = {
    "ConfigParser.ConfigParser": ((2, 3), None),  # TODO
    "ConfigParser.RawConfigParser": ((2, 3), None),  # TODO
    "ConfigParser.SafeConfigParser": ((2, 3), None),  # TODO
    "Queue.LifoQueue": ((2, 6), None),  # TODO
    "Queue.PriorityQueue": ((2, 6), None),  # TODO
    "SimpleXMLRPCServer.CGIXMLRPCRequestHandler": ((2, 3), None),  # TODO
    "abc.ABC": (None, (3, 4)),
    "asyncio.MultiLoopChildWatcher": (None, (3, 8)),
    "asyncio.ThreadedChildWatcher": (None, (3, 8)),
    "bytearray": ((2, 6), None),  # TODO
    "calendar.Calendar": ((2, 5), None),  # TODO
    "calendar.HTMLCalendar": ((2, 5), None),  # TODO
    "calendar.LocaleHTMLCalendar": ((2, 5), None),  # TODO
    "calendar.LocaleTextCalendar": ((2, 5), None),  # TODO
    "calendar.TextCalendar": ((2, 5), None),  # TODO
    "codesc.IncrementalEncoder": ((2, 5), None),  # TODO
    "collections.ChainMap": (None, (3, 3)),
    "collections.Counter": ((2, 7), (3, 1)),
    "collections.OrderedDict": ((2, 7), (3, 1)),
    "collections.abc.AsyncGenerator": (None, (3, 6)),
    "collections.abc.AsyncIterable": (None, (3, 5)),
    "collections.abc.AsyncIterator": (None, (3, 5)),
    "collections.abc.Awaitable": (None, (3, 5)),
    "collections.abc.Collection": (None, (3, 6)),
    "collections.abc.Coroutine": (None, (3, 5)),
    "collections.abc.Generator": (None, (3, 5)),
    "collections.abc.Reversible": (None, (3, 6)),
    "collections.defaultdict": ((2, 5), None),  # TODO
    "collections.deque": ((2, 4), None),  # TODO
    "contextlib.AbstractAsyncContextManager": (None, (3, 7)),
    "contextlib.AbstractContextManager": (None, (3, 6)),
    "contextlib.AsyncExitStack": (None, (3, 7)),
    "contextlib.ContextDecorator": (None, (3, 2)),
    "contextlib.ExitStack": (None, (3, 3)),
    "csv.unix_dialect": (None, (3, 2)),
    "ctypes.c_bool": ((2, 6), None),  # TODO
    "ctypes.c_longdouble": ((2, 6), None),  # TODO
    "ctypes.c_ssize_t": ((2, 7), (3, 2)),
    "datetime.timezone": (None, (3, 2)),
    "decimal.Decimal": (None, (3, 6)),
    "dict": ((2, 2), None),  # TODO
    "difflib.HtmlDiff": ((2, 4), None),  # TODO
    "dis.Bytecode": (None, (3, 4)),
    "dis.Instruction": (None, (3, 4)),
    "doctest.DocTest": ((2, 4), None),  # TODO
    "doctest.DocTestFinder": ((2, 4), None),  # TODO
    "doctest.DocTestParser": ((2, 4), None),  # TODO
    "doctest.DocTestRunner": ((2, 4), None),  # TODO
    "doctest.Example": ((2, 4), None),  # TODO
    "doctest.OutputChecker": ((2, 4), None),  # TODO
    "email.errors.CloseBoundaryNotFoundDefect": (None, (3, 3)),
    "email.errors.FirstHeaderLineIsContinuationDefect": ((2, 4), None),  # TODO
    "email.errors.MalformedHeaderDefect": ((2, 4), None),  # TODO
    "email.errors.MisplacedEnvelopeHeaderDefect": ((2, 4), None),  # TODO
    "email.errors.MissingHeaderBodySeparatorDefect": (None, (3, 3)),
    "email.errors.MultipartInvariantViolationDefect": ((2, 4), None),  # TODO
    "email.errors.NoBoundaryInMultipartDefect": ((2, 4), None),  # TODO
    "email.errors.StartBoundaryNotFoundDefect": ((2, 4), None),  # TODO
    "email.generator.BytesGenerator": (None, (3, 2)),
    "email.generator.DecodedGenerator": ((2, 2), None),  # TODO
    "email.mime.application.MIMEApplication": ((2, 5), None),  # TODO
    "email.mime.multipart.MIMEMultipart": ((2, 2), None),  # TODO
    "email.mime.nonmultipart.MIMENonMultipart": ((2, 2), None),  # TODO
    "email.parser.BytesFeedParser": (None, (3, 2)),
    "email.parser.BytesHeaderParser": (None, (3, 3)),
    "email.parser.BytesParser": (None, (3, 2)),
    "email.parser.FeedParser": ((2, 4), None),  # TODO
    "email.policy.EmailPolicy": (None, (3, 6)),
    "enum.Flag": (None, (3, 6)),
    "enum.IntFlag": (None, (3, 6)),
    "enum.auto": (None, (3, 6)),
    "frozenset": ((2, 4), None),  # TODO
    "ftplib.FTP_TLS": ((2, 7), (3, 2)),
    "functools.partialmethod": (None, (3, 4)),
    "http.HTTPStatus": (None, (3, 5)),
    "http.server.ThreadingHTTPServer": (None, (3, 7)),
    "httplib.HTTPConnection": ((2, 0), None),  # TODO
    "httplib.HTTPResponse": ((2, 0), None),  # TODO
    "httplib.HTTPSConnection": ((2, 0), None),  # TODO
    "imaplib.IMAP4_stream": ((2, 3), None),  # TODO
    "imp.NullImporter": ((2, 5), None),  # TODO
    "importlib.abc.FileLoader": (None, (3, 3)),
    "importlib.abc.MetaPathFinder": (None, (3, 3)),
    "importlib.abc.PathEntryFinder": (None, (3, 3)),
    "importlib.abc.ResourceReader": (None, (3, 7)),
    "importlib.machinery.ExtensionFileLoader": (None, (3, 3)),
    "importlib.machinery.FileFinder": (None, (3, 3)),
    "importlib.machinery.ModuleSpec": (None, (3, 4)),
    "importlib.machinery.SourceFileLoader": (None, (3, 3)),
    "importlib.machinery.SourcelessFileLoader": (None, (3, 3)),
    "importlib.machinery.WindowsRegistryFinder": (None, (3, 3)),
    "importlib.util.LazyLoader": (None, (3, 5)),
    "inspect.BoundArguments": (None, (3, 3)),
    "inspect.Parameter": (None, (3, 3)),
    "inspect.Signature": (None, (3, 3)),
    "logging.LoggerAdapter": ((2, 6), None),  # TODO
    "logging.NullHandler": ((2, 7), (3, 1)),
    "logging.handlers.QueueHandler": (None, (3, 2)),
    "logging.handlers.QueueListener": (None, (3, 2)),
    "logging.handlers.WatchedFileHandler": ((2, 6), None),  # TODO
    "memoryview": ((2, 7), None),  # TODO
    "multiprocessing.Barrier": (None, (3, 3)),
    "nntplib.NNTP_SSL": (None, (3, 2)),
    "object": ((2, 2), None),  # TODO
    "os.DirEntry": (None, (3, 5)),
    "os.PathLike": (None, (3, 6)),
    "os.sched_param": (None, (3, 3)),
    "os.terminal_size": (None, (3, 3)),
    "pickle.PickleBuffer": (None, (3, 8)),
    "pkgutil.ModuleInfo": (None, (3, 6)),
    "plistlib.UID": (None, (3, 8)),
    "popen2.Popen4": ((2, 0), None),  # TODO
    "poplib.POP3_SSL": ((2, 4), None),  # TODO
    "pstats.Stats": ((2, 3), None),  # TODO
    "py_compile.PycInvalidationMode": (None, (3, 7)),
    "queue.SimpleQueue": (None, (3, 7)),
    "random.SystemRandom": ((2, 4), None),  # TODO
    "selectors.DevpollSelector": (None, (3, 5)),
    "set": ((2, 4), None),  # TODO
    "smtplib.LMTP": ((2, 6), None),  # TODO
    "smtplib.SMTP_SSL": ((2, 6), None),  # TODO
    "ssl.AlertDescription": (None, (3, 6)),
    "ssl.MemoryBIO": (None, (3, 5)),
    "ssl.Options": (None, (3, 6)),
    "ssl.SSLContext": ((2, 7), (3, 2)),
    "ssl.SSLErrorNumber": (None, (3, 6)),
    "ssl.SSLObject": (None, (3, 5)),
    "ssl.SSLSession": (None, (3, 6)),
    "ssl.TLSVersion": (None, (3, 7)),
    "ssl.VerifyFlags": (None, (3, 6)),
    "ssl.VerifyMode": (None, (3, 6)),
    "statistics.NormalDist": (None, (3, 8)),
    "string.Formatter": ((2, 6), None),  # TODO
    "string.Template": ((2, 4), None),  # TODO
    "struct.Struct": ((2, 5), None),  # TODO
    "subprocess.CompletedProcess": (None, (3, 5)),
    "sys.float_info": ((2, 6), None),  # TODO
    "sys.float_repr_style": ((2, 7), None),  # TODO
    "test.support.EnvironmentVarGuard": ((2, 6), None),  # TODO
    "test.support.TransientResource": ((2, 6), None),  # TODO
    "test.support.WarningsRecorder": ((2, 6), None),  # TODO
    "threading.Barrier": (None, (3, 2)),
    "threading.local": ((2, 4), None),  # TODO
    "time.struct_time": ((2, 2), None),  # TODO
    "traceback.FrameSummary": (None, (3, 5)),
    "traceback.StackSummary": (None, (3, 5)),
    "traceback.TracebackException": (None, (3, 5)),
    "tracemalloc.DomainFilter": (None, (3, 6)),
    "type": ((2, 2), None),  # TODO
    "types.MappingProxyType": (None, (3, 3)),
    "types.SimpleNamespace": (None, (3, 3)),
    "typing.AsyncContextManager": (None, (3, 5)),
    "typing.AsyncGenerator": (None, (3, 6)),
    "typing.AsyncIterable": (None, (3, 5)),
    "typing.AsyncIterator": (None, (3, 5)),
    "typing.Awaitable": (None, (3, 5)),
    "typing.ChainMap": (None, (3, 5)),
    "typing.Collection": (None, (3, 6)),
    "typing.ContextManager": (None, (3, 5)),
    "typing.Coroutine": (None, (3, 5)),
    "typing.Counter": (None, (3, 5)),
    "typing.DefaultDict": (None, (3, 5)),
    "typing.Deque": (None, (3, 5)),
    "typing.OrderedDict": (None, (3, 7)),
    "typing.Protocol": (None, (3, 8)),
    "typing.SupportsIndex": (None, (3, 8)),
    "typing.Text": (None, (3, 5)),
    "typing.Type": (None, (3, 5)),
    "typing.TypedDict": (None, (3, 8)),
    "unittest.IsolatedAsyncioTestCase": (None, (3, 8)),
    "unittest.TextTestResult": ((2, 7), (3, 2)),
    "unittest.mock.AsyncMock": (None, (3, 8)),
    "urllib.parse.DefragResult": (None, (3, 2)),
    "urllib.parse.DefragResultBytes": (None, (3, 2)),
    "urllib.parse.ParseResultBytes": (None, (3, 2)),
    "urllib.parse.SplitResultBytes": (None, (3, 2)),
    "urllib.request.DataHandler": (None, (3, 4)),
    "urllib.request.HTTPPasswordMgrWithPriorAuth": (None, (3, 5)),
    "urllib2.HTTPCookieProcessor": ((2, 4), None),  # TODO
    "urllib2.HTTPErrorProcessor": ((2, 4), None),  # TODO
    "uuid.SafeUUID": (None, (3, 7)),
    "warnings.catch_warnings": ((2, 6), None),  # TODO
    "weakref.WeakMethod": (None, (3, 4)),
    "weakref.WeakSet": ((2, 7), None),  # TODO
    "weakref.finalize": (None, (3, 4)),
    "wsgiref.handlers.IISCGIHandler": (None, (3, 2)),
    "xml.etree.ElementTree.C14NWriterTarget": (None, (3, 8)),
    "xml.etree.ElementTree.XMLPullParser": (None, (3, 4)),
    "xmlrpclib.MultiCall": ((2, 4), None),  # TODO
    "zipfile.Path": (None, (3, 8)),
    "zipimport.zipimporter": ((2, 7), None),  # TODO
}

exceptions_rules = {
    "BaseException": ((2, 5), None),  # TODO
    "BlockingIOError": (None, (3, 3)),
    "BrokenPipeError": (None, (3, 3)),
    "BytesWarning": ((2, 6), None),  # TODO
    "ChildProcessError": (None, (3, 3)),
    "ConfigParser.InterpolationMissingOptionError": ((2, 3), None),  # TODO
    "ConfigParser.InterpolationSyntaxError": ((2, 3), None),  # TODO
    "ConnectionAbortedError": (None, (3, 3)),
    "ConnectionError": (None, (3, 3)),
    "ConnectionRefusedError": (None, (3, 3)),
    "ConnectionResetError": (None, (3, 3)),
    "EnvironmentError": ((2, 0), None),  # TODO
    "FileExistsError": (None, (3, 3)),
    "FileNotFoundError": (None, (3, 3)),
    "GeneratorExit": ((2, 5), None),  # TODO
    "ImportWarning": ((2, 5), None),  # TODO
    "InterruptedError": (None, (3, 3)),
    "IsADirectoryError": (None, (3, 3)),
    "ModuleNotFoundError": (None, (3, 6)),
    "NotADirectoryError": (None, (3, 3)),
    "NotImplementedError": ((2, 0), None),  # TODO
    "OSError": ((2, 0), None),  # TODO
    "PermissionError": (None, (3, 3)),
    "ProcessLookupError": (None, (3, 3)),
    "RecursionError": (None, (3, 5)),
    "ReferenceError": ((2, 2), None),  # TODO
    "ResourceWarning": (None, (3, 2)),
    "StopAsyncIteration": (None, (3, 5)),
    "StopIteration": ((2, 2), None),  # TODO
    "TimeoutError": (None, (3, 3)),
    "UnboundLocalError": ((2, 0), None),  # TODO
    "UnicodeDecodeError": ((2, 3), None),  # TODO
    "UnicodeEncodeError": ((2, 3), None),  # TODO
    "UnicodeError": ((2, 0), None),  # TODO
    "UnicodeTranslateError": ((2, 3), None),  # TODO
    "UnicodeWarning": ((2, 5), None),  # TODO
    "WindowsError": ((2, 0), None),  # TODO
    "concurrent.futures.BrokenExecutor": (None, (3, 7)),
    "concurrent.futures.InvalidStateError": (None, (3, 8)),
    "concurrent.futures.process.BrokenProcessPool": (None, (3, 3)),
    "concurrent.futures.thread.BrokenThreadPool": (None, (3, 7)),
    "getopt.GetoptError": ((2, 0), None),  # TODO
    "gzip.BadGzipFile": (None, (3, 8)),
    "htmllib.HTMLParseError": ((2, 4), None),  # TODO
    "httplib.BadStatusLine": ((2, 0), None),  # TODO
    "httplib.CannotSendHeader": ((2, 0), None),  # TODO
    "httplib.CannotSendRequest": ((2, 0), None),  # TODO
    "httplib.HTTPException": ((2, 0), None),  # TODO
    "httplib.ImproperConnectionState": ((2, 0), None),  # TODO
    "httplib.IncompleteRead": ((2, 0), None),  # TODO
    "httplib.InvalidURL": ((2, 3), None),  # TODO
    "httplib.NotConnected": ((2, 0), None),  # TODO
    "httplib.ResponseNotReady": ((2, 0), None),  # TODO
    "httplib.UnimplementedFileMode": ((2, 0), None),  # TODO
    "httplib.UnknownProtocol": ((2, 0), None),  # TODO
    "httplib.UnknownTransferEncoding": ((2, 0), None),  # TODO
    "json.JSONDecodeError": (None, (3, 5)),
    "sgmllib.SGMLParseError": ((2, 1), None),  # TODO
    "shutil.Error": ((2, 3), None),  # TODO
    "shutil.SameFileError": (None, (3, 4)),
    "smtplib.SMTPNotSupportedError": (None, (3, 5)),
    "socket.timeout": ((2, 3), None),  # TODO
    "ssl.SSLCertVerificationError": (None, (3, 7)),
    "ssl.SSLEOFError": ((2, 7), (3, 3)),
    "ssl.SSLSyscallError": ((2, 7), (3, 3)),
    "ssl.SSLWantReadError": ((2, 7), (3, 3)),
    "ssl.SSLWantWriteError": ((2, 7), (3, 3)),
    "ssl.SSLZeroReturnError": ((2, 7), (3, 3)),
    "subprocess.SubprocessError": (None, (3, 3)),
    "subprocess.TimeoutExpired": (None, (3, 3)),
    "tarfile.HeaderError": ((2, 6), None),  # TODO
    "threading.BrokenBarrierError": (None, (3, 2)),
    "unittest.SkipTest": ((2, 7), (3, 1)),
    "urllib.ContentTooShortError": ((2, 6), None),  # TODO
    "xml.dom.DOMException": ((2, 1), None),  # TODO
    "xml.dom.DomstringSizeErr": ((2, 1), None),  # TODO
    "xml.dom.HierarchyRequestErr": ((2, 1), None),  # TODO
    "xml.dom.IndexSizeErr": ((2, 1), None),  # TODO
    "xml.dom.InuseAttributeErr": ((2, 1), None),  # TODO
    "xml.dom.InvalidAccessErr": ((2, 1), None),  # TODO
    "xml.dom.InvalidCharacterErr": ((2, 1), None),  # TODO
    "xml.dom.InvalidModificationErr": ((2, 1), None),  # TODO
    "xml.dom.InvalidStateErr": ((2, 1), None),  # TODO
    "xml.dom.NamespaceErr": ((2, 1), None),  # TODO
    "xml.dom.NoDataAllowedErr": ((2, 1), None),  # TODO
    "xml.dom.NoModificationAllowedErr": ((2, 1), None),  # TODO
    "xml.dom.NotFoundErr": ((2, 1), None),  # TODO
    "xml.dom.NotSupportedErr": ((2, 1), None),  # TODO
    "xml.dom.SyntaxErr": ((2, 1), None),  # TODO
    "xml.dom.WrongDocumentErr": ((2, 1), None),  # TODO
    "zipfile.BadZipFile": (None, (3, 2)),
}

functions_rules = {
    "ConfigParser.ConfigParser.items": ((2, 3), None),  # TODO
    "ConfigParser.RawConfigParser.has_option": ((2, 0), None),  # TODO
    "ConfigParser.RawConfigParser.remove_option": ((2, 0), None),  # TODO
    "ConfigParser.RawConfigParser.set": ((2, 0), None),  # TODO
    "ConfigParser.RawConfigParser.write": ((2, 0), None),  # TODO
    "ConfigParser.SafeConfigParser.set": ((2, 4), None),  # TODO
    "EasyDialogs.GetArgv": ((2, 0), None),  # TODO
    "Queue.Queue.join": ((2, 5), None),  # TODO
    "Queue.Queue.task_done": ((2, 5), None),  # TODO
    "SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET": ((2, 5), None),  # TODO
    "SimpleXMLRPCServer.SimpleXMLRPCServer.register_introspection_functions": ((2, 3), None),  # TODO
    "SocketServer.BaseServer.server_close": ((2, 6), None),  # TODO
    "SocketServer.BaseServer.shutdown": ((2, 6), None),  # TODO
    "Tkinter.Tcl": ((2, 4), None),  # TODO
    "_thread.get_native_id": (None, (3, 8)),
    "_winreg.CreateKeyEx": ((2, 7), None),  # TODO
    "_winreg.DeleteKeyEx": ((2, 7), None),  # TODO
    "_winreg.ExpandEnvironmentStrings": ((2, 6), None),  # TODO
    "abc.get_cache_token": (None, (3, 4)),
    "all": ((2, 5), None),  # TODO
    "any": ((2, 5), None),  # TODO
    "argparse.ArgumentParser.parse_intermixed_args": (None, (3, 7)),
    "argparse.ArgumentParser.parse_known_intermixed_args": (None, (3, 7)),
    "array.array.frombytes": (None, (3, 2)),
    "array.array.tobytes": (None, (3, 2)),
    "ast.get_source_segment": (None, (3, 8)),
    "asyncio.AbstractChildWatcher.is_active": (None, (3, 8)),
    "asyncio.Future.get_loop": (None, (3, 7)),
    "asyncio.Handle.cancelled": (None, (3, 7)),
    "asyncio.ReadTransport.is_reading": (None, (3, 7)),
    "asyncio.Server.get_loop": (None, (3, 7)),
    "asyncio.Server.is_serving": (None, (3, 7)),
    "asyncio.Server.serve_forever": (None, (3, 7)),
    "asyncio.Server.start_serving": (None, (3, 7)),
    "asyncio.StreamReader.readuntil": (None, (3, 5)),
    "asyncio.StreamWriter.is_closing": (None, (3, 7)),
    "asyncio.StreamWriter.wait_closed": (None, (3, 7)),
    "asyncio.Task.get_coro": (None, (3, 8)),
    "asyncio.Task.get_name": (None, (3, 8)),
    "asyncio.Task.set_name": (None, (3, 8)),
    "asyncio.TimerHandle.when": (None, (3, 7)),
    "asyncio.WriteTransport.get_write_buffer_limits": (None, (3, 4)),
    "asyncio.all_tasks": (None, (3, 7)),
    "asyncio.create_task": (None, (3, 7)),
    "asyncio.current_task": (None, (3, 7)),
    "asyncio.get_running_loop": (None, (3, 7)),
    "asyncio.isfuture": (None, (3, 5)),
    "asyncio.loop.connect_accepted_socket": (None, (3, 5)),
    "asyncio.loop.create_future": (None, (3, 5)),
    "asyncio.loop.get_exception_handler": (None, (3, 5)),
    "asyncio.loop.sendfile": (None, (3, 7)),
    "asyncio.loop.shutdown_asyncgens": (None, (3, 6)),
    "asyncio.loop.sock_recv_into": (None, (3, 7)),
    "asyncio.loop.sock_sendfile": (None, (3, 7)),
    "asyncio.loop.start_tls": (None, (3, 7)),
    "asyncio.run": (None, (3, 7)),
    "asyncio.run_coroutine_threadsafe": (None, (3, 5)),
    "asyncore.dispatcher.handle_accepted": (None, (3, 2)),
    "audioop.byteswap": (None, (3, 4)),
    "base64.a85decode": (None, (3, 4)),
    "base64.a85encode": (None, (3, 4)),
    "base64.b85decode": (None, (3, 4)),
    "base64.b85encode": (None, (3, 4)),
    "base64.decodebytes": (None, (3, 1)),
    "base64.encodebytes": (None, (3, 1)),
    "basestring": ((2, 3), None),  # TODO
    "bdb.Bdb.get_bpbynumber": (None, (3, 2)),
    "bdb.Breakpoint.bpformat": (None, (3, 2)),
    "bin": ((2, 6), None),  # TODO
    "bool": ((2, 2), None),  # TODO
    "breakpoint": (None, (3, 7)),
    "bytearray.hex": (None, (3, 5)),
    "bytearray.isascii": (None, (3, 7)),
    "bytearray.maketrans": (None, (3, 1)),
    "bytes.hex": (None, (3, 5)),
    "bytes.isascii": (None, (3, 7)),
    "bytes.maketrans": (None, (3, 1)),
    "bz2.BZ2File.fileno": (None, (3, 3)),
    "bz2.BZ2File.peek": (None, (3, 3)),
    "bz2.BZ2File.read1": (None, (3, 3)),
    "bz2.BZ2File.readable": (None, (3, 3)),
    "bz2.BZ2File.readinto": (None, (3, 3)),
    "bz2.BZ2File.seekable": (None, (3, 3)),
    "bz2.BZ2File.writable": (None, (3, 3)),
    "bz2.open": (None, (3, 3)),
    "calendar.Calendar.itermonthdays3": (None, (3, 7)),
    "calendar.Calendar.itermonthdays4": (None, (3, 7)),
    "calendar.calendar": ((2, 0), None),  # TODO
    "calendar.firstweekday": ((2, 0), None),  # TODO
    "calendar.month": ((2, 0), None),  # TODO
    "calendar.setfirstweekday": ((2, 0), None),  # TODO
    "calendar.timegm": ((2, 0), None),  # TODO
    "callable": (None, (3, 2)),
    "cgi.FieldStorage.getfirst": ((2, 2), None),  # TODO
    "cgi.FieldStorage.getlist": ((2, 2), None),  # TODO
    "cmath.isclose": (None, (3, 5)),
    "cmath.isfinite": (None, (3, 2)),
    "cmath.isinf": ((2, 6), None),  # TODO
    "cmath.isnan": ((2, 6), None),  # TODO
    "cmath.phase": ((2, 6), None),  # TODO
    "cmath.polar": ((2, 6), None),  # TODO
    "cmath.rect": ((2, 6), None),  # TODO
    "codecs.decode": ((2, 4), None),  # TODO
    "codecs.encode": ((2, 4), None),  # TODO
    "codecs.getincrementaldecoder": ((2, 5), None),  # TODO
    "codecs.getincrementalencoder": ((2, 5), None),  # TODO
    "codecs.namereplace_errors": (None, (3, 5)),
    "codesc.iterdecode": ((2, 5), None),  # TODO
    "codesc.iterencode": ((2, 5), None),  # TODO
    "collections.Counter.subtract": (None, (3, 2)),
    "collections.OrderedDict.move_to_end": (None, (3, 2)),
    "collections.UserString.__getnewargs__": (None, (3, 5)),
    "collections.UserString.__rmod__": (None, (3, 5)),
    "collections.UserString.casefold": (None, (3, 5)),
    "collections.UserString.format_map": (None, (3, 5)),
    "collections.UserString.isprintable": (None, (3, 5)),
    "collections.UserString.maketrans": (None, (3, 5)),
    "collections.abc.MutableSequence.clear": (None, (3, 3)),
    "collections.abc.MutableSequence.copy": (None, (3, 3)),
    "collections.deque.copy": (None, (3, 5)),
    "collections.deque.count": ((2, 7), (3, 2)),
    "collections.deque.index": (None, (3, 5)),
    "collections.deque.insert": (None, (3, 5)),
    "collections.deque.maxlen": ((2, 7), None),  # TODO
    "collections.deque.remove": ((2, 5), None),  # TODO
    "collections.deque.reverse": ((2, 7), (3, 2)),
    "collections.namedtuple": ((2, 6), None),  # TODO
    "compileall.compile_file": ((2, 7), (3, 2)),
    "configparser.ConfigParser.read_dict": (None, (3, 2)),
    "configparser.ConfigParser.read_file": (None, (3, 2)),
    "configparser.ConfigParser.read_string": (None, (3, 2)),
    "contextlib.nullcontext": (None, (3, 7)),
    "contextlib.redirect_stderr": (None, (3, 5)),
    "contextlib.redirect_stdout": (None, (3, 4)),
    "contextlib.suppress": (None, (3, 4)),
    "crypt.mksalt": (None, (3, 3)),
    "csv.DictWriter.writeheader": ((2, 7), (3, 2)),
    "csv.field_size_limit": ((2, 5), None),  # TODO
    "ctypes._CData.from_buffer": ((2, 6), None),  # TODO
    "ctypes._CData.from_buffer_copy": ((2, 6), None),  # TODO
    "ctypes.get_errno": ((2, 6), None),  # TODO
    "ctypes.get_last_error": ((2, 6), None),  # TODO
    "ctypes.set_errno": ((2, 6), None),  # TODO
    "ctypes.set_last_error": ((2, 6), None),  # TODO
    "ctypes.util.find_msvcrt": ((2, 6), None),  # TODO
    "curses.unget_wch": (None, (3, 3)),
    "curses.update_lines_cols": (None, (3, 5)),
    "curses.window.get_wch": (None, (3, 3)),
    "datetime.date.fromisocalendar": (None, (3, 8)),
    "datetime.date.fromisoformat": (None, (3, 7)),
    "datetime.datetime.fromisocalendar": (None, (3, 8)),
    "datetime.datetime.fromisoformat": (None, (3, 7)),
    "datetime.datetime.strptime": ((2, 5), None),  # TODO
    "datetime.datetime.timestamp": (None, (3, 3)),
    "datetime.time.fromisoformat": (None, (3, 7)),
    "datetime.timedelta.total_seconds": ((2, 7), (3, 2)),
    "decimal.Context.clear_traps": (None, (3, 3)),
    "decimal.Context.create_decimal_from_float": ((2, 7), (3, 1)),
    "decimal.Decimal.canonical": ((2, 6), None),  # TODO
    "decimal.Decimal.compare_signal": ((2, 6), None),  # TODO
    "decimal.Decimal.compare_total": ((2, 6), None),  # TODO
    "decimal.Decimal.compare_total_mag": ((2, 6), None),  # TODO
    "decimal.Decimal.conjugate": ((2, 6), None),  # TODO
    "decimal.Decimal.copy_abs": ((2, 6), None),  # TODO
    "decimal.Decimal.copy_negate": ((2, 6), None),  # TODO
    "decimal.Decimal.copy_sign": ((2, 6), None),  # TODO
    "decimal.Decimal.exp": ((2, 6), None),  # TODO
    "decimal.Decimal.fma": ((2, 6), None),  # TODO
    "decimal.Decimal.from_float": ((2, 7), (3, 1)),
    "decimal.Decimal.is_canonical": ((2, 6), None),  # TODO
    "decimal.Decimal.is_finite": ((2, 6), None),  # TODO
    "decimal.Decimal.is_infinite": ((2, 6), None),  # TODO
    "decimal.Decimal.is_nan": ((2, 6), None),  # TODO
    "decimal.Decimal.is_normal": ((2, 6), None),  # TODO
    "decimal.Decimal.is_qnan": ((2, 6), None),  # TODO
    "decimal.Decimal.is_signed": ((2, 6), None),  # TODO
    "decimal.Decimal.is_snan": ((2, 6), None),  # TODO
    "decimal.Decimal.is_subnormal": ((2, 6), None),  # TODO
    "decimal.Decimal.is_zero": ((2, 6), None),  # TODO
    "decimal.Decimal.ln": ((2, 6), None),  # TODO
    "decimal.Decimal.log10": ((2, 6), None),  # TODO
    "decimal.Decimal.logb": ((2, 6), None),  # TODO
    "decimal.Decimal.logical_and": ((2, 6), None),  # TODO
    "decimal.Decimal.logical_invert": ((2, 6), None),  # TODO
    "decimal.Decimal.logical_or": ((2, 6), None),  # TODO
    "decimal.Decimal.logical_xor": ((2, 6), None),  # TODO
    "decimal.Decimal.max_mag": ((2, 6), None),  # TODO
    "decimal.Decimal.min_mag": ((2, 6), None),  # TODO
    "decimal.Decimal.next_minus": ((2, 6), None),  # TODO
    "decimal.Decimal.next_plus": ((2, 6), None),  # TODO
    "decimal.Decimal.next_toward": ((2, 6), None),  # TODO
    "decimal.Decimal.number_class": ((2, 6), None),  # TODO
    "decimal.Decimal.radix": ((2, 6), None),  # TODO
    "decimal.Decimal.rotate": ((2, 6), None),  # TODO
    "decimal.Decimal.scaleb": ((2, 6), None),  # TODO
    "decimal.Decimal.shift": ((2, 6), None),  # TODO
    "decimal.Decimal.to_integral_exact": ((2, 6), None),  # TODO
    "decimal.Decimal.to_integral_value": ((2, 6), None),  # TODO
    "decimal.localcontext": ((2, 5), None),  # TODO
    "dict.fromkeys": ((2, 3), None),  # TODO
    "dict.iteritems": ((2, 2), None),  # TODO
    "dict.itervalues": ((2, 2), None),  # TODO
    "dict.pop": ((2, 3), None),  # TODO
    "dict.viewitems": ((2, 7), None),  # TODO
    "dict.viewkeys": ((2, 7), None),  # TODO
    "dict.viewvalues": ((2, 7), None),  # TODO
    "difflib.SequenceMatcher.get_grouped_opcodes": ((2, 3), None),  # TODO
    "difflib.context_diff": ((2, 3), None),  # TODO
    "difflib.diff_bytes": (None, (3, 5)),
    "difflib.unified_diff": ((2, 3), None),  # TODO
    "dis.code_info": (None, (3, 2)),
    "dis.get_instructions": (None, (3, 4)),
    "dis.show_code": (None, (3, 2)),
    "dis.stack_effect": (None, (3, 4)),
    "doctest.DocFileSuite": ((2, 4), None),  # TODO
    "doctest.DocTestSuite": ((2, 3), None),  # TODO
    "doctest.debug": ((2, 3), None),  # TODO
    "doctest.debug_src": ((2, 4), None),  # TODO
    "doctest.register_optionflag": ((2, 4), None),  # TODO
    "doctest.script_from_examples": ((2, 4), None),  # TODO
    "doctest.set_unittest_reportflags": ((2, 4), None),  # TODO
    "doctest.testfile": ((2, 4), None),  # TODO
    "doctest.testsource": ((2, 3), None),  # TODO
    "email.generator.Generator.clone": ((2, 2), None),  # TODO
    "email.generator.Generator.flatten": ((2, 2), None),  # TODO
    "email.message.EmailMessage.get_content_disposition": (None, (3, 5)),
    "email.message.Message.__bytes__": (None, (3, 4)),
    "email.message.Message.as_bytes": (None, (3, 4)),
    "email.message.Message.del_param": ((2, 2), None),  # TODO
    "email.message.Message.get_charset": ((2, 2), None),  # TODO
    "email.message.Message.get_content_charset": ((2, 2), None),  # TODO
    "email.message.Message.get_content_disposition": (None, (3, 5)),
    "email.message.Message.get_content_maintype": ((2, 2), None),  # TODO
    "email.message.Message.get_content_subtype": ((2, 2), None),  # TODO
    "email.message.Message.get_content_type": ((2, 2), None),  # TODO
    "email.message.Message.get_default_type": ((2, 2), None),  # TODO
    "email.message.Message.replace_header": ((2, 2), None),  # TODO
    "email.message.Message.set_charset": ((2, 2), None),  # TODO
    "email.message.Message.set_default_type": ((2, 2), None),  # TODO
    "email.message.Message.set_param": ((2, 2), None),  # TODO
    "email.message.Message.set_type": ((2, 2), None),  # TODO
    "email.message_from_binary_file": (None, (3, 2)),
    "email.message_from_bytes": (None, (3, 2)),
    "email.utils.format_datetime": (None, (3, 3)),
    "email.utils.formatdate": ((2, 4), None),  # TODO
    "email.utils.localtime": (None, (3, 3)),
    "email.utils.parsedate_to_datetime": (None, (3, 3)),
    "enumerate": ((2, 3), None),  # TODO
    "file": ((2, 4), None),  # TODO
    "file.next": ((2, 3), None),  # TODO
    "file.xreadlines": ((2, 1), None),  # TODO
    "filecmp.clear_cache": (None, (3, 4)),
    "fileinput.fileno": ((2, 5), None),  # TODO
    "fileinput.hook_compressed": ((2, 5), None),  # TODO
    "fileinput.hook_encoded": ((2, 5), None),  # TODO
    "float.as_integer_ratio": ((2, 6), None),  # TODO
    "float.fromhex": ((2, 6), None),  # TODO
    "float.hex": ((2, 6), None),  # TODO
    "float.is_integer": ((2, 6), None),  # TODO
    "fnmatch.filter": ((2, 2), None),  # TODO
    "fractions.Fraction.as_integer_ratio": (None, (3, 8)),
    "frozenset.isdisjoint": ((2, 6), None),  # TODO
    "ftplib.FTP.mlsd": (None, (3, 3)),
    "ftplib.FTP_TLS.ccc": (None, (3, 3)),
    "functools.cmp_to_key": ((2, 7), (3, 2)),
    "functools.reduce": ((2, 6), None),  # TODO
    "gc.freeze": (None, (3, 7)),
    "gc.get_count": ((2, 5), None),  # TODO
    "gc.get_freeze_count": (None, (3, 7)),
    "gc.get_objects": ((2, 2), None),  # TODO
    "gc.get_referents": ((2, 3), None),  # TODO
    "gc.get_referrers": ((2, 2), None),  # TODO
    "gc.get_stats": (None, (3, 4)),
    "gc.is_tracked": ((2, 7), (3, 1)),
    "gc.unfreeze": (None, (3, 7)),
    "getopt.gnu_getopt": ((2, 3), None),  # TODO
    "gettext.GNUTranslations.lgettext": ((2, 4), None),  # TODO
    "gettext.GNUTranslations.lngettext": ((2, 4), None),  # TODO
    "gettext.GNUTranslations.ngettext": ((2, 3), None),  # TODO
    "gettext.GNUTranslations.npgettext": (None, (3, 8)),
    "gettext.GNUTranslations.pgettext": (None, (3, 8)),
    "gettext.GNUTranslations.ungettext": ((2, 3), None),  # TODO
    "gettext.NullTranslations.lgettext": ((2, 4), None),  # TODO
    "gettext.NullTranslations.lngettext": ((2, 4), None),  # TODO
    "gettext.NullTranslations.ngettext": ((2, 3), None),  # TODO
    "gettext.NullTranslations.npgettext": (None, (3, 8)),
    "gettext.NullTranslations.output_charset": ((2, 4), None),  # TODO
    "gettext.NullTranslations.pgettext": (None, (3, 8)),
    "gettext.NullTranslations.set_output_charset": ((2, 4), None),  # TODO
    "gettext.NullTranslations.ungettext": ((2, 3), None),  # TODO
    "gettext.bind_textdomain_codeset": ((2, 4), None),  # TODO
    "gettext.dngettext": ((2, 3), None),  # TODO
    "gettext.dnpgettext": (None, (3, 8)),
    "gettext.ldgettext": ((2, 4), None),  # TODO
    "gettext.ldngettext": ((2, 4), None),  # TODO
    "gettext.lgettext": ((2, 4), None),  # TODO
    "gettext.lngettext": ((2, 4), None),  # TODO
    "gettext.ngettext": ((2, 3), None),  # TODO
    "glob.escape": (None, (3, 4)),
    "glob.iglob": ((2, 5), None),  # TODO
    "gzip.GzipFile.peek": (None, (3, 2)),
    "gzip.compress": (None, (3, 2)),
    "gzip.decompress": (None, (3, 2)),
    "hashlib.blake2b": (None, (3, 6)),
    "hashlib.blake2s": (None, (3, 6)),
    "hashlib.pbkdf2_hmac": ((2, 7), (3, 4)),
    "hashlib.scrypt": (None, (3, 6)),
    "hashlib.sha3_224": (None, (3, 6)),
    "hashlib.sha3_256": (None, (3, 6)),
    "hashlib.sha3_384": (None, (3, 6)),
    "hashlib.sha3_512": (None, (3, 6)),
    "hashlib.shake_128": (None, (3, 6)),
    "hashlib.shake_256": (None, (3, 6)),
    "heapq.heappushpop": ((2, 6), None),  # TODO
    "heapq.merge": ((2, 6), None),  # TODO
    "heapq.nlargest": ((2, 4), None),  # TODO
    "heapq.nsmallest": ((2, 4), None),  # TODO
    "hex": ((2, 4), None),  # TODO
    "hmac.compare_digest": ((2, 7), (3, 3)),
    "hmac.digest": (None, (3, 7)),
    "html.escape": (None, (3, 2)),
    "html.unescape": (None, (3, 4)),
    "http.client.HTTPConnection.set_debuglevel": (None, (3, 1)),
    "http.client.HTTPConnection.set_tunnel": (None, (3, 2)),
    "http.client.HTTPResponse.readinto": (None, (3, 3)),
    "http.server.BaseHTTPRequestHandler.flush_headers": (None, (3, 3)),
    "http.server.BaseHTTPRequestHandler.handle_expect_100": (None, (3, 2)),
    "http.server.BaseHTTPRequestHandler.send_response_only": (None, (3, 2)),
    "httplib.HTTPConnection.set_tunnel": ((2, 7), None),  # TODO
    "httplib.HTTPResponse.getheaders": ((2, 4), None),  # TODO
    "imaplib.IMAP4.deleteacl": ((2, 4), None),  # TODO
    "imaplib.IMAP4.enable": (None, (3, 5)),
    "imaplib.IMAP4.getannotation": ((2, 5), None),  # TODO
    "imaplib.IMAP4.getquota": ((2, 3), None),  # TODO
    "imaplib.IMAP4.getquotaroot": ((2, 3), None),  # TODO
    "imaplib.IMAP4.login_cram_md5": ((2, 3), None),  # TODO
    "imaplib.IMAP4.myrights": ((2, 4), None),  # TODO
    "imaplib.IMAP4.namespace": ((2, 3), None),  # TODO
    "imaplib.IMAP4.proxyauth": ((2, 3), None),  # TODO
    "imaplib.IMAP4.setannotation": ((2, 5), None),  # TODO
    "imaplib.IMAP4.setquota": ((2, 3), None),  # TODO
    "imaplib.IMAP4.starttls": (None, (3, 2)),
    "imaplib.IMAP4.thread": ((2, 4), None),  # TODO
    "imp.acquire_lock": ((2, 3), None),  # TODO
    "imp.cache_from_source": (None, (3, 2)),
    "imp.get_tag": (None, (3, 2)),
    "imp.release_lock": ((2, 3), None),  # TODO
    "imp.source_from_cache": (None, (3, 2)),
    "importlib.abc.InspectLoader.exec_module": (None, (3, 4)),
    "importlib.abc.InspectLoader.source_to_code": (None, (3, 4)),
    "importlib.abc.Loader.create_module": (None, (3, 4)),
    "importlib.abc.Loader.exec_module": (None, (3, 4)),
    "importlib.abc.Loader.module_repr": (None, (3, 3)),
    "importlib.abc.MetaPathFinder.find_spec": (None, (3, 4)),
    "importlib.abc.PathEntryFinder.find_spec": (None, (3, 4)),
    "importlib.abc.SourceLoader.exec_module": (None, (3, 4)),
    "importlib.abc.SourceLoader.path_stats": (None, (3, 3)),
    "importlib.find_loader": (None, (3, 3)),
    "importlib.invalidate_caches": (None, (3, 3)),
    "importlib.machinery.BuiltinImporter.create_module": (None, (3, 5)),
    "importlib.machinery.BuiltinImporter.exec_module": (None, (3, 5)),
    "importlib.machinery.ExtensionFileLoader.create_module": (None, (3, 5)),
    "importlib.machinery.ExtensionFileLoader.exec_module": (None, (3, 5)),
    "importlib.machinery.ExtensionFileLoader.get_filename": (None, (3, 4)),
    "importlib.machinery.FileFinder.find_spec": (None, (3, 4)),
    "importlib.machinery.PathFinder.find_spec": (None, (3, 4)),
    "importlib.machinery.all_suffixes": (None, (3, 3)),
    "importlib.reload": (None, (3, 4)),
    "importlib.util.cache_from_source": (None, (3, 4)),
    "importlib.util.decode_source": (None, (3, 4)),
    "importlib.util.find_spec": (None, (3, 4)),
    "importlib.util.module_from_spec": (None, (3, 5)),
    "importlib.util.resolve_name": (None, (3, 3)),
    "importlib.util.source_from_cache": (None, (3, 4)),
    "importlib.util.source_hash": (None, (3, 7)),
    "importlib.util.spec_from_file_location": (None, (3, 4)),
    "importlib.util.spec_from_loader": (None, (3, 4)),
    "inspect.BoundArguments.apply_defaults": (None, (3, 5)),
    "inspect.Signature.from_callable": (None, (3, 5)),
    "inspect.cleandoc": ((2, 6), None),  # TODO
    "inspect.getattr_static": (None, (3, 2)),
    "inspect.getcallargs": ((2, 7), (3, 2)),
    "inspect.getclosurevars": (None, (3, 3)),
    "inspect.getcoroutinelocals": (None, (3, 5)),
    "inspect.getcoroutinestate": (None, (3, 5)),
    "inspect.getgeneratorlocals": (None, (3, 3)),
    "inspect.getgeneratorstate": (None, (3, 2)),
    "inspect.isabstract": ((2, 6), None),  # TODO
    "inspect.isasyncgen": (None, (3, 6)),
    "inspect.isasyncgenfunction": (None, (3, 6)),
    "inspect.isawaitable": (None, (3, 5)),
    "inspect.iscoroutine": (None, (3, 5)),
    "inspect.iscoroutinefunction": (None, (3, 5)),
    "inspect.isdatadescriptor": ((2, 3), None),  # TODO
    "inspect.isgenerator": ((2, 6), None),  # TODO
    "inspect.isgeneratorfunction": ((2, 6), None),  # TODO
    "inspect.isgetsetdescriptor": ((2, 5), None),  # TODO
    "inspect.ismemberdescriptor": ((2, 5), None),  # TODO
    "inspect.signature": (None, (3, 3)),
    "inspect.unwrap": (None, (3, 4)),
    "int.as_integer_ratio": (None, (3, 8)),
    "int.bit_length": (None, (3, 1)),
    "int.from_bytes": (None, (3, 2)),
    "int.to_bytes": (None, (3, 2)),
    "io.BufferedIOBase.detach": ((2, 7), (3, 1)),
    "io.BufferedIOBase.readinto1": (None, (3, 5)),
    "io.BytesIO.getbuffer": (None, (3, 2)),
    "io.BytesIO.readinto1": (None, (3, 5)),
    "io.TextIOBase.detach": ((2, 7), (3, 1)),
    "io.TextIOWrapper.reconfigure": (None, (3, 7)),
    "io.open_code": (None, (3, 8)),
    "ipaddress.IPv4Network.subnet_of": (None, (3, 7)),
    "ipaddress.IPv4Network.supernet_of": (None, (3, 7)),
    "iter": ((2, 2), None),  # TODO
    "itertools.accumulate": (None, (3, 2)),
    "itertools.combinations_with_replacement": (None, (3, 1)),
    "itertools.compress": (None, (3, 1)),
    "itertools.groupby": ((2, 4), None),  # TODO
    "itertools.izip_longest": ((2, 6), None),  # TODO
    "itertools.permutations": ((2, 6), None),  # TODO
    "itertools.product": ((2, 6), None),  # TODO
    "itertools.tee": ((2, 4), None),  # TODO
    "linecache.lazycache": (None, (3, 5)),
    "locale.currency": ((2, 5), None),  # TODO
    "locale.delocalize": (None, (3, 5)),
    "locale.format_string": ((2, 5), None),  # TODO
    "locale.getdefaultlocale": ((2, 0), None),  # TODO
    "locale.getlocale": ((2, 0), None),  # TODO
    "locale.getpreferredencoding": ((2, 3), None),  # TODO
    "locale.normalize": ((2, 0), None),  # TODO
    "locale.resetlocale": ((2, 0), None),  # TODO
    "logging.Logger.getChild": ((2, 7), (3, 2)),
    "logging.Logger.hasHandlers": (None, (3, 2)),
    "logging.LoggerAdapter.getEffectiveLevel": (None, (3, 2)),
    "logging.LoggerAdapter.hasHandlers": (None, (3, 2)),
    "logging.LoggerAdapter.isEnabledFor": ((2, 7), (3, 2)),
    "logging.LoggerAdapter.setLevel": (None, (3, 2)),
    "logging.StreamHandler.setStream": (None, (3, 7)),
    "logging.config.dictConfig": ((2, 7), (3, 2)),
    "logging.getLogRecordFactory": (None, (3, 2)),
    "logging.handlers.BaseRotatingHandler.rotate": (None, (3, 3)),
    "logging.handlers.BaseRotatingHandler.rotation_filename": (None, (3, 3)),
    "logging.handlers.QueueListener.enqueue_sentinel": (None, (3, 3)),
    "logging.handlers.WatchedFileHandler.reopenIfNeeded": (None, (3, 6)),
    "logging.setLogRecordFactory": (None, (3, 2)),
    "long.bit_length": ((2, 7), None),  # TODO
    "mailbox.Mailbox.get_bytes": (None, (3, 2)),
    "math.acosh": ((2, 6), None),  # TODO
    "math.asinh": ((2, 6), None),  # TODO
    "math.atanh": ((2, 6), None),  # TODO
    "math.comb": (None, (3, 8)),
    "math.copysign": ((2, 6), None),  # TODO
    "math.dist": (None, (3, 8)),
    "math.erf": ((2, 7), (3, 2)),
    "math.erfc": ((2, 7), (3, 2)),
    "math.expm1": ((2, 7), (3, 2)),
    "math.factorial": ((2, 6), None),  # TODO
    "math.fsum": ((2, 6), None),  # TODO
    "math.gamma": ((2, 7), (3, 2)),
    "math.gcd": (None, (3, 5)),
    "math.isclose": (None, (3, 5)),
    "math.isfinite": (None, (3, 2)),
    "math.isinf": ((2, 6), None),  # TODO
    "math.isnan": ((2, 6), None),  # TODO
    "math.isqrt": (None, (3, 8)),
    "math.lgamma": ((2, 7), (3, 2)),
    "math.log1p": ((2, 6), None),  # TODO
    "math.log2": (None, (3, 3)),
    "math.perm": (None, (3, 8)),
    "math.prod": (None, (3, 8)),
    "math.remainder": (None, (3, 7)),
    "math.trunc": ((2, 6), None),  # TODO
    "memoryview.cast": (None, (3, 3)),
    "memoryview.hex": (None, (3, 5)),
    "memoryview.release": (None, (3, 2)),
    "memoryview.toreadonly": (None, (3, 8)),
    "mimetypes.MimeTypes.read_windows_registry": ((2, 7), (3, 2)),
    "mmap.mmap.madvise": (None, (3, 8)),
    "msilib.Database.Close": (None, (3, 7)),
    "msvcrt.getwch": ((2, 6), None),  # TODO
    "msvcrt.getwche": ((2, 6), None),  # TODO
    "msvcrt.putwch": ((2, 6), None),  # TODO
    "msvcrt.ungetwch": ((2, 6), None),  # TODO
    "multiprocessing.Condition.wait_for": (None, (3, 3)),
    "multiprocessing.Process.close": (None, (3, 7)),
    "multiprocessing.Process.kill": (None, (3, 7)),
    "multiprocessing.connection.wait": (None, (3, 3)),
    "multiprocessing.get_all_start_methods": (None, (3, 4)),
    "multiprocessing.get_context": (None, (3, 4)),
    "multiprocessing.get_start_method": (None, (3, 4)),
    "multiprocessing.managers.SyncManager.Barrier": (None, (3, 3)),
    "multiprocessing.managers.SyncManager.Condition.wait_for": (None, (3, 3)),
    "multiprocessing.parent_process": (None, (3, 8)),
    "multiprocessing.pool.Pool.starmap": (None, (3, 3)),
    "multiprocessing.pool.Pool.starmap_async": (None, (3, 3)),
    "multiprocessing.set_start_method": (None, (3, 4)),
    "next": ((2, 6), None),  # TODO
    "nis.get_default_domain": ((2, 5), None),  # TODO
    "nntplib.NNTP.description": ((2, 4), None),  # TODO
    "nntplib.NNTP.descriptions": ((2, 4), None),  # TODO
    "nntplib.NNTP.getcapabilities": (None, (3, 2)),
    "nntplib.NNTP.login": (None, (3, 2)),
    "nntplib.NNTP.over": (None, (3, 2)),
    "nntplib.NNTP.starttls": (None, (3, 2)),
    "object.__enter__": ((2, 5), None),  # TODO
    "object.__eq__": ((2, 1), None),  # TODO
    "object.__exit__": ((2, 5), None),  # TODO
    "object.__ge__": ((2, 1), None),  # TODO
    "object.__gt__": ((2, 1), None),  # TODO
    "object.__index__": ((2, 5), None),  # TODO
    "object.__instancecheck__": ((2, 6), None),  # TODO
    "object.__le__": ((2, 1), None),  # TODO
    "object.__lt__": ((2, 1), None),  # TODO
    "object.__metaclass__": ((2, 2), None),  # TODO
    "object.__ne__": ((2, 1), None),  # TODO
    "object.__reversed__": ((2, 6), None),  # TODO
    "object.__slots__": ((2, 2), None),  # TODO
    "object.__subclasscheck__": ((2, 6), None),  # TODO
    "operator.__contains__": ((2, 0), None),  # TODO
    "operator.__invert__": ((2, 0), None),  # TODO
    "operator.attrgetter": ((2, 4), None),  # TODO
    "operator.floordiv": ((2, 2), None),  # TODO
    "operator.iadd": ((2, 5), None),  # TODO
    "operator.iand": ((2, 5), None),  # TODO
    "operator.iconcat": ((2, 5), None),  # TODO
    "operator.idiv": ((2, 5), None),  # TODO
    "operator.ifloordiv": ((2, 5), None),  # TODO
    "operator.ilshift": ((2, 5), None),  # TODO
    "operator.imatmul": (None, (3, 5)),
    "operator.imod": ((2, 5), None),  # TODO
    "operator.imul": ((2, 5), None),  # TODO
    "operator.index": ((2, 5), None),  # TODO
    "operator.invert": ((2, 0), None),  # TODO
    "operator.ior": ((2, 5), None),  # TODO
    "operator.ipow": ((2, 5), None),  # TODO
    "operator.irepeat": ((2, 5), None),  # TODO
    "operator.irshift": ((2, 5), None),  # TODO
    "operator.is_": ((2, 3), None),  # TODO
    "operator.isub": ((2, 5), None),  # TODO
    "operator.itemgetter": ((2, 5), None),  # TODO
    "operator.itruediv": ((2, 5), None),  # TODO
    "operator.ixor": ((2, 5), None),  # TODO
    "operator.length_hint": (None, (3, 4)),
    "operator.lt": ((2, 2), None),  # TODO
    "operator.matmul": (None, (3, 5)),
    "operator.methodcaller": ((2, 6), None),  # TODO
    "operator.pow": ((2, 3), None),  # TODO
    "operator.truediv": ((2, 2), None),  # TODO
    "os.WCOREDUMP": ((2, 3), None),  # TODO
    "os.WIFCONTINUED": ((2, 3), None),  # TODO
    "os.chflags": ((2, 6), None),  # TODO
    "os.chroot": ((2, 2), None),  # TODO
    "os.closerange": ((2, 6), None),  # TODO
    "os.copy_file_range": (None, (3, 8)),
    "os.cpu_count": (None, (3, 4)),
    "os.fchdir": ((2, 3), None),  # TODO
    "os.fchmod": ((2, 6), None),  # TODO
    "os.fchown": ((2, 6), None),  # TODO
    "os.fsdecode": (None, (3, 2)),
    "os.fsencode": (None, (3, 2)),
    "os.fspath": (None, (3, 6)),
    "os.fwalk": (None, (3, 3)),
    "os.get_blocking": (None, (3, 5)),
    "os.get_exec_path": (None, (3, 2)),
    "os.get_handle_inheritable": (None, (3, 4)),
    "os.get_inheritable": (None, (3, 4)),
    "os.get_terminal_size": (None, (3, 3)),
    "os.getcwdu": ((2, 3), None),  # TODO
    "os.getenvb": (None, (3, 2)),
    "os.getgrouplist": (None, (3, 3)),
    "os.getloadavg": ((2, 3), None),  # TODO
    "os.getpgid": ((2, 3), None),  # TODO
    "os.getpriority": (None, (3, 3)),
    "os.getrandom": (None, (3, 6)),
    "os.getresgid": ((2, 7), (3, 2)),
    "os.getresuid": ((2, 7), (3, 2)),
    "os.getsid": ((2, 4), None),  # TODO
    "os.getxattr": (None, (3, 3)),
    "os.initgroups": ((2, 7), (3, 2)),
    "os.lchflags": ((2, 6), None),  # TODO
    "os.lchmod": ((2, 6), None),  # TODO
    "os.lchown": ((2, 3), None),  # TODO
    "os.listxattr": (None, (3, 3)),
    "os.lockf": (None, (3, 3)),
    "os.major": ((2, 3), None),  # TODO
    "os.makedev": ((2, 3), None),  # TODO
    "os.makedirs": ((2, 0), None),  # TODO
    "os.memfd_create": (None, (3, 8)),
    "os.minor": ((2, 3), None),  # TODO
    "os.mknod": ((2, 3), None),  # TODO
    "os.path.abspath": ((2, 0), None),  # TODO
    "os.path.commonpath": (None, (3, 5)),
    "os.path.getatime": ((2, 0), None),  # TODO
    "os.path.getctime": ((2, 3), None),  # TODO
    "os.path.getmtime": ((2, 0), None),  # TODO
    "os.path.getsize": ((2, 0), None),  # TODO
    "os.path.lexists": ((2, 3), None),  # TODO
    "os.path.realpath": ((2, 2), None),  # TODO
    "os.path.relpath": ((2, 6), None),  # TODO
    "os.path.splitdrive": ((2, 0), None),  # TODO
    "os.pipe2": (None, (3, 3)),
    "os.popen2": ((2, 0), None),  # TODO
    "os.popen3": ((2, 0), None),  # TODO
    "os.popen4": ((2, 0), None),  # TODO
    "os.posix_fadvise": (None, (3, 3)),
    "os.posix_fallocate": (None, (3, 3)),
    "os.posix_spawn": (None, (3, 8)),
    "os.posix_spawnp": (None, (3, 8)),
    "os.pread": (None, (3, 3)),
    "os.preadv": (None, (3, 7)),
    "os.pwrite": (None, (3, 3)),
    "os.pwritev": (None, (3, 7)),
    "os.readv": (None, (3, 3)),
    "os.register_at_fork": (None, (3, 7)),
    "os.removedirs": ((2, 0), None),  # TODO
    "os.removexattr": (None, (3, 3)),
    "os.renames": ((2, 0), None),  # TODO
    "os.replace": (None, (3, 3)),
    "os.scandir": (None, (3, 5)),
    "os.scandir.close": (None, (3, 6)),
    "os.sched_get_priority_max": (None, (3, 3)),
    "os.sched_get_priority_min": (None, (3, 3)),
    "os.sched_getaffinity": (None, (3, 3)),
    "os.sched_getparam": (None, (3, 3)),
    "os.sched_getscheduler": (None, (3, 3)),
    "os.sched_rr_get_interval": (None, (3, 3)),
    "os.sched_setaffinity": (None, (3, 3)),
    "os.sched_setparam": (None, (3, 3)),
    "os.sched_setscheduler": (None, (3, 3)),
    "os.sched_yield": (None, (3, 3)),
    "os.sendfile": (None, (3, 3)),
    "os.set_blocking": (None, (3, 5)),
    "os.set_handle_inheritable": (None, (3, 4)),
    "os.set_inheritable": (None, (3, 4)),
    "os.setgroups": ((2, 2), None),  # TODO
    "os.setpriority": (None, (3, 3)),
    "os.setresgid": ((2, 7), (3, 2)),
    "os.setresuid": ((2, 7), (3, 2)),
    "os.setxattr": (None, (3, 3)),
    "os.startfile": ((2, 0), None),  # TODO
    "os.sync": (None, (3, 3)),
    "os.truncate": (None, (3, 3)),
    "os.urandom": ((2, 4), None),  # TODO
    "os.wait3": ((2, 5), None),  # TODO
    "os.wait4": ((2, 5), None),  # TODO
    "os.waitid": (None, (3, 3)),
    "os.walk": ((2, 3), None),  # TODO
    "os.writev": (None, (3, 3)),
    "pathlib.Path.expanduser": (None, (3, 5)),
    "pathlib.Path.home": (None, (3, 5)),
    "pathlib.Path.is_mount": (None, (3, 7)),
    "pathlib.Path.link_to": (None, (3, 8)),
    "pathlib.Path.read_bytes": (None, (3, 5)),
    "pathlib.Path.read_text": (None, (3, 5)),
    "pathlib.Path.samefile": (None, (3, 5)),
    "pathlib.Path.write_bytes": (None, (3, 5)),
    "pathlib.Path.write_text": (None, (3, 5)),
    "pickle.Pickler.reducer_override": (None, (3, 8)),
    "pickletools.optimize": ((2, 6), None),  # TODO
    "pkgutil.get_data": ((2, 6), None),  # TODO
    "platform.linux_distribution": ((2, 6), None),  # TODO
    "platform.python_branch": ((2, 6), None),  # TODO
    "platform.python_implementation": ((2, 6), None),  # TODO
    "platform.python_revision": ((2, 6), None),  # TODO
    "platform.win32_edition": (None, (3, 8)),
    "platform.win32_is_iot": (None, (3, 8)),
    "plistlib.dump": (None, (3, 4)),
    "plistlib.dumps": (None, (3, 4)),
    "plistlib.load": (None, (3, 4)),
    "plistlib.loads": (None, (3, 4)),
    "popen2.popen4": ((2, 0), None),  # TODO
    "poplib.POP3.capa": (None, (3, 4)),
    "poplib.POP3.stls": (None, (3, 4)),
    "poplib.POP3.utf8": (None, (3, 5)),
    "pprint.PrettyPrinter.format": ((2, 3), None),  # TODO
    "pprint.pp": (None, (3, 8)),
    "print": ((2, 6), None),  # TODO
    "random.choices": (None, (3, 6)),
    "random.getrandbits": ((2, 4), None),  # TODO
    "random.getstate": ((2, 1), None),  # TODO
    "random.jumpahead": ((2, 1), None),  # TODO
    "random.randrange": ((2, 0), None),  # TODO
    "random.sample": ((2, 3), None),  # TODO
    "random.setstate": ((2, 1), None),  # TODO
    "random.triangular": ((2, 6), None),  # TODO
    "re.Match.__getitem__": (None, (3, 6)),
    "re.Pattern.fullmatch": (None, (3, 4)),
    "re.findall": ((2, 0), None),  # TODO
    "re.finditer": ((2, 2), None),  # TODO
    "re.fullmatch": (None, (3, 4)),
    "readline.append_history_file": (None, (3, 5)),
    "readline.clear_history": ((2, 4), None),  # TODO
    "readline.get_completer": ((2, 3), None),  # TODO
    "readline.get_completion_type": ((2, 6), None),  # TODO
    "readline.get_current_history_length": ((2, 3), None),  # TODO
    "readline.get_history_item": ((2, 3), None),  # TODO
    "readline.remove_history_item": ((2, 4), None),  # TODO
    "readline.replace_history_item": ((2, 4), None),  # TODO
    "readline.set_auto_history": (None, (3, 6)),
    "readline.set_completion_display_matches_hook": ((2, 6), None),  # TODO
    "readline.set_pre_input_hook": ((2, 3), None),  # TODO
    "readline.set_startup_hook": ((2, 3), None),  # TODO
    "resource.prlimit": (None, (3, 4)),
    "reversed": ((2, 4), None),  # TODO
    "runpy.run_path": ((2, 7), (3, 2)),
    "select.devpoll": (None, (3, 3)),
    "select.devpoll.close": (None, (3, 4)),
    "select.devpoll.fileno": (None, (3, 4)),
    "select.epoll": ((2, 6), None),  # TODO
    "select.kevent": ((2, 6), None),  # TODO
    "select.kqueue": ((2, 6), None),  # TODO
    "select.poll.modify": ((2, 6), None),  # TODO
    "set": ((2, 4), None),  # TODO
    "sgmllib.SGMLParser.convert_charref": ((2, 5), None),  # TODO
    "sgmllib.SGMLParser.convert_codepoint": ((2, 5), None),  # TODO
    "sgmllib.SGMLParser.convert_entityref": ((2, 5), None),  # TODO
    "shlex.join": (None, (3, 8)),
    "shlex.quote": (None, (3, 3)),
    "shlex.shlex.pop_source": ((2, 1), None),  # TODO
    "shlex.shlex.push_source": ((2, 1), None),  # TODO
    "shlex.split": ((2, 3), None),  # TODO
    "shutil.chown": (None, (3, 3)),
    "shutil.disk_usage": (None, (3, 3)),
    "shutil.get_archive_formats": ((2, 7), (3, 2)),
    "shutil.get_terminal_size": (None, (3, 3)),
    "shutil.get_unpack_formats": (None, (3, 2)),
    "shutil.ignore_patterns": ((2, 6), None),  # TODO
    "shutil.make_archive": ((2, 7), (3, 2)),
    "shutil.move": ((2, 3), None),  # TODO
    "shutil.register_archive_format": ((2, 7), (3, 2)),
    "shutil.register_unpack_format": (None, (3, 2)),
    "shutil.unpack_archive": (None, (3, 2)),
    "shutil.unregister_archive_format": ((2, 7), (3, 2)),
    "shutil.unregister_unpack_format": (None, (3, 2)),
    "shutil.which": (None, (3, 3)),
    "signal.getitimer": ((2, 6), None),  # TODO
    "signal.pthread_kill": (None, (3, 3)),
    "signal.pthread_sigmask": (None, (3, 3)),
    "signal.raise_signal": (None, (3, 8)),
    "signal.set_wakeup_fd": ((2, 6), None),  # TODO
    "signal.setitimer": ((2, 6), None),  # TODO
    "signal.siginterrupt": ((2, 6), None),  # TODO
    "signal.sigpending": (None, (3, 3)),
    "signal.sigtimedwait": (None, (3, 3)),
    "signal.sigwait": (None, (3, 3)),
    "signal.sigwaitinfo": (None, (3, 3)),
    "signal.strsignal": (None, (3, 8)),
    "signal.valid_signals": (None, (3, 8)),
    "site.getsitepackages": ((2, 7), (3, 2)),
    "site.getuserbase": ((2, 7), (3, 2)),
    "site.getusersitepackages": ((2, 7), (3, 2)),
    "slice.indices": ((2, 3), None),  # TODO
    "smtplib.SMTP.auth": (None, (3, 5)),
    "smtplib.SMTP.ehlo_or_helo_if_needed": ((2, 6), None),  # TODO
    "smtplib.SMTP.send_message": (None, (3, 2)),
    "smtplib.SMTP.starttls": ((2, 6), None),  # TODO
    "socket.CMSG_LEN": (None, (3, 3)),
    "socket.CMSG_SPACE": (None, (3, 3)),
    "socket.close": (None, (3, 7)),
    "socket.create_connection": ((2, 6), None),  # TODO
    "socket.create_server": (None, (3, 8)),
    "socket.fromshare": (None, (3, 3)),
    "socket.getaddrinfo": ((2, 2), None),  # TODO
    "socket.getdefaulttimeout": ((2, 3), None),  # TODO
    "socket.getfqdn": ((2, 0), None),  # TODO
    "socket.getnameinfo": ((2, 2), None),  # TODO
    "socket.has_dualstack_ipv6": (None, (3, 8)),
    "socket.if_indextoname": (None, (3, 3)),
    "socket.if_nameindex": (None, (3, 3)),
    "socket.if_nametoindex": (None, (3, 3)),
    "socket.inet_ntop": ((2, 3), None),  # TODO
    "socket.inet_pton": ((2, 3), None),  # TODO
    "socket.setdefaulttimeout": ((2, 3), None),  # TODO
    "socket.sethostname": (None, (3, 3)),
    "socket.socket.detach": (None, (3, 2)),
    "socket.socket.get_inheritable": (None, (3, 4)),
    "socket.socket.getblocking": (None, (3, 7)),
    "socket.socket.gettimeout": ((2, 3), None),  # TODO
    "socket.socket.ioctl": ((2, 6), None),  # TODO
    "socket.socket.recv_into": ((2, 5), None),  # TODO
    "socket.socket.recvfrom_into": ((2, 5), None),  # TODO
    "socket.socket.recvmsg": (None, (3, 3)),
    "socket.socket.recvmsg_into": (None, (3, 3)),
    "socket.socket.sendfile": (None, (3, 5)),
    "socket.socket.sendmsg": (None, (3, 3)),
    "socket.socket.sendmsg_afalg": (None, (3, 6)),
    "socket.socket.set_inheritable": (None, (3, 4)),
    "socket.socket.settimeout": ((2, 3), None),  # TODO
    "socket.socket.share": (None, (3, 3)),
    "socket.socketpair": ((2, 4), None),  # TODO
    "socketserver.BaseServer.service_actions": (None, (3, 3)),
    "sorted": ((2, 4), None),  # TODO
    "sqlite3.Connection.backup": (None, (3, 7)),
    "sqlite3.Connection.enable_load_extension": ((2, 7), (3, 2)),
    "sqlite3.Connection.load_extension": ((2, 7), (3, 2)),
    "sqlite3.Connection.set_progress_handler": ((2, 6), None),  # TODO
    "sqlite3.Connection.set_trace_callback": (None, (3, 3)),
    "sqlite3.Row.keys": ((2, 6), None),  # TODO
    "ssl.RAND_bytes": (None, (3, 3)),
    "ssl.RAND_pseudo_bytes": (None, (3, 3)),
    "ssl.SSLContext.cert_store_stats": (None, (3, 4)),
    "ssl.SSLContext.get_ca_certs": (None, (3, 4)),
    "ssl.SSLContext.get_ciphers": (None, (3, 6)),
    "ssl.SSLContext.load_default_certs": (None, (3, 4)),
    "ssl.SSLContext.load_dh_params": (None, (3, 3)),
    "ssl.SSLContext.set_alpn_protocols": ((2, 7), (3, 5)),
    "ssl.SSLContext.set_ecdh_curve": (None, (3, 3)),
    "ssl.SSLContext.set_npn_protocols": (None, (3, 3)),
    "ssl.SSLContext.set_servername_callback": (None, (3, 4)),
    "ssl.SSLSocket.compression": ((2, 7), (3, 3)),
    "ssl.SSLSocket.get_channel_binding": ((2, 7), (3, 3)),
    "ssl.SSLSocket.selected_alpn_protocol": ((2, 7), (3, 5)),
    "ssl.SSLSocket.selected_npn_protocol": ((2, 7), (3, 3)),
    "ssl.SSLSocket.sendfile": (None, (3, 5)),
    "ssl.SSLSocket.shared_ciphers": (None, (3, 5)),
    "ssl.SSLSocket.verify_client_post_handshake": (None, (3, 8)),
    "ssl.SSLSocket.version": ((2, 7), (3, 5)),
    "ssl._https_verify_certificates": ((2, 7), None),  # TODO
    "ssl.create_default_context": ((2, 7), (3, 4)),
    "ssl.enum_certificates": ((2, 7), (3, 4)),
    "ssl.enum_crls": ((2, 7), (3, 4)),
    "ssl.get_default_verify_paths": ((2, 7), (3, 4)),
    "ssl.match_hostname": ((2, 7), (3, 2)),
    "stat.S_ISDOOR": (None, (3, 4)),
    "stat.S_ISPORT": (None, (3, 4)),
    "stat.S_ISWHT": (None, (3, 4)),
    "stat.filemode": (None, (3, 3)),
    "statistics.fmean": (None, (3, 8)),
    "statistics.geometric_mean": (None, (3, 8)),
    "statistics.harmonic_mean": (None, (3, 6)),
    "statistics.multimode": (None, (3, 8)),
    "statistics.quantiles": (None, (3, 8)),
    "str.casefold": (None, (3, 3)),
    "str.decode": ((2, 2), None),  # TODO
    "str.encode": ((2, 0), None),  # TODO
    "str.format": ((2, 6), None),  # TODO
    "str.format_map": (None, (3, 2)),
    "str.isascii": (None, (3, 7)),
    "str.partition": ((2, 5), None),  # TODO
    "str.rpartition": ((2, 5), None),  # TODO
    "str.rsplit": ((2, 4), None),  # TODO
    "str.zfill": ((2, 2), None),  # TODO
    "string.rsplit": ((2, 4), None),  # TODO
    "struct.Struct.iter_unpack": (None, (3, 4)),
    "struct.iter_unpack": (None, (3, 4)),
    "struct.pack_into": ((2, 5), None),  # TODO
    "struct.unpack_from": ((2, 5), None),  # TODO
    "subprocess.Popen.kill": ((2, 6), None),  # TODO
    "subprocess.Popen.send_signal": ((2, 6), None),  # TODO
    "subprocess.Popen.terminate": ((2, 6), None),  # TODO
    "subprocess.check_call": ((2, 5), None),  # TODO
    "subprocess.check_output": ((2, 7), (3, 1)),
    "subprocess.run": (None, (3, 5)),
    "sum": ((2, 3), None),  # TODO
    "super": ((2, 2), None),  # TODO
    "sys._clear_type_cache": ((2, 6), None),  # TODO
    "sys._current_frames": ((2, 5), None),  # TODO
    "sys._debugmallocstats": (None, (3, 3)),
    "sys._enablelegacywindowsfsencoding": (None, (3, 6)),
    "sys.addaudithook": (None, (3, 8)),
    "sys.audit": (None, (3, 8)),
    "sys.breakpointhook": (None, (3, 7)),
    "sys.exc_clear": ((2, 3), None),  # TODO
    "sys.get_asyncgen_hooks": (None, (3, 6)),
    "sys.get_coroutine_origin_tracking_depth": (None, (3, 7)),
    "sys.getallocatedblocks": (None, (3, 4)),
    "sys.getandroidapilevel": (None, (3, 7)),
    "sys.getcheckinterval": ((2, 3), None),  # TODO
    "sys.getdefaultencoding": ((2, 0), None),  # TODO
    "sys.getdlopenflags": ((2, 2), None),  # TODO
    "sys.getfilesystemencodeerrors": (None, (3, 6)),
    "sys.getfilesystemencoding": ((2, 3), None),  # TODO
    "sys.getprofile": ((2, 6), None),  # TODO
    "sys.getsizeof": ((2, 6), None),  # TODO
    "sys.getswitchinterval": (None, (3, 2)),
    "sys.gettrace": ((2, 6), None),  # TODO
    "sys.getwindowsversion": ((2, 3), None),  # TODO
    "sys.is_finalizing": (None, (3, 5)),
    "sys.set_coroutine_origin_tracking_depth": (None, (3, 7)),
    "sys.setdefaultencoding": ((2, 0), None),  # TODO
    "sys.setdlopenflags": ((2, 2), None),  # TODO
    "sys.setswitchinterval": (None, (3, 2)),
    "sys.settscdump": ((2, 4), None),  # TODO
    "sys.unraisablehook": (None, (3, 8)),
    "tarfile.TarFile.extractall": ((2, 5), None),  # TODO
    "tarfile.TarInfo.fromtarfile": ((2, 6), None),  # TODO
    "telnetlib.Telnet.read_sb_data": ((2, 3), None),  # TODO
    "tempfile.NamedTemporaryFile": ((2, 3), None),  # TODO
    "tempfile.SpooledTemporaryFile": ((2, 6), None),  # TODO
    "tempfile.TemporaryDirectory": (None, (3, 2)),
    "tempfile.gettempdir": ((2, 3), None),  # TODO
    "tempfile.gettempdirb": (None, (3, 5)),
    "tempfile.gettempprefix": ((2, 0), None),  # TODO
    "tempfile.gettempprefixb": (None, (3, 5)),
    "tempfile.mkdtemp": ((2, 3), None),  # TODO
    "tempfile.mkstemp": ((2, 3), None),  # TODO
    "test.support.captured_stdout": ((2, 6), None),  # TODO
    "test.support.catch_threading_exception": (None, (3, 8)),
    "test.support.catch_unraisable_exception": (None, (3, 8)),
    "test.support.check__all__": (None, (3, 6)),
    "test.support.check_py3k_warnings": ((2, 7), None),  # TODO
    "test.support.check_syntax_warning": (None, (3, 8)),
    "test.support.check_warnings": ((2, 6), None),  # TODO
    "test.support.detect_api_mismatch": (None, (3, 5)),
    "test.support.import_fresh_module": ((2, 7), (3, 1)),
    "test.support.import_module": ((2, 7), (3, 1)),
    "textwrap.indent": (None, (3, 3)),
    "textwrap.shorten": (None, (3, 4)),
    "thread.interrupt_main": ((2, 3), None),  # TODO
    "thread.stack_size": ((2, 5), None),  # TODO
    "threading.Condition.notify_all": ((2, 6), None),  # TODO
    "threading.Condition.wait_for": (None, (3, 2)),
    "threading.Event.is_set": ((2, 6), None),  # TODO
    "threading.Thread.is_alive": ((2, 6), None),  # TODO
    "threading.active_count": ((2, 6), None),  # TODO
    "threading.current_thread": ((2, 6), None),  # TODO
    "threading.excepthook": (None, (3, 8)),
    "threading.get_ident": (None, (3, 3)),
    "threading.get_native_id": (None, (3, 8)),
    "threading.main_thread": (None, (3, 4)),
    "threading.setprofile": ((2, 3), None),  # TODO
    "threading.settrace": ((2, 3), None),  # TODO
    "threading.stack_size": ((2, 5), None),  # TODO
    "time.clock_getres": (None, (3, 3)),
    "time.clock_gettime": (None, (3, 3)),
    "time.clock_gettime_ns": (None, (3, 7)),
    "time.clock_settime": (None, (3, 3)),
    "time.clock_settime_ns": (None, (3, 7)),
    "time.get_clock_info": (None, (3, 3)),
    "time.monotonic": (None, (3, 3)),
    "time.monotonic_ns": (None, (3, 7)),
    "time.perf_counter": (None, (3, 3)),
    "time.perf_counter_ns": (None, (3, 7)),
    "time.process_time": (None, (3, 3)),
    "time.process_time_ns": (None, (3, 7)),
    "time.pthread_getcpuclockid": (None, (3, 7)),
    "time.thread_time": (None, (3, 7)),
    "time.thread_time_ns": (None, (3, 7)),
    "time.time_ns": (None, (3, 7)),
    "time.tzset": ((2, 3), None),  # TODO
    "timeit.Timer.autorange": (None, (3, 6)),
    "timeit.repeat": ((2, 6), None),  # TODO
    "timeit.timeit": ((2, 6), None),  # TODO
    "tokenize.generate_tokens": ((2, 2), None),  # TODO
    "tokenize.open": (None, (3, 2)),
    "tokenize.untokenize": ((2, 5), None),  # TODO
    "traceback.clear_frames": (None, (3, 4)),
    "traceback.format_exc": ((2, 4), None),  # TODO
    "traceback.walk_stack": (None, (3, 5)),
    "traceback.walk_tb": (None, (3, 5)),
    "types.CodeType.replace": (None, (3, 8)),
    "types.DynamicClassAttribute": (None, (3, 4)),
    "types.FrameType.clear": (None, (3, 4)),
    "types.coroutine": (None, (3, 5)),
    "types.new_class": (None, (3, 3)),
    "types.prepare_class": (None, (3, 3)),
    "types.resolve_bases": (None, (3, 7)),
    "typing.NewType": (None, (3, 5)),
    "typing.get_args": (None, (3, 8)),
    "unichr": ((2, 0), None),  # TODO
    "unicode": ((2, 0), None),  # TODO
    "unicodedata.east_asian_width": ((2, 4), None),  # TODO
    "unicodedata.is_normalized": (None, (3, 8)),
    "unicodedata.normalize": ((2, 3), None),  # TODO
    "unittest.TestCase.addClassCleanup": (None, (3, 8)),
    "unittest.TestCase.addCleanup": ((2, 7), (3, 1)),
    "unittest.TestCase.addTypeEqualityFunc": ((2, 7), (3, 1)),
    "unittest.TestCase.assertCountEqual": (None, (3, 2)),
    "unittest.TestCase.assertDictContainsSubset": ((2, 7), None),  # TODO
    "unittest.TestCase.assertDictEqual": ((2, 7), (3, 1)),
    "unittest.TestCase.assertGreater": ((2, 7), (3, 1)),
    "unittest.TestCase.assertGreaterEqual": (None, (3, 1)),
    "unittest.TestCase.assertIn": ((2, 7), (3, 1)),
    "unittest.TestCase.assertIs": ((2, 7), (3, 1)),
    "unittest.TestCase.assertIsInstance": ((2, 7), (3, 2)),
    "unittest.TestCase.assertIsNone": ((2, 7), (3, 1)),
    "unittest.TestCase.assertIsNot": (None, (3, 1)),
    "unittest.TestCase.assertIsNotNone": (None, (3, 1)),
    "unittest.TestCase.assertItemsEqual": ((2, 7), None),  # TODO
    "unittest.TestCase.assertLess": (None, (3, 1)),
    "unittest.TestCase.assertLessEqual": (None, (3, 1)),
    "unittest.TestCase.assertListEqual": ((2, 7), (3, 1)),
    "unittest.TestCase.assertLogs": (None, (3, 4)),
    "unittest.TestCase.assertMultiLineEqual": ((2, 7), (3, 1)),
    "unittest.TestCase.assertNotIn": (None, (3, 1)),
    "unittest.TestCase.assertNotIsInstance": (None, (3, 2)),
    "unittest.TestCase.assertNotRegex": (None, (3, 2)),
    "unittest.TestCase.assertNotRegexpMatches": ((2, 7), (3, 5)),
    "unittest.TestCase.assertRaisesRegex": (None, (3, 2)),
    "unittest.TestCase.assertRaisesRegexp": ((2, 7), (3, 1)),
    "unittest.TestCase.assertRegex": (None, (3, 2)),
    "unittest.TestCase.assertRegexpMatches": ((2, 7), (3, 1)),
    "unittest.TestCase.assertSequenceEqual": ((2, 7), (3, 1)),
    "unittest.TestCase.assertSetEqual": ((2, 7), (3, 1)),
    "unittest.TestCase.assertTupleEqual": (None, (3, 1)),
    "unittest.TestCase.assertWarns": (None, (3, 2)),
    "unittest.TestCase.assertWarnsRegex": (None, (3, 2)),
    "unittest.TestCase.doClassCleanups": (None, (3, 8)),
    "unittest.TestCase.doCleanups": ((2, 7), (3, 1)),
    "unittest.TestCase.longMessage": ((2, 7), None),  # TODO
    "unittest.TestCase.maxDiff": ((2, 7), None),  # TODO
    "unittest.TestCase.setUpClass": ((2, 7), (3, 2)),
    "unittest.TestCase.skipTest": ((2, 7), (3, 1)),
    "unittest.TestCase.subTest": (None, (3, 4)),
    "unittest.TestCase.tearDownClass": ((2, 7), (3, 2)),
    "unittest.TestLoader.discover": ((2, 7), (3, 2)),
    "unittest.TestResult.addSubTest": (None, (3, 4)),
    "unittest.TestResult.startTestRun": ((2, 7), (3, 1)),
    "unittest.TestResult.stopTestRun": ((2, 7), (3, 1)),
    "unittest.addModuleCleanup": (None, (3, 8)),
    "unittest.doModuleCleanups": (None, (3, 8)),
    "unittest.expectedFailure": ((2, 7), None),  # TODO
    "unittest.installHandler": ((2, 7), (3, 2)),
    "unittest.mock.Mock.assert_called": (None, (3, 6)),
    "unittest.mock.Mock.assert_called_once": (None, (3, 6)),
    "unittest.mock.Mock.assert_not_called": (None, (3, 5)),
    "unittest.mock.seal": (None, (3, 7)),
    "unittest.registerResult": ((2, 7), (3, 2)),
    "unittest.removeHandler": ((2, 7), (3, 2)),
    "unittest.removeResult": ((2, 7), (3, 2)),
    "unittest.skip": ((2, 7), None),  # TODO
    "unittest.skipIf": ((2, 7), None),  # TODO
    "unittest.skipUnless": ((2, 7), None),  # TODO
    "urllib.request.Request.remove_header": (None, (3, 4)),
    "urllib.robotparser.RobotFileParser.crawl_delay": (None, (3, 6)),
    "urllib.robotparser.RobotFileParser.request_rate": (None, (3, 6)),
    "urllib.robotparser.RobotFileParser.site_maps": (None, (3, 8)),
    "urllib.urlopen.getcode": ((2, 6), None),  # TODO
    "urllib2.Request.add_unredirected_header": ((2, 4), None),  # TODO
    "urllib2.Request.has_header": ((2, 4), None),  # TODO
    "urlparse.ParseResult.geturl": ((2, 5), None),  # TODO
    "urlparse.parse_qs": ((2, 6), None),  # TODO
    "urlparse.parse_qsl": ((2, 6), None),  # TODO
    "urlparse.urlsplit": ((2, 2), None),  # TODO
    "urlparse.urlunsplit": ((2, 2), None),  # TODO
    "venv.create": (None, (3, 3)),
    "warnings.warnpy3k": ((2, 6), None),  # TODO
    "weakref.WeakKeyDictionary.iterkeyrefs": ((2, 5), None),  # TODO
    "weakref.WeakKeyDictionary.keyrefs": ((2, 5), None),  # TODO
    "weakref.WeakValueDictionary.itervaluerefs": ((2, 5), None),  # TODO
    "weakref.WeakValueDictionary.valuerefs": ((2, 5), None),  # TODO
    "webbrowser.controller.open_new_tab": ((2, 5), None),  # TODO
    "webbrowser.open_new_tab": ((2, 5), None),  # TODO
    "winreg.CreateKeyEx": (None, (3, 2)),
    "winreg.DeleteKeyEx": (None, (3, 2)),
    "winsound.Beep": ((2, 0), None),  # TODO
    "winsound.MessageBeep": ((2, 3), None),  # TODO
    "wsgiref.handlers.read_environ": (None, (3, 2)),
    "xml.dom.Node.normalize": ((2, 1), None),  # TODO
    "xml.dom.minidom.Node.toprettyxml": ((2, 1), None),  # TODO
    "xml.etree.ElementTree.Element.extend": ((2, 7), (3, 2)),
    "xml.etree.ElementTree.Element.iter": ((2, 7), (3, 2)),
    "xml.etree.ElementTree.Element.iterfind": ((2, 7), (3, 2)),
    "xml.etree.ElementTree.Element.itertext": ((2, 7), (3, 2)),
    "xml.etree.ElementTree.ElementTree.iterfind": ((2, 7), (3, 2)),
    "xml.etree.ElementTree.TreeBuilder.comment": (None, (3, 8)),
    "xml.etree.ElementTree.TreeBuilder.doctype": ((2, 7), (3, 2)),
    "xml.etree.ElementTree.TreeBuilder.end_ns": (None, (3, 8)),
    "xml.etree.ElementTree.TreeBuilder.pi": (None, (3, 8)),
    "xml.etree.ElementTree.TreeBuilder.start_ns": (None, (3, 8)),
    "xml.etree.ElementTree.canonicalize": (None, (3, 8)),
    "xml.etree.ElementTree.fromstringlist": ((2, 7), (3, 2)),
    "xml.etree.ElementTree.register_namespace": ((2, 7), (3, 2)),
    "xml.etree.ElementTree.tostringlist": ((2, 7), (3, 2)),
    "xml.parsers.expat.XMLParserType.EntityDeclHandler": ((2, 1), None),  # TODO
    "xml.parsers.expat.XMLParserType.GetInputContext": ((2, 1), None),  # TODO
    "xml.parsers.expat.XMLParserType.UseForeignDTD": ((2, 3), None),  # TODO
    "xml.parsers.expat.XMLParserType.XmlDeclHandler": ((2, 1), None),  # TODO
    "xml.sax.saxutils.quoteattr": ((2, 2), None),  # TODO
    "xml.sax.saxutils.unescape": ((2, 3), None),  # TODO
    "zip": ((2, 0), None),  # TODO
    "zipfile.ZipFile.extract": ((2, 6), None),  # TODO
    "zipfile.ZipFile.extractall": ((2, 6), None),  # TODO
    "zipfile.ZipFile.open": ((2, 6), None),  # TODO
    "zipfile.ZipFile.setpassword": ((2, 6), None),  # TODO
    "zipfile.ZipInfo.from_file": (None, (3, 6)),
    "zipfile.ZipInfo.is_dir": (None, (3, 6)),
    "zipimport.zipimporter.get_filename": (None, (3, 1)),
    "zlib.Compress.copy": ((2, 5), None),  # TODO
    "zlib.Decompress.copy": ((2, 5), None),  # TODO
}

variables_and_constants_rules = {
    "BaseException.__suppress_context__": (None, (3, 3)),
    "BaseHTTPServer.BaseHTTPRequestHandler.error_content_type": ((2, 6), None),  # TODO
    "Cookie.Morsel.httponly": ((2, 6), None),  # TODO
    "False": ((2, 3), None),  # TODO
    "ImportError.name": (None, (3, 3)),
    "ImportError.path": (None, (3, 3)),
    "OSError.filename2": (None, (3, 4)),
    "SimpleXMLRPCServer.SimpleXMLRPCRequestHandler.encode_threshold": ((2, 7), None),  # TODO
    "SimpleXMLRPCServer.SimpleXMLRPCRequestHandler.rpc_paths": ((2, 5), None),  # TODO
    "StopIteration.value": (None, (3, 3)),
    "True": ((2, 3), None),  # TODO
    "_thread.TIMEOUT_MAX": (None, (3, 2)),
    "bz2.BZ2Decompressor.eof": (None, (3, 3)),
    "bz2.BZ2Decompressor.needs_input": (None, (3, 5)),
    "calendar.HTMLCalendar.cssclass_month": (None, (3, 7)),
    "calendar.HTMLCalendar.cssclass_month_head": (None, (3, 7)),
    "calendar.HTMLCalendar.cssclass_noday": (None, (3, 7)),
    "calendar.HTMLCalendar.cssclass_year": (None, (3, 7)),
    "calendar.HTMLCalendar.cssclass_year_head": (None, (3, 7)),
    "calendar.HTMLCalendar.cssclasses_weekday_head": (None, (3, 7)),
    "cmath.inf": (None, (3, 6)),
    "cmath.infj": (None, (3, 6)),
    "cmath.nan": (None, (3, 6)),
    "cmath.nanj": (None, (3, 6)),
    "cmath.tau": (None, (3, 6)),
    "collections.deque.maxlen": (None, (3, 1)),
    "collections.namedtuple._field_defaults": (None, (3, 7)),
    "configparser.DuplicateSectionError.lineno": (None, (3, 2)),
    "configparser.DuplicateSectionError.source": (None, (3, 2)),
    "configparser.ParsingError.source": (None, (3, 2)),
    "contextvars.ContextVar.name": (None, (3, 7)),
    "cookielib.Cookie.rfc2109": ((2, 5), None),  # TODO
    "cookielib.DefaultCookiePolicy.rfc2109_as_netscape": ((2, 5), None),  # TODO
    "crypt.METHOD_BLOWFISH": (None, (3, 7)),
    "crypt.METHOD_CRYPT": (None, (3, 3)),
    "crypt.METHOD_MD5": (None, (3, 3)),
    "crypt.METHOD_SHA256": (None, (3, 3)),
    "crypt.METHOD_SHA512": (None, (3, 3)),
    "crypt.methods": (None, (3, 3)),
    "csv.csvreader.fieldnames": ((2, 6), None),  # TODO
    "csv.csvreader.line_num": ((2, 5), None),  # TODO
    "curses.A_ITALIC": (None, (3, 7)),
    "curses.ncurses_version": (None, (3, 8)),
    "curses.window.encoding": (None, (3, 3)),
    "datetime.datetime.fold": (None, (3, 6)),
    "datetime.time.fold": (None, (3, 6)),
    "difflib.SequenceMatcher.bjunk": (None, (3, 2)),
    "difflib.SequenceMatcher.bpopular": (None, (3, 2)),
    "doctest.COMPARISON_FLAGS": ((2, 4), None),  # TODO
    "doctest.DONT_ACCEPT_BLANKLINE": ((2, 4), None),  # TODO
    "doctest.ELLIPSIS": ((2, 4), None),  # TODO
    "doctest.FAIL_FAST": (None, (3, 4)),
    "doctest.IGNORE_EXCEPTION_DETAIL": ((2, 4), None),  # TODO
    "doctest.NORMALIZE_WHITESPACE": ((2, 4), None),  # TODO
    "doctest.REPORTING_FLAGS": ((2, 4), None),  # TODO
    "doctest.REPORT_CDIFF": ((2, 4), None),  # TODO
    "doctest.REPORT_NDIFF": ((2, 4), None),  # TODO
    "doctest.REPORT_ONLY_FIRST_FAILURE": ((2, 4), None),  # TODO
    "doctest.REPORT_UDIFF": ((2, 4), None),  # TODO
    "doctest.skip": ((2, 5), None),  # TODO
    "email.message.Message.defects": ((2, 4), None),  # TODO
    "email.policy.EmailPolicy.content_manager": (None, (3, 4)),
    "email.policy.Policy.message_factory": (None, (3, 6)),
    "fcntl.F_ADD_SEALS": (None, (3, 8)),
    "fcntl.F_GET_SEALS": (None, (3, 8)),
    "fcntl.F_SEAL_GROW": (None, (3, 8)),
    "fcntl.F_SEAL_SEAL": (None, (3, 8)),
    "fcntl.F_SEAL_SHRINK": (None, (3, 8)),
    "fcntl.F_SEAL_WRITE": (None, (3, 8)),
    "file.encoding": ((2, 3), None),  # TODO
    "file.errors": ((2, 6), None),  # TODO
    "filecmp.DEFAULT_IGNORES": (None, (3, 4)),
    "gc.callbacks": (None, (3, 3)),
    "gzip.GzipFile.mtime": (None, (3, 1)),
    "hashlib.algorithms_available": ((2, 7), (3, 2)),
    "hashlib.algorithms_guaranteed": ((2, 7), (3, 2)),
    "hashlib.hash.name": (None, (3, 4)),
    "hashlib.hashlib.algorithms": ((2, 7), None),  # TODO
    "hmac.HMAC.block_size": (None, (3, 4)),
    "hmac.HMAC.name": (None, (3, 4)),
    "html.entities.html5": (None, (3, 3)),
    "htmlentitydefs.codepoint2name": ((2, 3), None),  # TODO
    "htmlentitydefs.name2codepoint": ((2, 3), None),  # TODO
    "http.HTTPStatus.MISDIRECTED_REQUEST": (None, (3, 7)),
    "http.HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS": (None, (3, 8)),
    "http.client.HTTPConnection.blocksize": (None, (3, 7)),
    "httplib.responses": ((2, 5), None),  # TODO
    "imaplib.IMAP4.utf8_enabled": (None, (3, 5)),
    "importlib.machinery.BYTECODE_SUFFIXES": (None, (3, 3)),
    "importlib.machinery.DEBUG_BYTECODE_SUFFIXES": (None, (3, 3)),
    "importlib.machinery.EXTENSION_SUFFIXES": (None, (3, 3)),
    "importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES": (None, (3, 3)),
    "importlib.machinery.SOURCE_SUFFIXES": (None, (3, 3)),
    "importlib.util.MAGIC_NUMBER": (None, (3, 4)),
    "inspect.CO_ASYNC_GENERATOR": (None, (3, 6)),
    "inspect.CO_COROUTINE": (None, (3, 5)),
    "inspect.CO_ITERABLE_COROUTINE": (None, (3, 5)),
    "inspect.Parameter.kind.description": (None, (3, 8)),
    "io.SEEK_CUR": ((2, 7), (3, 1)),
    "io.SEEK_END": ((2, 7), (3, 1)),
    "io.SEEK_SET": ((2, 7), (3, 1)),
    "io.TextIOWrapper.write_through": (None, (3, 7)),
    "ipaddress.IPv4Address.is_global": (None, (3, 4)),
    "ipaddress.IPv4Address.reverse_pointer": (None, (3, 5)),
    "logging.Formatter.default_msec_format": (None, (3, 3)),
    "logging.Formatter.default_time_format": (None, (3, 3)),
    "logging.LogRecord.funcName": ((2, 5), None),  # TODO
    "logging.LogRecord.processName": ((2, 6), None),  # TODO
    "logging.StreamHandler.terminator": (None, (3, 2)),
    "logging.handlers.BaseRotatingHandler.name": (None, (3, 3)),
    "logging.handlers.BaseRotatingHandler.rotator": (None, (3, 3)),
    "logging.lastResort": (None, (3, 2)),
    "lzma.LZMADecompressor.needs_input": (None, (3, 5)),
    "marshal.version": ((2, 4), None),  # TODO
    "math.inf": (None, (3, 5)),
    "math.nan": (None, (3, 5)),
    "math.tau": (None, (3, 6)),
    "memoryview.c_contiguous": (None, (3, 3)),
    "memoryview.contiguous": (None, (3, 3)),
    "memoryview.f_contiguous": (None, (3, 3)),
    "memoryview.nbytes": (None, (3, 3)),
    "memoryview.obj": (None, (3, 3)),
    "mmap.ACCESS_DEFAULT": (None, (3, 7)),
    "mmap.MADV_AUTOSYNC": (None, (3, 8)),
    "mmap.MADV_CORE": (None, (3, 8)),
    "mmap.MADV_DODUMP": (None, (3, 8)),
    "mmap.MADV_DOFORK": (None, (3, 8)),
    "mmap.MADV_DONTDUMP": (None, (3, 8)),
    "mmap.MADV_DONTFORK": (None, (3, 8)),
    "mmap.MADV_DONTNEED": (None, (3, 8)),
    "mmap.MADV_FREE": (None, (3, 8)),
    "mmap.MADV_HUGEPAGE": (None, (3, 8)),
    "mmap.MADV_HWPOISON": (None, (3, 8)),
    "mmap.MADV_MERGEABLE": (None, (3, 8)),
    "mmap.MADV_NOCORE": (None, (3, 8)),
    "mmap.MADV_NOHUGEPAGE": (None, (3, 8)),
    "mmap.MADV_NORMAL": (None, (3, 8)),
    "mmap.MADV_NOSYNC": (None, (3, 8)),
    "mmap.MADV_PROTECT": (None, (3, 8)),
    "mmap.MADV_RANDOM": (None, (3, 8)),
    "mmap.MADV_REMOVE": (None, (3, 8)),
    "mmap.MADV_SEQUENTIAL": (None, (3, 8)),
    "mmap.MADV_SOFT_OFFLINE": (None, (3, 8)),
    "mmap.MADV_UNMERGEABLE": (None, (3, 8)),
    "mmap.MADV_WILLNEED": (None, (3, 8)),
    "mmap.mmap.closed": (None, (3, 2)),
    "multiprocessing.Process.sentinel": (None, (3, 3)),
    "nntplib.NNTP.nntp_implementation": (None, (3, 2)),
    "nntplib.NNTP.nntp_version": (None, (3, 2)),
    "os.CLD_CONTINUED": (None, (3, 3)),
    "os.CLD_DUMPED": (None, (3, 3)),
    "os.CLD_EXITED": (None, (3, 3)),
    "os.CLD_TRAPPED": (None, (3, 3)),
    "os.EX_CANTCREAT": ((2, 3), None),  # TODO
    "os.EX_CONFIG": ((2, 3), None),  # TODO
    "os.EX_DATAERR": ((2, 3), None),  # TODO
    "os.EX_IOERR": ((2, 3), None),  # TODO
    "os.EX_NOHOST": ((2, 3), None),  # TODO
    "os.EX_NOINPUT": ((2, 3), None),  # TODO
    "os.EX_NOPERM": ((2, 3), None),  # TODO
    "os.EX_NOTFOUND": ((2, 3), None),  # TODO
    "os.EX_NOUSER": ((2, 3), None),  # TODO
    "os.EX_OK": ((2, 3), None),  # TODO
    "os.EX_OSERR": ((2, 3), None),  # TODO
    "os.EX_OSFILE": ((2, 3), None),  # TODO
    "os.EX_PROTOCOL": ((2, 3), None),  # TODO
    "os.EX_SOFTWARE": ((2, 3), None),  # TODO
    "os.EX_TEMPFAIL": ((2, 3), None),  # TODO
    "os.EX_UNAVAILABLE": ((2, 3), None),  # TODO
    "os.EX_USAGE": ((2, 3), None),  # TODO
    "os.F_LOCK": (None, (3, 3)),
    "os.F_TEST": (None, (3, 3)),
    "os.F_TLOCK": (None, (3, 3)),
    "os.F_ULOCK": (None, (3, 3)),
    "os.GRND_NONBLOCK": (None, (3, 6)),
    "os.GRND_RANDOM": (None, (3, 6)),
    "os.MFD_ALLOW_SEALING": (None, (3, 8)),
    "os.MFD_CLOEXEC": (None, (3, 8)),
    "os.MFD_HUGETLB": (None, (3, 8)),
    "os.MFD_HUGE_16GB": (None, (3, 8)),
    "os.MFD_HUGE_16MB": (None, (3, 8)),
    "os.MFD_HUGE_1GB": (None, (3, 8)),
    "os.MFD_HUGE_1MB": (None, (3, 8)),
    "os.MFD_HUGE_256MB": (None, (3, 8)),
    "os.MFD_HUGE_2GB": (None, (3, 8)),
    "os.MFD_HUGE_2MB": (None, (3, 8)),
    "os.MFD_HUGE_32MB": (None, (3, 8)),
    "os.MFD_HUGE_512KB": (None, (3, 8)),
    "os.MFD_HUGE_512MB": (None, (3, 8)),
    "os.MFD_HUGE_64KB": (None, (3, 8)),
    "os.MFD_HUGE_8MB": (None, (3, 8)),
    "os.MFD_HUGE_MASK": (None, (3, 8)),
    "os.MFD_HUGE_SHIFT": (None, (3, 8)),
    "os.O_CLOEXEC": (None, (3, 3)),
    "os.O_PATH": (None, (3, 4)),
    "os.O_TMPFILE": (None, (3, 4)),
    "os.POSIX_FADV_DONTNEED": (None, (3, 3)),
    "os.POSIX_FADV_NOREUSE": (None, (3, 3)),
    "os.POSIX_FADV_NORMAL": (None, (3, 3)),
    "os.POSIX_FADV_RANDOM": (None, (3, 3)),
    "os.POSIX_FADV_SEQUENTIAL": (None, (3, 3)),
    "os.POSIX_FADV_WILLNEED": (None, (3, 3)),
    "os.POSIX_SPAWN_CLOSE": (None, (3, 8)),
    "os.POSIX_SPAWN_DUP2": (None, (3, 8)),
    "os.POSIX_SPAWN_OPEN": (None, (3, 8)),
    "os.PRIO_PGRP": (None, (3, 3)),
    "os.PRIO_PROCESS": (None, (3, 3)),
    "os.PRIO_USER": (None, (3, 3)),
    "os.P_ALL": (None, (3, 3)),
    "os.P_DETACH": ((2, 0), None),  # TODO
    "os.P_NOWAIT": ((2, 0), None),  # TODO
    "os.P_NOWAITO": ((2, 0), None),  # TODO
    "os.P_OVERLAY": ((2, 0), None),  # TODO
    "os.P_PGID": (None, (3, 3)),
    "os.P_PID": (None, (3, 3)),
    "os.P_WAIT": ((2, 0), None),  # TODO
    "os.RTLD_DEEPBIND": (None, (3, 3)),
    "os.RTLD_GLOBAL": (None, (3, 3)),
    "os.RTLD_LAZY": (None, (3, 3)),
    "os.RTLD_LOCAL": (None, (3, 3)),
    "os.RTLD_NODELETE": (None, (3, 3)),
    "os.RTLD_NOLOAD": (None, (3, 3)),
    "os.RTLD_NOW": (None, (3, 3)),
    "os.RWF_DSYNC": (None, (3, 7)),
    "os.RWF_HIPRI": (None, (3, 7)),
    "os.RWF_NOWAIT": (None, (3, 7)),
    "os.RWF_SYNC": (None, (3, 7)),
    "os.SCHED_BATCH": (None, (3, 3)),
    "os.SCHED_FIFO": (None, (3, 3)),
    "os.SCHED_IDLE": (None, (3, 3)),
    "os.SCHED_OTHER": (None, (3, 3)),
    "os.SCHED_RESET_ON_FORK": (None, (3, 3)),
    "os.SCHED_RR": (None, (3, 3)),
    "os.SCHED_SPORADIC": (None, (3, 3)),
    "os.SEEK_CUR": ((2, 5), None),  # TODO
    "os.SEEK_DATA": (None, (3, 3)),
    "os.SEEK_END": ((2, 5), None),  # TODO
    "os.SEEK_HOLE": (None, (3, 3)),
    "os.SEEK_SET": ((2, 5), None),  # TODO
    "os.SF_MNOWAIT": (None, (3, 3)),
    "os.SF_NODISKIO": (None, (3, 3)),
    "os.SF_SYNC": (None, (3, 3)),
    "os.ST_APPEND": (None, (3, 4)),
    "os.ST_IMMUTABLE": (None, (3, 4)),
    "os.ST_MANDLOCK": (None, (3, 4)),
    "os.ST_NOATIME": (None, (3, 4)),
    "os.ST_NODEV": (None, (3, 4)),
    "os.ST_NODIRATIME": (None, (3, 4)),
    "os.ST_NOEXEC": (None, (3, 4)),
    "os.ST_NOSUID": (None, (3, 2)),
    "os.ST_RDONLY": (None, (3, 2)),
    "os.ST_RELATIME": (None, (3, 4)),
    "os.ST_SYNCHRONOUS": (None, (3, 4)),
    "os.ST_WRITE": (None, (3, 4)),
    "os.WCONTINUED": ((2, 3), None),  # TODO
    "os.WEXITED": (None, (3, 3)),
    "os.WNOWAIT": (None, (3, 3)),
    "os.WSTOPPED": (None, (3, 3)),
    "os.WUNTRACED": ((2, 3), None),  # TODO
    "os.XATTR_CREATE": (None, (3, 3)),
    "os.XATTR_REPLACE": (None, (3, 3)),
    "os.XATTR_SIZE_MAX": (None, (3, 3)),
    "os.devnull": ((2, 4), None),  # TODO
    "os.environb": (None, (3, 2)),
    "os.extsep": ((2, 2), None),  # TODO
    "os.killpg": ((2, 3), None),  # TODO
    "os.path.supports_unicode_filenames": ((2, 3), None),  # TODO
    "os.spawnl": ((2, 0), None),  # TODO
    "os.stat_result.st_atime": ((2, 2), None),  # TODO
    "os.stat_result.st_atime_ns": (None, (3, 3)),
    "os.stat_result.st_attrs": ((2, 2), None),  # TODO
    "os.stat_result.st_birthtime": ((2, 5), None),  # TODO
    "os.stat_result.st_blksize": ((2, 2), None),  # TODO
    "os.stat_result.st_blocks": ((2, 2), None),  # TODO
    "os.stat_result.st_ctime": ((2, 2), None),  # TODO
    "os.stat_result.st_ctime_ns": (None, (3, 3)),
    "os.stat_result.st_dev": ((2, 2), None),  # TODO
    "os.stat_result.st_file_attributes": (None, (3, 5)),
    "os.stat_result.st_flags": ((2, 2), None),  # TODO
    "os.stat_result.st_ftype": ((2, 2), None),  # TODO
    "os.stat_result.st_gen": ((2, 5), None),  # TODO
    "os.stat_result.st_gid": ((2, 2), None),  # TODO
    "os.stat_result.st_ino": ((2, 2), None),  # TODO
    "os.stat_result.st_mode": ((2, 2), None),  # TODO
    "os.stat_result.st_mtime": ((2, 2), None),  # TODO
    "os.stat_result.st_mtime_ns": (None, (3, 3)),
    "os.stat_result.st_obtype": ((2, 2), None),  # TODO
    "os.stat_result.st_rdev": ((2, 2), None),  # TODO
    "os.stat_result.st_reparse_tag": (None, (3, 8)),
    "os.stat_result.st_size": ((2, 2), None),  # TODO
    "os.stat_result.st_uid": ((2, 2), None),  # TODO
    "os.stat_result.st_ulink": ((2, 2), None),  # TODO
    "os.statvfs.f_avail": ((2, 2), None),  # TODO
    "os.statvfs.f_bavail": ((2, 2), None),  # TODO
    "os.statvfs.f_bfree": ((2, 2), None),  # TODO
    "os.statvfs.f_blocks": ((2, 2), None),  # TODO
    "os.statvfs.f_bsize": ((2, 2), None),  # TODO
    "os.statvfs.f_ffree": ((2, 2), None),  # TODO
    "os.statvfs.f_files": ((2, 2), None),  # TODO
    "os.statvfs.f_flag": ((2, 2), None),  # TODO
    "os.statvfs.f_frsize": ((2, 2), None),  # TODO
    "os.statvfs.f_namemax": ((2, 2), None),  # TODO
    "os.statvfs_result.f_fsid": (None, (3, 7)),
    "os.supports_bytes_environ": (None, (3, 2)),
    "os.supports_dir_fd": (None, (3, 3)),
    "os.supports_effective_ids": (None, (3, 3)),
    "os.supports_fd": (None, (3, 3)),
    "os.supports_follow_symlinks": (None, (3, 3)),
    "pickle.HIGHEST_PROTOCOL": ((2, 3), None),  # TODO
    "pickle.Pickler.dispatch_table": (None, (3, 3)),
    "plistlib.FMT_BINARY": (None, (3, 4)),
    "plistlib.FMT_XML": (None, (3, 4)),
    "pstats.SortKey": (None, (3, 7)),
    "pyclbr.Class.children": (None, (3, 7)),
    "pyclbr.Class.parent": (None, (3, 7)),
    "pyclbr.Function.children": (None, (3, 7)),
    "pyclbr.Function.parent": (None, (3, 7)),
    "range.start": (None, (3, 3)),
    "range.step": (None, (3, 3)),
    "range.stop": (None, (3, 3)),
    "re.U": ((2, 0), None),  # TODO
    "re.UNICODE": ((2, 0), None),  # TODO
    "re.error.colno": (None, (3, 5)),
    "re.error.lineno": (None, (3, 5)),
    "re.error.msg": (None, (3, 5)),
    "re.error.pattern": (None, (3, 5)),
    "re.error.pos": (None, (3, 5)),
    "repr.Repr.maxfrozenset": ((2, 4), None),  # TODO
    "repr.Repr.maxset": ((2, 4), None),  # TODO
    "repr.Repr.set": ((2, 4), None),  # TODO
    "resource.RLIMIT_MSGQUEUE": (None, (3, 4)),
    "resource.RLIMIT_NICE": (None, (3, 4)),
    "resource.RLIMIT_NPTS": (None, (3, 4)),
    "resource.RLIMIT_RTPRIO": (None, (3, 4)),
    "resource.RLIMIT_RTTIME": (None, (3, 4)),
    "resource.RLIMIT_SBSIZE": (None, (3, 4)),
    "resource.RLIMIT_SIGPENDING": (None, (3, 4)),
    "resource.RLIMIT_SWAP": (None, (3, 4)),
    "resource.RUSAGE_THREAD": (None, (3, 2)),
    "resource.getrusage.ru_idrss": ((2, 3), None),  # TODO
    "resource.getrusage.ru_inblock": ((2, 3), None),  # TODO
    "resource.getrusage.ru_isrss": ((2, 3), None),  # TODO
    "resource.getrusage.ru_ixrss": ((2, 3), None),  # TODO
    "resource.getrusage.ru_majflt": ((2, 3), None),  # TODO
    "resource.getrusage.ru_maxrss": ((2, 3), None),  # TODO
    "resource.getrusage.ru_minflt": ((2, 3), None),  # TODO
    "resource.getrusage.ru_msgrcv": ((2, 3), None),  # TODO
    "resource.getrusage.ru_msgsnd": ((2, 3), None),  # TODO
    "resource.getrusage.ru_nivcsw": ((2, 3), None),  # TODO
    "resource.getrusage.ru_nsignals": ((2, 3), None),  # TODO
    "resource.getrusage.ru_nswap": ((2, 3), None),  # TODO
    "resource.getrusage.ru_nvcsw": ((2, 3), None),  # TODO
    "resource.getrusage.ru_oublock": ((2, 3), None),  # TODO
    "resource.getrusage.ru_stime": ((2, 3), None),  # TODO
    "resource.getrusage.ru_utime": ((2, 3), None),  # TODO
    "sched.scheduler.queue": ((2, 6), None),  # TODO
    "select.EPOLLEXCLUSIVE": (None, (3, 6)),
    "select.PIPE_BUF": ((2, 7), (3, 2)),
    "select.devpoll.closed": (None, (3, 4)),
    "shlex.shlex.eof": ((2, 3), None),  # TODO
    "shlex.shlex.escape": ((2, 3), None),  # TODO
    "shlex.shlex.escapedquotes": ((2, 3), None),  # TODO
    "shlex.shlex.punctuation_chars": (None, (3, 6)),
    "shlex.shlex.whitespace_split": ((2, 3), None),  # TODO
    "shutil.rmtree.avoids_symlink_attacks": (None, (3, 3)),
    "signal.CTRL_BREAK_EVENT": ((2, 7), (3, 2)),
    "signal.CTRL_C_EVENT": ((2, 7), (3, 2)),
    "signal.SIG_BLOCK": (None, (3, 3)),
    "signal.SIG_SETMASK": (None, (3, 3)),
    "signal.SIG_UNBLOCK": (None, (3, 3)),
    "site.ENABLE_USER_SITE": ((2, 6), None),  # TODO
    "site.PREFIXES": ((2, 6), None),  # TODO
    "site.USER_BASE": ((2, 6), None),  # TODO
    "site.USER_SITE": ((2, 6), None),  # TODO
    "socket.AF_ALG": (None, (3, 6)),
    "socket.AF_CAN": (None, (3, 3)),
    "socket.AF_LINK": (None, (3, 4)),
    "socket.AF_QIPCRTR": (None, (3, 8)),
    "socket.AF_RDS": (None, (3, 3)),
    "socket.AF_TIPC": ((2, 6), None),  # TODO
    "socket.AF_VSOCK": (None, (3, 7)),
    "socket.ALG_OP_DECRYPT": (None, (3, 6)),
    "socket.ALG_OP_ENCRYPT": (None, (3, 6)),
    "socket.ALG_OP_SIGN": (None, (3, 6)),
    "socket.ALG_OP_VERIFY": (None, (3, 6)),
    "socket.ALG_SET_AEAD_ASSOCLEN": (None, (3, 6)),
    "socket.ALG_SET_AEAD_AUTHSIZE": (None, (3, 6)),
    "socket.ALG_SET_IV": (None, (3, 6)),
    "socket.ALG_SET_KEY": (None, (3, 6)),
    "socket.ALG_SET_OP": (None, (3, 6)),
    "socket.ALG_SET_PUBKEY": (None, (3, 6)),
    "socket.CAN_BCM": (None, (3, 4)),
    "socket.CAN_BCM_CAN_FD_FRAME": (None, (3, 4)),
    "socket.CAN_BCM_RX_ANNOUNCE_RESUME": (None, (3, 4)),
    "socket.CAN_BCM_RX_CHANGED": (None, (3, 4)),
    "socket.CAN_BCM_RX_CHECK_DLC": (None, (3, 4)),
    "socket.CAN_BCM_RX_DELETE": (None, (3, 4)),
    "socket.CAN_BCM_RX_FILTER_ID": (None, (3, 4)),
    "socket.CAN_BCM_RX_NO_AUTOTIMER": (None, (3, 4)),
    "socket.CAN_BCM_RX_READ": (None, (3, 4)),
    "socket.CAN_BCM_RX_RTR_FRAME": (None, (3, 4)),
    "socket.CAN_BCM_RX_SETUP": (None, (3, 4)),
    "socket.CAN_BCM_RX_STATUS": (None, (3, 4)),
    "socket.CAN_BCM_RX_TIMEOUT": (None, (3, 4)),
    "socket.CAN_BCM_SETTIMER": (None, (3, 4)),
    "socket.CAN_BCM_STARTTIMER": (None, (3, 4)),
    "socket.CAN_BCM_TX_ANNOUNCE": (None, (3, 4)),
    "socket.CAN_BCM_TX_COUNTEVT": (None, (3, 4)),
    "socket.CAN_BCM_TX_CP_CAN_ID": (None, (3, 4)),
    "socket.CAN_BCM_TX_DELETE": (None, (3, 4)),
    "socket.CAN_BCM_TX_EXPIRED": (None, (3, 4)),
    "socket.CAN_BCM_TX_READ": (None, (3, 4)),
    "socket.CAN_BCM_TX_RESET_MULTI_IDX": (None, (3, 4)),
    "socket.CAN_BCM_TX_SEND": (None, (3, 4)),
    "socket.CAN_BCM_TX_SETUP": (None, (3, 4)),
    "socket.CAN_BCM_TX_STATUS": (None, (3, 4)),
    "socket.CAN_EFF_FLAG": (None, (3, 3)),
    "socket.CAN_EFF_MASK": (None, (3, 3)),
    "socket.CAN_ERR_FLAG": (None, (3, 3)),
    "socket.CAN_ERR_MASK": (None, (3, 3)),
    "socket.CAN_ISOTP": (None, (3, 7)),
    "socket.CAN_RAW": (None, (3, 3)),
    "socket.CAN_RAW_ERR_FILTER": (None, (3, 3)),
    "socket.CAN_RAW_FD_FRAMES": (None, (3, 5)),
    "socket.CAN_RAW_FILTER": (None, (3, 3)),
    "socket.CAN_RAW_LOOPBACK": (None, (3, 3)),
    "socket.CAN_RAW_RECV_OWN_MSGS": (None, (3, 3)),
    "socket.CAN_RTR_FLAG": (None, (3, 3)),
    "socket.CAN_SFF_MASK": (None, (3, 3)),
    "socket.IOCTL_VM_SOCKETS_GET_LOCAL_CID": (None, (3, 7)),
    "socket.PF_CAN": (None, (3, 3)),
    "socket.PF_RDS": (None, (3, 3)),
    "socket.RCVALL_IPLEVEL": ((2, 6), None),  # TODO
    "socket.RCVALL_MAX": ((2, 6), None),  # TODO
    "socket.RCVALL_OFF": ((2, 6), None),  # TODO
    "socket.RCVALL_ON": ((2, 6), None),  # TODO
    "socket.RCVALL_SOCKETLEVELONLY": ((2, 6), None),  # TODO
    "socket.RDS_CANCEL_SENT_TO": (None, (3, 3)),
    "socket.RDS_CMSG_RDMA_ARGS": (None, (3, 3)),
    "socket.RDS_CMSG_RDMA_DEST": (None, (3, 3)),
    "socket.RDS_CMSG_RDMA_MAP": (None, (3, 3)),
    "socket.RDS_CMSG_RDMA_STATUS": (None, (3, 3)),
    "socket.RDS_CMSG_RDMA_UPDATE": (None, (3, 3)),
    "socket.RDS_CONG_MONITOR": (None, (3, 3)),
    "socket.RDS_FREE_MR": (None, (3, 3)),
    "socket.RDS_GET_MR": (None, (3, 3)),
    "socket.RDS_GET_MR_FOR_DEST": (None, (3, 3)),
    "socket.RDS_RDMA_DONTWAIT": (None, (3, 3)),
    "socket.RDS_RDMA_FENCE": (None, (3, 3)),
    "socket.RDS_RDMA_INVALIDATE": (None, (3, 3)),
    "socket.RDS_RDMA_NOTIFY_ME": (None, (3, 3)),
    "socket.RDS_RDMA_READWRITE": (None, (3, 3)),
    "socket.RDS_RDMA_SILENT": (None, (3, 3)),
    "socket.RDS_RDMA_USE_ONCE": (None, (3, 3)),
    "socket.RDS_RECVERR": (None, (3, 3)),
    "socket.SIO_KEEPALIVE_VALS": ((2, 6), None),  # TODO
    "socket.SIO_LOOPBACK_FAST_PATH": (None, (3, 6)),
    "socket.SIO_RCVALL": ((2, 6), None),  # TODO
    "socket.SOCK_CLOEXEC": (None, (3, 2)),
    "socket.SOCK_NONBLOCK": (None, (3, 2)),
    "socket.SOL_ALG": (None, (3, 6)),
    "socket.SOL_CAN_BASE": (None, (3, 3)),
    "socket.SOL_CAN_RAW": (None, (3, 3)),
    "socket.SOL_RDS": (None, (3, 3)),
    "socket.SOL_TIPC": ((2, 6), None),  # TODO
    "socket.SO_DOMAIN": (None, (3, 6)),
    "socket.SO_PASSSEC": (None, (3, 6)),
    "socket.SO_PEERSEC": (None, (3, 6)),
    "socket.SO_PROTOCOL": (None, (3, 6)),
    "socket.SO_VM_SOCKETS_BUFFER_MAX_SIZE": (None, (3, 7)),
    "socket.SO_VM_SOCKETS_BUFFER_MIN_SIZE": (None, (3, 7)),
    "socket.SO_VM_SOCKETS_BUFFER_SIZE": (None, (3, 7)),
    "socket.TCP_CONGESTION": (None, (3, 6)),
    "socket.TCP_NOTSENT_LOWAT": (None, (3, 7)),
    "socket.TCP_USER_TIMEOUT": (None, (3, 6)),
    "socket.TIPC_ADDR_ID": ((2, 6), None),  # TODO
    "socket.TIPC_ADDR_NAME": ((2, 6), None),  # TODO
    "socket.TIPC_ADDR_NAMESEQ": ((2, 6), None),  # TODO
    "socket.TIPC_CFG_SRV": ((2, 6), None),  # TODO
    "socket.TIPC_CLUSTER_SCOPE": ((2, 6), None),  # TODO
    "socket.TIPC_CONN_TIMEOUT": ((2, 6), None),  # TODO
    "socket.TIPC_CRITICAL_IMPORTANCE": ((2, 6), None),  # TODO
    "socket.TIPC_DEST_DROPPABLE": ((2, 6), None),  # TODO
    "socket.TIPC_HIGH_IMPORTANCE": ((2, 6), None),  # TODO
    "socket.TIPC_IMPORTANCE": ((2, 6), None),  # TODO
    "socket.TIPC_LOW_IMPORTANCE": ((2, 6), None),  # TODO
    "socket.TIPC_MEDIUM_IMPORTANCE": ((2, 6), None),  # TODO
    "socket.TIPC_NODE_SCOPE": ((2, 6), None),  # TODO
    "socket.TIPC_PUBLISHED": ((2, 6), None),  # TODO
    "socket.TIPC_SRC_DROPPABLE": ((2, 6), None),  # TODO
    "socket.TIPC_SUBSCR_TIMEOUT": ((2, 6), None),  # TODO
    "socket.TIPC_SUB_CANCEL": ((2, 6), None),  # TODO
    "socket.TIPC_SUB_PORTS": ((2, 6), None),  # TODO
    "socket.TIPC_SUB_SERVICE": ((2, 6), None),  # TODO
    "socket.TIPC_TOP_SRV": ((2, 6), None),  # TODO
    "socket.TIPC_WAIT_FOREVER": ((2, 6), None),  # TODO
    "socket.TIPC_WITHDRAWN": ((2, 6), None),  # TODO
    "socket.TIPC_ZONE_SCOPE": ((2, 6), None),  # TODO
    "socket.VMADDR_CID_ANY": (None, (3, 7)),
    "socket.VMADDR_CID_HOST": (None, (3, 7)),
    "socket.VMADDR_PORT_ANY": (None, (3, 7)),
    "socket.has_ipv6": ((2, 3), None),  # TODO
    "socket.socket.family": ((2, 5), None),  # TODO
    "socket.socket.proto": ((2, 5), None),  # TODO
    "socket.socket.type": ((2, 5), None),  # TODO
    "socketserver.ForkingMixIn.block_on_close": (None, (3, 7)),
    "sqlite3.Connection.in_transaction": (None, (3, 2)),
    "sqlite3.Connection.iterdump": ((2, 6), None),  # TODO
    "ssl.ALERT_DESCRIPTION_ACCESS_DENIED": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_BAD_CERTIFICATE": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_BAD_CERTIFICATE_HASH_VALUE": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_BAD_CERTIFICATE_STATUS_RESPONSE": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_BAD_RECORD_MAC": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_CERTIFICATE_EXPIRED": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_CERTIFICATE_REVOKED": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_CERTIFICATE_UNKNOWN": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_CERTIFICATE_UNOBTAINABLE": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_CLOSE_NOTIFY": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_DECODE_ERROR": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_DECOMPRESSION_FAILURE": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_DECRYPT_ERROR": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_HANDSHAKE_FAILURE": ((2, 7), (3, 4)),
    "ssl.ALERT_DESCRIPTION_ILLEGAL_PARAMETER": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_INSUFFICIENT_SECURITY": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_INTERNAL_ERROR": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_NO_RENEGOTIATION": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_PROTOCOL_VERSION": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_RECORD_OVERFLOW": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_UNEXPECTED_MESSAGE": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_UNKNOWN_CA": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_UNKNOWN_PSK_IDENTITY": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_UNRECOGNIZED_NAME": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_UNSUPPORTED_CERTIFICATE": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_UNSUPPORTED_EXTENSION": (None, (3, 4)),
    "ssl.ALERT_DESCRIPTION_USER_CANCELLED": (None, (3, 4)),
    "ssl.CHANNEL_BINDING_TYPES": ((2, 7), (3, 3)),
    "ssl.HAS_ALPN": ((2, 7), (3, 5)),
    "ssl.HAS_ECDH": ((2, 7), (3, 3)),
    "ssl.HAS_NEVER_CHECK_COMMON_NAME": (None, (3, 7)),
    "ssl.HAS_NPN": ((2, 7), (3, 3)),
    "ssl.HAS_SNI": ((2, 7), (3, 2)),
    "ssl.HAS_SSLv2": (None, (3, 7)),
    "ssl.HAS_SSLv3": (None, (3, 7)),
    "ssl.HAS_TLSv1": (None, (3, 7)),
    "ssl.HAS_TLSv1_1": (None, (3, 7)),
    "ssl.HAS_TLSv1_2": (None, (3, 7)),
    "ssl.HAS_TLSv1_3": ((2, 7), (3, 7)),
    "ssl.OPENSSL_VERSION": ((2, 7), (3, 2)),
    "ssl.OPENSSL_VERSION_INFO": ((2, 7), (3, 2)),
    "ssl.OPENSSL_VERSION_NUMBER": ((2, 7), (3, 2)),
    "ssl.OP_ALL": ((2, 7), (3, 2)),
    "ssl.OP_CIPHER_SERVER_PREFERENCE": ((2, 7), (3, 3)),
    "ssl.OP_ENABLE_MIDDLEBOX_COMPAT": ((2, 7), (3, 8)),
    "ssl.OP_NO_COMPRESSION": ((2, 7), (3, 3)),
    "ssl.OP_NO_RENEGOTIATION": (None, (3, 7)),
    "ssl.OP_NO_SSLv2": ((2, 7), (3, 2)),
    "ssl.OP_NO_SSLv3": ((2, 7), (3, 2)),
    "ssl.OP_NO_TICKET": (None, (3, 6)),
    "ssl.OP_NO_TLSv1": ((2, 7), (3, 2)),
    "ssl.OP_NO_TLSv1_1": ((2, 7), (3, 4)),
    "ssl.OP_NO_TLSv1_2": ((2, 7), (3, 4)),
    "ssl.OP_NO_TLSv1_3": ((2, 7), (3, 7)),
    "ssl.OP_SINGLE_DH_USE": ((2, 7), (3, 3)),
    "ssl.OP_SINGLE_ECDH_USE": ((2, 7), (3, 3)),
    "ssl.PROTOCOL_TLS": ((2, 7), (3, 6)),
    "ssl.PROTOCOL_TLS_CLIENT": (None, (3, 6)),
    "ssl.PROTOCOL_TLS_SERVER": (None, (3, 6)),
    "ssl.PROTOCOL_TLSv1_1": ((2, 7), (3, 4)),
    "ssl.PROTOCOL_TLSv1_2": ((2, 7), (3, 4)),
    "ssl.Purpose.CLIENT_AUTH": ((2, 7), (3, 4)),
    "ssl.Purpose.SERVER_AUTH": ((2, 7), (3, 4)),
    "ssl.SSLContext.check_hostname": (None, (3, 4)),
    "ssl.SSLContext.hostname_checks_common_name": (None, (3, 7)),
    "ssl.SSLContext.keylog_filename": (None, (3, 8)),
    "ssl.SSLContext.maximum_version": (None, (3, 7)),
    "ssl.SSLContext.minimum_version": (None, (3, 7)),
    "ssl.SSLContext.num_tickets": (None, (3, 8)),
    "ssl.SSLContext.post_handshake_auth": (None, (3, 8)),
    "ssl.SSLContext.sni_callback": (None, (3, 7)),
    "ssl.SSLContext.sslobject_class": (None, (3, 7)),
    "ssl.SSLContext.sslsocket_class": (None, (3, 7)),
    "ssl.SSLContext.verify_flags": (None, (3, 4)),
    "ssl.SSLError.library": ((2, 7), (3, 3)),
    "ssl.SSLError.reason": ((2, 7), (3, 3)),
    "ssl.SSLSocket.context": ((2, 7), (3, 2)),
    "ssl.SSLSocket.server_hostname": (None, (3, 2)),
    "ssl.SSLSocket.server_side": (None, (3, 2)),
    "ssl.SSLSocket.session": (None, (3, 6)),
    "ssl.SSLSocket.session_reused": (None, (3, 6)),
    "ssl.VERIFY_CRL_CHECK_CHAIN": ((2, 7), (3, 4)),
    "ssl.VERIFY_CRL_CHECK_LEAF": ((2, 7), (3, 4)),
    "ssl.VERIFY_DEFAULT": ((2, 7), (3, 4)),
    "ssl.VERIFY_X509_STRICT": ((2, 7), (3, 4)),
    "ssl.VERIFY_X509_TRUSTED_FIRST": ((2, 7), (3, 4)),
    "stat.FILE_ATTRIBUTE_ARCHIVE": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_COMPRESSED": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_DEVICE": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_DIRECTORY": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_ENCRYPTED": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_HIDDEN": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_INTEGRITY_STREAM": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_NORMAL": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_NOT_CONTENT_INDEXED": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_NO_SCRUB_DATA": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_OFFLINE": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_READONLY": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_REPARSE_POINT": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_SPARSE_FILE": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_SYSTEM": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_TEMPORARY": (None, (3, 5)),
    "stat.FILE_ATTRIBUTE_VIRTUAL": (None, (3, 5)),
    "stat.IO_REPARSE_TAG_APPEXECLINK": (None, (3, 8)),
    "stat.IO_REPARSE_TAG_MOUNT_POINT": (None, (3, 8)),
    "stat.IO_REPARSE_TAG_SYMLINK": (None, (3, 8)),
    "stat.S_IFDOOR": (None, (3, 4)),
    "stat.S_IFPORT": (None, (3, 4)),
    "stat.S_IFWHT": (None, (3, 4)),
    "string.Template.braceidpattern": (None, (3, 7)),
    "string.Template.flags": (None, (3, 2)),
    "subprocess.ABOVE_NORMAL_PRIORITY_CLASS": (None, (3, 7)),
    "subprocess.BELOW_NORMAL_PRIORITY_CLASS": (None, (3, 7)),
    "subprocess.CREATE_BREAKAWAY_FROM_JOB": (None, (3, 7)),
    "subprocess.CREATE_DEFAULT_ERROR_MODE": (None, (3, 7)),
    "subprocess.CREATE_NO_WINDOW": (None, (3, 7)),
    "subprocess.CalledProcessError.stderr": (None, (3, 5)),
    "subprocess.CalledProcessError.stdout": (None, (3, 5)),
    "subprocess.DETACHED_PROCESS": (None, (3, 7)),
    "subprocess.DEVNULL": (None, (3, 3)),
    "subprocess.HIGH_PRIORITY_CLASS": (None, (3, 7)),
    "subprocess.IDLE_PRIORITY_CLASS": (None, (3, 7)),
    "subprocess.NORMAL_PRIORITY_CLASS": (None, (3, 7)),
    "subprocess.Popen.args": (None, (3, 3)),
    "subprocess.REALTIME_PRIORITY_CLASS": (None, (3, 7)),
    "subprocess.STARTUPINFO.lpAttributeList": (None, (3, 7)),
    "subprocess.TimeoutExpired.stderr": (None, (3, 5)),
    "subprocess.TimeoutExpired.stdout": (None, (3, 5)),
    "sys.__breakpointhook__": (None, (3, 7)),
    "sys.__interactivehook__": (None, (3, 4)),
    "sys.__unraisablehook__": (None, (3, 8)),
    "sys._xoptions": (None, (3, 2)),
    "sys.abiflags": (None, (3, 2)),
    "sys.api_version": ((2, 3), None),  # TODO
    "sys.base_exec_prefix": (None, (3, 3)),
    "sys.base_prefix": (None, (3, 3)),
    "sys.byteorder": ((2, 0), None),  # TODO
    "sys.dont_write_bytecode": ((2, 6), None),  # TODO
    "sys.flags": ((2, 6), None),  # TODO
    "sys.flags.dev_mode": (None, (3, 7)),
    "sys.flags.hash_randomization": ((2, 7), (3, 2)),
    "sys.flags.isolated": (None, (3, 4)),
    "sys.flags.quiet": (None, (3, 2)),
    "sys.flags.utf8_mode": (None, (3, 7)),
    "sys.float_repr_style": (None, (3, 1)),
    "sys.getwindowsversion.build": ((2, 7), None),  # TODO
    "sys.getwindowsversion.major": ((2, 7), None),  # TODO
    "sys.getwindowsversion.minor": ((2, 7), None),  # TODO
    "sys.getwindowsversion.platform": ((2, 7), None),  # TODO
    "sys.getwindowsversion.product_type": ((2, 7), None),  # TODO
    "sys.getwindowsversion.service_pack": ((2, 7), None),  # TODO
    "sys.getwindowsversion.service_pack_major": ((2, 7), None),  # TODO
    "sys.getwindowsversion.service_pack_minor": ((2, 7), None),  # TODO
    "sys.getwindowsversion.suite_mask": ((2, 7), None),  # TODO
    "sys.hash_info": (None, (3, 2)),
    "sys.hash_info.algorithm": (None, (3, 4)),
    "sys.hash_info.hash_bits": (None, (3, 4)),
    "sys.hash_info.seed_bits": (None, (3, 4)),
    "sys.hexversion": ((2, 0), None),  # TODO
    "sys.implementation": (None, (3, 3)),
    "sys.int_info": (None, (3, 1)),
    "sys.long_info": ((2, 7), None),  # TODO
    "sys.py3kwarning": ((2, 6), None),  # TODO
    "sys.pycache_prefix": (None, (3, 8)),
    "sys.subversion": ((2, 5), None),  # TODO
    "sys.thread_info": (None, (3, 3)),
    "sys.version_info": ((2, 0), None),  # TODO
    "sys.version_info.major": ((2, 7), None),  # TODO
    "sys.version_info.micro": ((2, 7), None),  # TODO
    "sys.version_info.minor": ((2, 7), None),  # TODO
    "sys.version_info.releaselevel": ((2, 7), None),  # TODO
    "tarfile.DEFAULT_FORMAT": ((2, 6), None),  # TODO
    "tarfile.GNU_FORMAT": ((2, 6), None),  # TODO
    "tarfile.PAX_FORMAT": ((2, 6), None),  # TODO
    "tarfile.TarInfo.pax_headers": ((2, 6), None),  # TODO
    "tarfile.USTAR_FORMAT": ((2, 6), None),  # TODO
    "textwrap.TextWrapper.break_on_hyphens": ((2, 6), None),  # TODO
    "textwrap.TextWrapper.drop_whitespace": ((2, 6), None),  # TODO
    "textwrap.TextWrapper.max_lines": (None, (3, 4)),
    "textwrap.TextWrapper.placeholder": (None, (3, 4)),
    "textwrap.TextWrapper.tabsize": (None, (3, 3)),
    "threading.TIMEOUT_MAX": (None, (3, 2)),
    "threading.Thread.daemon": ((2, 6), None),  # TODO
    "threading.Thread.ident": ((2, 6), None),  # TODO
    "threading.Thread.name": ((2, 6), None),  # TODO
    "threading.Thread.native_id": (None, (3, 8)),
    "time.CLOCK_BOOTTIME": (None, (3, 7)),
    "time.CLOCK_HIGHRES": (None, (3, 3)),
    "time.CLOCK_MONOTONIC": (None, (3, 3)),
    "time.CLOCK_MONOTONIC_RAW": (None, (3, 3)),
    "time.CLOCK_PROCESS_CPUTIME_ID": (None, (3, 3)),
    "time.CLOCK_PROF": (None, (3, 7)),
    "time.CLOCK_REALTIME": (None, (3, 3)),
    "time.CLOCK_THREAD_CPUTIME_ID": (None, (3, 3)),
    "time.CLOCK_UPTIME": (None, (3, 7)),
    "time.CLOCK_UPTIME_RAW": (None, (3, 8)),
    "time.struct_time.tm_gmtoff": (None, (3, 3)),
    "time.struct_time.tm_zone": (None, (3, 3)),
    "token.ASYNC": (None, (3, 5)),
    "token.AWAIT": (None, (3, 5)),
    "token.COMMENT": (None, (3, 7)),
    "token.ENCODING": (None, (3, 7)),
    "token.NL": (None, (3, 7)),
    "token.TYPE_COMMENT": (None, (3, 8)),
    "tracemalloc.Filter.domain": (None, (3, 6)),
    "tracemalloc.Trace.domain": (None, (3, 6)),
    "types.AsyncGeneratorType": (None, (3, 6)),
    "types.BooleanType": ((2, 3), None),  # TODO
    "types.CellType": (None, (3, 8)),
    "types.ClassMethodDescriptorType": (None, (3, 7)),
    "types.CoroutineType": (None, (3, 5)),
    "types.GeneratorType": ((2, 2), None),  # TODO
    "types.GetSetDescriptorType": ((2, 5), None),  # TODO
    "types.MemberDescriptorType": ((2, 5), None),  # TODO
    "types.MethodDescriptorType": (None, (3, 7)),
    "types.MethodWrapperType": (None, (3, 7)),
    "types.StringTypes": ((2, 2), None),  # TODO
    "types.WrapperDescriptorType": (None, (3, 7)),
    "typing.ClassVar": (None, (3, 5)),
    "typing.Final": (None, (3, 8)),
    "typing.Literal": (None, (3, 8)),
    "typing.NoReturn": (None, (3, 5)),
    "typing.TYPE_CHECKING": (None, (3, 5)),
    "unicodedata.ucd_3_2_0": ((2, 3), None),  # TODO
    "unicodedata.unidata_version": ((2, 3), None),  # TODO
    "unittest.TestCase.longMessage": (None, (3, 1)),
    "unittest.TestCase.maxDiff": (None, (3, 2)),
    "unittest.TestLoader.errors": (None, (3, 5)),
    "unittest.TestLoader.testNamePatterns": (None, (3, 7)),
    "unittest.TestResult.buffer": ((2, 7), (3, 2)),
    "unittest.TestResult.failfast": ((2, 7), (3, 2)),
    "unittest.TestResult.skipped": ((2, 7), (3, 1)),
    "unittest.TestResult.tb_locals": (None, (3, 5)),
    "urllib.error.HTTPError.headers": (None, (3, 4)),
    "urllib.request.Request.method": (None, (3, 3)),
    "urlparse.urlparse.fragment": ((2, 5), None),  # TODO
    "urlparse.urlparse.hostname": ((2, 5), None),  # TODO
    "urlparse.urlparse.netloc": ((2, 5), None),  # TODO
    "urlparse.urlparse.params": ((2, 5), None),  # TODO
    "urlparse.urlparse.password": ((2, 5), None),  # TODO
    "urlparse.urlparse.path": ((2, 5), None),  # TODO
    "urlparse.urlparse.port": ((2, 5), None),  # TODO
    "urlparse.urlparse.query": ((2, 5), None),  # TODO
    "urlparse.urlparse.scheme": ((2, 5), None),  # TODO
    "urlparse.urlparse.username": ((2, 5), None),  # TODO
    "urlparse.urlsplit.fragment": ((2, 5), None),  # TODO
    "urlparse.urlsplit.hostname": ((2, 5), None),  # TODO
    "urlparse.urlsplit.netloc": ((2, 5), None),  # TODO
    "urlparse.urlsplit.password": ((2, 5), None),  # TODO
    "urlparse.urlsplit.path": ((2, 5), None),  # TODO
    "urlparse.urlsplit.port": ((2, 5), None),  # TODO
    "urlparse.urlsplit.query": ((2, 5), None),  # TODO
    "urlparse.urlsplit.scheme": ((2, 5), None),  # TODO
    "urlparse.urlsplit.username": ((2, 5), None),  # TODO
    "uuid.UUID.is_safe": (None, (3, 7)),
    "weakref.ref.__callback__": (None, (3, 4)),
    "winreg.REG_QWORD": (None, (3, 6)),
    "winreg.REG_QWORD_LITTLE_ENDIAN": (None, (3, 6)),
    "xml.dom.DOMSTRING_SIZE_ERR": ((2, 1), None),  # TODO
    "xml.dom.EMPTY_NAMESPACE": ((2, 2), None),  # TODO
    "xml.dom.HIERARCHY_REQUEST_ERR": ((2, 1), None),  # TODO
    "xml.dom.INDEX_SIZE_ERR": ((2, 1), None),  # TODO
    "xml.dom.INUSE_ATTRIBUTE_ERR": ((2, 1), None),  # TODO
    "xml.dom.INVALID_ACCESS_ERR": ((2, 1), None),  # TODO
    "xml.dom.INVALID_CHARACTER_ERR": ((2, 1), None),  # TODO
    "xml.dom.INVALID_MODIFICATION_ERR": ((2, 1), None),  # TODO
    "xml.dom.INVALID_STATE_ERR": ((2, 1), None),  # TODO
    "xml.dom.NAMESPACE_ERR": ((2, 1), None),  # TODO
    "xml.dom.NOT_FOUND_ERR": ((2, 1), None),  # TODO
    "xml.dom.NOT_SUPPORTED_ERR": ((2, 1), None),  # TODO
    "xml.dom.NO_DATA_ALLOWED_ERR": ((2, 1), None),  # TODO
    "xml.dom.NO_MODIFICATION_ALLOWED_ERR": ((2, 1), None),  # TODO
    "xml.dom.SYNTAX_ERR": ((2, 1), None),  # TODO
    "xml.dom.WRONG_DOCUMENT_ERR": ((2, 1), None),  # TODO
    "xml.dom.XHTML_NAMESPACE": ((2, 2), None),  # TODO
    "xml.dom.XMLNS_NAMESPACE": ((2, 2), None),  # TODO
    "xml.dom.XML_NAMESPACE": ((2, 2), None),  # TODO
    "xml.parsers.expat.ExpatError.code": ((2, 1), None),  # TODO
    "xml.parsers.expat.ExpatError.lineno": ((2, 1), None),  # TODO
    "xml.parsers.expat.ExpatError.offset": ((2, 1), None),  # TODO
    "xml.parsers.expat.XMLParserType.CurrentByteIndex": ((2, 4), None),  # TODO
    "xml.parsers.expat.XMLParserType.CurrentColumnNumber": ((2, 4), None),  # TODO
    "xml.parsers.expat.XMLParserType.CurrentLineNumber": ((2, 4), None),  # TODO
    "xml.parsers.expat.XMLParserType.buffer_size": ((2, 3), None),  # TODO
    "xml.parsers.expat.XMLParserType.buffer_text": ((2, 3), None),  # TODO
    "xml.parsers.expat.XMLParserType.buffer_used": ((2, 3), None),  # TODO
    "xml.parsers.expat.XMLParserType.ordered_attributes": ((2, 1), None),  # TODO
    "xml.parsers.expat.XMLParserType.returns_unicode": ((2, 0), None),  # TODO
    "xml.parsers.expat.XMLParserType.specified_attributes": ((2, 1), None),  # TODO
    "xml.parsers.expat.errors.codes": (None, (3, 2)),
    "xml.parsers.expat.errors.messages": (None, (3, 2)),
    "zipfile.ZIP_BZIP2": (None, (3, 3)),
    "zipfile.ZIP_LZMA": (None, (3, 3)),
    "zlib.Decompress.eof": (None, (3, 3)),
    "zlib.ZLIB_RUNTIME_VERSION": (None, (3, 3)),
}

decorators_rules = {
    "abc.abstractclassmethod": (None, (3, 2)),
    "abc.abstractstaticmethod": (None, (3, 2)),
    "classmethod": ((2, 2), None),  # TODO
    "contextlib.asynccontextmanager": (None, (3, 7)),
    "functools.cached_property": (None, (3, 8)),
    "functools.lru_cache": (None, (3, 2)),
    "functools.singledispatch": (None, (3, 4)),
    "functools.singledispatchmethod": (None, (3, 8)),
    "functools.total_ordering": ((2, 7), (3, 2)),
    "property": ((2, 2), None),  # TODO
    "property.deleter": ((2, 6), None),  # TODO
    "property.getter": ((2, 6), None),  # TODO
    "property.setter": ((2, 6), None),  # TODO
    "reprlib.recursive_repr": (None, (3, 2)),
    "staticmethod": ((2, 2), None),  # TODO
    "typing.final": (None, (3, 8)),
    "typing.runtime_checkable": (None, (3, 8)),
    "unittest.expectedFailure": (None, (3, 1)),
    "unittest.skip": (None, (3, 1)),
    "unittest.skipIf": (None, (3, 1)),
    "unittest.skipUnless": (None, (3, 1)),
}

kwargs_rules = {
    ("BaseHTTPServer.BaseHTTPRequestHandler.date_time_string", "timestamp"): ((2, 5), None),  # TODO
    ("ConfigParser.ConfigParser", "allow_no_value"): ((2, 6), None),  # TODO
    ("ConfigParser.ConfigParser", "dict_type"): ((2, 6), None),  # TODO
    ("ConfigParser.RawConfigParser", "allow_no_value"): ((2, 6), None),  # TODO
    ("ConfigParser.RawConfigParser", "dict_type"): ((2, 6), None),  # TODO
    ("ConfigParser.SafeConfigParser", "allow_no_value"): ((2, 6), None),  # TODO
    ("ConfigParser.SafeConfigParser", "dict_type"): ((2, 6), None),  # TODO
    ("ImportError", "name"): (None, (3, 3)),
    ("ImportError", "path"): (None, (3, 3)),
    ("OSError", "filename2"): (None, (3, 4)),
    ("Queue.Queue.get", "timeout"): ((2, 3), None),  # TODO
    ("Queue.Queue.put", "timeout"): ((2, 3), None),  # TODO
    ("SimpleXMLRPCServer.CGIXMLRPCRequestHandler", "allow_none"): ((2, 5), None),  # TODO
    ("SimpleXMLRPCServer.CGIXMLRPCRequestHandler", "encoding"): ((2, 5), None),  # TODO
    ("SimpleXMLRPCServer.SimpleXMLRPCServer", "allow_none"): ((2, 5), None),  # TODO
    ("SimpleXMLRPCServer.SimpleXMLRPCServer", "bind_and_activate"): ((2, 6), None),  # TODO
    ("SimpleXMLRPCServer.SimpleXMLRPCServer", "encoding"): ((2, 5), None),  # TODO
    ("SimpleXMLRPCServer.SimpleXMLRPCServer.register_instance", "allow_dotted_names"): ((2, 3), None),  # TODO
    ("Tkinter.Tk", "useTk"): ((2, 4), None),  # TODO
    ("__import__", "level"): ((2, 5), None),  # TODO
    ("_thread.lock.acquire", "timeout"): (None, (3, 2)),
    ("argparse.ArgumentParser", "allow_abbrev"): (None, (3, 5)),
    ("argparse.ArgumentParser.add_subparsers", "required"): (None, (3, 7)),
    ("argparse.FileType", "encodings"): (None, (3, 4)),
    ("argparse.FileType", "errors"): (None, (3, 4)),
    ("ast.parse", "feature_version"): (None, (3, 8)),
    ("ast.parse", "type_comments"): (None, (3, 8)),
    ("asyncio.Future.add_done_callback", "context"): (None, (3, 7)),
    ("asyncio.Task", "name"): (None, (3, 8)),
    ("asyncio.create_task", "name"): (None, (3, 8)),
    ("asyncio.loop.call_at", "context"): (None, (3, 7)),
    ("asyncio.loop.call_later", "context"): (None, (3, 7)),
    ("asyncio.loop.call_soon", "context"): (None, (3, 7)),
    ("asyncio.loop.call_soon_threadsafe", "context"): (None, (3, 7)),
    ("asyncio.loop.connect_accepted_socket", "ssl_handshake_timeout"): (None, (3, 7)),
    ("asyncio.loop.create_connection", "happy_eyeballs_delay"): (None, (3, 8)),
    ("asyncio.loop.create_connection", "interleave"): (None, (3, 8)),
    ("asyncio.loop.create_connection", "ssl_handshake_timeout"): (None, (3, 7)),
    ("asyncio.loop.create_datagram_endpoint", "allow_broadcast"): (None, (3, 4)),
    ("asyncio.loop.create_datagram_endpoint", "family"): (None, (3, 4)),
    ("asyncio.loop.create_datagram_endpoint", "flags"): (None, (3, 4)),
    ("asyncio.loop.create_datagram_endpoint", "proto"): (None, (3, 4)),
    ("asyncio.loop.create_datagram_endpoint", "reuse_address"): (None, (3, 4)),
    ("asyncio.loop.create_datagram_endpoint", "reuse_port"): (None, (3, 4)),
    ("asyncio.loop.create_datagram_endpoint", "sock"): (None, (3, 4)),
    ("asyncio.loop.create_server", "ssl_handshake_timeout"): (None, (3, 7)),
    ("asyncio.loop.create_server", "start_serving"): (None, (3, 7)),
    ("asyncio.loop.create_task", "name"): (None, (3, 8)),
    ("asyncio.loop.create_unix_connection", "ssl_handshake_timeout"): (None, (3, 7)),
    ("asyncio.loop.create_unix_server", "ssl_handshake_timeout"): (None, (3, 7)),
    ("asyncio.loop.create_unix_server", "start_serving"): (None, (3, 7)),
    ("asyncio.open_connection", "ssl_handshake_timeout"): (None, (3, 7)),
    ("asyncio.open_unix_connection", "ssl_handshake_timeout"): (None, (3, 7)),
    ("asyncio.start_server", "ssl_handshake_timeout"): (None, (3, 7)),
    ("asyncio.start_server", "start_serving"): (None, (3, 7)),
    ("asyncio.start_unix_server", "ssl_handshake_timeout"): (None, (3, 7)),
    ("asyncio.start_unix_server", "start_serving"): (None, (3, 7)),
    ("bdb.Bdb", "skip"): ((2, 7), (3, 1)),
    ("binascii.b2a_base64", "newline"): (None, (3, 6)),
    ("binascii.b2a_hex", "bytes_per_sep"): (None, (3, 8)),
    ("binascii.b2a_hex", "sep"): (None, (3, 8)),
    ("binascii.b2a_uu", "backtick"): (None, (3, 7)),
    ("bytearray.hex", "bytes_per_sep"): (None, (3, 8)),
    ("bytearray.hex", "sep"): (None, (3, 8)),
    ("bytearray.translate", "delete"): (None, (3, 6)),
    ("bytes.hex", "bytes_per_sep"): (None, (3, 8)),
    ("bytes.hex", "sep"): (None, (3, 8)),
    ("bytes.translate", "delete"): (None, (3, 6)),
    ("bz2.BZ2Decompressor.decompress", "max_length"): (None, (3, 5)),
    ("cgi.parse_multipart", "encoding"): (None, (3, 7)),
    ("cgi.parse_multipart", "errors"): (None, (3, 7)),
    ("cmath.log", "base"): ((2, 4), None),  # TODO
    ("cmd.Cmd", "stdin"): ((2, 3), None),  # TODO
    ("cmd.Cmd", "stdout"): ((2, 3), None),  # TODO
    ("code.interact", "exitmsg"): (None, (3, 6)),
    ("codecs.StreamReader.read", "chars"): ((2, 4), None),  # TODO
    ("codecs.StreamReader.read", "firstline"): ((2, 4), None),  # TODO
    ("codecs.StreamReader.readline", "keepends"): ((2, 4), None),  # TODO
    ("collections.ChainMap.new_child", "m"): (None, (3, 4)),
    ("collections.deque", "maxlen"): ((2, 6), None),  # TODO
    ("collections.namedtuple", "defaults"): (None, (3, 7)),
    ("collections.namedtuple", "module"): (None, (3, 6)),
    ("collections.namedtuple", "rename"): ((2, 7), (3, 1)),
    ("compile", "dont_inherit"): ((2, 3), None),  # TODO
    ("compile", "flags"): ((2, 3), None),  # TODO
    ("compile", "optimize"): (None, (3, 2)),
    ("compileall.compile_dir", "invalidation_mode"): (None, (3, 7)),
    ("compileall.compile_dir", "legacy"): (None, (3, 2)),
    ("compileall.compile_dir", "optimize"): (None, (3, 2)),
    ("compileall.compile_dir", "workers"): (None, (3, 5)),
    ("compileall.compile_file", "invalidation_mode"): (None, (3, 7)),
    ("compileall.compile_path", "invalidation_mode"): (None, (3, 7)),
    ("compileall.compile_path", "legacy"): (None, (3, 2)),
    ("compileall.compile_path", "optimize"): (None, (3, 2)),
    ("concurrent.futures.Executor.map", "chunksize"): (None, (3, 5)),
    ("concurrent.futures.ProcessPoolExecutor", "initargs"): (None, (3, 7)),
    ("concurrent.futures.ProcessPoolExecutor", "initializer"): (None, (3, 7)),
    ("concurrent.futures.ProcessPoolExecutor", "mp_context"): (None, (3, 7)),
    ("concurrent.futures.ThreadPoolExecutor", "initargs"): (None, (3, 7)),
    ("concurrent.futures.ThreadPoolExecutor", "initializer"): (None, (3, 7)),
    ("concurrent.futures.ThreadPoolExecutor", "thread_name_prefix"): (None, (3, 6)),
    ("configparser.ConfigParser", "allow_no_value"): (None, (3, 2)),
    ("configparser.ConfigParser", "comment_prefixes"): (None, (3, 2)),
    ("configparser.ConfigParser", "converters"): (None, (3, 5)),
    ("configparser.ConfigParser", "default_section"): (None, (3, 2)),
    ("configparser.ConfigParser", "delimiters"): (None, (3, 2)),
    ("configparser.ConfigParser", "empty_lines_in_values"): (None, (3, 2)),
    ("configparser.ConfigParser", "interpolation"): (None, (3, 2)),
    ("configparser.ConfigParser", "strict"): (None, (3, 2)),
    ("configparser.ConfigParser.read", "encoding"): (None, (3, 2)),
    ("configparser.DuplicateSectionError", "lineno"): (None, (3, 2)),
    ("configparser.DuplicateSectionError", "source"): (None, (3, 2)),
    ("configparser.ParsingError", "source"): (None, (3, 2)),
    ("crypt.mksalt", "rounds"): (None, (3, 7)),
    ("ctypes.CDLL", "use_errno"): ((2, 6), None),  # TODO
    ("ctypes.CDLL", "use_last_error"): ((2, 6), None),  # TODO
    ("ctypes.CDLL", "winmode"): (None, (3, 8)),
    ("ctypes.CFUNCTYPE", "use_errno"): ((2, 6), None),  # TODO
    ("ctypes.CFUNCTYPE", "use_last_error"): ((2, 6), None),  # TODO
    ("ctypes.OleDLL", "use_errno"): ((2, 6), None),  # TODO
    ("ctypes.OleDLL", "use_last_error"): ((2, 6), None),  # TODO
    ("ctypes.OleDLL", "winmode"): (None, (3, 8)),
    ("ctypes.WinDLL", "use_errno"): ((2, 6), None),  # TODO
    ("ctypes.WinDLL", "use_last_error"): ((2, 6), None),  # TODO
    ("ctypes.WinDLL", "winmode"): (None, (3, 8)),
    ("ctypes.byref", "offset"): ((2, 6), None),  # TODO
    ("datetime.datetime", "fold"): (None, (3, 6)),
    ("datetime.datetime.combine", "tzinfo"): (None, (3, 6)),
    ("datetime.datetime.isoformat", "timespec"): (None, (3, 6)),
    ("datetime.datetime.replace", "fold"): (None, (3, 6)),
    ("datetime.time.isoformat", "timespec"): (None, (3, 6)),
    ("datetime.time.replace", "fold"): (None, (3, 6)),
    ("difflib.HtmlDiff.make_file", "charset"): (None, (3, 5)),
    ("difflib.SequenceMatcher", "autojunk"): ((2, 7), (3, 2)),
    ("dis.dis", "depth"): (None, (3, 7)),
    ("dis.dis", "file"): (None, (3, 4)),
    ("dis.disassemble", "file"): (None, (3, 4)),
    ("dis.distb", "file"): (None, (3, 4)),
    ("dis.show_code", "file"): (None, (3, 4)),
    ("dis.stack_effect", "jump"): (None, (3, 8)),
    ("doctest.DocFileSuite", "encoding"): ((2, 5), None),  # TODO
    ("doctest.DocTestSuite", "extraglobs"): ((2, 4), None),  # TODO
    ("doctest.DocTestSuite", "globs"): ((2, 4), None),  # TODO
    ("doctest.DocTestSuite", "optionflags"): ((2, 4), None),  # TODO
    ("doctest.DocTestSuite", "setUp"): ((2, 4), None),  # TODO
    ("doctest.DocTestSuite", "tearDown"): ((2, 4), None),  # TODO
    ("doctest.DocTestSuite", "test_finder"): ((2, 4), None),  # TODO
    ("doctest.debug", "pm"): ((2, 4), None),  # TODO
    ("doctest.testfile", "encoding"): ((2, 5), None),  # TODO
    ("doctest.testmod", "exclude_empty"): ((2, 4), None),  # TODO
    ("doctest.testmod", "extraglobs"): ((2, 4), None),  # TODO
    ("doctest.testmod", "optionflags"): ((2, 3), None),  # TODO
    ("doctest.testmod", "raise_on_error"): ((2, 4), None),  # TODO
    ("email.generator.BytesGenerator", "policy"): (None, (3, 3)),
    ("email.generator.Generator", "policy"): (None, (3, 3)),
    ("email.generator.Generator.flatten", "linesep"): (None, (3, 2)),
    ("email.header.Header.encode", "linesep"): (None, (3, 2)),
    ("email.message.EmailMessage.set_param", "replace"): (None, (3, 4)),
    ("email.message.Message", "policy"): (None, (3, 3)),
    ("email.message.Message.as_string", "policy"): (None, (3, 4)),
    ("email.message.Message.get_param", "unquote"): ((2, 2), None),  # TODO
    ("email.message.Message.get_params", "unquote"): ((2, 2), None),  # TODO
    ("email.message.Message.set_param", "replace"): (None, (3, 4)),
    ("email.message.Message.set_payload", "charset"): ((2, 2), None),  # TODO
    ("email.message_from_binary_file", "policy"): (None, (3, 3)),
    ("email.message_from_bytes", "policy"): (None, (3, 3)),
    ("email.message_from_file", "policy"): (None, (3, 3)),
    ("email.message_from_file", "strict"): ((2, 2), None),  # TODO
    ("email.message_from_string", "policy"): (None, (3, 3)),
    ("email.message_from_string", "strict"): ((2, 2), None),  # TODO
    ("email.mime.application.MIMEApplication", "policy"): (None, (3, 6)),
    ("email.mime.audio.MIMEAudio", "policy"): (None, (3, 6)),
    ("email.mime.base.MIMEBase", "policy"): (None, (3, 6)),
    ("email.mime.image.MIMEImage", "policy"): (None, (3, 6)),
    ("email.mime.message.MIMEMessage", "policy"): (None, (3, 6)),
    ("email.mime.multipart.MIMEMultipart", "policy"): (None, (3, 6)),
    ("email.mime.text.MIMEText", "policy"): (None, (3, 6)),
    ("email.parser.BytesFeedParser", "policy"): (None, (3, 3)),
    ("email.parser.BytesParser", "policy"): (None, (3, 3)),
    ("email.parser.FeedParser", "policy"): (None, (3, 3)),
    ("email.parser.Parser", "policy"): (None, (3, 3)),
    ("email.policy.Policy", "mangle_from_"): (None, (3, 5)),
    ("email.utils.formataddr", "charset"): (None, (3, 3)),
    ("email.utils.make_msgid", "domain"): (None, (3, 2)),
    ("enum.Enum", "start"): (None, (3, 5)),
    ("enumerate", "start"): ((2, 6), None),  # TODO
    ("fileinput.FileInput", "mode"): ((2, 5), None),  # TODO
    ("fileinput.FileInput", "openhook"): ((2, 5), None),  # TODO
    ("fileinput.hook_encoded", "errors"): (None, (3, 6)),
    ("fileinput.input", "mode"): ((2, 5), None),  # TODO
    ("fileinput.input", "openhook"): ((2, 5), None),  # TODO
    ("ftplib.FTP", "source_address"): (None, (3, 3)),
    ("ftplib.FTP", "timeout"): ((2, 6), None),  # TODO
    ("ftplib.FTP.connect", "source_address"): (None, (3, 3)),
    ("ftplib.FTP.connect", "timeout"): ((2, 6), None),  # TODO
    ("ftplib.FTP.storbinary", "callback"): ((2, 6), None),  # TODO
    ("ftplib.FTP.storbinary", "rest"): ((2, 7), (3, 2)),
    ("ftplib.FTP.storlines", "callback"): ((2, 6), None),  # TODO
    ("ftplib.FTP_TLS", "context"): ((2, 7), None),  # TODO
    ("ftplib.FTP_TLS", "source_address"): (None, (3, 3)),
    ("functools.lru_cache", "typed"): (None, (3, 3)),
    ("functools.lru_cache", "user_function"): (None, (3, 8)),
    ("gc.collect", "generation"): ((2, 5), None),  # TODO
    ("gc.get_objects", "generation"): (None, (3, 8)),
    ("getpass.getpass", "stream"): ((2, 5), None),  # TODO
    ("gettext.NullTranslations.install", "names"): ((2, 5), None),  # TODO
    ("gettext.install", "codeset"): ((2, 4), None),  # TODO
    ("gettext.install", "names"): ((2, 5), None),  # TODO
    ("gettext.translation", "codeset"): ((2, 4), None),  # TODO
    ("glob.glob", "recursive"): (None, (3, 5)),
    ("gzip.GzipFile", "mtime"): ((2, 7), (3, 1)),
    ("gzip.compress", "mtime"): (None, (3, 8)),
    ("gzip.open", "encoding"): (None, (3, 3)),
    ("gzip.open", "errors"): (None, (3, 3)),
    ("gzip.open", "newline"): (None, (3, 3)),
    ("heapq.merge", "key"): (None, (3, 5)),
    ("heapq.merge", "reverse"): (None, (3, 5)),
    ("heapq.nlargest", "key"): ((2, 5), None),  # TODO
    ("heapq.nsmallest", "key"): ((2, 5), None),  # TODO
    ("html.parser.HTMLParser", "convert_charrefs"): (None, (3, 4)),
    ("http.client.HTTPConnection", "blocksize"): (None, (3, 7)),
    ("http.client.HTTPConnection", "source_address"): (None, (3, 2)),
    ("http.client.HTTPConnection.endheaders", "encode_chunked"): (None, (3, 6)),
    ("http.client.HTTPConnection.request", "encode_chunked"): (None, (3, 6)),
    ("http.client.HTTPSConnection", "check_hostname"): (None, (3, 2)),
    ("http.client.HTTPSConnection", "context"): (None, (3, 2)),
    ("http.client.HTTPSConnection", "source_address"): (None, (3, 2)),
    ("http.server.BaseHTTPRequestHandler.send_error", "explain"): (None, (3, 4)),
    ("httplib.HTTPConnection", "source_address"): ((2, 7), None),  # TODO
    ("httplib.HTTPConnection", "timeout"): ((2, 6), None),  # TODO
    ("httplib.HTTPConnection.endheaders", "message_body"): ((2, 7), None),  # TODO
    ("httplib.HTTPConnection.putrequest", "skip_accept_encoding"): ((2, 4), None),  # TODO
    ("httplib.HTTPSConnection", "context"): ((2, 7), None),  # TODO
    ("httplib.HTTPSConnection", "source_address"): ((2, 7), None),  # TODO
    ("httplib.HTTPSConnection", "timeout"): ((2, 6), None),  # TODO
    ("imaplib.IMAP4_SSL", "ssl_context"): (None, (3, 3)),
    ("importlib.util.cache_from_source", "optimization"): (None, (3, 5)),
    ("inspect.signature", "follow_wrapped"): (None, (3, 5)),
    ("io.FileIO", "opener"): (None, (3, 3)),
    ("io.TextIOWrapper", "write_through"): (None, (3, 3)),
    ("itertools.accumulate", "func"): (None, (3, 3)),
    ("itertools.accumulate", "initial"): (None, (3, 8)),
    ("itertools.count", "step"): ((2, 7), (3, 1)),
    ("json.JSONDecoder", "object_pairs_hook"): ((2, 7), (3, 1)),
    ("json.load", "object_pairs_hook"): ((2, 7), (3, 1)),
    ("linecache.getline", "module_globals"): ((2, 5), None),  # TODO
    ("locale.format", "monetary"): ((2, 5), None),  # TODO
    ("locale.format_string", "monetary"): (None, (3, 7)),
    ("logging.FileHandler", "delay"): ((2, 6), None),  # TODO
    ("logging.Formatter", "style"): (None, (3, 2)),
    ("logging.Formatter", "validate"): (None, (3, 8)),
    ("logging.LogRecord", "func"): ((2, 5), None),  # TODO
    ("logging.Logger.critical", "stack_info"): (None, (3, 2)),
    ("logging.Logger.critical", "stacklevel"): (None, (3, 8)),
    ("logging.Logger.debug", "stack_info"): (None, (3, 2)),
    ("logging.Logger.debug", "stacklevel"): (None, (3, 8)),
    ("logging.Logger.error", "stack_info"): (None, (3, 2)),
    ("logging.Logger.error", "stacklevel"): (None, (3, 8)),
    ("logging.Logger.exception", "stack_info"): (None, (3, 2)),
    ("logging.Logger.exception", "stacklevel"): (None, (3, 8)),
    ("logging.Logger.info", "stack_info"): (None, (3, 2)),
    ("logging.Logger.info", "stacklevel"): (None, (3, 8)),
    ("logging.Logger.log", "stack_info"): (None, (3, 2)),
    ("logging.Logger.log", "stacklevel"): (None, (3, 8)),
    ("logging.Logger.makeRecord", "extra"): ((2, 5), None),  # TODO
    ("logging.Logger.makeRecord", "func"): ((2, 5), None),  # TODO
    ("logging.Logger.warn", "stack_info"): (None, (3, 2)),
    ("logging.Logger.warn", "stacklevel"): (None, (3, 8)),
    ("logging.Logger.warning", "stack_info"): (None, (3, 2)),
    ("logging.Logger.warning", "stacklevel"): (None, (3, 8)),
    ("logging.basicConfig", "datefmt"): ((2, 4), None),  # TODO
    ("logging.basicConfig", "filemode"): ((2, 4), None),  # TODO
    ("logging.basicConfig", "filename"): ((2, 4), None),  # TODO
    ("logging.basicConfig", "force"): (None, (3, 8)),
    ("logging.basicConfig", "format"): ((2, 4), None),  # TODO
    ("logging.basicConfig", "handlers"): (None, (3, 3)),
    ("logging.basicConfig", "level"): ((2, 4), None),  # TODO
    ("logging.basicConfig", "stream"): ((2, 4), None),  # TODO
    ("logging.basicConfig", "style"): (None, (3, 2)),
    ("logging.config.fileConfig", "disable_existing_loggers"): ((2, 6), None),  # TODO
    ("logging.config.listen", "verify"): (None, (3, 4)),
    ("logging.critical", "extra"): ((2, 5), None),  # TODO
    ("logging.critical", "stack_info"): (None, (3, 2)),
    ("logging.critical", "stacklevel"): (None, (3, 8)),
    ("logging.debug", "extra"): ((2, 5), None),  # TODO
    ("logging.debug", "stack_info"): (None, (3, 2)),
    ("logging.debug", "stacklevel"): (None, (3, 8)),
    ("logging.error", "extra"): ((2, 5), None),  # TODO
    ("logging.error", "stack_info"): (None, (3, 2)),
    ("logging.error", "stacklevel"): (None, (3, 8)),
    ("logging.exception", "extra"): ((2, 5), None),  # TODO
    ("logging.exception", "stack_info"): (None, (3, 2)),
    ("logging.exception", "stacklevel"): (None, (3, 8)),
    ("logging.handlers.HTTPHandler", "context"): (None, (3, 5)),
    ("logging.handlers.MemoryHandler", "flushOnClose"): (None, (3, 6)),
    ("logging.handlers.QueueListener", "respect_handler_level"): (None, (3, 5)),
    ("logging.handlers.RotatingFileHandler", "delay"): ((2, 6), None),  # TODO
    ("logging.handlers.SMTPHandler", "credentials"): ((2, 6), None),  # TODO
    ("logging.handlers.SMTPHandler", "secure"): ((2, 7), None),  # TODO
    ("logging.handlers.SMTPHandler", "timeout"): (None, (3, 3)),
    ("logging.handlers.SysLogHandler", "socktype"): ((2, 7), (3, 2)),
    ("logging.handlers.TimedRotatingFileHandler", "atTime"): (None, (3, 4)),
    ("logging.handlers.TimedRotatingFileHandler", "delay"): ((2, 6), None),  # TODO
    ("logging.handlers.TimedRotatingFileHandler", "utc"): ((2, 6), None),  # TODO
    ("logging.info", "extra"): ((2, 5), None),  # TODO
    ("logging.info", "stack_info"): (None, (3, 2)),
    ("logging.info", "stacklevel"): (None, (3, 8)),
    ("logging.log", "extra"): ((2, 5), None),  # TODO
    ("logging.log", "stack_info"): (None, (3, 2)),
    ("logging.log", "stacklevel"): (None, (3, 8)),
    ("logging.warn", "stack_info"): (None, (3, 2)),
    ("logging.warn", "stacklevel"): (None, (3, 8)),
    ("logging.warning", "extra"): ((2, 5), None),  # TODO
    ("logging.warning", "stack_info"): (None, (3, 2)),
    ("logging.warning", "stacklevel"): (None, (3, 8)),
    ("lzma.LZMADecompressor.decompress", "max_length"): (None, (3, 5)),
    ("marshal.dump", "version"): ((2, 4), None),  # TODO
    ("marshal.dumps", "version"): ((2, 4), None),  # TODO
    ("math.log", "base"): ((2, 3), None),  # TODO
    ("max", "default"): (None, (3, 4)),
    ("max", "key"): ((2, 5), None),  # TODO
    ("min", "default"): (None, (3, 4)),
    ("min", "key"): ((2, 5), None),  # TODO
    ("multiprocessing.Pool", "maxtasksperchild"): ((2, 7), None),  # TODO
    ("multiprocessing.Process", "daemon"): (None, (3, 3)),
    ("multiprocessing.pool.Pool", "context"): (None, (3, 4)),
    ("multiprocessing.pool.Pool", "maxtasksperchild"): (None, (3, 2)),
    ("nis.cat", "domain"): ((2, 5), None),  # TODO
    ("nis.maps", "domain"): ((2, 5), None),  # TODO
    ("nis.match", "domain"): ((2, 5), None),  # TODO
    ("nntplib.NNTP", "usenetrc"): ((2, 4), None),  # TODO
    ("nntplib.NNTP.list", "group_pattern"): (None, (3, 2)),
    ("open", "opener"): (None, (3, 3)),
    ("os.access", "dir_fd"): (None, (3, 3)),
    ("os.access", "effective_ids"): (None, (3, 3)),
    ("os.access", "follow_symlinks"): (None, (3, 3)),
    ("os.chflags", "follow_symlinks"): (None, (3, 3)),
    ("os.chmod", "dir_fd"): (None, (3, 3)),
    ("os.chmod", "follow_symlinks"): (None, (3, 3)),
    ("os.chown", "dir_fd"): (None, (3, 3)),
    ("os.chown", "follow_symlinks"): (None, (3, 3)),
    ("os.dup2", "inheritable"): (None, (3, 4)),
    ("os.link", "dst_dir_fd"): (None, (3, 3)),
    ("os.link", "follow_symlinks"): (None, (3, 3)),
    ("os.link", "src_dir_fd"): (None, (3, 3)),
    ("os.lstat", "dir_fd"): (None, (3, 3)),
    ("os.makedirs", "exist_ok"): (None, (3, 2)),
    ("os.mkdir", "dir_fd"): (None, (3, 3)),
    ("os.mkfifo", "dir_fd"): (None, (3, 3)),
    ("os.mknod", "dir_fd"): (None, (3, 3)),
    ("os.open", "dir_fd"): (None, (3, 3)),
    ("os.readlink", "dir_fd"): (None, (3, 3)),
    ("os.remove", "dir_fd"): (None, (3, 3)),
    ("os.rename", "dst_dir_fd"): (None, (3, 3)),
    ("os.rename", "src_dir_fd"): (None, (3, 3)),
    ("os.rmdir", "dir_fd"): (None, (3, 3)),
    ("os.startfile", "operation"): ((2, 5), None),  # TODO
    ("os.stat", "dir_fd"): (None, (3, 3)),
    ("os.stat", "follow_symlinks"): (None, (3, 3)),
    ("os.symlink", "dir_fd"): (None, (3, 3)),
    ("os.unlink", "dir_fd"): (None, (3, 3)),
    ("os.utime", "dir_fd"): (None, (3, 3)),
    ("os.utime", "follow_symlinks"): (None, (3, 3)),
    ("os.utime", "ns"): (None, (3, 3)),
    ("os.walk", "followlinks"): ((2, 6), None),  # TODO
    ("pathlib.Path.mkdir", "exist_ok"): (None, (3, 5)),
    ("pathlib.Path.resolve", "strict"): (None, (3, 6)),
    ("pathlib.Path.unlink", "missing_ok"): (None, (3, 8)),
    ("pdb.Pdb", "nosigint"): (None, (3, 2)),
    ("pdb.Pdb", "readrc"): (None, (3, 6)),
    ("pdb.Pdb", "skip"): ((2, 7), (3, 1)),
    ("pdb.set_trace", "header"): (None, (3, 7)),
    ("pickle.Pickler", "buffer_callback"): (None, (3, 8)),
    ("pickle.Pickler", "protocol"): ((2, 3), None),  # TODO
    ("pickle.Unpickler", "buffers"): (None, (3, 8)),
    ("pickle.dump", "buffer_callback"): (None, (3, 8)),
    ("pickle.dump", "protocol"): ((2, 3), None),  # TODO
    ("pickle.dumps", "buffer_callback"): (None, (3, 8)),
    ("pickle.dumps", "protocol"): ((2, 3), None),  # TODO
    ("pickle.load", "buffers"): (None, (3, 8)),
    ("pickle.loads", "buffers"): (None, (3, 8)),
    ("pickletools.dis", "annotate"): (None, (3, 2)),
    ("poplib.POP3", "timeout"): ((2, 6), None),  # TODO
    ("poplib.POP3_SSL", "context"): (None, (3, 2)),
    ("pprint.PrettyPrinter", "compact"): (None, (3, 4)),
    ("pprint.PrettyPrinter", "sort_dicts"): (None, (3, 8)),
    ("pprint.pformat", "compact"): (None, (3, 4)),
    ("pprint.pformat", "depth"): ((2, 4), None),  # TODO
    ("pprint.pformat", "indent"): ((2, 4), None),  # TODO
    ("pprint.pformat", "sort_dicts"): (None, (3, 8)),
    ("pprint.pformat", "width"): ((2, 4), None),  # TODO
    ("pprint.pprint", "compact"): (None, (3, 4)),
    ("pprint.pprint", "depth"): ((2, 4), None),  # TODO
    ("pprint.pprint", "indent"): ((2, 4), None),  # TODO
    ("pprint.pprint", "sort_dicts"): (None, (3, 8)),
    ("pprint.pprint", "width"): ((2, 4), None),  # TODO
    ("print", "flush"): (None, (3, 3)),
    ("py_compile.compile", "invalidation_mode"): (None, (3, 7)),
    ("py_compile.compile", "optimize"): (None, (3, 2)),
    ("py_compile.compile", "quiet"): (None, (3, 8)),
    ("re.findall", "flags"): ((2, 4), None),  # TODO
    ("re.finditer", "flags"): ((2, 4), None),  # TODO
    ("re.split", "flags"): ((2, 7), (3, 1)),
    ("re.sub", "flags"): ((2, 7), (3, 1)),
    ("re.subn", "flags"): ((2, 7), (3, 1)),
    ("sched.scheduler.enter", "kwargs"): (None, (3, 3)),
    ("sched.scheduler.enterabs", "kwargs"): (None, (3, 3)),
    ("sched.scheduler.run", "blocking"): (None, (3, 3)),
    ("select.epoll", "flags"): (None, (3, 3)),
    ("shelve.Shelf", "keyencoding"): (None, (3, 2)),
    ("shelve.Shelf", "protocol"): ((2, 3), None),  # TODO
    ("shelve.open", "protocol"): ((2, 3), None),  # TODO
    ("shlex.shlex", "punctuation_chars"): (None, (3, 6)),
    ("shlex.split", "posix"): ((2, 6), None),  # TODO
    ("shutil.copy", "follow_symlinks"): (None, (3, 3)),
    ("shutil.copy2", "follow_symlinks"): (None, (3, 3)),
    ("shutil.copyfile", "follow_symlinks"): (None, (3, 3)),
    ("shutil.copymode", "follow_symlinks"): (None, (3, 3)),
    ("shutil.copystat", "follow_symlinks"): (None, (3, 3)),
    ("shutil.copytree", "copy_function"): (None, (3, 2)),
    ("shutil.copytree", "dirs_exist_ok"): (None, (3, 8)),
    ("shutil.copytree", "ignore"): ((2, 6), None),  # TODO
    ("shutil.copytree", "ignore_dangling_symlinks"): (None, (3, 2)),
    ("shutil.move", "copy_function"): (None, (3, 5)),
    ("signal.set_wakeup_fd", "warn_on_full_buffer"): (None, (3, 7)),
    ("smtpd.SMTPChannel", "decode_data"): (None, (3, 5)),
    ("smtpd.SMTPChannel", "enable_SMTPUTF8"): (None, (3, 5)),
    ("smtpd.SMTPServer", "decode_data"): (None, (3, 5)),
    ("smtpd.SMTPServer", "enable_SMTPUTF8"): (None, (3, 5)),
    ("smtpd.SMTPServer", "map"): (None, (3, 4)),
    ("smtplib.SMTP", "source_address"): (None, (3, 3)),
    ("smtplib.SMTP", "timeout"): ((2, 6), None),  # TODO
    ("smtplib.SMTP.login", "initial_response_ok"): (None, (3, 5)),
    ("smtplib.SMTP.starttls", "context"): (None, (3, 3)),
    ("smtplib.SMTP_SSL", "context"): (None, (3, 3)),
    ("smtplib.SMTP_SSL", "source_address"): (None, (3, 3)),
    ("socket.create_connection", "source_address"): ((2, 7), (3, 2)),
    ("socket.setsockopt", "optlen"): (None, (3, 6)),
    ("sort", "key"): ((2, 4), None),  # TODO
    ("sort", "reverse"): ((2, 4), None),  # TODO
    ("sqlite3.Connection.create_function", "deterministic"): (None, (3, 8)),
    ("sqlite3.connect", "uri"): (None, (3, 4)),
    ("ssl.SSLContext.load_cert_chain", "password"): (None, (3, 3)),
    ("ssl.SSLContext.load_verify_locations", "cadata"): (None, (3, 4)),
    ("ssl.SSLContext.wrap_bio", "session"): (None, (3, 6)),
    ("ssl.SSLContext.wrap_socket", "session"): (None, (3, 6)),
    ("ssl.wrap_socket", "ciphers"): ((2, 7), None),  # TODO
    ("str.center", "fillchar"): ((2, 4), None),  # TODO
    ("str.ljust", "fillchar"): ((2, 4), None),  # TODO
    ("str.lstrip", "chars"): ((2, 2), None),  # TODO
    ("str.rjust", "fillchar"): ((2, 4), None),  # TODO
    ("str.rstrip", "chars"): ((2, 2), None),  # TODO
    ("str.strip", "chars"): ((2, 2), None),  # TODO
    ("string.lstrip", "chars"): ((2, 3), None),  # TODO
    ("string.rstrip", "chars"): ((2, 3), None),  # TODO
    ("string.strip", "chars"): ((2, 3), None),  # TODO
    ("subprocess.Popen", "encoding"): (None, (3, 6)),
    ("subprocess.Popen", "errors"): (None, (3, 6)),
    ("subprocess.Popen", "pass_fds"): (None, (3, 2)),
    ("subprocess.Popen", "restore_signals"): (None, (3, 2)),
    ("subprocess.Popen", "start_new_session"): (None, (3, 2)),
    ("subprocess.Popen", "text"): (None, (3, 7)),
    ("subprocess.Popen.communicate", "timeout"): (None, (3, 3)),
    ("subprocess.Popen.wait", "timeout"): (None, (3, 3)),
    ("subprocess.call", "timeout"): (None, (3, 3)),
    ("subprocess.check_call", "timeout"): (None, (3, 3)),
    ("subprocess.check_output", "encoding"): (None, (3, 6)),
    ("subprocess.check_output", "errors"): (None, (3, 6)),
    ("subprocess.check_output", "input"): (None, (3, 4)),
    ("subprocess.check_output", "text"): (None, (3, 7)),
    ("subprocess.check_output", "timeout"): (None, (3, 3)),
    ("subprocess.run", "capture_output"): (None, (3, 7)),
    ("subprocess.run", "encoding"): (None, (3, 6)),
    ("subprocess.run", "errors"): (None, (3, 6)),
    ("subprocess.run", "text"): (None, (3, 7)),
    ("sum", "start"): (None, (3, 8)),
    ("tarfile.TarFile", "encoding"): ((2, 6), None),  # TODO
    ("tarfile.TarFile", "errors"): ((2, 6), None),  # TODO
    ("tarfile.TarFile", "format"): ((2, 6), None),  # TODO
    ("tarfile.TarFile", "pax_headers"): ((2, 6), None),  # TODO
    ("tarfile.TarFile", "tarinfo"): ((2, 6), None),  # TODO
    ("tarfile.TarFile.add", "exclude"): ((2, 6), None),  # TODO
    ("tarfile.TarFile.add", "filter"): ((2, 7), (3, 2)),
    ("tarfile.TarFile.extract", "numeric_owner"): (None, (3, 5)),
    ("tarfile.TarFile.extract", "set_attrs"): (None, (3, 2)),
    ("tarfile.TarFile.extractall", "numeric_owner"): (None, (3, 5)),
    ("tarfile.TarFile.list", "members"): (None, (3, 5)),
    ("tarfile.TarInfo.tobuf", "encoding"): ((2, 6), None),  # TODO
    ("tarfile.TarInfo.tobuf", "errors"): ((2, 6), None),  # TODO
    ("tarfile.TarInfo.tobuf", "format"): ((2, 6), None),  # TODO
    ("telnetlib.Telnet", "timeout"): ((2, 6), None),  # TODO
    ("telnetlib.Telnet.open", "timeout"): ((2, 6), None),  # TODO
    ("tempfile.NamedTemporaryFile", "delete"): ((2, 6), None),  # TODO
    ("tempfile.NamedTemporaryFile", "errors"): (None, (3, 8)),
    ("tempfile.SpooledTemporaryFile", "errors"): (None, (3, 8)),
    ("tempfile.SpooledTemporaryFile.truncate", "size"): (None, (3, 3)),
    ("tempfile.TemporaryFile", "errors"): (None, (3, 8)),
    ("test.support.check_warnings", "filters"): ((2, 7), None),  # TODO
    ("test.support.check_warnings", "quiet"): ((2, 7), (3, 2)),
    ("threading.Lock.acquire", "timeout"): (None, (3, 2)),
    ("threading.RLock.acquire", "timeout"): (None, (3, 2)),
    ("threading.Semaphore.acquire", "timeout"): (None, (3, 2)),
    ("threading.Thread", "daemon"): (None, (3, 3)),
    ("timeit.Timer", "globals"): (None, (3, 5)),
    ("timeit.repeat", "globals"): (None, (3, 5)),
    ("timeit.timeit", "globals"): (None, (3, 5)),
    ("unittest.TestCase.assertAlmostEqual", "delta"): ((2, 7), (3, 2)),
    ("unittest.TestCase.assertRaises", "msg"): (None, (3, 3)),
    ("unittest.TestCase.assertRaisesRegex", "msg"): (None, (3, 3)),
    ("unittest.TestCase.assertWarns", "msg"): (None, (3, 3)),
    ("unittest.TestCase.assertWarnsRegex", "msg"): (None, (3, 3)),
    ("unittest.TestLoader.loadTestsFromModule", "pattern"): (None, (3, 5)),
    ("unittest.TextTestRunner", "tb_locals"): (None, (3, 5)),
    ("unittest.TextTestRunner", "warnings"): (None, (3, 2)),
    ("unittest.main", "buffer"): ((2, 7), (3, 2)),
    ("unittest.main", "catchbreak"): ((2, 7), (3, 2)),
    ("unittest.main", "exit"): ((2, 7), (3, 1)),
    ("unittest.main", "failfast"): ((2, 7), (3, 2)),
    ("unittest.main", "verbosity"): ((2, 7), (3, 2)),
    ("unittest.main", "warnings"): (None, (3, 2)),
    ("unittest.mock.Mock", "unsafe"): (None, (3, 5)),
    ("unittest.mock.Mock.reset_mock", "return_value"): (None, (3, 6)),
    ("unittest.mock.Mock.reset_mock", "side_effect"): (None, (3, 6)),
    ("urllib.URLopener", "context"): ((2, 7), None),  # TODO
    ("urllib.parse.parse_qs", "encoding"): (None, (3, 2)),
    ("urllib.parse.parse_qs", "errors"): (None, (3, 2)),
    ("urllib.parse.parse_qs", "max_num_fields"): (None, (3, 8)),
    ("urllib.parse.parse_qsl", "encoding"): (None, (3, 2)),
    ("urllib.parse.parse_qsl", "errors"): (None, (3, 2)),
    ("urllib.parse.parse_qsl", "max_num_fields"): (None, (3, 8)),
    ("urllib.parse.urlencode", "quote_via"): (None, (3, 5)),
    ("urllib.request.HTTPSHandler", "check_hostname"): (None, (3, 2)),
    ("urllib.request.HTTPSHandler", "context"): (None, (3, 2)),
    ("urllib.request.Request", "method"): (None, (3, 3)),
    ("urllib.request.urlopen", "cadefault"): (None, (3, 3)),
    ("urllib.request.urlopen", "cafile"): (None, (3, 2)),
    ("urllib.request.urlopen", "capath"): (None, (3, 2)),
    ("urllib.request.urlopen", "context"): (None, (3, 4)),
    ("urllib.urlopen", "context"): ((2, 7), None),  # TODO
    ("urllib.urlopen", "proxies"): ((2, 3), None),  # TODO
    ("urllib.urlretrieve", "context"): ((2, 7), None),  # TODO
    ("urllib2.HTTPSHandler", "context"): ((2, 7), None),  # TODO
    ("urllib2.OpenerDirector.open", "timeout"): ((2, 6), None),  # TODO
    ("urllib2.urlopen", "cadefault"): ((2, 7), None),  # TODO
    ("urllib2.urlopen", "cafile"): ((2, 7), None),  # TODO
    ("urllib2.urlopen", "capth"): ((2, 7), None),  # TODO
    ("urllib2.urlopen", "context"): ((2, 7), None),  # TODO
    ("urllib2.urlopen", "timeout"): ((2, 6), None),  # TODO
    ("urlparse.parse_qs", "max_num_fields"): ((2, 7), None),  # TODO
    ("urlparse.parse_qsl", "max_num_fields"): ((2, 7), None),  # TODO
    ("uu.encode", "backtick"): (None, (3, 7)),
    ("venv.EnvBuilder", "prompt"): (None, (3, 6)),
    ("venv.EnvBuilder", "with_pip"): (None, (3, 4)),
    ("venv.create", "prompt"): (None, (3, 6)),
    ("venv.create", "with_pip"): (None, (3, 4)),
    ("warnings.formatwarning", "line"): ((2, 6), None),  # TODO
    ("warnings.showwarning", "line"): ((2, 7), None),  # TODO
    ("warnings.warn", "source"): (None, (3, 6)),
    ("warnings.warn_explicit", "module_globals"): ((2, 5), None),  # TODO
    ("warnings.warn_explicit", "source"): (None, (3, 6)),
    ("webbrowser.register", "preferred"): (None, (3, 7)),
    ("xml.dom.minidom.Document.writexml", "encoding"): ((2, 3), None),  # TODO
    ("xml.dom.minidom.Node.toprettyxml", "encoding"): ((2, 3), None),  # TODO
    ("xml.dom.minidom.Node.toxml", "encoding"): ((2, 3), None),  # TODO
    ("xml.dom.minidom.Node.writexml", "addindent"): ((2, 1), None),  # TODO
    ("xml.dom.minidom.Node.writexml", "indent"): ((2, 1), None),  # TODO
    ("xml.dom.minidom.Node.writexml", "newl"): ((2, 1), None),  # TODO
    ("xml.etree.ElementTree.ElementTree.write", "short_empty_elements"): (None, (3, 4)),
    ("xml.etree.ElementTree.tostring", "default_namespace"): (None, (3, 8)),
    ("xml.etree.ElementTree.tostring", "short_empty_elements"): (None, (3, 4)),
    ("xml.etree.ElementTree.tostring", "xml_declaration"): (None, (3, 8)),
    ("xml.etree.ElementTree.tostringlist", "default_namespace"): (None, (3, 8)),
    ("xml.etree.ElementTree.tostringlist", "short_empty_elements"): (None, (3, 4)),
    ("xml.etree.ElementTree.tostringlist", "xml_declaration"): (None, (3, 8)),
    ("xml.sax.saxutils.XMLGenerator", "short_empty_elements"): (None, (3, 2)),
    ("xmlrpc.client.ServerProxy", "context"): (None, (3, 4)),
    ("xmlrpc.client.ServerProxy", "headers"): (None, (3, 8)),
    ("xmlrpc.client.ServerProxy", "use_builtin_types"): (None, (3, 3)),
    ("xmlrpc.client.loads", "use_builtin_types"): (None, (3, 3)),
    ("xmlrpc.server.CGIXMLRPCRequestHandler", "use_builtin_types"): (None, (3, 3)),
    ("xmlrpc.server.DocXMLRPCServer", "use_builtin_types"): (None, (3, 3)),
    ("xmlrpc.server.SimpleXMLRPCServer", "use_builtin_types"): (None, (3, 3)),
    ("xmlrpclib.ServerProxy", "context"): ((2, 7), None),  # TODO
    ("xmlrpclib.ServerProxy", "use_datetime"): ((2, 5), None),  # TODO
    ("xmlrpclib.loads", "use_datetime"): ((2, 5), None),  # TODO
    ("zipapp.create_archive", "compressed"): (None, (3, 7)),
    ("zipapp.create_archive", "filter"): (None, (3, 7)),
    ("zipfile.PyZipFile", "optimize"): (None, (3, 2)),
    ("zipfile.PyZipFile.writepy", "filterfunc"): (None, (3, 4)),
    ("zipfile.ZipFile", "compresslevel"): (None, (3, 7)),
    ("zipfile.ZipFile", "strict_timestamps"): (None, (3, 8)),
    ("zipfile.ZipFile.read", "pwd"): ((2, 6), None),  # TODO
    ("zipfile.ZipFile.writestr", "compress_type"): ((2, 7), (3, 2)),
    ("zipfile.ZipInfo.from_file", "strict_timestamps"): (None, (3, 8)),
    ("zlib.Decompress.decompress", "max_length"): (None, (3, 6)),
    ("zlib.compress", "level"): (None, (3, 6)),
    ("zlib.compressobj", "zdict"): (None, (3, 3)),
    ("zlib.decompress", "bufsize"): (None, (3, 6)),
    ("zlib.decompress", "wbits"): (None, (3, 6)),
    ("zlib.decompressobj", "zdict"): (None, (3, 3)),
}
