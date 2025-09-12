[![CloudNativePG](../logo/cloudnativepg.png)](https://cloudnative-pg.io/)

# Cluster Image Catalogs

This directory contains the **official `ClusterImageCatalog` manifests**
maintained by [CloudNativePG](https://cloudnative-pg.io/).  

See the [documentation](https://cloudnative-pg.io/documentation/current/image_catalog/)
for full details.

## What they are

Each catalog defines the latest container images for all supported PostgreSQL
major versions, based on a specific **image type** (e.g. `minimal`) and
**Debian release** (e.g. `trixie`).

By applying a catalog, administrators ensure that CloudNativePG clusters
automatically upgrade to the latest patch release within a given PostgreSQL
major version.

## Usage

Install a single catalog (e.g. `minimal` images on Debian `trixie`):

```sh
kubectl apply -f \
  https://raw.githubusercontent.com/cloudnative-pg/artifacts/refs/heads/main/image-catalogs/catalog-minimal-trixie.yaml
````

Install all catalogs at once:

```sh
kubectl apply -k \
  https://github.com/cloudnative-pg/artifacts/image-catalogs?ref=main
```
