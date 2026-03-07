[![CloudNativePG](../logo/cloudnativepg.png)](https://cloudnative-pg.io/)

# Cluster Image Catalogs

> [!NOTE]
> **CloudNativePG 1.29+ and the `extensions` Stanza**
> The catalogs in this directory are currently the mainstream definitions for older CNPG versions.
> - **For CNPG 1.29+**: Please use the manifests in the [`extensions/` > subdirectory](./extensions)
> to leverage the new `extensions` stanza and PostgreSQL 18 support for
> `extensions_control_path`.
> 
> **Roadmap Note:** In the coming months, once CloudNativePG 1.28 reaches EOL,
> the catalogs in this main folder will be updated to support the `extensions`
> format directly, and the temporary `/extensions` directory will be
> decommissioned.

This directory contains the **official `ClusterImageCatalog` manifests**
maintained by [CloudNativePG](https://cloudnative-pg.io/).  

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

---

For full details, please refer to the
[official documentation](https://cloudnative-pg.io/documentation/current/image_catalog/).
