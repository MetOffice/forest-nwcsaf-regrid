# FOREST NWCSAF regrid
NWCSAF re-grid pre-processor for FOREST

## Dependencies

These might need some careful thought to make it more portable.

- [Typer](https://typer.tiangolo.com/) - A command line generator library
- Cartopy
- NumPy
- Datashader
- Xarray

## Usage

This is a simple Typer command line script, it requires a file with the source grid longitude/latitude
values.

```sh
./bin/regrid.py --help
```

**Note:** It has some minor EIDA50 specific peculiarities that could be cleaned up.

**Note:** FOREST-Lite supports `web_mercator_x` and `web_mercator_y` dimensions. Perhaps this could be back-ported to FOREST-Original.
