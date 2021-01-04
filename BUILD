load("@py_deps//:requirements.bzl", "requirement")
load("@rules_python//python:defs.bzl", "py_binary", "py_library")

py_binary(
    name = "basic_tweepy_functions",
    srcs = ["basic_tweepy_functions.py"],
    deps = [
        requirement("tweepy"),
    ]
)

py_library(
    name = "twitter_functions",
    srcs = ["twitter_functions.py"],
    deps = [
        requirement("tweepy"),
    ]
)