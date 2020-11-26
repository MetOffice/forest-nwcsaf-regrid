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

Usage: regrid.py [OPTIONS] LON_LAT_FILE FILE_NAME OUT_FILE

Arguments:
  LON_LAT_FILE  [required]
  FILE_NAME     [required]
  OUT_FILE      [required]

Options:
  --plot-width INTEGER  [default: 256]
  --install-completion  Install completion for the current shell.
  --show-completion     Show completion for the current shell, to copy it or
                        customize the installation.

  --help                Show this message and exit.
```

**Note:** It has some minor EIDA50 specific peculiarities that could be cleaned up.

**Note:** FOREST-Lite supports `web_mercator_x` and `web_mercator_y` dimensions. Perhaps this could be back-ported to FOREST-Original.
