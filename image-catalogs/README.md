[![CloudNativePG](../logo/cloudnativepg.png)](https://cloudnative-pg.io/)

# Cluster Image Catalogs

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

## Verifying catalog's signature

CloudNativePG cryptographically signs all official image catalogs.
Verifying these signatures ensures that assets originate from official CloudNativePG repositories
and were published through our automated release workflow.

Prerequisites:
- **Signature verification:** [cosign](https://github.com/sigstore/cosign) CLI

You can verify a catalog's YAML file by using the corresponding bundle (the `.sigstore.json` file)
present inside the `image-catalogs` directory.

For example:

```bash
cosign verify-blob \
  catalog-minimal-trixie.yaml \
  --bundle catalog-minimal-trixie.sigstore.json \
  --certificate-identity-regexp "^https://github.com/cloudnative-pg/postgres-containers/.github/workflows/catalogs.yml@main" \
  --certificate-oidc-issuer "https://token.actions.githubusercontent.com"
```

---

For full details, please refer to the
[official documentation](https://cloudnative-pg.io/documentation/current/image_catalog/).
