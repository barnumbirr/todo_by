#!/usr/bin/env python3

import re

def _get_version(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        pattern = r'\b(\d+\.\d+\.\d+(?:-[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?)\b'
        version_match = re.search(pattern, content)
        if version_match:
            return version_match.group(1)
    raise ValueError(f"Unable to extract version number from {file_path}")

def _compare_semver(version1, version2):
    def _split_version(version):
        pre_release = None
        build_metadata = None
        if '-' in version:
            version, pre_release = version.split('-', 1)
        if '+' in version:
            version, build_metadata = version.split('+', 1)
        return version, pre_release, build_metadata

    v1, pre1, build1 = _split_version(version1)
    v2, pre2, build2 = _split_version(version2)

    components1 = list(map(int, v1.split('.')))
    components2 = list(map(int, v2.split('.')))

    for i in range(max(len(components1), len(components2))):
        val1 = components1[i] if i < len(components1) else 0
        val2 = components2[i] if i < len(components2) else 0

        if val1 < val2:
            return -1
        elif val1 > val2:
            return 1

    if pre1 and not pre2:
        return -1
    elif not pre1 and pre2:
        return 1
    elif pre1 and pre2:
        if pre1 < pre2:
            return -1
        elif pre1 > pre2:
            return 1

    return 0
