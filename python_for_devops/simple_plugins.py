#!/usr/bin/env python3
import fire
import pkgutil
import importlib


def find_and_run_plugin(plugin_prefix):
    plugins = {}

    # Discover and Load Plugins
