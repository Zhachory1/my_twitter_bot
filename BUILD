load("@py_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_library", "py_test")

py_binary(
    name = "basic_tweepy_functions",
    srcs = ["basic_tweepy_functions.py"],
    deps = [
        requirement("tweepy"),
    ],
    data = ["//secrets:keys.json"]
)

py_library(
    name = "twitter_functions",
    srcs = ["twitter_functions.py"],
    deps = [
        requirement("tweepy"),
        requirement("mechanize"),
        requirement("beautifulsoup4"),
    ]
)

py_test(
    name = "twitter_functions_test",
    srcs = ["twitter_functions_test.py"],
    deps = [
        ":twitter_functions"
    ],
    data = ["//secrets:keys.json"]
)