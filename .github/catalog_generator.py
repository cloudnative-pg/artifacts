#
# Copyright © contributors to CloudNativePG, established as
# CloudNativePG a Series of LF Projects, LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: Apache-2.0
#

import re
import json
import yaml
from packaging import version
from subprocess import check_output

min_supported_major = 13

pg_repo_name = "ghcr.io/cloudnative-pg/postgresql"
pg_regexp = r"(\d+)(?:\.\d+|beta\d+|rc\d+|alpha\d+)-(\d{12})"


def get_json(repo_name):
    data = check_output([
        "docker",
        "run",
        "--rm",
        "quay.io/skopeo/stable",
        "list-tags",
        f"docker://{repo_name}"
    ])
    repo_json = json.loads(data.decode("utf-8"))
    return repo_json


def get_digest(repo_name, tag):
    data = check_output([
        "docker",
        "run",
        "--rm",
        "quay.io/skopeo/stable",
        "inspect",
        "-n",
        f"docker://{repo_name}:{tag}"
    ])
    repo_json = json.loads(data.decode("utf-8"))
    return repo_json["Digest"]


def write_catalog(tags, version_re, suffix):
    version_re = re.compile(rf"^{version_re}{re.escape(suffix)}$")

    # Filter out all the tags which do not match the version regexp
    tags = [item for item in tags if version_re.search(item)]

    # Sort the tags according to semantic versioning
    tags.sort(
        key=lambda v: version.Version(v.removesuffix(suffix)),
        reverse=True
    )

    results = {}
    for item in tags:
        match = version_re.search(item)
        if not match:
            continue

        major = match.group(1)

        # Skip too old versions
        if int(major) < min_supported_major:
            continue

        if major not in results:
            digest = get_digest(pg_repo_name, item)
            results[major] = [f"{pg_repo_name}:{item}@{digest}"]

    catalog = {
        "apiVersion": "postgresql.cnpg.io/v1",
        "kind": "ClusterImageCatalog",
        "metadata": {"name": f"postgresql{suffix}"},
        "spec": {
            "images": [
                {"major": int(major), "image": images[0]} for major, images in sorted(results.items(), key=lambda x: int(x[0]))
            ]
        }
    }

    with open(f"catalog{suffix}.yaml", "w") as f:
        yaml.dump(catalog, f, sort_keys=False)

if __name__ == "__main__":
    repo_json = get_json(pg_repo_name)
    tags = repo_json["Tags"]

    for suffix in [
        "-minimal-bullseye",
        "-standard-bullseye",
        "-minimal-bookworm",
        "-standard-bookworm",
        "-minimal-trixie",
        "-standard-trixie",
    ]:
        write_catalog(tags, pg_regexp, suffix)
