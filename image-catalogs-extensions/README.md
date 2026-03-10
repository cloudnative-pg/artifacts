[![CloudNativePG](../logo/cloudnativepg.png)](https://cloudnative-pg.io/)

# Cluster Image Catalogs (v1.29+)

> [!IMPORTANT]
> **Compatibility & Lifecycle**
> This is a temporary folder for **CloudNativePG 1.29+ only**.
> Version 1.29 of the image catalogs introduced the `extensions` stanza, which
> makes them incompatible with earlier versions of CloudNativePG. Note that
> CNPG 1.28.2+ and 1.27.4+ are also compatible with the new format, but until
> CloudNativePG 1.28 reaches End-of-Life (EOL), the mainstream catalogs in the
> [parent folder](../) will serve those users. Once 1.28 is decommissioned,
> these definitions will move to the main folder.

This directory contains the **official `ClusterImageCatalog` manifests**
maintained by [CloudNativePG](https://cloudnative-pg.io/) for CloudNativePG 1.29+.

## Key Details

- **PostgreSQL 18 Support:** The minimal catalog includes supported extensions
  for Postgres 18.
- **Automation:** By applying a catalog, administrators ensure clusters
  automatically upgrade to the latest patch release within a major version.
- **Flavor Selection:** Each catalog is based on a specific **image type**
  (e.g., `minimal`) and **Debian release** (e.g., `trixie`).

## Usage

Install a single catalog (e.g. `minimal` images on Debian `trixie`):

```sh
kubectl apply -f \
  https://raw.githubusercontent.com/cloudnative-pg/artifacts/refs/heads/main/image-catalogs-extensions/catalog-minimal-trixie.yaml
```

Install all catalogs at once:

```sh
kubectl apply -k \
  https://github.com/cloudnative-pg/artifacts/image-catalogs-extensions?ref=main
```

---

For full details, please refer to the
[official documentation](https://cloudnative-pg.io/docs/devel/image_catalog/).
