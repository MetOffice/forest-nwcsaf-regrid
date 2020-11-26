#!/usr/bin/env python
import typer
import datashader
import xarray
from tiling import web_mercator


app = typer.Typer()


def main(lon_lat_file: str, file_name: str, out_file: str, plot_width: int = 256):
    print(file_name)

    # Geostationary coordinate file
    lon_lat_ds = xarray.open_dataset(lon_lat_file)

    # Read Geostationary projection
    longitudes = lon_lat_ds.longitude
    latitudes = lon_lat_ds.latitude[::-1]  # TODO: Remove reverse lats step
    dataset = xarray.open_dataset(file_name)
    values = dataset["data"]

    print("Map to web Mercator coords")
    # Map to WebMercator coordinates
    gx, gy = web_mercator(longitudes, latitudes)

    # Data array
    x_coord_name = "web_mercator_x"
    y_coord_name = "web_mercator_y"
    data_array = xarray.DataArray(
        values,
        dims=["Y", "X"],
        coords={
            x_coord_name: (["Y", "X"], gx),
            y_coord_name: (["Y", "X"], gy)
        }
    )

    # Map to regular lon/lat coordinate system
    plot_height = plot_width
    canvas = datashader.Canvas(
        plot_height=plot_height,
        plot_width=plot_width,
    )

    print("quadmesh")
    mesh = canvas.quadmesh(data_array, x=x_coord_name, y=y_coord_name)

    print(f"write: {out_file}")
    mesh_dataset = mesh.to_dataset(name="data")
    mesh_dataset.to_netcdf(out_file)


if __name__ == '__main__':
    typer.run(main)
